#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   155_Min_Stack.py
@Time    :   2025/05/12 17:38:18
@Author  :   rj
@Version :   1.0
@Desc    :   最小栈
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    # 每当push()新值进来时，如果 小于等于 min_stack 栈顶值，则一起 push() 到 min_stack，即更新了栈顶最小值；
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    # 判断将 pop() 出去的元素值是否是 min_stack 栈顶元素值（即最小值），
    # 如果是则将 min_stack 栈顶元素一起 pop()，这样可以保证 min_stack 栈顶元素始终是 stack 中的最小值。
    def pop(self) -> None:
        if self.stack.pop() == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
