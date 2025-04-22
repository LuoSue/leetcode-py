#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1901_Find_a_Peak_Element_II.py
@Time    :   2025/04/22 14:43:36
@Author  :   rj 
@Version :   1.0
@Desc    :   寻找峰值 II
"""

from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # 获取矩阵的行数 m 和列数 n
        m, n = len(mat), len(mat[0])
        # 二分查找的左右边界（在列的维度上查找）
        low, high = 0, n - 1
        
        # 在列的范围内进行二分搜索
        while low <= high:
            mid = (low + high) // 2  # 当前中间列
            max_row = 0  # 初始化当前列中最大值所在的行索引
            
            # 在当前列中找出最大值所在的行
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            
            # 获取当前列中最大元素左右两侧的值（避免越界）
            left = mat[max_row][mid - 1] if mid > 0 else -1
            right = mat[max_row][mid + 1] if mid < n - 1 else -1
            
            # 如果当前列中最大值比左右两侧都大，说明找到了峰值
            if mat[max_row][mid] > left and mat[max_row][mid] > right:
                return [max_row, mid]
            # 如果左侧值更大，则说明峰值可能在左边
            elif left > mat[max_row][mid]:
                high = mid - 1
            # 否则向右查找
            else:
                low = mid + 1

        # 如果没有找到（按理说不会出现），返回 [-1, -1]
        return [-1, -1]
