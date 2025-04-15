#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   438_Find_All_Anagrams_in_a_String.py
@Time    :   2025/04/15 14:31:40
@Author  :   rj
@Version :   1.0
@Desc    :   找到字符串中所有字母异位词
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        找到字符串s中所有是p的字母异位词的子串的起始索引
        
        参数:
            s: 目标字符串
            p: 要匹配的字符串
            
        返回:
            所有符合条件的子串起始索引列表
        """
        p_len = len(p)  # 模式串p的长度
        s_len = len(s)  # 目标字符串s的长度

        # 如果p比s长，直接返回空列表
        if p_len > s_len:
            return []

        # 初始化两个长度为26的数组，用于统计字母出现次数
        p_count = [0] * 26  # 记录p中各字母出现次数
        windows_count = [0] * 26  # 记录滑动窗口中各字母出现次数
        result = []  # 存储结果

        # 统计p中各字母出现次数
        for c in p:
            # ord(c) - ord("a")将字母映射到0-25的索引
            p_count[ord(c) - ord("a")] += 1

        # 初始化滑动窗口，统计前p_len个字符的字母出现次数
        for i in range(p_len):
            windows_count[ord(s[i]) - ord("a")] += 1

        # 检查初始窗口是否匹配
        if windows_count == p_count:
            result.append(0)  # 匹配则记录起始索引0

        # 滑动窗口向右移动
        for i in range(p_len, s_len):
            left = i - p_len  # 窗口左边界
            left_char = s[left]  # 将要移出窗口的字符

            # 移出左边界字符
            windows_count[ord(left_char) - ord("a")] -= 1
            # 移入右边界新字符
            windows_count[ord(s[i]) - ord("a")] += 1

            # 检查当前窗口是否匹配
            if windows_count == p_count:
                # 记录窗口起始位置(left + 1)
                result.append(left + 1)

        return result