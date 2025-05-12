#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1143_Longest_Common_Subsequence.py
@Time    :   2025/05/12 22:55:58
@Author  :   rj
@Version :   1.0
@Desc    :   最长公共子序列
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 创建一个二维数组 dp
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # 当前字符相等，公共子序列长度加1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 当前字符不等，取最大值

        # 返回最终结果
        return dp[m][n]
