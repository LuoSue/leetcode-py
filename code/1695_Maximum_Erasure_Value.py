#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1695_Maximum_Erasure_Value.py
@Time    :   2025/04/20 14:08:01
@Author  :   rj 
@Version :   1.0
@Desc    :   删除子数组的最大得分
"""

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0  # 滑动窗口的左边界
        hash_set = set()  # 用于存储当前窗口内的唯一元素
        current_points = 0  # 当前窗口的得分（子数组元素和）
        max_points = 0  # 当前为止的最大得分

        # 遍历数组的每个元素，使用 right 作为窗口的右边界
        for right, x in enumerate(nums):
            # 如果当前元素已经存在于窗口中，则不断移动左边界，直到窗口中不再有重复元素
            while x in hash_set:
                hash_set.remove(nums[left])  # 从集合中移除左边界的元素
                current_points -= nums[left]  # 减去该元素的得分
                left += 1  # 左边界右移

            # 将当前元素加入集合，并加到当前得分中
            hash_set.add(x)
            current_points += x

            # 更新最大得分
            max_points = max(max_points, current_points)
        
        return max_points  # 返回最大得分
