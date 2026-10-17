package com.oceancleanup.model;

import java.util.Objects;

/**
 * Represents boat upgrade tiers matching OceanCleanup2's progression specs.
 */
public class BoatLevel {
    private final int level;
    private final String name;
    private final int trashNeeded;
    private final int slots;
    private final double speed;

    public BoatLevel(int level, String name, int trashNeeded, int slots, double speed) {
        this.level = level;
        this.name = name;
        this.trashNeeded = trashNeeded;
        this.slots = slots;
        this.speed = speed;
    }

    public int getLevel() {
        return level;
    }

    public String getName() {
        return name;
    }

    public int getTrashNeeded() {
        return trashNeeded;
    }

    public int getSlots() {
        return slots;
    }

    public double getSpeed() {
        return speed;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof BoatLevel that)) return false;
        return level == that.level && trashNeeded == that.trashNeeded && slots == that.slots && Double.compare(that.speed, speed) == 0 && Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(level, name, trashNeeded, slots, speed);
    }

    @Override
    public String toString() {
        return "BoatLevel{" +
                "level=" + level +
                ", name='" + name + '\'' +
                ", trashNeeded=" + trashNeeded +
                ", slots=" + slots +
                ", speed=" + speed +
                '}';
    }
}
