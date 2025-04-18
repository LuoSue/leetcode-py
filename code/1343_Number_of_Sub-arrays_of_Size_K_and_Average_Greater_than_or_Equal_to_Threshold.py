#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1343_Number_of_Sub-arrays_of_Size_K_and_Average_Greater_than_or_Equal_to_Threshold.py
@Time    :   2025/04/18 11:53:19
@Author  :   rj 
@Version :   1.0
@Desc    :   大小为 K 且平均值大于等于阈值的子数组数目
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)  # 数组长度
        current_sum = 0  # 用于记录当前窗口的和
        ans = 0  # 满足条件的子数组数量

        # 初始化窗口：计算前 k 个元素的和
        for i in range(k):
            current_sum += arr[i]

        # 判断第一个窗口是否满足平均值大于等于 threshold
        if current_sum / k >= threshold:
            ans += 1

        # 滑动窗口：从索引 k 开始，依次向右移动窗口
        for j in range(k, n):
            left = j - k  # 被移出窗口的左端元素的索引

            current_sum += arr[j]        # 加入右端的新元素
            current_sum -= arr[left]     # 移除左端的旧元素

            # 判断当前窗口是否满足平均值大于等于 threshold
            if current_sum / k >= threshold:
                ans += 1
        
        return ans  # 返回满足条件的子数组个数
