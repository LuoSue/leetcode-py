#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   560_Subarray_Sum_Equals_K.py
@Time    :   2025/04/29 11:21:05
@Author  :   rj 
@Version :   1.0
@Desc    :   和为 K 的子数组
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 初始化计数器，记录满足条件的子数组数量
        count = 0
        # 当前数组的前缀和
        current_sum = 0
        # 哈希表，用于记录每个前缀和出现的次数
        prefix_sum_count = defaultdict(int)
        # 初始条件：前缀和为0的出现次数为1（考虑空子数组的情况）
        prefix_sum_count[0] = 1

        # 遍历数组
        for num in nums:
            # 更新当前前缀和
            current_sum += num
            # 如果当前前缀和减去k在哈希表中出现过，说明找到了一个子数组，其和为k
            count += prefix_sum_count[current_sum - k]
            # 记录当前前缀和出现的次数
            prefix_sum_count[current_sum] += 1

        # 返回满足条件的子数组的总数量
        return count
