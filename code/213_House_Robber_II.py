#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   213_House_Robber_II.py
@Time    :   2025/04/27 11:05:46
@Author  :   rj 
@Version :   1.0
@Desc    :   打家劫舍 II - 解法
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 辅助函数，解决普通的打家劫舍问题（房子排列成一条线）
        def simple_rob(nums):
            n = len(nums)

            # 如果只有一座房子，直接返回它的金额
            if n == 1:
                return nums[0]

            # 初始化前两个房子的金额：prev2 (房子 0)，prev1 (房子 0 和房子 1 中的较大值)
            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])

            # 从第三座房子开始，遍历每一座房子
            for i in range(2, n):
                # 对每一座房子，决定是抢还是不抢
                current = max(prev1, prev2 + nums[i])
                prev2 = prev1  # 将前两座房子的结果往前移
                prev1 = current

            # 返回能抢到的最大金额
            return prev1

        # 如果只有一座房子，直接返回它的金额
        n = len(nums)
        if n == 1:
            return nums[0]

        # 情况 1：抢除了最后一座房子以外的所有房子
        case1 = simple_rob(nums[:-1])
        
        # 情况 2：抢除了第一座房子以外的所有房子
        case2 = simple_rob(nums[1:])

        # 返回两种情况中的最大值
        return max(case1, case2)
