#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-11-07 14:41 
"""
data = {
    "followup_id": "adfb48f45c2d11ed800d0242ac130003",
    "user_id": "f4a712c2bae511ec907e0242ac14000b",
    "detects": [
        "16bb4f5c5c0f11ed815a0242ac130011",
        "d6d1493c5c0e11edaf0a0242ac130011"
    ],
    "stores": [
        "162c50545c0f11ed815a0242ac130011",
        "d63419fa5c0e11edaf0a0242ac130011"
    ],
    "study_days": [
        0,
        343
    ],
    "groups": [
        "ae2e1d6a5c2d11ed800d0242ac130003"
    ],
    "status": "succeed",
    "created": 1667558678,
    "updated": 1667558679
}


def main():
    detects = data["detects"]
    stores = data["stores"]
    new_data = []
    for i in range(len(detects)):
        new_data.append({
            "store_id": stores[i],
            "detect_id": detects[i]
        })
    # new_data = [{"detect_id": d, "store_id": s} for d in detects for s in stores]
    print(new_data)
    return new_data


if __name__ == "__main__":
    main()
