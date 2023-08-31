#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：base_enum.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-03-08 14:40 
"""
from enum import Enum


class EnvEnum(Enum):
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"
