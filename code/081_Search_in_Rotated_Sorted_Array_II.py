#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   081_Search_in_Rotated_Sorted_Array_II.py
@Time    :   2025/05/22 11:45:30
@Author  :   rj 
@Version :   1.0
@Desc    :   搜索旋转排序数组 II
"""

from typing import List


class Solution:
    """
    🧠 为什么 不需要判断 nums[right]？
    判断右端点的本质目的是想确认数组两边是否都可能重复。但：
    只要 nums[left] == nums[mid]，你已经无法判断哪边有序了；
    继续看右边有没有重复不会改变这个判断失效的事实；
    同时判断 nums[right] == nums[mid] 并不能提供比 left == mid 更有用的信息，还会多做一次比较；
    因此：判断 nums[left] == nums[mid] 是必要且充分的条件来处理重复元素。
    """

    def search(self, nums: List[int], target: int) -> int:
        # 初始化左右指针
        left, right = 0, len(nums) - 1

        # 二分查找
        while left <= right:
            mid = (left + right) // 2  # 取中间位置

            # 找到目标值，返回 True
            if nums[mid] == target:
                return True
            
            # 重复值处理，缩小搜索区间
            if nums[left] == nums[mid]:
                left += 1
                continue

            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                # 如果目标值在左半部分的有序区间内，缩小右边界
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # 否则在右半部分，移动左边界
                    left = mid + 1
            else:
                # 否则右半部分是有序的
                # 如果目标值在右半部分的有序区间内，缩小左边界
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # 否则在左半部分，移动右边界
                    right = mid - 1

        # 未找到目标值，返回 False
        return False