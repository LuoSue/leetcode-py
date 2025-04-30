#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   048_Rotate_Image.py
@Time    :   2025/04/30 17:44:49
@Author  :   rj 
@Version :   1.0
@Desc    :   旋转图像
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 转置矩阵
        for i in range(n):
            for j in range(i, n):  # 注意从i开始，避免重复交换
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 反转每一行
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        for i in range(n):
            reverse(matrix[i], 0, n - 1)