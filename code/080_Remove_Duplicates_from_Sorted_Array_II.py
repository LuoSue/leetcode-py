#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   080_Remove_Duplicates_from_Sorted_Array_II.py
@Time    :   2025/07/07 14:34:57
@Author  :   rj
@Version :   1.0
@Desc    :   删除有序数组中的重复项 II
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        删除有序数组中重复出现的元素，使得每个元素最多出现两次
        原地修改数组，并返回新数组的长度

        Args:
            nums (List[int]): 有序数组

        Returns:
            int: 新数组的长度
        """
        # 如果数组长度小于等于2，直接返回数组长度，因为最多保留两个元素
        if len(nums) <= 2:
            return len(nums)

        # 初始化慢指针，从索引2开始
        slow = 2

        # 快指针从索引2开始遍历数组
        for fast in range(2, len(nums)):
            # 如果当前元素与慢指针前两个位置的元素不同
            if nums[fast] != nums[slow - 2]:
                # 将当前元素复制到慢指针位置
                nums[slow] = nums[fast]
                # 慢指针向前移动
                slow += 1

        # 返回新数组的长度
        return slow
