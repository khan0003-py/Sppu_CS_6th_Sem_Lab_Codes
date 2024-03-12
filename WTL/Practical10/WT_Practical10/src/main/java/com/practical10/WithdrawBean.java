package com.practical10;

import jakarta.ejb.LocalBean;
import jakarta.ejb.Stateless;

/**
 * Session Bean implementation class WithdrawBean
 */
@Stateless
@LocalBean
public class WithdrawBean {

    /**
     * Default constructor. 
     */
    public WithdrawBean() {
        // TODO Auto-generated constructor stub
    }
    
    public static void withdrawAmount(double amount) {
    	System.out.println("Withdrawing Amount : "+amount);
    }

}
