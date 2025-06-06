#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   034_Find_First_and_Last_Position_of_Element_in_Sorted_Array.py
@Time    :   2025/04/16 11:24:16
@Author  :   rj
@Version :   1.0
@Desc    :   在排序数组中查找元素的第一个和最后一个位置
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        在排序数组nums中查找target的第一个和最后一个位置
        如果target不存在，返回[-1, -1]
        时间复杂度: O(log n)
        """

        def find_left(nums, target):
            """
            使用二分查找找到target的最左位置
            """
            if not nums:
                return -1

            left, right = 0, len(nums)
            result = -1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid  # 找到目标，但继续向左搜索
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return result

        def find_right(nums, target):
            """
            使用二分查找找到target的最右位置
            """
            if not nums:
                return -1

            left, right = 0, len(nums)
            result = -1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid  # 找到目标，但继续向右搜索
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return result

        # 先找左边界
        left_pos = find_left(nums, target)
        if left_pos == -1:
            return [-1, -1]

        # 再找右边界
        right_pos = find_right(nums, target)
        return [left_pos, right_pos]
