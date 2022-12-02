#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：path_constants.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-03-08 15:40 
"""
import os

from app.common.constants.env_constants import CONF_SERVER_ENV
from pathlib import Path

APP_PATH = Path(".")

YAML_DIR = APP_PATH.joinpath("app/conf", CONF_SERVER_ENV.lower())

BASE_CONF_YAML_PATH = YAML_DIR.joinpath("base_conf.yml")
