#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1456_Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length.py
@Time    :   2025/04/18 11:39:28
@Author  :   rj 
@Version :   1.0
@Desc    :   定长子串中元音的最大数目
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 定义元音字符集合
        vowels = {'a','e','i','o','u'}
        n = len(s)

        # 初始化滑动窗口中元音的计数器
        windows_count = 0

        # 先处理第一个长度为 k 的窗口，统计其中的元音数量
        for i in range(k):
            if s[i] in vowels:
                windows_count += 1

        # 初始化最大值为第一个窗口的元音数
        max_count = windows_count

        # 使用滑动窗口遍历后续的子串，窗口每次右移一位
        for j in range(k, n):
            left = j - k  # 窗口左边界的索引

            # 如果新进入窗口的字符是元音，增加计数
            if s[j] in vowels:
                windows_count += 1

            # 如果移出窗口的字符是元音，减少计数
            if s[left] in vowels:
                windows_count -= 1

            # 更新最大值
            max_count = max(max_count, windows_count)
        
        # 返回定长子串中包含最多元音的数量
        return max_count
