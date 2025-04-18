#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2090_K_Radius_Subarray_Averages.py
@Time    :   2025/04/18 14:16:01
@Author  :   rj 
@Version :   1.0
@Desc    :   半径为 k 的子数组平均值
"""

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)  # 数组长度
        avg = [-1] * n  # 初始化返回数组，默认值为 -1
        window_len = 2 * k + 1  # 窗口长度，即包含当前元素左右各 k 个元素的子数组长度

        # 如果窗口长度大于数组长度，无法形成任何合法子数组，直接返回初始结果
        if window_len > n:
            return avg

        current_sum = 0  # 当前窗口的总和

        # 计算第一个窗口的总和（前 window_len 个元素）
        for i in range(window_len):
            current_sum += nums[i]

        # 将第一个合法子数组的平均值放在中心位置
        avg[k] = current_sum // window_len

        # 滑动窗口，依次计算后续每个窗口的平均值
        for i in range(window_len, n):
            left = i - window_len  # 窗口最左端的元素索引
            current_sum += nums[i]  # 加入右端新元素
            current_sum -= nums[left]  # 移除左端旧元素
            avg[i - k] = current_sum // window_len  # 存储平均值于中心位置

        return avg
