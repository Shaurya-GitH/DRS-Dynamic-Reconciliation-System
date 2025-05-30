package websocket;

import Servlets.CheckingEmotion;
import com.google.gson.Gson;
import payloads.Message;
import utility.Config;
import utility.ReturnText;

import javax.websocket.*;
import javax.websocket.server.ServerEndpoint;
import java.io.*;
import java.nio.ByteBuffer;
import java.util.concurrent.*;
import java.util.logging.Level;
import java.util.logging.Logger;

@ServerEndpoint(value = "/socket", configurator = Config.class)
public class WebSocketServer {
    private static final Logger LOGGER = Logger.getLogger(WebSocketServer.class.getName());
    private volatile Process p;
    private Process p2;
    private volatile boolean ses = false;
    private volatile CheckingEmotion thread;

    private final ExecutorService executor = new ThreadPoolExecutor(
            2,
            5,
            60L,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(100),
            new ThreadPoolExecutor.CallerRunsPolicy()
    );

    @OnOpen
    public void onOpen(Session session) {
        LOGGER.info(() -> "WebSocket Opening: " + session.getId());

        try {
            // Increase buffer size with safety check
            int maxBufferSize = 5 * 1024 * 1024;
            session.setMaxBinaryMessageBufferSize(maxBufferSize);
            session.setMaxTextMessageBufferSize(maxBufferSize);
            LOGGER.info(() -> "Buffer Size Set: " + session.getMaxBinaryMessageBufferSize());

            // Start Python process with timeout
            String python = "C:/Users/lenovo/PycharmProjects/Facial-Emotion-Recognition-using-OpenCV-and-Deepface/.venv/Scripts/python.exe";
            String scriptPath = "C:\\Users\\lenovo\\PycharmProjects\\Facial-Emotion-Recognition-using-OpenCV-and-Deepface\\usage.py";
            String textPath= "C:\\Users\\lenovo\\PycharmProjects\\Facial-Emotion-Recognition-using-OpenCV-and-Deepface\\Emotion_detector.py";
            //starting text process


            ProcessBuilder pb1= new ProcessBuilder(python,textPath);
            p2= pb1.start();
            ProcessBuilder pb = new ProcessBuilder(python, scriptPath);
            pb.redirectErrorStream(true); // Capture error stream

            // Start the process
            p = pb.start();


            // Start a thread to read and log Python process output
            new Thread(() -> {
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        LOGGER.info("Python Process Output: " + line);
                    }
                } catch (IOException e) {
                    LOGGER.log(Level.SEVERE, "Error reading Python process output", e);
                }
            }).start();

            // Start checking emotion thread
            thread = new CheckingEmotion(session);
            Thread t = new Thread(thread);
            t.setUncaughtExceptionHandler((th, ex) -> {
                LOGGER.log(Level.SEVERE, "Uncaught exception in checking emotion thread", ex);
            });
            t.start();

            LOGGER.info("WebSocket Open Complete");
        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "Error initializing WebSocket", e);
            // Attempt to close the session if initialization fails
            try {
                session.close();
            } catch (IOException ioException) {
                LOGGER.log(Level.SEVERE, "Error closing session", ioException);
            }
        }
    }

    @OnMessage
    public void binaryMessage(ByteBuffer data, Session session) {
        // Validate input
        if (data == null || !data.hasRemaining()) {
            LOGGER.warning("Received empty or null message");
            return;
        }

        try {
            byte messageType = data.get();
            int len = data.remaining();

            LOGGER.info(() -> String.format("Received message. Type: %02X, Length: %d", messageType, len));

            if (messageType == 0x01) {
                // Text message handling
                processTextMessage(data, len, session);
            } else {
                // Image message handling
                processImageMessage(data, len);
            }

        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "Error processing binary message", e);
        }
    }

    private void processTextMessage(ByteBuffer data, int len, Session session) {
        byte[] str = new byte[len];
        data.get(str);
        String rec = new String(str);

        executor.submit(() -> {
            try {
                LOGGER.info(() -> "Processing text message: " + rec);
                Gson gson = new Gson();
                Message dat = gson.fromJson(rec, Message.class);
                ReturnText rt = new ReturnText(ses, session, dat,p2);
                Thread t2 = new Thread(rt);
                t2.setUncaughtExceptionHandler((th, ex) -> {
                    LOGGER.log(Level.SEVERE, "Error in text return thread", ex);
                });
                t2.start();
                ses = true;
                LOGGER.info("Text message processing completed");
            } catch (Exception e) {
                LOGGER.log(Level.SEVERE, "Error processing text message", e);
            }
        });
    }

    private void processImageMessage(ByteBuffer data, int len) {
        // Create a copy of the byte data to prevent concurrent modification
        byte[] file = new byte[len];
        data.get(file);

        executor.submit(() -> {
            try {
                try (FileOutputStream fos = new FileOutputStream("C:\\Users\\lenovo\\Desktop\\debug_image.jpg")) {
                    fos.write(file);
                }
                LOGGER.info(() -> "Processing image. Size: " + file.length + " bytes");

                // Check if process is alive
                if (!p.isAlive()) {
                    LOGGER.severe("Python process has terminated unexpectedly");
                    return;
                }

                // Get the output stream with error handling
                OutputStream pythonInput = p.getOutputStream();

                // Send the image size first (4 bytes)
                byte[] sizeBytes = ByteBuffer.allocate(4).putInt(file.length).array();
                pythonInput.write(sizeBytes);

                // Send the image data
                pythonInput.write(file);
                pythonInput.flush();

                LOGGER.info("Image sent successfully");
            } catch (IOException e) {
                LOGGER.log(Level.SEVERE, "Error sending image", e);

                // Additional diagnostics
                if (p != null) {
                    LOGGER.info("Process alive status: " + p.isAlive());
                    try {
                        int exitValue = p.exitValue();
                        LOGGER.severe("Process exit value: " + exitValue);
                    } catch (IllegalThreadStateException ex) {
                        LOGGER.info("Process is still running");
                    }
                }
            }
        });
    }

    @OnClose
    public void onClose(Session session) {
        LOGGER.info("WebSocket Closing");

        // Graceful shutdown sequence
        try {
            // Stop checking emotion thread
            if (thread != null) {
                thread.stopThread();
            }

            // Shutdown executor
            executor.shutdown();
            if (!executor.awaitTermination(10, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }

            // Forcibly terminate Python process
            if (p != null) {
                p.destroyForcibly();
            }
        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "Error during WebSocket closure", e);
        } finally {
            LOGGER.info("WebSocket Closed");
        }
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        LOGGER.log(Level.SEVERE, "WebSocket critical error", throwable);

        // Attempt to close the session
        try {
            if (session.isOpen()) {
                session.close();
            }
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Error closing session after error", e);
        }
    }
}