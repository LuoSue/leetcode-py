#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   209_Minimum_Size_Subarray_Sum.py
@Time    :   2025/04/15 17:22:51
@Author  :   rj
@Version :   1.0
@Desc    :   长度最小的子数组
            给定一个含有 n 个正整数的数组和一个正整数 target，
            找出该数组中满足其和 ≥ target 的长度最小的连续子数组，
            并返回其长度。如果不存在符合条件的子数组，返回 0。
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # 滑动窗口的左边界
        n = len(nums)
        min_len = n + 1  # 初始化为不可能的大值（比数组长度大）
        s = 0  # 当前窗口的和

        # 遍历数组，right是滑动窗口的右边界
        for right, x in enumerate(nums):
            s += x  # 将当前元素加入窗口和

            # 尝试收缩左边界：如果去掉左边界的元素后和仍然>=target
            # 说明可以缩小窗口以寻找更小的长度
            while s - nums[left] >= target:
                s -= nums[left]  # 从和中移除左边界元素
                left += 1  # 左边界右移

            # 检查当前窗口和是否满足条件
            if s >= target:
                # 更新最小长度（当前窗口长度是right-left+1）
                min_len = min(min_len, right - left + 1)

        # 如果min_len未被更新过（仍为n+1），说明没有满足条件的子数组，返回0
        # 否则返回找到的最小长度
        return min_len if min_len != n + 1 else 0
