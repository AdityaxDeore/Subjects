package com.oceancleanup.service;

import com.oceancleanup.exception.InvalidGameStateException;
import com.oceancleanup.model.GameState;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Finite State Machine orchestrating game lifecycle and valid phase transitions.
 */
public class GameStateManagerService {

    private GameState currentState;
    private final Map<GameState, List<Runnable>> enterListeners;
    private final Map<GameState, List<Runnable>> exitListeners;

    public GameStateManagerService() {
        this(GameState.LOADING);
    }

    public GameStateManagerService(GameState initialState) {
        this.currentState = initialState;
        this.enterListeners = new HashMap<>();
        this.exitListeners = new HashMap<>();
    }

    public GameState getCurrentState() {
        return currentState;
    }

    public boolean is(GameState state) {
        return this.currentState == state;
    }

    public void transition(GameState newState) {
        if (this.currentState == newState) {
            return; // No-op for same state
        }

        if (!isValidTransition(this.currentState, newState)) {
            throw new InvalidGameStateException(
                    "Illegal state transition from " + this.currentState + " to " + newState
            );
        }

        fireListeners(exitListeners.get(this.currentState));
        GameState prev = this.currentState;
        this.currentState = newState;
        fireListeners(enterListeners.get(this.currentState));
    }

    public boolean isValidTransition(GameState from, GameState to) {
        if (from == null || to == null) return false;
        return switch (from) {
            case LOADING -> to == GameState.PLAYING;
            case PLAYING -> to == GameState.PAUSED || to == GameState.GAMEOVER;
            case PAUSED -> to == GameState.PLAYING || to == GameState.GAMEOVER;
            case GAMEOVER -> to == GameState.PLAYING || to == GameState.LOADING;
        };
    }

    public void addOnEnter(GameState state, Runnable callback) {
        enterListeners.computeIfAbsent(state, k -> new ArrayList<>()).add(callback);
    }

    public void addOnExit(GameState state, Runnable callback) {
        exitListeners.computeIfAbsent(state, k -> new ArrayList<>()).add(callback);
    }

    private void fireListeners(List<Runnable> listeners) {
        if (listeners != null) {
            for (Runnable r : listeners) {
                r.run();
            }
        }
    }
}
