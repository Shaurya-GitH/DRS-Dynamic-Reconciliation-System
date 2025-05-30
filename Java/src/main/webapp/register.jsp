<!doctype html>
<html>
<head>
    <title>Servlets.Register</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="./output.css" rel="stylesheet">
</head>
<body class="overflow-x-hidden ">
<div class="sticky top-0 z-3 flex h-[10vh] w-full items-center justify-between bg-[#FAF9F6] text-gray-700">
    <a href="index.jsp"> <h1 class="pl-3 text-[5vh] font-bold">AI-Craft.ai</h1></a>
    <div class="group mr-4 text-3xl font-thin text-mint-500 ">
        <h1>about us</h1>
        <div class="invisible absolute top-[10vh] right-0 flex flex-col bg-[#FAF9F6] p-2 opacity-0 transition-all duration-200 group-hover:visible group-hover:opacity-100 md:flex-row">
            <div class="flex flex-col border-b-2 p-2 md:border-r-2 md:border-b-0">
                <p>Shaurya Mehta</p>
                <p>full stack</p>
            </div>
            <div class="flex flex-col border-b-2 p-2 md:border-r-2 md:border-b-0">
                <p>Raunak Saoji</p>
                <p>AI</p>
            </div>
            <div class="flex flex-col p-2">
                <p>Devansh Gauniyal</p>
                <p>AI</p>
            </div>
        </div>
    </div>
</div>
<div class="w-screen min-h-screen flex justify-center items-center bg-gradient-to-t from-[#646176] to-gray-800">
    <div class="w-9/10  bg-[#2c2638] rounded-4xl flex flex-col-reverse md:flex-row justify-center items-center p-5 ">
        <div >
            <img src="https://cdn.stocksnap.io/img-thumbs/960w/futuristic-circuits_OZPRB0FQZK.jpg" class="rounded-4xl md:h-[90vh] md:w-[70vw]">
        </div>
        <div class="flex flex-col gap-5 items-center justify-center  w-[80vw] rounded-4xl md:h-[90vh] md:w-[50vw]">
            <h1 class="text-white text-6xl p-5 pb-0 font-thin mx-auto">Create an account</h1>
            <p class="text-white">Already have an account? <a href="login.jsp" class="text-purple-500">log in</a> </p>
            <form action="checkRegister" method="post" class="flex flex-col items-center p-5  ">
                <label>
                    <input type="text" required name="name" placeholder="username" class="text-white p-2 rounded-2xl bg-[#3c364b]  focus:outline-2 focus:outline-white ">
                </label><br>
                <label>
                    <input type="password" required name="pwd" placeholder="password" class=" p-2 text-white rounded-2xl bg-[#3c364b] focus:outline-2 focus:outline-white ">
                </label><br>
                <label>
                    <input type="email" required name="email" placeholder="email" class=" p-2 text-white rounded-2xl bg-[#3c364b]  focus:outline-2 focus:outline-white" >
                </label><br>
                <label>
                    <input type="date" required name="dob" class=" p-2 text-white rounded-2xl bg-[#3c364b]  focus:outline-2 focus:outline-white" >
                </label><br>
                <input type="submit" name="Register" class=" pl-5 pr-5 p-2 rounded-2xl bg-[#6d54b5] text-white hover:bg-purple-900 hover:cursor-pointer" >
            </form>
        </div>
    </div>
</div>
</body>
</html>

