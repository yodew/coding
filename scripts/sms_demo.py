#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：sms_demo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-11-15 17:57 
"""
import os

from ronglian_sms_sdk import SmsSDK


def main():
    sdk = SmsSDK("8aaf0708659e8e420165a81674eb068d", "399635f9dce8466bbf03f3103b4e04e0", "8aaf0708659e8e420165a83c02bc06a9")
    sdk.sendMessage(tid="323287", mobile="15501525803", datas=(123123, 5))

os.listdir("")

if __name__ == '__main__':
    main()