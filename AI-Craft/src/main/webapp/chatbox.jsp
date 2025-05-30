<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Therapist</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Fear effect */
        @keyframes flicker {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }

        .fear-mode {
            background-color: #1a1a1a !important;
            color: white !important;
        }

        .fear-mode .chatbox {
            border: 2px solid red !important;
            box-shadow: 0 0 10px red !important;
            animation: flicker 0.1s infinite alternate;
        }

        .fear-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 0, 0, 0.1);
            pointer-events: none;
            z-index: 10;
            display: none;
        }
    </style>
</head>

<body class="  flex justify-center items-center min-h-screen transition-all duration-500">
<img src="https://www.kapwing.com/resources/content/images/2020/08/video_image-1CTN5yg07.jpeg" class="absolute w-full h-full z-[-1]">
<div class="fear-overlay"></div>

<!-- Sidebar -->
<div class="sticky top-0 z-3 flex h-[10vh] w-full items-center bg-[#FAF9F6] text-gray-700 md:fixed md:left-0 md:top-0 md:h-screen md:w-[13vw] md:flex-col md:items-start md:justify-start">
    <a href="index.jsp" class="ml-4 md:ml-6 md:mt-6">
        <h1 class="text-[4vh] font-bold">AI-Craft.ai</h1>
    </a>
    <div class="ml-auto mr-4 md:ml-6 md:mr-0 md:mt-6 relative group text-mint-500 text-2xl font-thin">
        <h1>about us</h1>
        <div class="invisible absolute top-[10vh] right-0 flex flex-col bg-[#FAF9F6] p-2 opacity-0 transition-all duration-200 group-hover:visible group-hover:opacity-100 md:relative md:top-0 md:right-auto md:flex-col">
            <div class="flex flex-col border-b-2 p-2 md:border-b-0 md:border-l-2">
                <p>Shaurya Mehta</p>
                <p>full stack</p>
            </div>
            <div class="flex flex-col border-b-2 p-2 md:border-b-0 md:border-l-2">
                <p>Raunak Saoji</p>
                <p>AI</p>
            </div>
            <div class="flex flex-col p-2 md:border-l-2">
                <p>Devansh Gauniyal</p>
                <p>AI</p>
            </div>
        </div>
    </div>
</div>

<!-- Main Content -->
<div class="ml-[17vw] flex justify-center w-full">
    <div class="container mx-auto p-6 bg-[#2c2638] shadow-lg rounded-lg w-full max-w-4xl flex flex-col gap-4 transition-all duration-500">
        <!-- Webcam and Emotion Display -->
        <div class="flex flex-col md:flex-row gap-4">
            <div id="webcam" class="w-full md:w-1/2 h-60 bg-gray-200 rounded-lg flex justify-center items-center">
                <p class="text-gray-500">Webcam Feed</p>
            </div>
            <div class="w-full md:w-1/2 flex flex-col items-center justify-center text-center">
                <p class="text-lg font-semibold text-white">Detected Emotion:</p>
                <p id="emotion-text" class="text-9xl mt-2"></p>
            </div>
        </div>

        <!-- Chatbox -->
        <div id="chatbox" class="flex flex-col border rounded-lg p-4 bg-gradient-to-bl from-gray-900 to-gray-800 h-72 overflow-hidden chatbox transition-all duration-500">
            <textarea id="area" disabled class="flex-grow p-2 bg-[#3c364b] text-white rounded-md border resize-none text-xl scroll-auto"></textarea>
            <form id="form" class="mt-2 flex items-center">
                <input type="text" id="text" placeholder="Type a message..." class="flex-grow p-2 rounded-md text-white focus:outline-white focus:outline-2 bg-[#3c364b]">
                <button id="send" class="rounded-2xl bg-[#6d54b5] p-2 pr-5 ml-2 pl-5 text-white hover:cursor-pointer hover:bg-purple-900 transition">
                    Send
                </button>
            </form>
        </div>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/webcamjs/1.0.26/webcam.min.js"></script>
<script src="JavaScript/functionality.js"></script>
</body>
</html>
