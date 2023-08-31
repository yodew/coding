#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-07-18 15:41 
"""
import contextlib
import time


@contextlib.contextmanager
def timeit(title):
    print('1...')
    start = time.time()
    yield
    print('2...')
    end = time.time()
    usedTime = (end - start) * 1000
    print('Use time %d ms' % usedTime)


with timeit("zhangsan") as t:
    a = dowm(123)

