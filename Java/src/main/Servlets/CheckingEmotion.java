package Servlets;

import javax.websocket.Session;
import java.io.BufferedReader;
import java.io.FileReader;

public class CheckingEmotion implements Runnable {
    Session a=null;
    String emotion;
    boolean running= true;
    public CheckingEmotion(Session session){
      a  = session;
    }
    @Override
    public void run() {
        while(running){
            try (BufferedReader em = new BufferedReader(new FileReader("C:/Users/lenovo/Desktop/emotion.txt"))){
                emotion= em.readLine();
                a.getBasicRemote().sendText("EMOTION:"+emotion);
                Thread.sleep(1000);
            }catch (Exception e){
                System.out.println(e.getMessage());
                running=false;
                break;
            }
        }
    }
    public void stopThread(){
        running=false;
    }
}
