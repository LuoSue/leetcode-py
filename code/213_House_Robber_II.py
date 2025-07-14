#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   213_House_Robber_II.py
@Time    :   2025/04/27 11:05:46
@Author  :   rj
@Version :   1.0
@Desc    :   打家劫舍 II - 解法
             房屋排成一个环形，不能同时抢第一间和最后一间
"""

from typing import List

class Solution:
    def simple_rob(self, nums: List[int]) -> int:
        # f0 表示不抢当前房屋时的最大金额
        # f1 表示抢当前房屋时的最大金额
        f0 = f1 = 0

        for num in nums:
            # 状态转移：
            # f0变为上一个f1（即不抢当前房屋）
            # f1更新为当前的最大值（抢当前房屋或者不抢）
            f0, f1 = f1, max(f1, f0 + num)

        return f1  # 返回最大收益

    def rob(self, nums: List[int]) -> int:
        # 特殊情况：只有一家，直接抢
        if len(nums) == 1:
            return nums[0]

        # 环形处理：不能同时抢第一家和最后一家
        # 所以分两种情况取最大值：
        # 1. 抢第1到倒数第2家（不抢最后一家）
        # 2. 抢第2到最后一家（不抢第一家）
        return max(self.simple_rob(nums[1:]), self.simple_rob(nums[:-1]))
