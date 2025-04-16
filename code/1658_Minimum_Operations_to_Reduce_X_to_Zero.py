#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1658_Minimum_Operations_to_Reduce_X_to_Zero.py
@Time    :   2025/04/16 10:39:08
@Author  :   rj 
@Version :   1.0
@Desc    :   将 x 减到 0 的最小操作数
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 如果数组总和小于x，不可能达成目标
        total = sum(nums)
        if total < x:
            return -1
        
        # 如果总和等于x，需要移除所有元素
        if total == x:
            return len(nums)
        
        # 我们实际上要找一个最长的子数组，其和等于total-x
        target = total - x
        n = len(nums)
        max_len = -1  # 记录最长符合条件的子数组长度
        windows_sum = 0     # 当前窗口的和
        left = 0         # 窗口左边界
        
        # 滑动窗口
        for right in range(n):
            windows_sum += nums[right]
            
            # 当窗口和大于目标时，缩小窗口
            while windows_sum > target and left <= right:
                windows_sum -= nums[left]
                left += 1
                
            # 当窗口和等于目标时，更新最大长度
            if windows_sum == target:
                max_len = max(max_len, right - left + 1)
        
        # 如果没找到符合条件的子数组，返回-1
        if max_len == -1:
            return -1
        
        # 总长度减去最大子数组长度就是最小操作次数
        return n - max_len