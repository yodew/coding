#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：sanic-demo 
@File    ：gen_city.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-03-03 19:38 
"""
import json


def return_city(item, city_map):
    if "cityList" in item:
        for child_item in item["cityList"]:
            return_city(child_item, city_map)
    else:
        city_map[item["name"]] = item["code"]


def main():
    city_dict = {}
    with open(r"area.json", "r", encoding='UTF-8') as f:
        city_json = f.read()
        for i in json.loads(city_json):
            return_city(i, city_dict)
    print(len(city_dict.keys()))


if __name__ == "__main__":
    main()
