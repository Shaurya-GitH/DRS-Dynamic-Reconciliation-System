package Servlets;

import org.mindrot.jbcrypt.BCrypt;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/checkLogin")
public class CheckLogin extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException{
        String name= req.getParameter("name");
        String password= req.getParameter("pwd");
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn= DriverManager.getConnection("jdbc:mysql://localhost:3306/mysql","root","shaurya");
            PreparedStatement ps= conn.prepareStatement("Select name,password from users where name=?");
            ps.setString(1,name);
            ResultSet rs= ps.executeQuery();
            if(rs.next()){
                boolean isCorrect= BCrypt.checkpw(password,rs.getString("password"));
                if(isCorrect){
                    HttpSession hs= req.getSession();
                    hs.setAttribute("name",name);
                    resp.sendRedirect("chatbox");
                }
                else{
                    incorrect(req,resp);
                }
            }
            else{
                incorrect(req,resp);
            }
        }
        catch (Exception e){
            System.out.print(e);
        }

    }
    void incorrect(HttpServletRequest req,HttpServletResponse resp) throws IOException,ServletException{
        RequestDispatcher rd= req.getRequestDispatcher("login.jsp");
        PrintWriter pw= resp.getWriter();
        resp.setContentType("text/html");
        pw.print("<h3 style='color:red'>incorrect username or password</h3>");
        rd.include(req,resp);
    }
}
