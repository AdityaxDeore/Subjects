package com.oceancleanup.exception;

/**
 * Thrown when trying to upgrade a boat beyond its maximum supported tier.
 */
public class MaxLevelReachedException extends RuntimeException {
    public MaxLevelReachedException(String message) {
        super(message);
    }
}
