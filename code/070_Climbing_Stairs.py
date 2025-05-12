#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   070_Climbing_Stairs.py
@Time    :   2025/05/12 22:47:51
@Author  :   rj
@Version :   1.0
@Desc    :   爬楼梯
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 如果只有1阶楼梯，只有一种走法
        if n == 1:
            return 1
        # 如果有2阶楼梯，有两种走法（一次走1阶，或者一次走2阶）
        if n == 2:
            return 2

        # 初始化前两阶楼梯的走法数
        prev2 = 1  # 第1阶楼梯的走法数
        prev1 = 2  # 第2阶楼梯的走法数

        # 从第3阶开始，逐步计算每阶的走法数
        for i in range(2, n):
            # 当前阶梯的走法数等于前两阶的走法数之和
            cur = prev2 + prev1
            # 更新前两阶的走法数
            prev2 = prev1
            prev1 = cur

        # 返回第n阶楼梯的走法数
        return prev1
