#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：min.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2023-02-15 10:53 
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.main_stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.main_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.main_stack[-1] if self.main_stack else None

    def min(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None


if __name__ == "__main__":
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(-1)
    print(s.top())
    s.pop()
    print(s.top())
    print(s.min())
    s.pop()
    print(s.top())
    print(s.min())


