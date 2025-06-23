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
        def backtrack(row: int, cols: set, diag1: set, diag2: set, path: List[str]):
            # 如果已经成功放置了 n 个皇后（即 n 行），将当前路径加入结果中
            if row == n:
                result.append(path[:])  # 注意要复制 path（不可直接引用）
                return

            # 尝试在当前行的每一列放置皇后
            for col in range(n):
                # 判断当前位置是否与之前放置的皇后冲突：
                # 列相同：col ∈ cols
                # 主对角线相同：row - col ∈ diag1
                # 副对角线相同：row + col ∈ diag2
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # 有冲突，跳过

                # 构造当前行的字符串，例如在第 2 列放皇后：'..Q.'
                row_str = "." * col + "Q" + "." * (n - col - 1)

                # 做出选择：标记列和对角线，并将当前行加入路径
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # 递归进入下一行，path + [row_str] 生成一个新的列表（函数式风格）
                backtrack(row + 1, cols, diag1, diag2, path + [row_str])

                # 回溯：撤销选择，移除标记（注意 path 不需要撤销，因为是新列表）
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        result = []  # 用于保存所有合法的解决方案
        # 初始化回溯：从第 0 行开始，path 初始为空
        backtrack(0, set(), set(), set(), [])
        return result
