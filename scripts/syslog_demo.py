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
import re

from pydicom import Dataset


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
    ds = Dataset()
    ds.StudyInstanceUID = "1.2.840.113619.2.340.3.2831184007.204.1564910584.894"
    ds.QueryRetrieveLevel = 'STUDY'
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('192.168.253.192', 514)
    print(socket.AF_INET, socket.SOCK_DGRAM)
    client_name = b"test-pacs"

    client_name = str(client_name, "utf-8")
    ack_msg = f"{client_name} start c-find dataset {str(ds)}"
    msg = f"{udp.getsockname()[0]} AE: {ack_msg}"
    udp.sendto(msg.encode('utf8'), addr)


if __name__ == '__main__':
    main_2()
