#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   240_Search_a_2D_Matrix_II.py
@Time    :   2025/04/30 17:47:01
@Author  :   rj
@Version :   1.0
@Desc    :   搜索二维矩阵 II
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # 获取矩阵的行数
        n = len(matrix[0])  # 获取矩阵的列数

        # 从矩阵的右上角开始搜索
        row, col = 0, n - 1

        # 当行和列的索引有效时，继续搜索
        while row < m and col >= 0:
            if target == matrix[row][col]:  # 如果当前元素是目标值，返回 True
                return True
            elif target < matrix[row][col]:  # 如果目标值小于当前元素，移动到左边
                col -= 1
            else:  # 如果目标值大于当前元素，移动到下方
                row += 1
        return False  # 如果没有找到目标值，返回 False
