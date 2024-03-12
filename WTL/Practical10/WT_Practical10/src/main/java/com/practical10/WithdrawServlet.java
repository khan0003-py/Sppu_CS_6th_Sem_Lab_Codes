package com.practical10;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/withdraw")
public class WithdrawServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		double amount = Double.parseDouble(request.getParameter("amount"));
		WithdrawBean.withdrawAmount(amount);
		response.sendRedirect("success.html");
	}

}
