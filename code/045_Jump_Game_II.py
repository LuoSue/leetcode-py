#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   045_Jump_Game_II.py
@Time    :   2025/05/12 22:39:58
@Author  :   rj
@Version :   1.0
@Desc    :   跳跃游戏 II
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 获取数组的长度
        n = len(nums)

        # 如果只有一个元素，不需要跳跃
        if n == 1:
            return 0

        # 初始化跳跃次数
        jumps = 0
        # 当前跳跃范围的右边界
        current_end = 0
        # 当前跳跃可以到达的最远位置
        farthest = 0

        # 遍历数组，计算最少跳跃次数
        for i in range(n - 1):
            # 更新当前能跳到的最远位置
            farthest = max(farthest, i + nums[i])

            # 如果到达了当前跳跃范围的右边界，需要增加跳跃次数，并更新右边界
            if i == current_end:
                jumps += 1
                current_end = farthest
                # 如果右边界已经到达或超过了最后一个位置，跳出循环
                if current_end >= n - 1:
                    break

        return jumps
