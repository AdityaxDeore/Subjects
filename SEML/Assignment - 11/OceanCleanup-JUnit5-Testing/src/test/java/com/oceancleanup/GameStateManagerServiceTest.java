package com.oceancleanup;

import com.oceancleanup.exception.InvalidGameStateException;
import com.oceancleanup.model.GameState;
import com.oceancleanup.service.GameStateManagerService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import java.util.concurrent.atomic.AtomicBoolean;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("GameStateManagerService Test Suite")
class GameStateManagerServiceTest {

    private GameStateManagerService stateManager;

    @BeforeEach
    void setUp() {
        stateManager = new GameStateManagerService();
    }

    @Test
    @DisplayName("Should initialize in LOADING state by default")
    void testInitialStateIsLoading() {
        assertEquals(GameState.LOADING, stateManager.getCurrentState());
        assertTrue(stateManager.is(GameState.LOADING));
    }

    @Test
    @DisplayName("Should execute valid normal game lifecycle progression")
    void testValidLifecycleProgression() {
        // LOADING -> PLAYING
        stateManager.transition(GameState.PLAYING);
        assertEquals(GameState.PLAYING, stateManager.getCurrentState());

        // PLAYING -> PAUSED
        stateManager.transition(GameState.PAUSED);
        assertEquals(GameState.PAUSED, stateManager.getCurrentState());

        // PAUSED -> PLAYING (resume)
        stateManager.transition(GameState.PLAYING);
        assertEquals(GameState.PLAYING, stateManager.getCurrentState());

        // PLAYING -> GAMEOVER
        stateManager.transition(GameState.GAMEOVER);
        assertEquals(GameState.GAMEOVER, stateManager.getCurrentState());

        // GAMEOVER -> PLAYING (restart)
        stateManager.transition(GameState.PLAYING);
        assertEquals(GameState.PLAYING, stateManager.getCurrentState());
    }

    @ParameterizedTest(name = "From {0} to {1} should be illegal")
    @CsvSource({
            "LOADING, PAUSED",
            "LOADING, GAMEOVER",
            "GAMEOVER, PAUSED"
    })
    @DisplayName("Parameterized Test: Verify illegal state transitions throw InvalidGameStateException")
    void testIllegalStateTransitions(GameState from, GameState to) {
        GameStateManagerService manager = new GameStateManagerService(from);

        InvalidGameStateException ex = assertThrows(InvalidGameStateException.class, () ->
                manager.transition(to)
        );

        assertTrue(ex.getMessage().contains("Illegal state transition"));
        assertEquals(from, manager.getCurrentState(), "State must remain unchanged after illegal transition attempt");
    }

    @Test
    @DisplayName("Should trigger enter and exit callbacks during valid transitions")
    void testTransitionCallbacks() {
        AtomicBoolean exitedLoading = new AtomicBoolean(false);
        AtomicBoolean enteredPlaying = new AtomicBoolean(false);

        stateManager.addOnExit(GameState.LOADING, () -> exitedLoading.set(true));
        stateManager.addOnEnter(GameState.PLAYING, () -> enteredPlaying.set(true));

        stateManager.transition(GameState.PLAYING);

        assertTrue(exitedLoading.get(), "Exit callback for LOADING must be fired");
        assertTrue(enteredPlaying.get(), "Enter callback for PLAYING must be fired");
    }

    @Test
    @DisplayName("Should treat transitioning to the same state as safe no-op")
    void testSameStateTransitionIsNoOp() {
        stateManager.transition(GameState.PLAYING);
        assertDoesNotThrow(() -> stateManager.transition(GameState.PLAYING));
        assertEquals(GameState.PLAYING, stateManager.getCurrentState());
    }
}
