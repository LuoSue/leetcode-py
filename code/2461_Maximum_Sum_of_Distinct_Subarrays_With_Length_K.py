#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2461_Maximum_Sum_of_Distinct_Subarrays_With_Length_K.py
@Time    :   2025/04/18 15:37:24
@Author  :   rj
@Version :   1.0
@Desc    :   长度为 K 子数组中的最大和
"""

from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)  # 用于记录滑动窗口内每个数字的出现次数
        current_sum = max_sum = 0  # 当前窗口的和和最大和初始化为 0

        # 初始化前 k 个元素的窗口
        for i in range(k):
            count[nums[i]] += 1  # 记录元素频次
            current_sum += nums[i]  # 累加当前窗口和

        # 如果前 k 个元素都是不同的（即集合大小等于 k），则更新最大和
        if len(count) == k:
            max_sum = current_sum

        # 开始滑动窗口，窗口大小始终为 k
        for i in range(k, n):
            left = i - k  # 滑出窗口的左边元素下标

            # 将新元素加入窗口
            count[nums[i]] += 1
            current_sum += nums[i]

            # 移除滑出窗口的左边元素
            count[nums[left]] -= 1
            current_sum -= nums[left]
            
            # 如果某个元素频次为 0，就从字典中删除它
            if count[nums[left]] == 0:
                del count[nums[left]]

            # 只有当窗口中元素都不同（频次字典大小等于 k）时，才有资格更新最大和
            if len(count) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
