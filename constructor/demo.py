#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-09-22 9:55 
"""


class A:
    def __call__(self):
        print("A")

    def __init__(self, ):
        ...


if __name__ == "__main__":
    a = A()
    a()
