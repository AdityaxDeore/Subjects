package com.oceancleanup.service;

import com.oceancleanup.exception.InsufficientFundsException;
import com.oceancleanup.model.Player;
import com.oceancleanup.model.TrashItem;

import java.util.List;

/**
 * Service managing in-game economy, recycling plant transactions, energy replenishment, and food consumption.
 */
public class EconomyAndRecyclingService {

    public static final int FOOD_COST = 15;
    public static final double FOOD_ENERGY_RESTORE = 50.0;
    public static final double MAX_ENERGY = 100.0;
    public static final double ENERGY_DRAIN_PER_SECOND = 0.3; // Game tick consumption

    public int recycleAllTrash(Player player) {
        if (player == null) throw new IllegalArgumentException("Player cannot be null");
        List<TrashItem> items = player.clearTrash();
        if (items.isEmpty()) return 0;

        int earnedGold = items.stream().mapToInt(TrashItem::getCoinValue).sum();
        player.addGold(earnedGold);
        return earnedGold;
    }

    public boolean purchaseFood(Player player) {
        if (player == null) throw new IllegalArgumentException("Player cannot be null");

        if (player.getEnergy() >= MAX_ENERGY) {
            return false; // Already full energy, cannot buy food unnecessarily
        }

        if (player.getGold() < FOOD_COST) {
            throw new InsufficientFundsException(
                    "Insufficient gold to purchase food. Cost: " + FOOD_COST + ", Balance: " + player.getGold()
            );
        }

        player.deductGold(FOOD_COST);
        player.restoreEnergy(FOOD_ENERGY_RESTORE);
        return true;
    }

    public void restAndSleep(Player player) {
        if (player == null) throw new IllegalArgumentException("Player cannot be null");
        player.setEnergy(MAX_ENERGY);
    }

    public void applyEnergyDrain(Player player, double deltaSeconds) {
        if (player == null || deltaSeconds <= 0) return;
        double drain = deltaSeconds * ENERGY_DRAIN_PER_SECOND;
        player.drainEnergy(drain);
    }
}
