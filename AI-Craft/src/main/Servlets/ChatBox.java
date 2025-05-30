package Servlets;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/chatbox")
public class ChatBox extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest res, HttpServletResponse resp) throws ServletException, IOException {
        RequestDispatcher rd= res.getRequestDispatcher("chatbox.jsp");
        rd.forward(res,resp);
    }

}
