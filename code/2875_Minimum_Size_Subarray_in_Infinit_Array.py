#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2875_Minimum_Size_Subarray_in_Infinit_Array.py
@Time    :   2025/04/20 16:47:02
@Author  :   rj 
@Version :   1.0
@Desc    :   无限数组的最短子数组
"""

import math
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)

        if total == 0:
            return -1
        
        # 抽取滑动窗口逻辑
        def min_subarray_with_sum(val):
            left = curr_sum = 0
            res = math.inf
            for right in range(2 * n):
                curr_sum += nums[right % n]
                while curr_sum > val:
                    curr_sum -= nums[left % n]
                    left += 1
                if curr_sum == val:
                    res = min(res, right - left + 1)
            return res if res != math.inf else -1

        if total >= target:
            return min_subarray_with_sum(target)
        else:
            k = target // total
            rem = target % total
            if rem == 0:
                return k * n
            remainder_min_len = min_subarray_with_sum(rem)
            return k * n + remainder_min_len if remainder_min_len != -1 else -1