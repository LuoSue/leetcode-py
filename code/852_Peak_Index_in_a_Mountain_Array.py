#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   852_Peak_Index_in_a_Mountain_Array.py
@Time    :   2026/01/14 16:27:25
@Author  :   rj 
@Version :   1.0
@Desc    :   山脉数组的峰顶索引
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 初始化左右边界
        # 从1开始是因为题目保证arr[0]不可能是峰顶（山脉数组定义）
        # 到len(arr)-2结束是因为arr[-1]也不可能是峰顶
        left, right = 1, len(arr) - 2

        # 使用二分查找寻找峰顶
        # 条件 left < right 确保最终left和right会收敛到同一个位置
        while left < right:
            # 计算中间索引
            mid = (left + right) // 2

            # 比较中间元素和它右边的元素
            if arr[mid] < arr[mid + 1]:
                # 如果当前处于上升坡，峰顶在右侧
                # 将左边界移到mid+1，排除左侧不可能的区域
                left = mid + 1
            else:
                # 如果当前处于下降坡或峰顶位置，峰顶在左侧或就是当前位置
                # 将右边界移到mid，保留mid作为可能的峰顶候选
                right = mid
        
        # 循环结束时，left == right，这就是峰顶的索引
        # 因为山脉数组保证有且只有一个峰顶，所以一定能找到
        return left