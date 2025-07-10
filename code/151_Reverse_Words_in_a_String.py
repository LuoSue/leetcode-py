#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   151_Reverse_Words_in_a_String.py
@Time    :   2025/07/10 15:29:15
@Author  :   rj
@Version :   1.0
@Desc    :   反转字符串中的单词
"""


class Solution:
    def reverseWordsEasy(self, s: str) -> str:
        # 先去掉前后空格并按空格分割为单词列表（自动去除多余空格）
        words = s.strip().split()
        # 反转单词列表
        words.reverse()
        # 用单个空格连接单词列表
        return ' '.join(words)
    
    
    def reverseWords(self, s: str) -> str:
        s = s.strip()                            # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1])          # 添加单词
            while i >= 0 and s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i                                # j 指向下个单词的尾字符
        return ' '.join(res)                     # 拼接并返回