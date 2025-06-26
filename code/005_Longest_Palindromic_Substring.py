#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   005_Longest_Palindromic_Substring.py
@Time    :   2025/05/12 22:55:10
@Author  :   rj
@Version :   1.0
@Desc    :   最长回文子串
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # dp[i][j] 表示子串 s[i:j+1] 是否是回文串
        dp = [[False] * n for _ in range(n)]

        # 初始化：所有长度为1的子串都是回文串
        for i in range(n):
            dp[i][i] = True

        start = 0  # 用来记录最长回文子串的起始位置
        max_len = 1  # 最长回文串的长度

        # 处理长度大于1的子串
        for length in range(2, n + 1):  # 子串长度从2到n
            for i in range(n - length + 1):
                j = i + length - 1  # 子串的右边界

                if s[i] == s[j]:  # 如果左右字符相等
                    if length == 2:  # 如果长度为2，且两个字符相等
                        dp[i][j] = True
                    else:  # 如果长度大于2，检查中间部分是否是回文
                        dp[i][j] = dp[i + 1][j - 1]

                    # 更新最长回文子串的起始位置和长度
                    if dp[i][j] and length > max_len:
                        start = i
                        max_len = length

        return s[start : start + max_len]

    def longestPalindromeCenter(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, end = 0, 0

        def expandAroundCenter(left: int, right: int):
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - start:
                start = left + 1
                end = right

        for i in range(len(s)):
            # 以单个字符为中心（奇数长度）
            expandAroundCenter(i, i)
            # 以两个字符为中心（偶数长度）
            expandAroundCenter(i, i + 1)

        return s[start:end]
