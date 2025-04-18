#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1052_Grumpy_Bookstore_Owner.py
@Time    :   2025/04/18 16:05:57
@Author  :   rj
@Version :   1.0
@Desc    :   爱生气的书店老板
"""

from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # base_satisfied 记录本来就满意的顾客数量（老板不生气时的顾客）
        base_satisfied = 0
        n = len(customers)

        # 第一步：统计老板本来不生气时的满意顾客
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]

        # 第二步：计算初始窗口（前 minutes 分钟内老板生气的情况）
        # 该窗口表示使用技巧让老板在该时间段不生气后，能额外满意的顾客数量
        current_window = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                current_window += customers[i]

        # max_window 用于记录可以通过技巧额外满意的最大顾客数
        max_window = current_window

        # 第三步：使用滑动窗口遍历所有可能的技巧时间段
        for i in range(minutes, n):
            left = i - minutes  # 窗口左端位置

            # 如果当前位置老板原本生气，那么使用技巧可以让这些顾客满意
            if grumpy[i] == 1:
                current_window += customers[i]
            # 如果左边移出窗口的那分钟老板原本是生气的，需要减去之前加上的顾客
            if grumpy[left] == 1:
                current_window -= customers[left]

            # 更新最大可额外满意顾客数
            max_window = max(max_window, current_window)

        # 最终满意的顾客 = 本来就满意的 + 技巧额外带来的
        return base_satisfied + max_window
