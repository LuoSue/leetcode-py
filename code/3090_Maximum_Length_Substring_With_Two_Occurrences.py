#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   3090_Maximum_Length_Substring_With_Two_Occurrences.py
@Time    :   2025/04/20 10:36:29
@Author  :   rj 
@Version :   1.0
@Desc    :   每个字符最多出现两次的最长子字符串
"""

from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        找出每个字符最多出现两次的最长子字符串的长度
        
        参数:
            s: 输入字符串
            
        返回:
            int: 满足条件的最长子字符串的长度
        """
        # 使用defaultdict来记录窗口中每个字符的出现次数
        char_count = defaultdict(int)
        max_len = 0  # 记录最大长度
        start = 0     # 滑动窗口的起始位置

        # 遍历字符串，end是滑动窗口的结束位置
        for end, char in enumerate(s):
            # 当前字符的计数加1
            char_count[char] += 1

            # 如果当前字符的出现次数超过2次，需要移动窗口的起始位置
            while char_count[char] > 2:
                # 将窗口起始位置的字符计数减1
                char_count[s[start]] -= 1
                # 移动窗口起始位置向右
                start += 1
                
            # 更新最大长度，当前窗口长度为 end - start + 1
            max_len = max(max_len, end - start + 1)

        return max_len