import websockets
from sanic import Blueprint, Sanic
from sanic.response import json


hello_bp = Blueprint("hello", version=1)
hello_bp2 = Blueprint("hello2", version=2)


@hello_bp.route("/hello")
async def hello(request):
    uri = "ws://127.0.0.1:8181/feed"
    async with websockets.connect(uri) as ws:
        # 发送给服务端的信息
        message = "hello"
        print(f"发送给服务端的信息：{message}")
        await ws.send(message)
        # 接收服务端的信息
        bytes_data = await ws.recv()

        # bytes 转 string
        str_data = str(bytes_data)
        print("接收来自服务端的信息:{}".format(str_data))

    return json({"content": "hello"})


@hello_bp2.route("/hello")
async def hello2(request):
    app = Sanic.get_app()
    return json({"content": app.config.get("X_TEST", "")})
