package com.oceancleanup.model;

import java.util.Objects;

/**
 * Represents catchable and companion marine wildlife in OceanCleanup.
 */
public class MarineCreature {

    public enum Species {
        CLOWNFISH(1.0, 1.0, 50),
        SEA_TURTLE(2.5, 1.5, 150),
        DOLPHIN(4.0, 2.0, 300),
        MANTA_RAY(5.0, 2.5, 450),
        BLUE_WHALE(10.0, 5.0, 1000);

        private final double scale;
        private final double catchDifficulty;
        private final int rescuePoints;

        Species(double scale, double catchDifficulty, int rescuePoints) {
            this.scale = scale;
            this.catchDifficulty = catchDifficulty;
            this.rescuePoints = rescuePoints;
        }

        public double getScale() {
            return scale;
        }

        public double getCatchDifficulty() {
            return catchDifficulty;
        }

        public int getRescuePoints() {
            return rescuePoints;
        }
    }

    private final String id;
    private final Species species;
    private final String customNickname;
    private boolean isCompanion;

    public MarineCreature(String id, Species species) {
        this(id, species, species.name());
    }

    public MarineCreature(String id, Species species, String customNickname) {
        this.id = id;
        this.species = species;
        this.customNickname = customNickname;
        this.isCompanion = false;
    }

    public String getId() {
        return id;
    }

    public Species getSpecies() {
        return species;
    }

    public String getCustomNickname() {
        return customNickname;
    }

    public boolean isCompanion() {
        return isCompanion;
    }

    public void setCompanion(boolean companion) {
        isCompanion = companion;
    }

    public int getRescueScore() {
        return species.getRescuePoints();
    }

    public double getHitboxRadius() {
        return species.getScale() * 4.0;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof MarineCreature that)) return false;
        return Objects.equals(id, that.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
