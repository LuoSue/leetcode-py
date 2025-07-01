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

    def longestPalindromeManacher(self, s: str) -> str:
        """
        使用 Manacher 算法求解最长回文子串。
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not s:
            return ""

        # 1. 预处理：加入分隔符 '#'，并添加哨兵字符 '^' 和 '$' 防止越界
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        P = [0] * n  # P[i] 表示以 i 为中心的最大回文半径
        center = right = 0  # 当前回文的中心和右边界

        for i in range(1, n - 1):
            mirror = 2 * center - i  # i 关于 center 的对称位置

            if i < right:
                P[i] = min(right - i, P[mirror])  # 尝试缩小搜索范围

            # 尝试扩展回文
            while t[i + P[i] + 1] == t[i - P[i] - 1]:
                P[i] += 1

            # 更新回文右边界和中心
            if i + P[i] > right:
                center = i
                right = i + P[i]

        # 找出最大回文子串的中心及长度
        max_len = max(P)
        center_index = P.index(max_len)
        start = (center_index - max_len) // 2  # 还原在原始字符串中的起点

        return s[start : start + max_len]
