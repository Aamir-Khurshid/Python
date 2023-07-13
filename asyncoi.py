import requests
import asyncio


async def function1():
    url = "https://www.wallpaperflare.com/cherry-blossom-tree-on-cliff-digital-wallpaper-cherry-blossom-on-cliff-mountain-wallpaper-gn"
    response = requests.get(url)
    open("image1.jpg", "wb").write(response.content)
    print("fun1")

async def function2():
    url = "https://www.wallpaperflare.com/vector-forest-sunset-forest-nature-sky-atmosphere-darkness-wallpaper-cvfha"
    response = requests.get(url)
    open("image2.jpg", "wb").write(response.content)
    print("fun2")

async def function3():
    url = "https://www.wallpaperflare.com/bare-tree-and-desert-wallpaper-bald-tree-under-blue-sky-illustration-wallpaper-ae"
    response = requests.get(url)
    open("image3.jpg", "wb").write(response.content)
    print("fun3")
async def main():
    #await function1()
    #await function2()
    #await function3()
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
asyncio.run(main())