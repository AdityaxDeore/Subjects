package com.oceancleanup;

import com.oceancleanup.model.MarineCreature;
import com.oceancleanup.model.Player;
import com.oceancleanup.service.WildlifeRescueService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.EnumSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("WildlifeRescueService Test Suite")
class WildlifeRescueServiceTest {

    private WildlifeRescueService rescueService;
    private Player player;

    @BeforeEach
    void setUp() {
        rescueService = new WildlifeRescueService();
        player = new Player("MarineProtector");
    }

    @Test
    @DisplayName("Should successfully rescue creature when throw distance is within hitbox radius")
    void testSuccessfulCreatureRescue() {
        MarineCreature dolphin = new MarineCreature("d_01", MarineCreature.Species.DOLPHIN);
        // Dolphin scale is 4.0 -> hitbox radius = 4.0 * 4 = 16.0
        double throwDistance = 12.0;

        boolean rescued = rescueService.attemptRescue(player, dolphin, throwDistance);

        assertAll("Dolphin Rescue Validation",
                () -> assertTrue(rescued, "Rescue attempt should succeed within 16.0m radius"),
                () -> assertTrue(player.getCaughtCreatures().contains(dolphin)),
                () -> assertEquals(300, player.getScore(), "Dolphin rescue awards 300 points")
        );
    }

    @Test
    @DisplayName("Should fail rescue when throw distance falls outside creature hitbox radius")
    void testFailedRescueDueToDistance() {
        MarineCreature clownfish = new MarineCreature("c_01", MarineCreature.Species.CLOWNFISH);
        // Clownfish scale = 1.0 -> hitbox = 4.0
        double throwDistance = 8.5; // Missed

        boolean rescued = rescueService.attemptRescue(player, clownfish, throwDistance);

        assertAll("Missed Rescue State",
                () -> assertFalse(rescued, "Throw exceeded hitbox radius"),
                () -> assertFalse(player.getCaughtCreatures().contains(clownfish)),
                () -> assertEquals(0, player.getScore(), "No points awarded on missed attempt")
        );
    }

    @ParameterizedTest(name = "Species {0}")
    @EnumSource(MarineCreature.Species.class)
    @DisplayName("Parameterized Test: Verify scale and positive rescue points across all marine species")
    void testAllSpeciesAttributes(MarineCreature.Species species) {
        MarineCreature creature = new MarineCreature("creature_" + species.name(), species);
        assertAll("Species Attribute Check",
                () -> assertTrue(creature.getHitboxRadius() > 0.0),
                () -> assertTrue(creature.getRescueScore() > 0),
                () -> assertNotNull(creature.getCustomNickname())
        );
    }

    @Test
    @DisplayName("Should successfully assign a rescued creature as active companion")
    void testAssignCompanionSuccess() {
        MarineCreature turtle = new MarineCreature("t_01", MarineCreature.Species.SEA_TURTLE, "Shelly");
        // Rescue first
        rescueService.attemptRescue(player, turtle, 2.0);

        boolean assigned = rescueService.assignCompanion(player, turtle);

        assertAll("Companion Assignment",
                () -> assertTrue(assigned),
                () -> assertTrue(turtle.isCompanion()),
                () -> assertEquals(turtle, player.getActiveCompanion())
        );
    }

    @Test
    @DisplayName("Should reject companion assignment if creature has not been rescued first")
    void testCannotAssignUnrescuedCompanion() {
        MarineCreature wildWhale = new MarineCreature("w_01", MarineCreature.Species.BLUE_WHALE);

        boolean assigned = rescueService.assignCompanion(player, wildWhale);

        assertFalse(assigned, "Cannot set wild unrescued animal as companion");
        assertNull(player.getActiveCompanion());
        assertFalse(wildWhale.isCompanion());
    }

    @Test
    @DisplayName("Should cleanly replace active companion when player switches to another creature")
    void testCompanionSwitching() {
        MarineCreature turtle = new MarineCreature("t_01", MarineCreature.Species.SEA_TURTLE);
        MarineCreature dolphin = new MarineCreature("d_01", MarineCreature.Species.DOLPHIN);

        rescueService.attemptRescue(player, turtle, 1.0);
        rescueService.attemptRescue(player, dolphin, 1.0);

        rescueService.assignCompanion(player, turtle);
        assertTrue(turtle.isCompanion());

        // Switch to dolphin
        rescueService.assignCompanion(player, dolphin);

        assertAll("Companion Swap Verification",
                () -> assertFalse(turtle.isCompanion(), "Old companion must be deactivated"),
                () -> assertTrue(dolphin.isCompanion(), "New companion must be active"),
                () -> assertEquals(dolphin, player.getActiveCompanion())
        );
    }

    @Test
    @DisplayName("Should dismiss active companion leaving player with no active companion")
    void testDismissCompanion() {
        MarineCreature turtle = new MarineCreature("t_01", MarineCreature.Species.SEA_TURTLE);
        rescueService.attemptRescue(player, turtle, 1.0);
        rescueService.assignCompanion(player, turtle);

        rescueService.dismissCompanion(player);

        assertNull(player.getActiveCompanion());
        assertFalse(turtle.isCompanion());
    }
}
