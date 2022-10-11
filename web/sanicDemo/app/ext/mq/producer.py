#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：producer.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-07-20 10:27 
"""
import asyncio

from base import connect, queues, channel_init


async def publish(queue):
    channel = await channel_init()
    await channel.publish(queue["msg"], exchange_name=queue["exchange_name"],
                          routing_key=queue["routing_key"])

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    tasks = [publish(queue)for queue in queues]
    loop.run_until_complete(asyncio.wait(tasks))
