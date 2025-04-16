#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2958_Length_of_Longest_Subarray_With_at_Most_K_Frequency.py
@Time    :   2025/04/16 09:44:11
@Author  :   rj 
@Version :   1.0
@Desc    :   最多 K 个重复元素的最长子数组
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        找出最多包含 k 个重复元素的最长子数组的长度
        
        参数:
            nums: 整数数组
            k: 允许的最大重复次数
            
        返回:
            满足条件的最长子数组的长度
        """
        left = 0               # 滑动窗口的左指针
        max_len = 0            # 记录最大子数组长度
        num_dict = defaultdict(int)  # 用于记录当前窗口中各数字的出现次数

        # 右指针遍历整个数组
        for right, x in enumerate(nums):
            num_dict[x] += 1   # 当前数字的计数加1

            # 当当前数字的计数超过k时，移动左指针直到满足条件
            while num_dict[x] > k:
                y = nums[left]  # 左指针指向的数字
                num_dict[y] -= 1  # 减少该数字的计数
                left += 1        # 左指针右移
            
            # 更新最大子数组长度
            max_len = max(max_len, right - left + 1)
        
        return max_len