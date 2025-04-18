#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   643_Maximum_Average_Subarray_I.py
@Time    :   2025/04/18 11:43:55
@Author  :   rj 
@Version :   1.0
@Desc    :   子数组最大平均数 I
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)  # 获取数组长度
        current_sum = 0  # 初始化当前窗口的和

        # 计算第一个窗口（前k个元素）的和
        for i in range(k):
            current_sum += nums[i]
        max_sum = current_sum  # 初始化最大和为第一个窗口的和

        # 滑动窗口遍历后续子数组
        for j in range(k, n):
            current_sum += nums[j]        # 加入窗口右边的元素
            current_sum -= nums[j - k]    # 移除窗口左边的元素
            max_sum = max(max_sum, current_sum)  # 更新最大和

        # 返回最大平均值
        return max_sum / k
