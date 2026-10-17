package com.oceancleanup.service;

/**
 * Service managing in-game 24-hour day/night cycle, sun elevation, and light calculations.
 * Reflects TimeSystem.js in OceanCleanup2.
 */
public class DayNightCycleService {

    private double timeOfDay; // 0.0 to 24.0 (starts at 8.0 = 8 AM)
    private int totalDays;
    private final double timeScale; // 1 second real-time = 1 minute in-game (1/60 hr per sec)

    public DayNightCycleService() {
        this(8.0, 1, 1.0 / 60.0);
    }

    public DayNightCycleService(double initialTimeOfDay, int initialDays, double timeScale) {
        this.timeOfDay = initialTimeOfDay;
        this.totalDays = initialDays;
        this.timeScale = timeScale;
    }

    public double getTimeOfDay() {
        return timeOfDay;
    }

    public int getTotalDays() {
        return totalDays;
    }

    public void update(double dtSeconds) {
        if (dtSeconds < 0) {
            throw new IllegalArgumentException("Delta time cannot be negative");
        }
        this.timeOfDay += (dtSeconds * timeScale);
        while (this.timeOfDay >= 24.0) {
            this.timeOfDay -= 24.0;
            this.totalDays += 1;
        }
    }

    public double calculateSunElevation() {
        // Map 6..18 (sunrise to sunset) to 0..PI
        double timeRatio = (this.timeOfDay - 6.0) / 12.0;
        double elevation = Math.sin(timeRatio * Math.PI) * (Math.PI / 2.0);
        return Math.max(-0.2, elevation);
    }

    public double calculateSunIntensity() {
        double elevation = calculateSunElevation();
        if (elevation <= 0) {
            return 0.0;
        }
        return Math.min(1.0, elevation / 0.2) * 1.6;
    }

    public boolean isDaytime() {
        return calculateSunElevation() > 0;
    }

    public boolean isNight() {
        return !isDaytime();
    }
}
