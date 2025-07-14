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
        # f0 表示不抢当前房屋时的最大金额
        # f1 表示抢当前房屋时的最大金额
        f0 = f1 = 0

        for num in nums:
            # 状态转移：
            # f0变为上一个f1（即不抢当前房屋）
            # f1更新为当前的最大值（抢当前房屋或者不抢）
            f0, f1 = f1, max(f1, f0 + num)

        return f1  # 返回最大收益
