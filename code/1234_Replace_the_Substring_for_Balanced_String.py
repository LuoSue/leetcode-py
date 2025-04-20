#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1234_Replace_the_Substring_for_Balanced_String.py
@Time    :   2025/04/20 16:30:19
@Author  :   rj 
@Version :   1.0
@Desc    :   替换子串得到平衡字符串
"""

from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        limit = n // 4  # 每种字符最多出现的次数（平衡时）

        count = Counter(s)  # 初始统计每个字符的出现次数

        # 如果已经平衡了，直接返回 0
        if all(count[c] == limit for c in 'QWER'):
            return 0

        min_len = n  # 初始化结果为最大可能值（整个字符串）
        left = 0     # 滑动窗口左指针

        # 右指针从左到右滑动
        for right in range(n):
            count[s[right]] -= 1  # 将当前字符包含进窗口，减少窗口外的统计

            # 如果窗口外的字符都不超过 limit，说明这个窗口可以替换
            while left < n and all(count[c] <= limit for c in 'QWER'):
                # 更新最小窗口长度
                min_len = min(min_len, right - left + 1)
                # 缩小窗口：将左边字符移出窗口，恢复它在窗口外的统计
                count[s[left]] += 1
                left += 1

        return min_len