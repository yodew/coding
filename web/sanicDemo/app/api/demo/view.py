#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：view.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-10-11 17:08 
"""

from sanic import Blueprint
from sanic.response import text
from sanic.views import HTTPMethodView

sample_view_bp = Blueprint('sample_view')


class SimpleView(HTTPMethodView):
    async def get(self, request):
        return text("Hi 😎 this is get view")

    async def post(self, request):
        return text("Hi 😎 this is post view")


sample_view_bp.add_route(SimpleView.as_view(), "/sample_view")
