#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：feed.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-10-11 16:15 
"""
from sanic import Blueprint

ws_bp = Blueprint("ws")


@ws_bp.websocket("/feed")
async def feed(request, ws):
    while True:
        data = "hello!"
        print("Sending: " + data)
        await ws.send(data)
        data = await ws.recv()
        print("Received: " + data)
