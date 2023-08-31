#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：base.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-07-20 10:17 
"""
import time

import aioamqp
from aioamqp import channel

queues = [
    {"exchange_name": "aio_msg", "routing_key": "aio_msg_A", "queue_name": "aio_msg_A_queue",
     "msg": "message content AAA"},
    {"exchange_name": "aio_msg", "routing_key": "aio_msg_B", "queue_name": "aio_msg_B_queue",
     "msg": "message content BBB"},
]


async def connect(host="192.168.253.246", port=5672, login="alice", password="wonderland"):
    try:
        transport, protocol = await aioamqp.connect(host, port, login=login,
                                                    password=password)  # use default parameters
        return await protocol.channel()
    except aioamqp.AmqpClosedConnection:
        print("closed connections")
        time.sleep(5)
        return await connect(host)


async def channel_init():
    channel = await connect()
    for queue_arg in queues:
        await channel.exchange(exchange_name=queue_arg["exchange_name"], type_name='direct')
        await channel.queue(queue_name=queue_arg["queue_name"], durable=True, auto_delete=False)
        await channel.queue_bind(exchange_name=queue_arg["exchange_name"],
                                 queue_name=queue_arg["queue_name"],
                                 routing_key=queue_arg["routing_key"]
                                 )
    return channel

