#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   377_Combination_Sum_IV.py
@Time    :   2025/06/26 16:02:01
@Author  :   rj
@Version :   1.0
@Desc    :   组合总和 Ⅳ
"""


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        完全背包排列问题：
        dp[i] 表示和为 i 的排列数。
        状态转移：
            dp[i] += dp[i - num] (for each num in nums if i >= num)
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]
