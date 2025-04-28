#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   062_Unique_Paths.py
@Time    :   2025/04/28 10:32:06
@Author  :   rj
@Version :   1.0
@Desc    :   不同路径
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个 m 行 n 列的二维数组，初始值都是 1
        # 因为第一行和第一列的路径数都是 1
        dp = [[1] * n for _ in range(m)]

        # 从 (1,1) 开始遍历，计算每个位置的路径数量
        for i in range(1, m):
            for j in range(1, n):
                # 当前格子的路径数 = 上方格子的路径数 + 左侧格子的路径数
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 返回右下角的路径数
        return dp[m - 1][n - 1]
