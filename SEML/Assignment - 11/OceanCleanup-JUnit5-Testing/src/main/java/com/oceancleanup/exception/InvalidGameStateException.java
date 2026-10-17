package com.oceancleanup.exception;

/**
 * Thrown when an illegal state transition is attempted on the game lifecycle.
 */
public class InvalidGameStateException extends RuntimeException {
    public InvalidGameStateException(String message) {
        super(message);
    }
}
