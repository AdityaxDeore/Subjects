package com.oceancleanup;

import com.oceancleanup.exception.InventoryFullException;
import com.oceancleanup.model.Player;
import com.oceancleanup.model.TrashItem;
import com.oceancleanup.service.BoatProgressionService;
import com.oceancleanup.service.TrashCollectionService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.EnumSource;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("TrashCollectionService Test Suite")
@Tag("CoreGameplay")
class TrashCollectionServiceTest {

    private BoatProgressionService boatService;
    private TrashCollectionService trashService;
    private Player player;

    @BeforeEach
    void setUp() {
        boatService = new BoatProgressionService();
        trashService = new TrashCollectionService(boatService);
        player = new Player("EcoWarrior");
    }

    @Test
    @DisplayName("Should successfully collect single trash item and increment player score")
    void testCollectSingleItemSuccess() {
        TrashItem oilDrum = new TrashItem("item_01", TrashItem.TrashType.OIL_DRUM, 10.0, 15.0);

        boolean collected = trashService.collectTrash(player, oilDrum);

        assertAll("Single Collection State",
                () -> assertTrue(collected, "Collection must return true"),
                () -> assertEquals(1, player.getTrashCount(), "Inventory size must be 1"),
                () -> assertEquals(50, player.getScore(), "Score should match OIL_DRUM 50 points")
        );
    }

    @ParameterizedTest(name = "TrashType: {0}")
    @EnumSource(TrashItem.TrashType.class)
    @DisplayName("Parameterized Test: Verify points and positive weights for every trash category")
    void testTrashTypesAttributes(TrashItem.TrashType type) {
        TrashItem item = new TrashItem("test_id", type, 0.0, 0.0);
        assertAll("TrashType Validation",
                () -> assertTrue(item.getPoints() > 0, "Base points must be strictly positive"),
                () -> assertTrue(item.getWeight() > 0.0, "Weight must be positive"),
                () -> assertTrue(item.getCoinValue() > 0, "Coin value must be positive")
        );
    }

    @Test
    @DisplayName("Should enforce inventory capacity limit and throw InventoryFullException when capacity exceeded")
    void testInventoryCapacityBoundaryEnforcement() {
        int capacity = boatService.getCapacityForPlayer(player); // 20 for Level 1

        // Fill up to exact max capacity
        for (int i = 0; i < capacity; i++) {
            TrashItem bottle = new TrashItem("bot_" + i, TrashItem.TrashType.PLASTIC_BOTTLE, i, i);
            assertDoesNotThrow(() -> trashService.collectTrash(player, bottle));
        }

        assertEquals(capacity, player.getTrashCount(), "Inventory should be at full 20 capacity");

        // Attempt to collect 21st item
        TrashItem extraItem = new TrashItem("bot_overflow", TrashItem.TrashType.PLASTIC_BOTTLE, 50, 50);
        InventoryFullException ex = assertThrows(InventoryFullException.class, () ->
                trashService.collectTrash(player, extraItem)
        );

        assertTrue(ex.getMessage().contains("capacity (20) reached"));
        assertEquals(capacity, player.getTrashCount(), "Inventory must remain unchanged after overflow attempt");
    }

    @Test
    @DisplayName("Should compute cumulative weight and score for multiple trash items")
    void testTotalScoreAndWeightCalculations() {
        List<TrashItem> items = List.of(
                new TrashItem("1", TrashItem.TrashType.PLASTIC_BOTTLE, 0, 0), // 10 pts, 0.2 kg
                new TrashItem("2", TrashItem.TrashType.OIL_DRUM, 0, 0),       // 50 pts, 5.0 kg
                new TrashItem("3", TrashItem.TrashType.OLD_TIRE, 0, 0)        // 25 pts, 2.5 kg
        );

        int totalScore = trashService.calculateTotalScore(items);
        double totalWeight = trashService.calculateTotalWeight(items);

        assertEquals(85, totalScore, "Total score must sum to 85");
        assertEquals(7.7, totalWeight, 0.001, "Total weight must sum to 7.7 kg");
    }

    @Test
    @DisplayName("Should categorize trash inventory into distinct item counts")
    void testTrashTypeBreakdown() {
        List<TrashItem> items = List.of(
                new TrashItem("1", TrashItem.TrashType.PLASTIC_BOTTLE, 0, 0),
                new TrashItem("2", TrashItem.TrashType.PLASTIC_BOTTLE, 0, 0),
                new TrashItem("3", TrashItem.TrashType.CRATE, 0, 0)
        );

        Map<TrashItem.TrashType, Long> breakdown = trashService.getTrashTypeBreakdown(items);

        assertEquals(2L, breakdown.get(TrashItem.TrashType.PLASTIC_BOTTLE));
        assertEquals(1L, breakdown.get(TrashItem.TrashType.CRATE));
        assertNull(breakdown.get(TrashItem.TrashType.OIL_DRUM));
    }

    @Test
    @DisplayName("Should accurately verify proximity within reel distance radius")
    void testReelProximityDistance() {
        TrashItem target = new TrashItem("target", TrashItem.TrashType.GARBAGE_BAG, 10.0, 10.0);

        // Player at (11.0, 11.0) -> dist = sqrt(1^2 + 1^2) = 1.414 <= 5.0 -> TRUE
        assertTrue(trashService.isWithinReelRadius(11.0, 11.0, target, 5.0));

        // Player at (20.0, 20.0) -> dist = sqrt(10^2 + 10^2) = 14.14 > 5.0 -> FALSE
        assertFalse(trashService.isWithinReelRadius(20.0, 20.0, target, 5.0));
    }
}
