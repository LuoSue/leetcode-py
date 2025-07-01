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
        """
        解题思路：
        本题使用「单调递增栈」来解决，核心思想是：
        - 对于每根柱子，想知道它左边和右边第一个比它矮的位置，
          以确定以它为高时，能够扩展的最大宽度。
        - 使用栈维护一个递增的柱子序列，当遇到比栈顶矮的柱子时，
          就可以计算以栈顶为高的矩形面积。
        - 为了统一处理边界情况，在原数组前后各加一个高度为0的柱子。
        
        算法步骤：
        1. 在 heights 前后添加 0，形成新的列表，避免边界判断。
        2. 遍历每个柱子，如果当前高度大于等于栈顶，则入栈。
        3. 如果当前高度小于栈顶元素：
            - 弹出栈顶索引，计算该柱子能形成的最大矩形面积：
              - 高度为 heights[弹出的索引]
              - 宽度为 当前索引 - 新栈顶索引 - 1
        4. 不断更新 max_area。

        时间复杂度：O(n)，每个柱子最多进栈和出栈一次。
        空间复杂度：O(n)，辅助栈空间。
        """
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
