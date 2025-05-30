<!doctype html>
<html>
<head>
    <title>Servlets.Login Page</title>
    <link rel="stylesheet" href="./output.css" />
</head>
<body class="">


<div class="sticky top-0 z-3 flex h-[10vh] w-full items-center justify-between bg-[#FAF9F6] text-gray-700">
    <a href="index.jsp"> <h1 class="pl-3 text-[5vh] font-bold">AI-Craft.ai</h1></a>
    <div class="group text-mint-500 mr-4 text-3xl font-thin">
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
<img src="https://cdn.stocksnap.io/img-thumbs/960w/abstract-waves_XYBLVEGDJM.jpg" class="absolute z-[-1] h-full w-full object-cover blur-sm" />
<div class="flex min-h-screen w-full items-center justify-center">
    <div class="flex w-9/10 flex-col-reverse items-center justify-center gap-5 rounded-4xl bg-[#2c2638] p-5 md:flex-row">
        <div class="flex h-[30vh] w-[80vw] rounded-4xl md:h-[90vh] md:w-[70vw]"><img src="https://cdn.stocksnap.io/img-thumbs/960w/abstract-waves_XYBLVEGDJM.jpg" class="rounded-4xl" /></div>
        <div class="flex w-[80vw] flex-col items-center justify-center gap-5 rounded-4xl p-10 pb-2 md:h-[90vh] md:w-[50vw]">
            <h1 class="text-center text-3xl text-[#FAF9F6]">Welcome Back</h1>
            <p class="text-[#FAF9F6]">Enter your username and password to access you account</p>
            <form action="checkLogin" method="post" class="flex flex-col">
                <label class="text-[#FAF9F6]">Name </label>
                <input type="text" required placeholder="your name" name="name" class="rounded-2xl bg-[#3c364b] p-2 text-[#FAF9F6] focus:outline-2 focus:outline-white" />
                <label class="text-[#FAF9F6] mt-2">Password </label>
                <input type="password" required placeholder="your password" name="pwd" class="rounded-2xl bg-[#3c364b] p-2 text-[#FAF9F6] focus:outline-2 focus:outline-white" />
                <input type="submit" value="login" class="mt-5 rounded-2xl bg-[#6d54b5] p-2 pr-5 pl-5 text-white hover:cursor-pointer hover:bg-purple-900" />
            </form>
            <p class="text-sm text-[#FAF9F6]">Dont have an account? <a href="register.jsp" class="text-purple-500">Sign up</a></p>
        </div>
    </div>
</div>
</body>
</html>
