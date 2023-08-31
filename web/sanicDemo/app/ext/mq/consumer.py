#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：consumer.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-07-19 18:04 
"""
import asyncio


from base import queues, channel_init


async def consume(queue):
    channel = await channel_init()
    await channel.basic_consume(callback, queue["queue_name"], no_ack=False)


async def callback(channel, body, envelope, properties):
    await asyncio.sleep(2)
    print(body, envelope.delivery_tag)
    try:
        await channel.basic_client_ack(delivery_tag=envelope.delivery_tag)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    consumers = [loop.create_task(consume(queue))for queue in queues]
    # 这里与前几个例子一样，将coroutine添加到loop中
    try:
        loop.run_forever()
    except KeyboardInterrupt:  # 在本例中，只有Ctrl-C会终止loop，然后像前例中进行善后工作
        print('<Got signal: SIGINT, shutting down.>')
