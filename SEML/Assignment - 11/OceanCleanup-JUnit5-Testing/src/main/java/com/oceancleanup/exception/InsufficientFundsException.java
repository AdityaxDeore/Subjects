package com.oceancleanup.exception;

/**
 * Thrown when an economy transaction fails due to inadequate gold.
 */
public class InsufficientFundsException extends RuntimeException {
    public InsufficientFundsException(String message) {
        super(message);
    }
}
