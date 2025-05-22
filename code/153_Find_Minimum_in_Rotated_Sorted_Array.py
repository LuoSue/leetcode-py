#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   153_Find_Minimum_in_Rotated_Sorted_Array.py
@Time    :   2025/04/22 11:54:40
@Author  :   rj
@Version :   1.0
@Desc    :   寻找旋转排序数组中的最小值
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 初始化左右指针
        left, right = 0, len(nums) - 1

        # 当左指针不超过右指针时继续搜索
        while left <= right:
            # 如果当前区间是有序的，说明最小值就是左端点
            if nums[left] <= nums[right]:
                return nums[left]

            # 计算中间索引
            mid = (left + right) // 2

            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                # 左半部分有序，说明最小值在右半部分
                left = mid + 1
            else:
                # 否则，最小值在左半部分（包含mid）
                right = mid

        # 如果数组不符合旋转数组的性质，理论上不会走到这里
        return -1
