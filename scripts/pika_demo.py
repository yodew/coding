#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：pika_demo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-11-10 17:09 
"""

import ssl

import pika


def main():
    credentials = pika.PlainCredentials("alice", "wonderland")
    context = ssl.create_default_context(
        cafile="ca_certificate.pem")

    context.check_hostname = False
    # context.set_ciphers("ALL")
    context.load_cert_chain("client_certificate.pem", "client_key.pem", password="rabbit")
    ssl_options = pika.SSLOptions(context)

    parameters = pika.ConnectionParameters(
        host="192.168.40.10",
        port=5671,
        virtual_host="/",
        credentials=credentials,
        heartbeat=0,
        ssl_options=ssl_options
    )
    with pika.BlockingConnection(parameters) as conn:
        ch = conn.channel()
        ch.queue_declare("foobar")
        ch.basic_publish("", "foobar", "Hello, world!")
        print(ch.basic_get("foobar"))


def main2():
    credentials = pika.PlainCredentials("alice", "wonderland")
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context.verify_mode = ssl.CERT_REQUIRED
    # context.check_hostname = False
    # context.set_ciphers("ALL")
    context.load_verify_locations("ca_certificate.pem")
    # context.load_verify_locations("client_certificate.pem", "client_key.pem")
    #
    parameters = pika.ConnectionParameters(
        host="192.168.253.2",
        port=5671,
        virtual_host="/",
        credentials=credentials,
        heartbeat=0,
        ssl_options=pika.SSLOptions(context)
    )
    parameters = pika.ConnectionParameters(ssl_options = pika.SSLOptions(context))
    with pika.BlockingConnection(parameters) as conn:
        ch = conn.channel()
        ch.queue_declare("foobar")
        ch.basic_publish("", "foobar", "Hello, world!")
        print(ch.basic_get("foobar"))


if __name__ == "__main__":
    main()
