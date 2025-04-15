#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   003_Longest_Substring_Without_Repeating_Characters.py
@Time    :   2025/04/15 14:22:04
@Author  :   rj 
@Version :   1.0
@Desc    :   无重复字符的最长子串
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        使用滑动窗口法找出不含重复字符的最长子串长度
        
        参数:
            s: 输入字符串
            
        返回:
            最长无重复字符子串的长度
        """
        left = 0  # 滑动窗口的左边界
        max_len = 0  # 记录最大长度
        longest_set = set()  # 用于存储当前窗口中的字符（集合查找效率高）

        # 遍历字符串，i是右边界索引，x是当前字符
        for i, x in enumerate(s):
            # 如果当前字符已经在集合中，说明出现重复
            while x in longest_set:
                # 不断移除左边界字符，并向右移动左边界，直到消除重复
                longest_set.remove(s[left])
                left += 1
            # 将当前字符加入集合
            longest_set.add(x)
            # 更新最大长度（当前窗口长度：i - left + 1）
            max_len = max(max_len, i - left + 1)
        
        return max_len