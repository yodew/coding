#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：lottery.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2023/8/22 16:20 
"""
import random


def main():
    people_set = set(range(1, 301))
    award = {
        "三等奖：三斤苹果""三等奖：三斤苹果": 30,
        "二等奖：iPhone14手机": 6,
        "一等奖：泰国5日游+手术费报销": 3
    }
    for k, v in award.items():
        print(f"{k}\n获奖名单如下：")
        result = random.sample(people_set, v)
        people_set -= set(result)
        print(result)


if __name__ == "__main__":
    main()
