package Servlets;

import utility.HashGenerator;

import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;
import javax.servlet.http.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

@WebServlet("/checkRegister")
public class CheckRegister extends HttpServlet {
    @Override
            protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn= DriverManager.getConnection("jdbc:mysql://localhost:3306/mysql","root","shaurya");
            String username= req.getParameter("name");
            String password= HashGenerator.generateHash(req.getParameter("pwd"));
            String email= req.getParameter("email");
            String dob=req.getParameter("dob");
            Date date = new SimpleDateFormat("yyyy-MM-dd", Locale.ENGLISH).parse(dob);

            PreparedStatement ps= conn.prepareStatement("SELECT name from users where name=? ");
            ps.setString(1,username);
            ResultSet rs= ps.executeQuery();
            if(rs.next()){
                        resp.setContentType("text/html");
                        RequestDispatcher rd= req.getRequestDispatcher("register.jsp");
                        PrintWriter pw= resp.getWriter();
                        pw.print("<h3 style='color:red'>Username already exists </h3>");
                        rd.include(req,resp);
                }
            else{
                PreparedStatement ins=conn.prepareStatement("insert into users values(?,?,?,?)");
                ins.setString(1,username);
                ins.setString(2,password);
                ins.setString(3,email);
                ins.setDate(4,new java.sql.Date(date.getTime()));
                ins.executeUpdate();
                resp.setContentType("text/html");
                RequestDispatcher rd= req.getRequestDispatcher("login.jsp");
                PrintWriter pw= resp.getWriter();
                pw.print("<h3 style='color:green'>Account created </h3>");
                rd.include(req,resp);
            }
        }
        catch (Exception e){
            System.out.print(e);
        }

    }
}
