package com.oceancleanup;

import com.oceancleanup.service.DayNightCycleService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Timeout;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import java.util.concurrent.TimeUnit;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("DayNightCycleService Test Suite")
class DayNightCycleServiceTest {

    private DayNightCycleService timeService;

    @BeforeEach
    void setUp() {
        timeService = new DayNightCycleService(8.0, 1, 1.0 / 60.0);
    }

    @Test
    @DisplayName("Should initialize default time at 8:00 AM on Day 1")
    void testInitialTimeAndDay() {
        assertAll("Initial Temporal State",
                () -> assertEquals(8.0, timeService.getTimeOfDay(), 0.001),
                () -> assertEquals(1, timeService.getTotalDays()),
                () -> assertTrue(timeService.isDaytime())
        );
    }

    @Test
    @DisplayName("Should advance game time by 1 hour for every 60 real-time seconds elapsed")
    void testTimeProgression() {
        timeService.update(60.0); // 60 seconds * (1/60 hr/sec) = 1.0 hr

        assertEquals(9.0, timeService.getTimeOfDay(), 0.001);
        assertEquals(1, timeService.getTotalDays());
    }

    @Test
    @DisplayName("Should rollover from 24:00 to 0:00 and increment day count accurately")
    void testDayRollover() {
        // From 8:00 AM, advance 18 hours (18 * 60 = 1080 seconds) -> 26.0 -> 2:00 AM, Day 2
        timeService.update(1080.0);

        assertEquals(2.0, timeService.getTimeOfDay(), 0.001);
        assertEquals(2, timeService.getTotalDays());
    }

    @ParameterizedTest(name = "Hour {0}: expectedDaytime={1}")
    @CsvSource({
            "12.0, true",   // Noon
            "10.0, true",   // Mid-morning
            "20.0, false",  // Night
            "2.0,  false"   // Deep night
    })
    @DisplayName("Parameterized Test: Verify daytime vs nighttime determination across the 24-hour cycle")
    void testDaytimeNighttimeClassification(double hour, boolean expectedDaytime) {
        DayNightCycleService service = new DayNightCycleService(hour, 1, 1.0 / 60.0);
        assertEquals(expectedDaytime, service.isDaytime(), "Hour " + hour + " daytime check");
        assertEquals(!expectedDaytime, service.isNight(), "Hour " + hour + " nighttime check");
    }

    @Test
    @DisplayName("Should calculate peak sun elevation and intensity at solar noon (12:00 PM)")
    void testSolarNoonSunCalculations() {
        DayNightCycleService noonService = new DayNightCycleService(12.0, 1, 1.0 / 60.0);

        double elevation = noonService.calculateSunElevation();
        double intensity = noonService.calculateSunIntensity();

        // At noon (timeRatio = 0.5), sin(0.5 * PI) = 1.0 -> elevation = PI / 2 ~= 1.5707
        assertEquals(Math.PI / 2.0, elevation, 0.001);
        assertEquals(1.6, intensity, 0.001, "Full solar intensity should be 1.6");
    }

    @Test
    @DisplayName("Should clamp night sun elevation to minimum -0.2 to prevent visual artifacts")
    void testNightSunElevationClamping() {
        DayNightCycleService midnightService = new DayNightCycleService(0.0, 1, 1.0 / 60.0);

        double elevation = midnightService.calculateSunElevation();
        double intensity = midnightService.calculateSunIntensity();

        assertEquals(-0.2, elevation, 0.001, "Elevation should clamp at -0.2 floor");
        assertEquals(0.0, intensity, 0.001, "Night solar intensity must be 0.0");
    }

    @Test
    @Timeout(value = 1, unit = TimeUnit.SECONDS)
    @DisplayName("Performance Test with @Timeout: Rapidly simulate 100,000 tick updates within 1 second")
    void testHighFrequencyTickPerformance() {
        assertTimeoutPreemptively(java.time.Duration.ofMillis(800), () -> {
            for (int i = 0; i < 100_000; i++) {
                timeService.update(0.016);
            }
        });
        assertTrue(timeService.getTotalDays() > 1);
    }

    @Test
    @DisplayName("Should throw IllegalArgumentException when supplied with negative delta time")
    void testNegativeDeltaTimeThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> timeService.update(-5.0));
    }
}
