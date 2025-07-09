#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   014_Longest_Common_Prefix.py
@Time    :   2025/07/09 14:46:08
@Author  :   rj
@Version :   1.0
@Desc    :   最长公共前缀
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]  # 假设第一个是最长前缀

        for s in strs[1:]:
            i = 0
            # 与当前前缀逐个字符比较
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1
            prefix = prefix[:i]
            if prefix == "":
                return ""

        return prefix
