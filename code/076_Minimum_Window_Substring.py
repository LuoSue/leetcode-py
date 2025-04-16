#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   076_Minimum_Window_Substring.py
@Time    :   2025/04/16 11:02:24
@Author  :   rj
@Version :   1.0
@Desc    :   最小覆盖子串
"""

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        在字符串s中找出包含字符串t所有字符的最小子串
        :param s: 源字符串
        :param t: 目标字符集
        :return: 最小子串，如果不存在则返回空字符串
        """
        # 如果s比t短，直接返回空字符串
        if len(s) < len(t):
            return ""

        # 使用defaultdict来记录字符出现次数，避免KeyError
        t_map = defaultdict(int)  # 记录t中每个字符的出现次数
        windows_map = defaultdict(int)  # 记录当前窗口中各字符的出现次数

        # 统计t中每个字符的出现次数
        for c in t:
            t_map[c] += 1

        left = 0  # 滑动窗口左指针
        valid = 0  # 记录当前窗口中满足t字符出现次数的字符种类数
        start = 0  # 最小子串的起始位置
        min_len = len(s) + 1  # 最小子串长度，初始设为不可能的大值

        # 遍历字符串s，right为滑动窗口右指针
        for right, x in enumerate(s):
            # 如果当前字符在t中
            if x in t_map:
                windows_map[x] += 1  # 增加窗口中该字符的计数

                # 如果窗口中该字符的数量刚好等于t中该字符的数量
                if windows_map[x] == t_map[x]:
                    valid += 1  # 满足条件的字符种类数+1

            # 当窗口中包含t所有字符时，尝试收缩左边界
            while valid == len(t_map):
                # 如果当前窗口比之前记录的最小窗口更小
                if right - left + 1 < min_len:
                    min_len = right - left + 1  # 更新最小长度
                    start = left  # 更新最小窗口起始位置

                y = s[left]  # 左边界要右移，获取移出的字符
                left += 1  # 左指针右移

                # 如果移出的字符在t中
                if y in t_map:
                    # 如果移出前该字符的数量刚好满足t中的要求
                    if windows_map[y] == t_map[y]:
                        valid -= 1  # 满足条件的字符种类数-1
                    windows_map[y] -= 1  # 减少窗口中该字符的计数

        # 如果找到了符合条件的子串，返回它；否则返回空字符串
        return s[start : start + min_len] if min_len != len(s) + 1 else ""
