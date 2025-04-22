#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   154_Find_Minimum_in_Rotated_Sorted_Array_II.py
@Time    :   2025/04/22 14:49:45
@Author  :   rj 
@Version :   1.0
@Desc    :   寻找旋转排序数组中的最小值 II
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 初始化左右指针，分别指向数组的开头和结尾
        left, right = 0, len(nums) - 1

        # 使用二分查找，在有重复元素的旋转排序数组中查找最小值
        while left <= right:
            # 计算中间位置
            mid = (left + right) // 2

            # 如果中间元素大于右边界元素，说明最小值在右半部分
            if nums[mid] > nums[right]:
                left = mid + 1
            # 如果中间元素小于右边界元素，说明最小值在左半部分或就是 mid
            elif nums[mid] < nums[right]:
                right = mid
            # 如果中间元素等于右边界元素，无法判断最小值在哪一侧，右边界左移缩小范围
            else:
                right -= 1

        # 循环结束后，left 指向最小值的位置
        return nums[left]
