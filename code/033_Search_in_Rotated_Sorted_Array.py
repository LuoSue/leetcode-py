#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   033_Search_in_Rotated_Sorted_Array.py
@Time    :   2025/04/22 14:28:08
@Author  :   rj 
@Version :   1.0
@Desc    :   搜索旋转排序数组
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 初始化左右指针
        left, right = 0, len(nums) - 1

        # 二分查找
        while left <= right:
            mid = (left + right) // 2  # 取中间位置

            # 找到目标值，直接返回索引
            if nums[mid] == target:
                return mid

            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                # 如果目标值在左半部分的有序区间内，缩小右边界
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # 否则在右半部分，移动左边界
                    left = mid + 1
            if nums[mid] <= nums[right]:
                # 否则右半部分是有序的
                # 如果目标值在右半部分的有序区间内，缩小左边界
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # 否则在左半部分，移动右边界
                    right = mid - 1

        # 未找到目标值，返回 -1
        return -1
