package com.practical10;

import jakarta.ejb.LocalBean;
import jakarta.ejb.Stateless;

/**
 * Session Bean implementation class DepositBean
 */
@Stateless
@LocalBean
public class DepositBean {

    /**
     * Default constructor. 
     */
    public DepositBean() {
        // TODO Auto-generated constructor stub
    }
    
    public static void depositAmount(double amount) {
    	System.out.println("Depositing Amount : "+amount);
    }

}
