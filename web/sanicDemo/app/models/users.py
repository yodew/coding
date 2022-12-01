#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：users.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-11-30 14:01 
"""
from tortoise import Model, fields


class UsersModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(30)

    class Meta:
        table = "users_111"
        table_description = "用户表"

