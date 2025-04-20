#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1208_Get_Equal_Substrings_Within_Budget.py
@Time    :   2025/04/20 13:31:57
@Author  :   rj 
@Version :   1.0
@Desc    :   尽可能使字符串相等
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 计算每一位字符从s变为t所需的代价（ASCII差值的绝对值）
        costs = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]

        n = len(s)
        left = 0               # 滑动窗口的左指针
        max_len = 0            # 满足条件的最大子串长度
        current_cost = 0       # 当前窗口内的总转换代价

        # 使用滑动窗口遍历字符串
        for right in range(n):
            current_cost += costs[right]  # 将当前字符的转换代价加入窗口

            # 如果当前窗口总代价超过预算，缩小窗口
            while current_cost > maxCost:
                current_cost -= costs[left]  # 移除左边字符的代价
                left += 1                   # 左指针右移，缩小窗口

            # 更新最大满足条件的窗口长度
            max_len = max(max_len, right - left + 1)

        return max_len
