#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2841_Maximum_Sum_of_Almost_Unique_Subarray.py
@Time    :   2025/04/18 15:21:35
@Author  :   rj 
@Version :   1.0
@Desc    :   几乎唯一子数组的最大和
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        """
        在数组中找到长度为 k 的连续子数组，这个子数组中至少包含 m 个不同的元素，
        返回这些符合条件的子数组中元素和的最大值。
        
        :param nums: 整数数组
        :param m: 至少包含 m 个不同元素
        :param k: 子数组的固定长度
        :return: 最大和
        """
        n = len(nums)
        count = defaultdict(int)  # 记录当前滑动窗口中每个元素的出现次数
        current_sum = 0  # 当前滑动窗口的元素和
        max_sum = 0  # 满足条件的最大子数组和
        
        # 初始化第一个窗口 [0, k-1]
        for i in range(k):
            count[nums[i]] += 1
            current_sum += nums[i]
        
        # 如果不同元素的数量不少于 m，则更新最大值
        if len(count) >= m:
            max_sum = current_sum
        
        # 滑动窗口，逐步向右滑动一个元素
        for i in range(k, n):
            left = i - k  # 要移除的左侧元素下标
            
            # 增加新进入窗口的元素
            count[nums[i]] += 1
            current_sum += nums[i]
            
            # 移除滑出窗口的元素
            count[nums[left]] -= 1
            current_sum -= nums[left]
            if count[nums[left]] == 0:
                del count[nums[left]]  # 如果计数为0，彻底移除该元素
            
            # 检查当前窗口中是否有至少 m 个不同元素
            if len(count) >= m:
                max_sum = max(max_sum, current_sum)
        
        return max_sum
