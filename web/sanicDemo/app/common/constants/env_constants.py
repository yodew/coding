#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：env_constants.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-03-14 15:05 
"""
import os
# 服务环境
CONF_SERVER_ENV = os.environ.get("SERVER_ENV") if os.environ.get("SERVER_ENV") else ""
# consul配置
CONF_CONSUL_HOST = os.environ.get("CONSUL_HOST") if os.environ.get("CONSUL_HOST") else ""
CONF_CONSUL_PORT = os.environ.get("CONSUL_PORT") if os.environ.get("CONSUL_PORT") else None
