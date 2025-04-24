#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   739_Daily_Temperatures.py
@Time    :   2025/04/24 11:39:05
@Author  :   rj 
@Version :   1.0
@Desc    :   每日温度
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 初始化结果数组，默认值为0，表示如果之后没有更高温度，则为0
        result = [0] * len(temperatures)
        # 使用栈保存下标，用于找到下一个比当前温度高的日子
        stack = []
        
        # 遍历温度数组，i是当前的索引，x是当前温度
        for i, x in enumerate(temperatures):
            # 如果栈不为空，且当前温度比栈顶对应的温度高
            while stack and temperatures[stack[-1]] < x:
                # 弹出栈顶索引
                current = stack.pop()
                # 计算当前天之后多少天温度升高，并存入结果数组
                result[current] = i - current
            # 将当前索引压入栈中
            stack.append(i)
        
        # 返回最终结果
        return result
