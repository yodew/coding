#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：auth.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-03-08 10:42 
"""


def check_auth(app):
    @app.on_request
    async def run_before_handler(request):
        request.ctx.user = "123"
