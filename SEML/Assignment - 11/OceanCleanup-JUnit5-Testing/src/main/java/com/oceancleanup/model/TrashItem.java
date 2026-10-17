package com.oceancleanup.model;

import java.util.Objects;

/**
 * Represents ocean trash objects collected during cleanup gameplay.
 */
public class TrashItem {

    public enum TrashType {
        PLASTIC_BOTTLE(10, 0.2, 5),
        OIL_DRUM(50, 5.0, 25),
        WOOD_PLANK(15, 1.0, 8),
        CRATE(30, 3.0, 15),
        OLD_TIRE(25, 2.5, 12),
        GARBAGE_BAG(20, 1.5, 10);

        private final int basePoints;
        private final double weight;
        private final int coinValue;

        TrashType(int basePoints, double weight, int coinValue) {
            this.basePoints = basePoints;
            this.weight = weight;
            this.coinValue = coinValue;
        }

        public int getBasePoints() {
            return basePoints;
        }

        public double getWeight() {
            return weight;
        }

        public int getCoinValue() {
            return coinValue;
        }
    }

    private final String id;
    private final TrashType type;
    private final double posX;
    private final double posZ;

    public TrashItem(String id, TrashType type, double posX, double posZ) {
        this.id = id;
        this.type = type;
        this.posX = posX;
        this.posZ = posZ;
    }

    public String getId() {
        return id;
    }

    public TrashType getType() {
        return type;
    }

    public double getPosX() {
        return posX;
    }

    public double getPosZ() {
        return posZ;
    }

    public int getPoints() {
        return type.getBasePoints();
    }

    public double getWeight() {
        return type.getWeight();
    }

    public int getCoinValue() {
        return type.getCoinValue();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof TrashItem trashItem)) return false;
        return Objects.equals(id, trashItem.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
