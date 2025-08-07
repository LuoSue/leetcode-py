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

        参数:
            nums (List[int]): 递增排序的整数数组

        返回:
            int: 修改后的数组长度，前 length 个元素为最终结果
        """
        # 如果数组长度不超过2，直接返回原长度即可
        if len(nums) <= 2:
            return len(nums)

        # 初始化慢指针 slow，表示下一个要填入元素的位置，从2开始
        # 因为前两个元素最多可以保留，不用检查
        slow = 2

        # 从索引2开始遍历数组，使用 fast 指针
        for fast in range(2, len(nums)):
            # 如果当前 fast 指向的元素不等于 slow - 2 位置的元素，
            # 说明当前元素没有出现超过两次，可以保留
            if nums[fast] != nums[slow - 2]:
                # 将当前元素放到 slow 指向的位置
                nums[slow] = nums[fast]
                # 移动 slow 指针，准备填入下一个有效元素
                slow += 1

        # 遍历完成后，slow 就是新数组的长度
        return slow
