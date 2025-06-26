#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   062_Unique_Paths.py
@Time    :   2025/04/28 10:32:06
@Author  :   rj
@Version :   1.2
@Desc    :   不同路径（包含三种解法）
"""

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        方法一：二维动态规划
        创建一个 m 行 n 列的二维数组，初始值都是 1
        因为第一行和第一列的路径数都是 1
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                # 当前格子的路径数 = 上方格子的路径数 + 左侧格子的路径数
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsOptimized(self, m: int, n: int) -> int:
        """
        方法二：一维动态规划优化
        使用一个长度为 n 的数组来滚动更新路径数量
        空间复杂度降为 O(n)
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # 当前列的路径数 = 上一行的同列 + 左边一列的路径数
                # dp[j] 是上一行的 dp[i-1][j]
                # dp[j - 1] 是当前行的 dp[i][j-1]，已经被更新了
                # 更新后的 dp[j] 就是新一行的新值：dp[i][j] = dp[i-1][j] + dp[i][j-1]
                dp[j] += dp[j - 1]
        return dp[-1]

    def uniquePathsMath(self, m: int, n: int) -> int:
        """
        方法三：组合数学
        从 m+n-2 步中选出 m-1 步向下，其余为向右
        C(m+n-2, m-1) = (m+n-2)! / [(m-1)! * (n-1)!]
        """
        return math.comb(m + n - 2, m - 1)
