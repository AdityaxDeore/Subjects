package com.oceancleanup;

import com.oceancleanup.exception.MaxLevelReachedException;
import com.oceancleanup.model.BoatLevel;
import com.oceancleanup.model.Player;
import com.oceancleanup.model.TrashItem;
import com.oceancleanup.service.BoatProgressionService;
import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("BoatProgressionService Test Suite")
class BoatProgressionServiceTest {

    private BoatProgressionService boatService;
    private Player player;

    @BeforeAll
    static void initAll() {
        System.out.println("[TEST SETUP] Initializing BoatProgressionService Test Suite");
    }

    @AfterAll
    static void tearDownAll() {
        System.out.println("[TEST TEARDOWN] BoatProgressionService Test Suite Completed");
    }

    @BeforeEach
    void setUp() {
        boatService = new BoatProgressionService();
        player = new Player("OceanHero_Aditya");
    }

    @AfterEach
    void tearDown() {
        player = null;
    }

    @Test
    @DisplayName("Should initialize default player at Boat Level 1 with standard capacity and speed")
    void testInitialBoatLevelAttributes() {
        assertAll("Initial Boat Attributes Verification",
                () -> assertEquals(1, player.getBoatLevel(), "Default boat level must be 1"),
                () -> assertEquals(20, boatService.getCapacityForPlayer(player), "Level 1 capacity must be 20 slots"),
                () -> assertEquals(12.0, boatService.getSpeedForPlayer(player), 0.001, "Level 1 speed must be 12.0 knots"),
                () -> assertFalse(boatService.canUpgrade(player), "Player with 0 trash cannot upgrade yet")
        );
    }

    @ParameterizedTest(name = "Tier {0}: name=''{1}'', slots={2}, speed={3}")
    @CsvSource({
            "1, Small Fishing Boat, 20, 12.0",
            "2, Hanger Boat,        40, 15.0",
            "3, Large Vessel,       70, 18.0",
            "4, House Boat,        120, 20.0"
    })
    @DisplayName("Parameterized Test: Verify all boat tier configurations match OceanCleanup2 specs")
    void testAllBoatTiersConfig(int level, String expectedName, int expectedSlots, double expectedSpeed) {
        BoatLevel tier = boatService.getBoatLevel(level);
        assertNotNull(tier, "Tier config must not be null");
        assertAll("Tier Details Check",
                () -> assertEquals(expectedName, tier.getName()),
                () -> assertEquals(expectedSlots, tier.getSlots()),
                () -> assertEquals(expectedSpeed, tier.getSpeed(), 0.001)
        );
    }

    @ParameterizedTest
    @ValueSource(ints = { -1, 0, 5, 99 })
    @DisplayName("Parameterized Test: Should throw IllegalArgumentException for non-existent boat levels")
    void testInvalidBoatLevelLookup(int invalidLevel) {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () ->
                boatService.getBoatLevel(invalidLevel)
        );
        assertTrue(ex.getMessage().contains("Invalid boat tier"));
    }

    @Nested
    @DisplayName("Nested Tests: Upgrade Logic and Boundary Scenarios")
    class UpgradeBoundaryTests {

        @Test
        @DisplayName("Should prevent upgrade when player collects fewer trash items than required")
        void testUpgradeFailsWithInsufficientTrash() {
            // Level 2 requires 5 trash items, player collects 4
            for (int i = 0; i < 4; i++) {
                player.addTrash(new TrashItem("t_" + i, TrashItem.TrashType.PLASTIC_BOTTLE, i, i));
            }

            assertFalse(boatService.canUpgrade(player));
            IllegalStateException ex = assertThrows(IllegalStateException.class, () ->
                    boatService.upgradeBoat(player)
            );
            assertTrue(ex.getMessage().contains("Insufficient trash"));
            assertEquals(1, player.getBoatLevel(), "Player level must remain unchanged on failure");
        }

        @Test
        @DisplayName("Should successfully upgrade to Level 2 upon reaching 5 trash items")
        void testSuccessfulLevel2Upgrade() {
            for (int i = 0; i < 5; i++) {
                player.addTrash(new TrashItem("t_" + i, TrashItem.TrashType.PLASTIC_BOTTLE, i, i));
            }

            assertTrue(boatService.canUpgrade(player));
            BoatLevel upgraded = boatService.upgradeBoat(player);

            assertAll("Level 2 Upgrade State",
                    () -> assertEquals(2, upgraded.getLevel()),
                    () -> assertEquals("Hanger Boat", upgraded.getName()),
                    () -> assertEquals(2, player.getBoatLevel()),
                    () -> assertEquals(40, boatService.getCapacityForPlayer(player)),
                    () -> assertEquals(15.0, boatService.getSpeedForPlayer(player), 0.001)
            );
        }

        @Test
        @DisplayName("Should throw MaxLevelReachedException when upgrading beyond Level 4")
        void testMaxLevelBoundary() {
            player.setBoatLevel(4);
            // Collect sufficient trash
            for (int i = 0; i < 20; i++) {
                player.addTrash(new TrashItem("t_" + i, TrashItem.TrashType.CRATE, i, i));
            }

            assertFalse(boatService.canUpgrade(player), "Max level boat cannot be upgraded");
            assertThrows(MaxLevelReachedException.class, () ->
                    boatService.upgradeBoat(player)
            );
        }
    }
}
