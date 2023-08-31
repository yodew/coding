#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：consul.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-03-08 18:09 
"""

import uuid

from consul.aio import Consul as BaseConsul


class ConsulClient(object):

    def __init__(self, *args, **kwargs):
        self.host = kwargs["host"]
        self.port = kwargs["port"]
        self.scheme = kwargs.get("scheme", "http")
        self.consul = BaseConsul(host=self.host, port=self.port, scheme=self.scheme)
        self.service_id = uuid.uuid4()

    async def register(self, service_name, service_id, interval="10s"):
        response = await self.consul.agent.service.register(
            name=service_name,
            service_id=service_id,
            interval=interval,
            tags=["sanic脚手架"],
            port=8181,
            check=self.consul.agent.check
        )

    async def deregister(self) -> bool:
        response = await self.consul.agent.service.deregister()
        return response

    async def get_remote_config(self):
        return self.consul.kv.get()


consul_client = ConsulClient(host="192.168.253.246", port=8500, scheme="http")

if __name__ == "__main__":
    print(uuid.uuid4())
    # result = consul_client.register()
    # kv = consul_client.get_config()
    print(1)
