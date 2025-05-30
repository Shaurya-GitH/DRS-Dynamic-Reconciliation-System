function webSocket() {
    console.log("Function called");

    const send = document.getElementById("send");
    const area = document.getElementById("area");
    const form = document.getElementById("form");
    const text = document.getElementById("text");
    const video= document.getElementById("webcam");
    const emotionText= document.getElementById("emotion-text");
    let textReceived = false;
    const socket = new WebSocket("ws://localhost:8080/AI-Craft/socket");
    socket.binaryType="arraybuffer";
    socket.onopen = () => {
        console.log("Connection Secured");
    };
    Webcam.set({
        width: 480,
        height: 240,

        image_format: 'jpeg',
        jpeg_quality: 100,
        force_flash: false
    });
    function base64ToUint8Array(base64) {
        let binaryString = atob(base64.split(',')[1]);
        let bytes = new Uint8Array(binaryString.length);
        for (let i = 0; i < binaryString.length; i++) {
            bytes[i] = binaryString.charCodeAt(i);
        }
        return bytes;
    }
    Webcam.attach(video);
    Webcam.on('live', function () {
        function sendImage() {
            if (textReceived === false) {
                Webcam.snap((data_uri) => {
                    var b = base64ToUint8Array(data_uri);
                    let arr2 = new Uint8Array(1 + b.length);
                    arr2.set([0x02], 0);
                    arr2.set(b, 1);
                    socket.send(arr2.buffer);
                    setTimeout(sendImage, 1000); // Continue sending images after 3 second
                });
            } else {
                setTimeout(sendImage, 1000); // Wait and retry after 1 second
            }
        }
        sendImage(); // Start the loop
    });

    const body = document.body;
    const fearOverlay = document.createElement("div");
    const chatbox = document.getElementById("chatbox");

// Create and style the fear overlay (for red tint)
    fearOverlay.classList.add("fear-overlay");
    fearOverlay.style.position = "fixed";
    fearOverlay.style.top = "0";
    fearOverlay.style.left = "0";
    fearOverlay.style.width = "100%";
    fearOverlay.style.height = "100%";
    fearOverlay.style.background = "rgba(255, 0, 0, 0.1)";
    fearOverlay.style.pointerEvents = "none";
    fearOverlay.style.zIndex = "10";
    fearOverlay.style.display = "none";
    document.body.appendChild(fearOverlay);

// Emotion mapping
    const emotionMap = {
        "happy": "\uD83D\uDE0A",     // 😊
        "sad": "\uD83D\uDE22",       // 😢
        "angry": "\uD83D\uDE20",     // 😠
        "surprised": "\uD83D\uDE32", // 😲
        "neutral": "\uD83D\uDE10",   // 😐
        "fear": "\uD83D\uDE28"       // 😨
    };


// Function to update emotion and UI
    function updateEmotion(emotion) {
        emotionText.innerText = emotionMap[emotion] ||  "\uD83D\uDE36"; // Default 😶

        if (emotion === "fear") {
            body.classList.add("fear-mode");
            chatbox.classList.add("chatbox");
            fearOverlay.style.display = "block";
        } else {
            body.classList.remove("fear-mode");
            chatbox.classList.remove("chatbox");
            fearOverlay.style.display = "none";
        }
    }

    let user=null;
    let session=false;
    socket.onmessage = (event) => {
        if(event.data.startsWith("EMOTION:")){
            let emotion = event.data.replace("EMOTION:", "").trim();
            updateEmotion(emotion);
        }
        else{
            if(session===false){
                java=JSON.parse(event.data);
                user= java.user;
                session=true;
            }
            else{
                java=JSON.parse(event.data);
                area.textContent += `\n[${java.time}] ${java.user}: ${java.name}\n`;
                area.scrollTop = area.scrollHeight;
            }
        }
    };

    var java={
       "name":text.value,
        "time": null,
        "user":null
    };
   window.onload =()=>{
       let a=JSON.stringify(java);
       let t= new TextEncoder();
      let buf=t.encode(a);
      let arr= new Uint8Array(1+buf.length);
      arr.set([0x01],0);
      arr.set(buf,1);
     socket.send(arr.buffer);
   }
    send.addEventListener("click", (event) => {
        event.preventDefault();
        textReceived=true;
        java.name=text.value;
        java.time=new Date().getHours()+":"+ new Date().getMinutes();
        const variable= JSON.stringify(java);
        let en= new TextEncoder();
        let sending=en.encode(variable);
        let arr1= new Uint8Array(1+sending.length);
        arr1.set([0x01],0);
        arr1.set(sending,1);
        socket.send(arr1.buffer);
        area.textContent += `\n[${java.time}] ${user}: ${java.name}\n`;
        area.scrollTop = area.scrollHeight;
        text.value="";
        textReceived=false;
        });
    socket.onclose= ()=>{
        console.log("connection closed");
    }
    socket.onerror=(Event)=>{
        console.log("error: "+Event);
    }
}
webSocket();
