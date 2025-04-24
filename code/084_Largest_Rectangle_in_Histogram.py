#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   084_Largest_Rectangle_in_Histogram.py
@Time    :   2025/04/24 14:42:09
@Author  :   rj 
@Version :   1.0
@Desc    :   柱状图中最大的矩形
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 在原始高度数组前后各添加一个0，方便统一处理边界情况
        heights = [0] + heights + [0]
        
        stack = []  # 单调递增栈，存储柱子的下标
        max_area = 0  # 用于记录最大矩形面积

        for i in range(len(heights)):
            # 当当前高度小于栈顶元素的高度时，说明可以结算之前的柱子了
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]  # 当前要处理的柱子的高度
                left = stack[-1]          # 左边界是新的栈顶元素
                right = i                 # 右边界是当前元素
                w = right - left - 1      # 宽度为右边界与左边界之间的距离
                max_area = max(h * w, max_area)  # 更新最大面积
            stack.append(i)  # 当前柱子的下标入栈

        return max_area
