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
        """
        动态规划思路：

        假设 f(n) 表示爬到第 n 阶楼梯的方法数。
        每次可以选择爬 1 阶或 2 阶。

        要爬到第 n 阶，可以从：
            - 第 n-1 阶爬 1 阶上来，有 f(n-1) 种方法；
            - 第 n-2 阶爬 2 阶上来，有 f(n-2) 种方法。

        所以状态转移方程为：
            f(n) = f(n-1) + f(n-2)

        初始条件：
            f(1) = 1  # 只有一种方式：爬 1 阶
            f(2) = 2  # 两种方式：1+1 或 2

        为了优化空间，我们只保存前两项，使用滚动变量实现。
        """

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
        for i in range(3, n + 1):
            # 当前阶梯的走法数等于前两阶的走法数之和
            cur = prev2 + prev1
            # 更新前两阶的走法数
            prev2 = prev1
            prev1 = cur

        # 返回第n阶楼梯的走法数
        return prev1
