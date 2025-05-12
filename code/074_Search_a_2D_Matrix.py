#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   074_Search_a_2D_Matrix.py
@Time    :   2025/05/12 14:52:28
@Author  :   rj
@Version :   1.0
@Desc    :   搜索二维矩阵
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 获取矩阵的行数
        m = len(matrix)
        # 获取矩阵的列数
        n = len(matrix[0])

        # 初始化左指针和右指针，准备进行二分查找
        left, right = 0, m * n - 1

        # 二分查找的循环条件
        while left <= right:
            # 计算中间位置的索引
            mid = (left + right) // 2
            # 将一维索引映射回二维矩阵中的行列索引
            mid_value = matrix[mid // n][mid % n]

            # 如果中间元素等于目标值，返回 True
            if mid_value == target:
                return True
            # 如果中间元素大于目标值，则搜索左半部分
            elif mid_value > target:
                right = mid - 1
            # 如果中间元素小于目标值，则搜索右半部分
            else:
                left = mid + 1

        # 如果循环结束仍未找到目标值，返回 False
        return False
