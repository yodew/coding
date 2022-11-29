#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：redisDemo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-10-14 11:12 
"""
from datetime import datetime
from time import sleep

import redis
pool = redis.ConnectionPool(host='192.168.253.246', db=1, port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def main():
    lock = r.lock("job_check", timeout=60*60*24)
    acq = lock.acquire(blocking=False)
    if acq:
        print("job can running")
    else:
        print("job is locked")


if __name__ == '__main__':
    for i in range(50):
        print(datetime.now())
        main()
        sleep(1)
