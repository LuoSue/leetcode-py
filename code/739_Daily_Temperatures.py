#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   739_Daily_Temperatures.py
@Time    :   2025/04/24 11:39:05
@Author  :   rj
@Version :   1.1
@Desc    :   每日温度 - 包含正向遍历和反向遍历两种解法
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        正向遍历 + 单调栈（栈中存储递减温度对应的索引）
        每遇到更高的温度，就更新栈顶元素对应的等待天数
        """
        result = [0] * len(temperatures)
        stack = []

        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                current = stack.pop()
                result[current] = i - current
            stack.append(i)

        return result

    def dailyTemperaturesReverse(self, temperatures: List[int]) -> List[int]:
        """
        反向遍历 + 单调栈（栈中存储递增温度对应的索引）
        从后往前找下一个比当前温度高的日子
        """
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # 弹出所有小于等于当前温度的索引
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            # 如果栈不为空，说明栈顶是第一个更高温度的日子
            if stack:
                result[i] = stack[-1] - i
            # 当前索引入栈
            stack.append(i)

        return result
