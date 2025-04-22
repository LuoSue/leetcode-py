#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   704_Binary_Search.py
@Time    :   2025/04/22 17:32:17
@Author  :   rj 
@Version :   1.0
@Desc    :   二分查找
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 初始化搜索区间的左右边界
        low, high = 0, len(nums)
        # 用于记录搜索结果，默认为 -1（表示未找到）
        res = -1

        # 当左边界小于右边界时继续搜索
        while low < high:
            # 计算中间位置，避免直接 (low + high) // 2 可能导致的整数溢出
            mid = low + (high - low) // 2

            # 如果中间元素正好是目标值，则返回其索引
            if nums[mid] == target:
                res = mid
                return res
            # 如果中间元素大于目标值，则目标值在左半部分，缩小右边界
            elif nums[mid] > target:
                high = mid
            # 如果中间元素小于目标值，则目标值在右半部分，缩小左边界
            elif nums[mid] < target:
                low = mid + 1
        
        # 如果循环结束仍未找到目标值，返回 -1
        return res
