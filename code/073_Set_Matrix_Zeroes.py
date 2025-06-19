#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   073_Set_Matrix_Zeroes.py
@Time    :   2025/04/30 17:37:06
@Author  :   rj
@Version :   1.0
@Desc    :   矩阵置零
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 如果输入矩阵为空或第一行为空，直接返回
        if not matrix or not matrix[0]:
            return

        # 获取矩阵的行数 m 和列数 n
        m, n = len(matrix), len(matrix[0])

        # 使用两个布尔变量来记录第一行和第一列是否需要置零
        # 优化点 1: 更简洁的布尔变量初始化
        first_row_has_zero = False
        first_col_has_zero = False

        # 检查第一行是否包含 0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break  # 找到一个0即可，无需继续遍历

        # 检查第一列是否包含 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break  # 找到一个0即可，无需继续遍历

        # Step 2: 用第一行和第一列标记其他部分的 0
        # 从矩阵的第 2 行和第 2 列开始遍历（因为第一行和第一列用于标记）
        for i in range(1, m):
            for j in range(1, n):
                # 如果当前位置为 0，则用第一行和第一列标记该行和该列
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 标记该行
                    matrix[0][j] = 0  # 标记该列

        # Step 3 & 4: 根据第一列和第一行标记，将内部区域置零
        # 遍历矩阵的第 2 行到最后一行，根据第一列标记来将该行置零
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # 遍历矩阵的第 2 列到最后一列，根据第一行标记来将该列置零
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Step 5: 处理第一行和第一列
        # 如果第一行本身包含0，将整个第一行置零
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        # 如果第一列本身包含0，将整个第一列置零
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
