#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：pendulum_demo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-10-18 17:19 
"""
import pendulum


def main():
    # 今天
    today = pendulum.today()
    print(today)
    # 昨天
    yesterday = pendulum.yesterday()
    print(yesterday)
    # 今天-昨天相差的秒数
    print(today.diff(yesterday).in_seconds())
    # 今天-昨天相差的天数
    print(today.diff(yesterday).in_days())
    # 时间转字符串
    print(today.to_datetime_string())
    # 转日期字符串
    print(today.to_date_string())
    # 年份+2
    target = today.add(years=2)
    print(target)
    # 年份-1
    target2 = target.subtract(years=1)
    print(target2)
    # 下个周一的日期
    print(target2.next(pendulum.TUESDAY))
    # 计算年龄
    print(pendulum.datetime(2000, 1, 1).age)
    # 计算2000-1-1 到此时的中间时间
    print(pendulum.datetime(2000, 1, 1).average())


if __name__ == '__main__':
    main()

