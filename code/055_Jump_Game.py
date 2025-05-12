#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   055_Jump_Game.py
@Time    :   2025/05/12 22:38:22
@Author  :   rj
@Version :   1.0
@Desc    :   跳跃游戏
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 获取数组的长度
        n = len(nums)
        # 初始化最大可达位置
        max_reach = 0

        # 遍历每个位置
        for i in range(n):
            # 如果当前索引超过了最大可达位置，说明无法跳到当前索引
            if i > max_reach:
                return False
            # 更新最大可达位置：当前位置 + 当前位置的跳跃距离
            max_reach = max(i + nums[i], max_reach)

        # 如果遍历完成后可以跳到最后一个位置，返回True
        return True
