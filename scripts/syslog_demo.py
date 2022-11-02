#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：syslog_demo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-10-31 14:58 
"""
import logging
import logging.handlers  # handlers要单独import


def main():
    logger = logging.getLogger()
    fh = logging.handlers.SysLogHandler(('192.168.253.192', 514))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.warning("start")
    logger.info("start")


def main_2():
    import socket
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(socket.AF_INET, socket.SOCK_DGRAM)
    client_name = "dn-pacs"
    action = "c-find start"
    ack_msg = f"{client_name} {action}"
    addr = ('192.168.253.192', 514)
    udp.sendto(ack_msg.encode('utf8'), addr)


if __name__ == '__main__':
    main_2()
