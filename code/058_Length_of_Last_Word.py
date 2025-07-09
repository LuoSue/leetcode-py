#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   058_Length_of_Last_Word.py
@Time    :   2025/07/09 14:34:52
@Author  :   rj
@Version :   1.0
@Desc    :   最后一个单词的长度
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        # 跳过末尾空格
        while i >= 0 and s[i] == " ":
            i -= 1

        # 开始计数最后一个单词的长度
        while i >= 0 and s[i].isalpha():
            length += 1
            i -= 1

        return length
