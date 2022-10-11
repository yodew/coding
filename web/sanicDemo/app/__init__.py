#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-02-28 11:53 
"""

from sanic import Sanic
from sanic_ext import Extend

from app.api import api_bp, ws_bp
from app.ext.init_config import all_config

from app.middlewares.auth import check_auth


def create_app():
    app = Sanic("SanicDemoApp")
    app.config.update_config(all_config)
    app.blueprint([api_bp, ws_bp])
    check_auth(app)
    Extend(app)
    return app


my_app = create_app()
