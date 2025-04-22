#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   035_Search_Insert_Position.py
@Time    :   2025/04/22 17:21:05
@Author  :   rj 
@Version :   1.0
@Desc    :   搜索插入位置
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 初始化左右边界。left 表示搜索范围的起始索引，right 是终止索引（不包括）。
        left, right = 0, len(nums)

        # 使用二分查找法，在有序数组中查找插入位置
        while left < right:
            # 计算中间位置索引
            mid = (left + right) // 2

            # 如果中间元素小于目标值，说明目标在右半部分
            if nums[mid] < target:
                left = mid + 1
            # 否则目标在左半部分或当前位置
            else:
                right = mid

        # 返回插入位置。当目标值在数组中时，这也是它的索引；
        # 如果不在数组中，这个位置是它应该插入的索引，以保持有序。
        return left
