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
