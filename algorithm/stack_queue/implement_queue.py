#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：queue.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2023-02-14 16:24 
"""
from collections import deque


class CQueue(object):
    """
    一个栈实现，用双端链表实现
    """
    def __init__(self):
        self.queue = deque([])

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        try:
            return self.queue.popleft()
        except IndexError:
            return -1


class BQueue:
    """
    两个栈实现队列，一个进， 一个出
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, val):
        self.in_stack.append(val)

    def deleteHead(self):
        if self.out_stack:
            return self.out_stack.pop()
        if not self.in_stack:
            return -1
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

# Your CQueue object will be instantiated and called as such:
if __name__ == "__main__":
    obj = BQueue()
    obj.appendTail(1)
    param_2 = obj.deleteHead()
    param_3 = obj.deleteHead()
