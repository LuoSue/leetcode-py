#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   042_Trapping_Rain_Water.py
@Time    :   2025/04/15 11:33:22
@Author  :   rj
@Version :   1.0
@Desc    :   接雨水问题 - 给定一个高度图，计算能接多少雨水
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        使用双指针法计算能接的雨水量
        
        参数:
            height: 一个非负整数列表，表示每个柱子的高度
            
        返回:
            能接住的雨水总量
        """
        # 如果柱子数量少于3个，无法形成凹槽接住雨水
        if len(height) < 3:
            return 0

        water = 0  # 初始化雨水总量
        left, right = 0, len(height) - 1  # 初始化左右指针
        left_max, right_max = height[0], height[-1]  # 初始化左右两边的最大高度

        # 当左指针小于右指针时循环
        while left < right:
            if height[left] < height[right]:
                # 如果左边当前高度大于等于左边最大高度，更新左边最大高度
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # 否则计算当前位置能接的雨水量并累加
                    water += left_max - height[left]
                left += 1  # 左指针右移
            else:
                # 如果右边当前高度大于等于右边最大高度，更新右边最大高度
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # 否则计算当前位置能接的雨水量并累加
                    water += right_max - height[right]
                right -= 1  # 右指针左移

        return water  # 返回总雨水量
    
    def trap_monotone_stack(self, height: List[int]) -> int:
        """
        使用单调栈解法计算能接的雨水量
        
        参数:
            height: 一个非负整数列表，表示每个柱子的高度
            
        返回:
            能接住的雨水总量
        """
        # 如果柱子数量少于3个，无法形成凹槽接住雨水
        if len(height) < 3:
            return 0
        
        water = 0  # 初始化雨水总量
        stack = []  # 初始化单调栈，存储柱子的索引
        
        # 遍历每个柱子
        for i in range(len(height)):
            # 当栈不为空且当前柱子高度大于栈顶柱子高度时
            while stack and height[stack[-1]] < height[i]:
                current = stack.pop()  # 弹出栈顶元素作为当前凹槽的底部
                
                # 如果栈为空，说明左边没有边界，无法形成凹槽
                if not stack:
                    break
                
                left = stack[-1]  # 新的栈顶元素作为左边界
                right = i         # 当前索引作为右边界
                
                # 计算当前凹槽的高度
                # 取左右边界中较小的那个减去底部高度
                h = min(height[i], height[left]) - height[current]
                
                # 计算当前凹槽的宽度
                w = right - left - 1
                
                # 将当前凹槽的雨水量累加到总量中
                water += h * w
            
            # 将当前柱子索引入栈
            stack.append(i)
        
        return water  # 返回总雨水量
    
    
    def trap_dynamic_programming(self, height: List[int]) -> int:
        """
        使用动态规划解法(前缀和，后缀和)计算能接的雨水量
        
        参数:
            height: 一个非负整数列表，表示每个柱子的高度
            
        返回:
            能接住的雨水总量
        """
        # 如果柱子数量少于3个，无法形成凹槽接住雨水
        if len(height) < 3:
            return 0

        n = len(height)  # 柱子总数
        water = 0        # 初始化雨水总量

        # 初始化两个数组：
        # left_max[i] 表示位置i左侧的最高柱子（包括i本身）
        # right_max[i] 表示位置i右侧的最高柱子（包括i本身）
        left_max = [0] * n
        right_max = [0] * n

        # 初始化边界值：
        # 最左边的柱子，左侧最大值就是它自己
        left_max[0] = height[0]
        # 最右边的柱子，右侧最大值就是它自己
        right_max[-1] = height[-1]

        # 从左向右遍历，计算每个位置的左侧最大值
        for i in range(1, n):
            # 当前位置的左侧最大值等于前一个位置的左侧最大值和当前高度的较大者
            left_max[i] = max(left_max[i - 1], height[i])

        # 从右向左遍历，计算每个位置的右侧最大值
        for j in range(n - 2, -1, -1):
            # 当前位置的右侧最大值等于后一个位置的右侧最大值和当前高度的较大者
            right_max[j] = max(right_max[j + 1], height[j])

        # 计算每个位置能接的雨水量
        for k in range(n):
            # 当前位置能接的雨水量等于：
            # 左右两侧最大值中的较小者（决定水位高度）减去当前柱子高度
            water += min(left_max[k], right_max[k]) - height[k]

        return water  # 返回总雨水量