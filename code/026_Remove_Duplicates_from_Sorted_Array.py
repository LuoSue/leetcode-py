#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   026_Remove_Duplicates_from_Sorted_Array.py
@Time    :   2025/07/07 14:15:16
@Author  :   rj
@Version :   1.0
@Desc    :   删除有序数组中的重复项
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        删除有序数组中的重复项，使得每个元素只出现一次，并返回新数组的长度

        参数:
            nums: 有序整数数组(List[int])

        返回:
            新数组的长度(int)

        算法思路:
            使用双指针法：
            1. 指针k记录不重复元素的位置
            2. 指针i遍历整个数组
            3. 当遇到新元素时，将其放到k位置，并移动k指针
            4. 最终k即为不重复元素的个数
        """
        # 如果数组为空，直接返回0
        if not nums:
            return 0

        # k从1开始，因为第一个元素肯定是不重复的
        k = 1

        # 从第二个元素开始遍历数组
        for i in range(1, len(nums)):
            # 如果当前元素与前一个元素不同
            if nums[i] != nums[i - 1]:
                # 将当前元素放到k位置
                nums[k] = nums[i]
                # k指针后移
                k += 1
        # 返回不重复元素的个数
        return k
