#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   054_Spiral_Matrix.py
@Time    :   2025/04/30 17:39:54
@Author  :   rj
@Version :   1.0
@Desc    :   螺旋矩阵
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []  # 用于存储结果
        m, n = len(matrix), len(matrix[0])  # 获取矩阵的行数和列数

        # 初始化四个边界：左、右、上、下
        left, right, top, bottom = 0, n - 1, 0, m - 1

        # 开始遍历矩阵，按照螺旋顺序
        while True:
            # 如果左边界超过右边界，说明已经遍历完毕，跳出循环
            if left > right:
                break

            # 1. 从左到右遍历当前上边界的元素
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            # 上边界下移
            top += 1

            # 如果上边界超过下边界，说明已经遍历完，跳出循环
            if top > bottom:
                break

            # 2. 从上到下遍历当前右边界的元素
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            # 右边界左移
            right -= 1

            # 如果左边界超过右边界，说明已经遍历完，跳出循环
            if left > right:
                break

            # 3. 从右到左遍历当前下边界的元素
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            # 下边界上移
            bottom -= 1

            # 如果上边界超过下边界，说明已经遍历完，跳出循环
            if top > bottom:
                break

            # 4. 从下到上遍历当前左边界的元素
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            # 左边界右移
            left += 1

        return result  # 返回螺旋顺序的结果
