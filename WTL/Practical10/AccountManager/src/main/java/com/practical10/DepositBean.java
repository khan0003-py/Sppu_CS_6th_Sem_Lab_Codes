package com.practical10;

import javax.ejb.EJB;
import javax.ejb.LocalBean;
import javax.ejb.Stateless;

@Stateless
@LocalBean
@EJB
public class DepositBean {

    public DepositBean() {
        // Default constructor
    }

    public static void depositAmount(double amount) {
        // Business logic for deposit
        // Example: Update account balance by adding the deposited amount
        // In a real-world scenario, you would interact with a database or external service
        System.out.println("Depositing amount: " + amount);
        // Update account balance in the database or any other storage mechanism
    }
}
