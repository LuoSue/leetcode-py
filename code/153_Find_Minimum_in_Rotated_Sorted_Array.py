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
        
        # 使用二分查找
        while left < right:
            # 取中间索引
            mid = (left + right) // 2
            
            # 如果中间值大于右侧值，说明最小值一定在右半部分
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 否则最小值在左半部分（包含mid）
                right = mid
        
        # 循环结束时，left即为最小值的索引
        return nums[left]
