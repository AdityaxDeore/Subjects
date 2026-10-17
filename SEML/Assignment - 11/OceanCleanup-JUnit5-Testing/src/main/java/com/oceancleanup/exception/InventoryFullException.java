package com.oceancleanup.exception;

/**
 * Thrown when attempting to collect trash beyond the boat's inventory capacity.
 */
public class InventoryFullException extends RuntimeException {
    public InventoryFullException(String message) {
        super(message);
    }
}
