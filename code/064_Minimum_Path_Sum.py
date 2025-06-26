#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   064_Minimum_Path_Sum.py
@Time    :   2025/04/28 10:34:02
@Author  :   rj
@Version :   1.0
@Desc    :   最小路径和
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        原地修改 grid，空间复杂度 O(1)，时间复杂度 O(mn)
        """
        m, n = len(grid), len(grid[0])

        # 更新第一行
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # 更新第一列
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # 更新其余位置
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # 返回右下角的值
        return grid[m - 1][n - 1]

    def minPathSum_dp_full(self, grid: List[List[int]]) -> int:
        """
        不修改原输入，使用额外二维数组 dp
        空间复杂度 O(mn)
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]

    def minPathSum_dp_rolling(self, grid: List[List[int]]) -> int:
        """
        使用滚动数组优化空间，空间复杂度 O(n)
        """
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]

        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]
