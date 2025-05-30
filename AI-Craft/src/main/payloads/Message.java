package payloads;

public class Message {
    private String name;
    private String time;
    private String user;
    public String getName(){
        return this.name;
    }
    public void setName(String name){
        this.name=name;
    }

    public String getTime() {
        return time;
    }
    void setTime(String time){
        this.time=time;
    }

    public String getUser() {
        return user;
    }
    public void setUser(String user){
        this.user=user;
    }
}
