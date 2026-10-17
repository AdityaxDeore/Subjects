package com.oceancleanup.service;

import com.oceancleanup.model.MarineCreature;
import com.oceancleanup.model.Player;

/**
 * Service managing wildlife capture ball interactions, rescue scoring, and companion mechanics.
 */
public class WildlifeRescueService {

    public boolean attemptRescue(Player player, MarineCreature creature, double throwDistance) {
        if (player == null || creature == null) {
            throw new IllegalArgumentException("Player and creature must not be null");
        }
        if (throwDistance < 0) {
            throw new IllegalArgumentException("Throw distance cannot be negative");
        }

        // Hit detection based on creature size and hitbox radius
        if (throwDistance <= creature.getHitboxRadius()) {
            player.addCaughtCreature(creature);
            player.addScore(creature.getRescueScore());
            return true;
        }

        return false;
    }

    public boolean assignCompanion(Player player, MarineCreature creature) {
        if (player == null || creature == null) {
            throw new IllegalArgumentException("Arguments must not be null");
        }

        // Must already be rescued before becoming a companion
        if (!player.getCaughtCreatures().contains(creature)) {
            return false;
        }

        if (player.getActiveCompanion() != null) {
            player.getActiveCompanion().setCompanion(false);
        }

        creature.setCompanion(true);
        player.setActiveCompanion(creature);
        return true;
    }

    public void dismissCompanion(Player player) {
        if (player == null) return;
        if (player.getActiveCompanion() != null) {
            player.getActiveCompanion().setCompanion(false);
            player.setActiveCompanion(null);
        }
    }
}
