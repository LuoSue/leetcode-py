#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   051_N-Queens.py
@Time    :   2025/05/12 09:48:06
@Author  :   rj
@Version :   1.0
@Desc    :   N 皇后
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(
            row: int,
            cols: List[bool],
            diag1: List[bool],
            diag2: List[bool],
            path: List[str],
        ):
            # 如果已经成功放置了 n 个皇后，说明找到一个合法方案
            if row == n:
                result.append(path[:])  # 保存当前路径的副本
                return

            # 尝试在当前行的每一列放置皇后
            for col in range(n):
                # 计算当前单元格对应的主对角线和副对角线下标
                d1 = row - col + n - 1  # 主对角线 row - col 映射到 0 ~ 2n-2
                d2 = row + col  # 副对角线 row + col 自然落在 0 ~ 2n-2

                # 如果当前位置被攻击（即列或对角线已被占用），则跳过
                if cols[col] or diag1[d1] or diag2[d2]:
                    continue

                # 放置皇后，标记当前列和对角线为 True（已占用）
                cols[col] = diag1[d1] = diag2[d2] = True

                # 构造当前行的字符串，如在第 2 列放皇后：'..Q.'
                row_str = "." * col + "Q" + "." * (n - col - 1)

                # 递归尝试放置下一行皇后，path + [row_str] 生成新的路径列表
                backtrack(row + 1, cols, diag1, diag2, path + [row_str])

                # 回溯：撤销选择，恢复列和对角线标记
                cols[col] = diag1[d1] = diag2[d2] = False

        result = []  # 用于保存所有合法解
        # 初始化布尔数组：列、主对角线、副对角线是否被占用
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)

        # 开始回溯，从第 0 行开始，路径初始为空
        backtrack(0, cols, diag1, diag2, [])
        return result
