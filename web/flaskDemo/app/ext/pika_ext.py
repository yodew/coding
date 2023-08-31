#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：base.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-09-19 13:47 
"""
import pika
from pika import DeliveryMode
from pika.exceptions import AMQPConnectionError
from pika.exchange_type import ExchangeType
from retry import retry


class PikaInit(object):
    def __init__(self, url, exchanges, heartbeat, connection_timeout):
        self.parameters = pika.URLParameters(url)
        self.parameters._heartbeat = int(heartbeat) if heartbeat is not None else 600
        self.parameters._blocked_connection_timeout = int(connection_timeout) if connection_timeout is not None else 300
        self.exchanges = exchanges
        self.connection = None
        self.channel = None
        self.heartbeat = heartbeat

    @retry(AMQPConnectionError, tries=5, delay=5, jitter=(1, 3))
    def create_connection(self):
        conn = pika.BlockingConnection(self.parameters)
        self.connection = conn
        self.channel = self.connection.channel()

    def check_connection(self):
        if self.connection is None or not self.connection.is_open:
            self.create_connection()

    def queues_declare(self):
        """
        脚本运行前调用
        :return:
        """
        self.check_connection()
        for exchange in self.exchanges:
            # 声明交换机
            self.channel.exchange_declare(exchange=exchange["exchange_name"],
                                          exchange_type=exchange.get("exchange_type", ExchangeType.direct),
                                          durable=True)
            for queue in exchange["queues"]:
                # 声明队列
                self.channel.queue_declare(queue=queue["queue_name"], auto_delete=True, durable=True,
                                           arguments={"x-max-priority": queue.get("max_priority", 0)})
                # 绑定队列
                self.channel.queue_bind(
                    queue=queue["queue_name"], exchange=exchange["exchange_name"], routing_key=queue["routing_key"])
        self.connection.close()

    def publish(self, exchange, routing_key, body):
        self.check_connection()
        self.channel.basic_publish(exchange, routing_key, body.encode("utf-8"),
                                   properties=pika.BasicProperties(content_type="application/json",
                                                                   delivery_mode=DeliveryMode.Transient
                                                                   ),
                                   mandatory=False
                                   )
        self.connection.close()

    def consume(self, queue):
        self.check_connection()
        self.channel.basic_qos(prefetch_count=queue.get("prefetch_count", 4))
        self.channel.basic_consume(queue=queue["queue_name"], on_message_callback=self.on_message, auto_ack=False)

    def on_message(self, channel, method, properties, body):
        print(body)
        channel.basic_ack(delivery_tag=method.delivery_tag)
