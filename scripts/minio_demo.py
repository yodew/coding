#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：minio_demo.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-11-11 17:41 
"""
import hashlib
from datetime import timedelta

import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

def read_in_chunks(file_path, chunk_size=1024 * 2048):
    """
    分割文件
    :param filepath:
    :param chunk_size:
    :return:
    """
    with open(file_path, 'rb') as file:
        while True:
            chunk_data = file.read(chunk_size)
            if not chunk_data:
                break
            yield chunk_data

def demo(object_name, file_path):
    from minio import Minio
    minioClient = Minio('192.168.253.246:9000',
                        access_key='minio',
                        secret_key='miniostorage',
                        secure=False)

    upload_url = minioClient.presigned_put_object('dnstore',
                                      object_name,
                                      expires=timedelta(days=3))
    for ch in read_in_chunks(file_path):
        md = hashlib.md5()
        md.update(ch)
        md5code = md.hexdigest()
        header = {'Content-Type': 'application/octet-stream; charset=UTF-8',
                  "Content-MD5": md5code}

        response = s.put(upload_url, ch, headers=header)

if __name__ == '__main__':
    a = [{"a": "1"}, {"a": "4"}]
    b = ["4", "1"]
    a = sorted(a, key=lambda x: b.index(x["a"]))
    print(a)
    # demo("test/presigned/abab", "practicalsaas.pdf")