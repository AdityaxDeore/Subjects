package com.oceancleanup.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Player model tracking gold, energy, score, inventory, boat level, and companions.
 */
public class Player {
    private final String username;
    private int score;
    private int gold;
    private double energy;
    private int boatLevel;
    private final List<TrashItem> trashInventory;
    private final List<MarineCreature> caughtCreatures;
    private MarineCreature activeCompanion;

    public Player(String username) {
        this(username, 0, 0, 100.0, 1);
    }

    public Player(String username, int score, int gold, double energy, int boatLevel) {
        this.username = username;
        this.score = score;
        this.gold = gold;
        this.energy = Math.max(0.0, Math.min(100.0, energy));
        this.boatLevel = Math.max(1, Math.min(4, boatLevel));
        this.trashInventory = new ArrayList<>();
        this.caughtCreatures = new ArrayList<>();
        this.activeCompanion = null;
    }

    public String getUsername() {
        return username;
    }

    public int getScore() {
        return score;
    }

    public void addScore(int points) {
        if (points > 0) {
            this.score += points;
        }
    }

    public int getGold() {
        return gold;
    }

    public void addGold(int amount) {
        if (amount > 0) {
            this.gold += amount;
        }
    }

    public boolean deductGold(int amount) {
        if (amount <= 0) return false;
        if (this.gold >= amount) {
            this.gold -= amount;
            return true;
        }
        return false;
    }

    public double getEnergy() {
        return energy;
    }

    public void setEnergy(double energy) {
        this.energy = Math.max(0.0, Math.min(100.0, energy));
    }

    public void restoreEnergy(double amount) {
        if (amount > 0) {
            this.energy = Math.min(100.0, this.energy + amount);
        }
    }

    public void drainEnergy(double amount) {
        if (amount > 0) {
            this.energy = Math.max(0.0, this.energy - amount);
        }
    }

    public int getBoatLevel() {
        return boatLevel;
    }

    public void setBoatLevel(int boatLevel) {
        this.boatLevel = Math.max(1, Math.min(4, boatLevel));
    }

    public List<TrashItem> getTrashInventory() {
        return Collections.unmodifiableList(trashInventory);
    }

    public int getTrashCount() {
        return trashInventory.size();
    }

    public void addTrash(TrashItem item) {
        if (item != null) {
            this.trashInventory.add(item);
        }
    }

    public List<TrashItem> clearTrash() {
        List<TrashItem> emptied = new ArrayList<>(this.trashInventory);
        this.trashInventory.clear();
        return emptied;
    }

    public List<MarineCreature> getCaughtCreatures() {
        return Collections.unmodifiableList(caughtCreatures);
    }

    public void addCaughtCreature(MarineCreature creature) {
        if (creature != null && !caughtCreatures.contains(creature)) {
            caughtCreatures.add(creature);
        }
    }

    public MarineCreature getActiveCompanion() {
        return activeCompanion;
    }

    public void setActiveCompanion(MarineCreature activeCompanion) {
        this.activeCompanion = activeCompanion;
    }
}
