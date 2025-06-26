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
        """
        动态规划思路：
        - 本题是经典的二维动态规划问题，用来求两个字符串的最长公共子序列长度。
        - 子序列：可以不连续，但顺序不能乱。

        状态定义：
        - dp[i][j] 表示 text1 前 i 个字符 与 text2 前 j 个字符 的最长公共子序列长度。

        状态转移：
        - 如果 text1[i-1] == text2[j-1]：
            dp[i][j] = dp[i-1][j-1] + 1
        - 否则：
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        初始化：
        - dp[0][*] 和 dp[*][0] = 0，表示空串与任意字符串的公共子序列长度为 0。

        最终结果：
        - dp[m][n] 即为 text1 和 text2 的最长公共子序列长度。

        时间复杂度：O(m * n)
        空间复杂度：O(m * n)
        """

        m, n = len(text1), len(text2)
        # 创建一个二维数组 dp，初始化为 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 当前字符相等，公共子序列长度加 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 当前字符不等，取最大值：跳过 text1[i-1] 或 text2[j-1]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 返回最终结果
        return dp[m][n]
