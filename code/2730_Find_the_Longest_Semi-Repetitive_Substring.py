#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2730_Find_the_Longest_Semi-Repetitive_Substring.py
@Time    :   2025/04/16 09:51:03
@Author  :   rj 
@Version :   1.0
@Desc    :   找到最长的半重复子字符串
"""

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """
        找到最长的半重复子字符串的长度
        
        半重复子字符串定义：最多包含一对连续相同字符的子字符串
        
        参数:
            s: 输入字符串
            
        返回:
            最长半重复子字符串的长度
        """
        left = 0           # 滑动窗口的左指针
        max_len = 1         # 记录最大长度，初始至少为1（单个字符）
        repeat_count = 0    # 记录当前窗口中连续相同字符对的数量

        # 遍历字符串，right从1开始，因为我们要比较s[right]和s[right-1]
        for right in range(1, len(s)):
            # 如果当前字符和前一个字符相同，增加重复计数
            if s[right] == s[right - 1]:
                repeat_count += 1
            
            # 当重复计数超过1时（即有超过一对连续相同字符），移动左指针
            while repeat_count > 1:
                # 如果左指针处的字符和下一个字符相同，减少重复计数
                if s[left] == s[left + 1]:
                    repeat_count -= 1
                left += 1  # 移动左指针
            
            # 更新最大长度
            max_len = max(max_len, right - left + 1)
        
        return max_len