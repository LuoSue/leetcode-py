#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   287_Find_the_Duplicate_Number.py
@Time    :   2025/05/12 23:02:29
@Author  :   rj
@Version :   1.0
@Desc    :   寻找重复数
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 初始化慢指针和快指针
        slow = nums[0]
        fast = nums[0]

        # 移动慢指针每次一步，快指针每次两步
        while True:
            slow = nums[slow]  # 慢指针走一步
            fast = nums[nums[fast]]  # 快指针走两步
            if slow == fast:  # 如果慢指针和快指针相遇，表示进入了环形
                break

        # 找到环的起点（重复的数字）
        slow = nums[0]  # 将慢指针重新置为起点
        while slow != fast:
            slow = nums[slow]  # 慢指针一步一步走
            fast = nums[fast]  # 快指针一步一步走

        return slow  # 当慢指针和快指针相遇时，即为重复的数字
