package com.oceancleanup.service;

import com.oceancleanup.exception.InventoryFullException;
import com.oceancleanup.model.Player;
import com.oceancleanup.model.TrashItem;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Service managing trash gathering, proximity checks, score tabulation, and inventory bounds.
 */
public class TrashCollectionService {

    private final BoatProgressionService boatService;

    public TrashCollectionService(BoatProgressionService boatService) {
        this.boatService = boatService;
    }

    public boolean collectTrash(Player player, TrashItem item) {
        if (player == null || item == null) {
            throw new IllegalArgumentException("Player and TrashItem must not be null");
        }

        int maxCapacity = boatService.getCapacityForPlayer(player);
        if (player.getTrashCount() >= maxCapacity) {
            throw new InventoryFullException(
                    "Cannot collect trash: boat inventory capacity (" + maxCapacity + ") reached."
            );
        }

        player.addTrash(item);
        player.addScore(item.getPoints());
        return true;
    }

    public int calculateTotalScore(List<TrashItem> items) {
        if (items == null || items.isEmpty()) return 0;
        return items.stream().mapToInt(TrashItem::getPoints).sum();
    }

    public double calculateTotalWeight(List<TrashItem> items) {
        if (items == null || items.isEmpty()) return 0.0;
        return items.stream().mapToDouble(TrashItem::getWeight).sum();
    }

    public Map<TrashItem.TrashType, Long> getTrashTypeBreakdown(List<TrashItem> items) {
        if (items == null) return Map.of();
        return items.stream().collect(Collectors.groupingBy(TrashItem::getType, Collectors.counting()));
    }

    public boolean isWithinReelRadius(double playerX, double playerZ, TrashItem item, double radius) {
        if (item == null) return false;
        double dx = playerX - item.getPosX();
        double dz = playerZ - item.getPosZ();
        double distanceSquared = (dx * dx) + (dz * dz);
        return distanceSquared <= (radius * radius);
    }
}
