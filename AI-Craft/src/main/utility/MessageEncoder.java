package utility;

import com.google.gson.Gson;
import payloads.Message;

import javax.websocket.EncodeException;
import javax.websocket.Encoder;
import javax.websocket.EndpointConfig;

public class MessageEncoder implements Encoder.Text<Message> {
        private static Gson gson= new Gson();

        @Override
        public void init(EndpointConfig endpointConfig) {

        }

        @Override
        public void destroy() {

        }

        @Override
        public String encode(Message message) throws EncodeException {
                return gson.toJson(message);
        }
}
