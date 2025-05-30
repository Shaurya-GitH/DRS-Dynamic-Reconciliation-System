package utility;
import org.mindrot.jbcrypt.BCrypt;

public class HashGenerator  {
    public static String generateHash(String pwd) {
        String pwd_hash= BCrypt.hashpw(pwd,BCrypt.gensalt(12));
        return pwd_hash;

    }
}
