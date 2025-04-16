#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2529_Maximum_Count_of_Positive_Integer_and_Negative_Integer.py
@Time    :   2025/04/16 11:59:56
@Author  :   rj 
@Version :   1.0
@Desc    :   正整数和负整数的最大计数
"""

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 计算数组中正整数的个数
        def countPos(nums):
            left, right = -1, len(nums)  # 初始化二分查找的左右边界
            while left + 1 < right:  # 通过二分查找寻找第一个正整数的位置
                mid = left + (right - left) // 2
                if nums[mid] <= 0:  # 如果当前数字是非正数，移动左边界
                    left = mid
                else:  # 如果是正数，移动右边界
                    right = mid
            # 返回正整数的个数，即总数减去第一个正整数的索引
            return len(nums) - (left + 1) if left + 1 < len(nums) else 0
        
        # 计算数组中负整数的个数
        def countNeg(nums):
            left, right = -1, len(nums)  # 初始化二分查找的左右边界
            while left + 1 < right:  # 通过二分查找寻找第一个负整数的位置
                mid = left + (right - left) // 2
                if nums[mid] < 0:  # 如果当前数字是负数，移动左边界
                    left = mid
                else:  # 如果是非负数，移动右边界
                    right = mid
            # 返回负整数的个数，即最后一个负整数的索引
            return left + 1 if left >= 0 else 0
        
        # 计算正整数和负整数的个数
        pos = countPos(nums)
        neg = countNeg(nums)
        
        # 返回正整数和负整数中较大的个数
        return max(pos, neg)
