package com.practical10;

import javax.ejb.LocalBean;
import javax.ejb.Stateless;

@Stateless
@LocalBean
public class WithdrawBean {

    public WithdrawBean() {
        // Default constructor
    }

    public static void withdrawAmount(double amount) {
        // Business logic for withdrawal
        // Example: Update account balance by subtracting the withdrawn amount
        // In a real-world scenario, you would interact with a database or external service
        System.out.println("Withdrawing amount: " + amount);
        // Update account balance in the database or any other storage mechanism
    }
}
