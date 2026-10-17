package com.oceancleanup.service;

import com.oceancleanup.exception.MaxLevelReachedException;
import com.oceancleanup.model.BoatLevel;
import com.oceancleanup.model.Player;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Service managing boat upgrade tiers, speed curves, and inventory storage capacities.
 */
public class BoatProgressionService {

    public static final int MAX_BOAT_LEVEL = 4;
    private static final Map<Integer, BoatLevel> TIERS;

    static {
        Map<Integer, BoatLevel> map = new LinkedHashMap<>();
        map.put(1, new BoatLevel(1, "Small Fishing Boat", 0, 20, 12.0));
        map.put(2, new BoatLevel(2, "Hanger Boat", 5, 40, 15.0));
        map.put(3, new BoatLevel(3, "Large Vessel", 10, 70, 18.0));
        map.put(4, new BoatLevel(4, "House Boat", 15, 120, 20.0));
        TIERS = Collections.unmodifiableMap(map);
    }

    public BoatLevel getBoatLevel(int level) {
        if (!TIERS.containsKey(level)) {
            throw new IllegalArgumentException("Invalid boat tier requested: " + level);
        }
        return TIERS.get(level);
    }

    public Map<Integer, BoatLevel> getAllTiers() {
        return TIERS;
    }

    public int getMaxLevel() {
        return MAX_BOAT_LEVEL;
    }

    public int getCapacityForPlayer(Player player) {
        if (player == null) throw new IllegalArgumentException("Player cannot be null");
        return getBoatLevel(player.getBoatLevel()).getSlots();
    }

    public double getSpeedForPlayer(Player player) {
        if (player == null) throw new IllegalArgumentException("Player cannot be null");
        return getBoatLevel(player.getBoatLevel()).getSpeed();
    }

    public boolean canUpgrade(Player player) {
        if (player == null) return false;
        int currentLevel = player.getBoatLevel();
        if (currentLevel >= MAX_BOAT_LEVEL) {
            return false;
        }
        BoatLevel nextTier = TIERS.get(currentLevel + 1);
        return player.getTrashCount() >= nextTier.getTrashNeeded();
    }

    public BoatLevel upgradeBoat(Player player) {
        if (player == null) {
            throw new IllegalArgumentException("Player cannot be null");
        }
        int currentLevel = player.getBoatLevel();
        if (currentLevel >= MAX_BOAT_LEVEL) {
            throw new MaxLevelReachedException("Boat is already at maximum level " + MAX_BOAT_LEVEL);
        }
        BoatLevel nextTier = TIERS.get(currentLevel + 1);
        if (player.getTrashCount() < nextTier.getTrashNeeded()) {
            throw new IllegalStateException("Insufficient trash collected to upgrade. Needed: " 
                    + nextTier.getTrashNeeded() + ", Current: " + player.getTrashCount());
        }

        player.setBoatLevel(nextTier.getLevel());
        return nextTier;
    }
}
