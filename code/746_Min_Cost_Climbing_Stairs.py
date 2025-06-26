#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   746_Min_Cost_Climbing_Stairs.py
@Time    :   2025/06/26 15:47:32
@Author  :   rj
@Version :   1.0
@Desc    :   使用最小花费爬楼梯
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        动态规划思路：

        定义 dp[i] 为到达第 i 阶台阶的最小花费。
        由于每次可以跨 1 或 2 个台阶，
        则状态转移方程为：
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        初始状态：
            dp[0] = 0  # 起点前一步，不花费
            dp[1] = 0  # 可以从下标 1 开始，不花费

        目标是到达下标为 len(cost) 的顶层。
        """

        n = len(cost)
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for i in range(2, n + 1):
            cur = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = cur

        return prev1
