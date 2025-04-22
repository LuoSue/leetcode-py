#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   162_Find_Peak_Element.py
@Time    :   2025/04/22 11:40:35
@Author  :   rj 
@Version :   1.0
@Desc    :   寻找峰值
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 初始化左右边界
        left, right = 0, len(nums) - 1

        # 使用二分查找的思想
        while left < right:
            # 取中间位置
            mid = (left + right) // 2

            # 如果中间元素大于其右侧的元素
            # 说明峰值可能在左边（包含 mid）
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                # 否则，峰值一定在右边（不包含 mid）
                left = mid + 1

        # 当左右指针重合时，即为峰值所在位置
        return left
