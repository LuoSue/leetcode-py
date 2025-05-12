#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   118_Pascal's_Triangle.py
@Time    :   2025/05/12 22:50:20
@Author  :   rj
@Version :   1.0
@Desc    :   杨辉三角
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []  # 存储 Pascal's 三角形
        for i in range(numRows):
            row = [1] * (i + 1)  # 创建当前行，并将所有元素初始化为 1
            for j in range(1, i):
                # 计算当前行除了第一个和最后一个位置之外的元素
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)  # 将当前行添加到 Pascal's 三角形中
        return triangle
