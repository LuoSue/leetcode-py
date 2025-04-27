#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   279_Perfect_Squares.py
@Time    :   2025/04/27 11:29:15
@Author  :   rj 
@Version :   1.0
@Desc    :   完全平方数问题的动态规划解法
"""

class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化一个 dp 数组，dp[i] 表示组成 i 的完全平方数的最小数量
        dp = [n + 1] * (n + 1)
        dp[0] = 0  # 0 需要 0 个完全平方数
        
        # 遍历每一个数字 i，从 1 到 n
        for i in range(1, n + 1):
            # 对每一个 i，尝试每一个小于等于 i 的平方数 j*j
            j = 1
            while j * j <= i:
                # 更新 dp[i] 为当前 dp[i] 和 dp[i - j*j] + 1 的最小值
                # dp[i - j*j] 表示构成 i - j*j 的最小平方数数量，加上 1 表示用 j*j 来构成当前 i
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        # 返回 dp[n]，即组成 n 的最小完全平方数的数量
        return dp[n]
