package utility;

import com.google.gson.Gson;
import payloads.Message;

import javax.websocket.Session;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class ReturnText implements Runnable{
    boolean ses;
    Message dat;
    Session session;
    Process p;
    boolean flag=true;
    public ReturnText(boolean ses, Session session, Message dat, Process p){
        this.ses=ses;
        this.dat=dat;
        this.session=session;
        this.p=p;
    }
    @Override
    public void run() {
        Gson gson=new Gson();
        if(ses==false){
            System.out.println("Bot Started");
            dat.setUser((String)session.getUserProperties().get("name"));
            String ret= gson.toJson(dat);
            try {
                session.getBasicRemote().sendText((ret));
                ses=true;
            }catch(Exception e){
                System.out.println(e);
            }

        }
        else {
            try{
                System.out.println("recieved " + dat.getName());
                BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
                bw.write(dat.getName()+"\n");
                bw.flush();
                System.out.println("sent text");
                BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
                StringBuilder sb = new StringBuilder();
                String line;
                if ((line = br.readLine()) != null) {  // Read everything Python sends
                    sb.append(line).append("\n");
                }
                String py = sb.toString().trim();
                System.out.println("reply read");
                dat.setUser("AI-Bot");
                dat.setName(py);
                String ret = gson.toJson(dat);
                session.getBasicRemote().sendText(ret);
            }
            catch (Exception e){
                System.out.println(e.getMessage());
            }
        }
    }
}
