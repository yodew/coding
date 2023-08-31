#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：best_v.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-12-04 17:55 
"""
from random import randint

n = 10
v = 200
tj = [randint(30, 99) for i in range(n)]
sy = [randint(10, 50) for i in range(n)]


def judge(a):
    k = tjs = sys = 0
    bh = []
    while a != 0:
        temp = a % 2
        if temp == 0:
            tjs += tj[k]
            sys += sy[k]
            pass
        a // 2
        k += 1
    return [tjs, sys, bh]


maxans = maxi = 0

for i in range(1, 2 ** n):
    ans = judge(i)
    if ans[0] <= v and ans[1] > maxans:
        pass
        zybh = ans[2]

for i in zybh:
    print(i, end=',')
