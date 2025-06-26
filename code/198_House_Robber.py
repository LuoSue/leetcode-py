#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   198_House_Robber.py
@Time    :   2025/04/27 10:52:47
@Author  :   rj
@Version :   1.0
@Desc    :   打家劫舍问题 (House Robber Problem)
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 如果只有一个房子，直接返回这个房子的金额
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        # prev2 表示抢劫当前房子之前，最大能抢到的钱（相当于前两间房子）
        prev2 = 0
        # prev1 表示抢劫当前房子的前一间房子，或者前两间房子的最大值
        prev1 = 0

        # 从第一个房子开始，依次判断每个房子是否抢劫
        for i in range(n):
            # 对于每个房子，选择是抢劫它（prev2 + nums[i]）还是跳过它（prev1）
            current = max(prev1, prev2 + nums[i])
            # 更新 prev2 和 prev1 为下次循环做准备
            prev2 = prev1
            prev1 = current

        # 返回最终的最大抢劫金额（即最后一次计算的 prev1）
        return prev1
