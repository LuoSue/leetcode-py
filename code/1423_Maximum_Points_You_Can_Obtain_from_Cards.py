#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1423_Maximum_Points_You_Can_Obtain_from_Cards.py
@Time    :   2025/04/18 15:53:07
@Author  :   rj 
@Version :   1.0
@Desc    :   可获得的最大点数
"""

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)  # 卡牌总数

        total = sum(cardPoints)  # 所有卡牌的总点数

        if k == n:
            # 如果可以拿所有的牌，那最大点数就是总点数
            return total

        # 滑动窗口的长度为 n - k，表示我们要舍弃的连续子数组的长度
        window_len = n - k
        current_sum = 0  # 当前滑动窗口内的和

        # 先计算初始窗口（前 window_len 个元素）的和
        for i in range(window_len):
            current_sum += cardPoints[i]

        # 初始化最小窗口和
        min_window_sum = current_sum

        # 使用滑动窗口遍历整个数组，找出最小窗口和
        for i in range(window_len, n):
            left = i - window_len  # 左边界向右移动

            # 增加窗口右端的新元素，减少左端的旧元素
            current_sum += cardPoints[i]
            current_sum -= cardPoints[left]

            # 更新最小窗口和
            min_window_sum = min(min_window_sum, current_sum)

        # 最大得分 = 总点数 - 被舍弃窗口的最小和
        return total - min_window_sum
