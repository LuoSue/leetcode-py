#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1493_Longest_Subarray_of_1's_After_Deleting_One_Element.py
@Time    :   2025/04/20 11:02:00
@Author  :   rj 
@Version :   1.0
@Desc    :   删掉一个元素以后全为 1 的最长子数组
"""

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0  # 左指针，表示当前滑动窗口的起点
        zero_count = 0  # 当前窗口中 0 的数量
        max_len = 0  # 记录满足条件的最长子数组长度

        # 遍历数组，right 是滑动窗口的右边界
        for right, x in enumerate(nums):
            if x == 0:
                zero_count += 1  # 窗口中出现了一个 0，计数加 1
            
            # 如果窗口中 0 的数量超过 1，说明需要移动左边界缩小窗口
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1  # 移除左边界的 0，计数减 1
                left += 1  # 无论是不是 0，左边界右移一位
            
            # 更新最大长度（注意：我们必须删掉一个元素，因此窗口长度为 right - left）
            max_len = max(max_len, right - left)
        
        return max_len  # 返回满足条件的最大子数组长度
