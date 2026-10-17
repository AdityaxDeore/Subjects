package com.oceancleanup;

import com.oceancleanup.exception.InsufficientFundsException;
import com.oceancleanup.model.Player;
import com.oceancleanup.model.TrashItem;
import com.oceancleanup.service.EconomyAndRecyclingService;
import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("EconomyAndRecyclingService Test Suite")
class EconomyAndRecyclingServiceTest {

    private EconomyAndRecyclingService economyService;
    private Player player;

    @BeforeEach
    void setUp() {
        economyService = new EconomyAndRecyclingService();
        player = new Player("Captain_Aditya");
    }

    @Test
    @DisplayName("Should recycle collected trash into gold and empty the player's inventory")
    void testRecycleAllTrashConvertsToGold() {
        // Collect 1 OIL_DRUM (25 coins) and 1 PLASTIC_BOTTLE (5 coins)
        player.addTrash(new TrashItem("t1", TrashItem.TrashType.OIL_DRUM, 0, 0));
        player.addTrash(new TrashItem("t2", TrashItem.TrashType.PLASTIC_BOTTLE, 0, 0));

        int earned = economyService.recycleAllTrash(player);

        assertAll("Recycling Transaction Results",
                () -> assertEquals(30, earned, "Earned gold should be 25 + 5 = 30"),
                () -> assertEquals(30, player.getGold(), "Player wallet must reflect 30 gold"),
                () -> assertEquals(0, player.getTrashCount(), "Inventory must be completely emptied")
        );
    }

    @Test
    @DisplayName("Should return 0 gold when attempting to recycle an empty inventory")
    void testRecycleEmptyInventory() {
        int earned = economyService.recycleAllTrash(player);
        assertEquals(0, earned);
        assertEquals(0, player.getGold());
    }

    @Test
    @DisplayName("Should successfully purchase food when gold is sufficient and replenish energy")
    void testPurchaseFoodSuccess() {
        player.addGold(30);
        player.setEnergy(40.0);

        boolean purchased = economyService.purchaseFood(player);

        assertAll("Food Purchase Execution",
                () -> assertTrue(purchased, "Purchase should succeed"),
                () -> assertEquals(15, player.getGold(), "30 - 15 = 15 gold remaining"),
                () -> assertEquals(90.0, player.getEnergy(), 0.001, "40 + 50 = 90 energy")
        );
    }

    @Test
    @DisplayName("Should cap restored energy at maximum 100.0 without overflow")
    void testPurchaseFoodEnergyCap() {
        player.addGold(50);
        player.setEnergy(80.0);

        economyService.purchaseFood(player);

        assertEquals(100.0, player.getEnergy(), 0.001, "Energy should cap at 100.0");
    }

    @Test
    @DisplayName("Should refuse food purchase without deducting gold when energy is already 100.0")
    void testPurchaseFoodWhenFullEnergy() {
        player.addGold(50);
        player.setEnergy(100.0);

        boolean purchased = economyService.purchaseFood(player);

        assertFalse(purchased, "Should not purchase food when energy is 100");
        assertEquals(50, player.getGold(), "Gold balance should remain intact");
    }

    @Test
    @DisplayName("Should throw InsufficientFundsException when player lacks 15 gold for food")
    void testPurchaseFoodThrowsInsufficientFunds() {
        player.addGold(14); // Exactly 1 gold below threshold
        player.setEnergy(50.0);

        InsufficientFundsException ex = assertThrows(InsufficientFundsException.class, () ->
                economyService.purchaseFood(player)
        );

        assertTrue(ex.getMessage().contains("Insufficient gold"));
        assertEquals(14, player.getGold(), "Gold must not be deducted on failed transaction");
        assertEquals(50.0, player.getEnergy(), "Energy must remain unchanged");
    }

    @Test
    @DisplayName("Should fully restore energy to 100.0 upon resting/sleeping")
    void testRestAndSleepRestoration() {
        player.setEnergy(10.0);

        economyService.restAndSleep(player);

        assertEquals(100.0, player.getEnergy(), 0.001);
    }

    @RepeatedTest(value = 5, name = "Drain cycle repetition {currentRepetition} of {totalRepetitions}")
    @DisplayName("Repeated Test: Verifying steady energy drain across delta time intervals")
    void testRepeatedEnergyDrain() {
        player.setEnergy(50.0);
        economyService.applyEnergyDrain(player, 10.0); // 10s * 0.3 = 3.0 drain

        assertEquals(47.0, player.getEnergy(), 0.001);
    }

    @Test
    @DisplayName("Should never allow energy to drop below 0.0 during intense drain")
    void testEnergyCannotDropBelowZero() {
        player.setEnergy(2.0);
        economyService.applyEnergyDrain(player, 100.0); // Drain far exceeds 2.0

        assertEquals(0.0, player.getEnergy(), 0.001, "Energy must clamp at 0.0 floor");
    }

    @Test
    @Disabled("Pending micro-banking and loan features slated for OceanCleanFlow v3.0 release")
    @DisplayName("Disabled Test: Ocean Micro-Finance / Bank Loan Feature (v3.0 Future Roadmap)")
    void testBankLoanFacility() {
        // Feature under development
        fail("Should not execute disabled test");
    }
}
