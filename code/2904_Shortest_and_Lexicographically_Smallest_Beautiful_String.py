#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2904_Shortest_and_Lexicographically_Smallest_Beautiful_String.py
@Time    :   2025/04/20 15:31:52
@Author  :   rj 
@Version :   1.0
@Desc    :   最短且字典序最小的美丽子字符串
"""

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)  # 字符串长度
        min_len = n + 1  # 初始化最小长度为一个不可能达到的最大值
        result = ""  # 存储结果子字符串
        ones_count = 0  # 当前窗口中1的个数
        left = 0  # 滑动窗口左指针

        # 使用滑动窗口遍历字符串
        for right in range(n):
            if s[right] == '1':
                ones_count += 1  # 统计窗口内1的数量

            # 当窗口中1的个数大于等于k时，尝试收缩左边界
            while ones_count >= k:
                if ones_count == k:
                    curr_len = right - left + 1  # 当前窗口长度
                    curr_substr = s[left:right + 1]  # 当前窗口对应的子字符串

                    # 更新最小长度和结果子字符串
                    if curr_len < min_len:
                        min_len = curr_len
                        result = curr_substr
                    elif curr_len == min_len:
                        # 如果长度相同，取字典序更小的子字符串
                        result = min(result, curr_substr)

                # 收缩左边界，同时更新1的计数
                if s[left] == '1':
                    ones_count -= 1
                left += 1

        return result  # 返回最终的最短且字典序最小的美丽子字符串
