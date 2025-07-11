#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2466_Count_Ways_To_Build_Good_Strings.py
@Time    :   2025/07/11 17:28:11
@Author  :   rj
@Version :   1.0
@Desc    :   统计构造好字符串的方案数
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7  # 定义取模的常量，防止结果过大
        dp = [0] * (high + 1)  # dp[i] 表示构造长度为 i 的字符串的方案数
        dp[0] = 1  # 空字符串是一种合法的初始情况

        for i in range(high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]  # 如果可以添加 zero 个 '0'，累加前面的方案
            if i >= one:
                dp[i] += dp[i - one]  # 如果可以添加 one 个 '1'，累加前面的方案
            dp[i] %= MOD  # 每次都取模，防止溢出

        # 统计所有长度在 [low, high] 范围内的字符串方案总数
        return sum(dp[low : high + 1]) % MOD
