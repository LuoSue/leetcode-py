#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   283_Move_Zeroes.py
@Time    :   2025/04/15 10:49:15
@Author  :   rj
@Version :   1.0
@Desc    :   移动零
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        将给定列表中的所有 0 移动到末尾，同时保持非零元素的相对顺序不变。
        该操作在原地进行，不返回任何值。

        参数:
        nums (List[int]): 要处理的整数列表。
        """
        slow = 0  # 慢指针，用于标记下一个非零元素应放置的位置

        # 第一轮遍历：将所有非零元素按顺序移动到前面
        for num in nums:
            if num != 0:
                nums[slow] = num  # 将当前非零元素赋值到 slow 指针位置
                slow += 1  # slow 前移，准备放下一个非零元素

        # 第二轮遍历：将 slow 之后的所有位置填充为 0
        for i in range(slow, len(nums)):
            nums[i] = 0  # 将剩余位置填充为 0
