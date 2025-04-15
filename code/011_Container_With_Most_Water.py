#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   011_Container_With_Most_Water.py
@Time    :   2025/04/15 11:01:35
@Author  :   rj 
@Version :   1.0
@Desc    :   盛最多水的容器
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        给定一个数组 `height`，每个元素代表一个柱子的高度。找出两个柱子之间的最大面积，
        该面积由两者的高度和它们之间的距离决定。

        参数:
        height (List[int]): 一个整数列表，表示柱子的高度。

        返回:
        int: 能容纳最多水的容器的面积。
        """
        left, right = 0, len(height) - 1  # 初始化左右指针，分别指向数组的两端
        max_area = 0  # 初始化最大面积

        # 当左右指针没有重合时，继续计算面积
        while left < right:
            # 计算当前容器的面积
            if height[left] < height[right]:
                max_area = max(max_area, (right - left) * height[left])  # 更新最大面积
                left += 1  # 左指针右移，尝试寻找更高的柱子
            else:
                max_area = max(max_area, (right - left) * height[right])  # 更新最大面积
                right -= 1  # 右指针左移，尝试寻找更高的柱子

        return max_area  # 返回最终的最大面积
