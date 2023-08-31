#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo
@File    ：__init__.py.py
@IDE     ：PyCharm
@Author  ：lu.yu
@Date    ：2022-02-28 11:53
"""
import asyncio
import json
import os

from consul import Consul as SyncConsul
from consul.aio import Consul
from sanic import Sanic
from sanic_ext import Extend
from tortoise.contrib.sanic import register_tortoise

from app.api import api_bp, ws_bp
from app.middlewares.auth import check_auth


def load_config_from_consul(current_app):
    consul = SyncConsul(host=os.environ['CONSUL_HOST'], port=os.environ["CONSUL_PORT"])
    index, data = consul.kv.get("config/sanic/dev", index=None)
    val = data['Value'].decode("utf-8")
    obj = json.loads(val)
    current_app.config.update(obj)


app = Sanic("SanicDemoApp")
load_config_from_consul(app)
register_tortoise(app, db_url=app.config['MYSQL_URL'], modules={"models": ["models"]},
                  generate_schemas=False)
app.blueprint([api_bp, ws_bp])
check_auth(app)
Extend(app)


@app.main_process_start
async def update_config_from_consul(current_app):
    """
    Load config from Consul.
    Pings the Consul service every 30 or so seconds for changes

    This version will look for a single config entry for the entire app.  Whenever something
    of it changes, it'll reload the entire thing.  The config should be stored as json, for easy parsing.
    """
    consul = Consul(host=os.environ['CONSUL_HOST'], port=os.environ["CONSUL_PORT"], loop=current_app.loop)

    index = None
    while True:
        index, data = await consul.kv.get("config/sanic/dev", index=index)
        if bool(data):
            val = data['Value'].decode("utf-8")
            obj = json.loads(val)
            current_app.config.update(obj)
            print("consul:config:App Updated")
            await asyncio.sleep(5)


@app.after_server_start
async def before_server_start_task(app):
    """
    添加服务开始前的任务
    :param app:
    :return:
    """
    app.add_task(update_config_from_consul)


async def after_server_start_task(app):
    """
    添加服务开始后的任务
    :param app:
    :return:
    """


if __name__ == "__main__":
    app.run(port=8181, host="127.0.0.1", debug=True, workers=4, access_log=True)
