#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2824_Count_Pairs_Whose_Sum_is_Less_than_Target.py
@Time    :   2025/04/15 15:20:39
@Author  :   rj 
@Version :   1.0
@Desc    :   统计和小于目标的下标对数目
             LeetCode 2824题：给定一个整数数组nums和一个整数target，
             返回满足i < j且nums[i] + nums[j] < target的下标对(i, j)的数目。
"""

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        使用双指针法统计数组中满足和小于目标值的下标对数目
        
        参数:
            nums: 整数数组
            target: 目标和阈值
            
        返回:
            满足条件的下标对数目
        """
        # 首先对数组进行排序，这是双指针法的前提
        nums.sort()
        # 初始化计数器
        ans = 0
        # 初始化双指针：left指向数组开头，right指向数组末尾
        left, right = 0, len(nums) - 1

        while left < right:
            # 计算当前两个指针指向的元素之和
            temp = nums[left] + nums[right]

            if temp < target:
                # 如果和小于目标值，那么left和left+1到right-1的所有元素与right的组合都满足条件
                # 所以可以一次性增加(right - left)个有效对
                ans += right - left
                # 然后尝试更大的左值，看看是否还有更多满足条件的组合
                left += 1
            else:
                # 如果和大于等于目标值，需要尝试更小的右值
                right -= 1

        return ans