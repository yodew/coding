#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-07-18 14:23 
"""

import asyncio
import logging
import time
from asyncio import sleep

import aioamqp

logger = logging.getLogger()

async def connect(host="192.168.253.246", port=5672, login="alice", password="wonderland"):
    try:
        transport, protocol = await aioamqp.connect(host, port, login=login,
                                                    password=password)  # use default parameters
        return await protocol.channel()
    except aioamqp.AmqpClosedConnection:
        print("closed connections")
        await sleep(5)
        return await connect(host)


async def pub(queue_arg):
    channel = await connect()
    await channel.exchange(exchange_name=queue_arg["exchange_name"], type_name='direct')
    await channel.queue(queue_name=queue_arg["queue_name"], durable=True, auto_delete=False)
    await channel.queue_bind(exchange_name=queue_arg["exchange_name"],
                             queue_name=queue_arg["queue_name"],
                             routing_key=queue_arg["routing_key"]
                             )

    await channel.publish(queue_arg["msg"], exchange_name=queue_arg["exchange_name"],
                          routing_key=queue_arg["routing_key"])





async def main():
    queues = [
        {"exchange_name": "aio_msg", "routing_key": "aio_msg_A", "queue_name": "aio_msg_A_queue",
         "msg": "message content AAA"},
        {"exchange_name": "aio_msg", "routing_key": "aio_msg_B", "queue_name": "aio_msg_B_queue",
         "msg": "message content BBB"},
    ]
    print(f"started at {time.strftime('%X')}")

    for _ in range(5):
        for i in queues:
            await pub(i)


if __name__ == '__main__':
    queues = [
        {"exchange_name": "aio_msg", "routing_key": "aio_msg_A", "queue_name": "aio_msg_A_queue",
         "msg": "message content AAA"},
        {"exchange_name": "aio_msg", "routing_key": "aio_msg_B", "queue_name": "aio_msg_B_queue",
         "msg": "message content BBB"},
    ]

    loop = asyncio.get_event_loop()
    channel = await connect()
    tasks= [consume(channel, queue)for queue in queues]
    loop.create_task()
    try:
        loop.run_forever()
    except KeyboardInterrupt:  # 在本例中，只有Ctrl-C会终止loop，然后像前例中进行善后工作
        print('<Got signal: SIGINT, shutting down.>')
