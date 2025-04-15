#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   016_3Sum_Closest.py
@Time    :   2025/04/15 15:43:03
@Author  :   rj 
@Version :   1.0
@Desc    :   最接近的三数之和 - 双指针解法
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 首先对数组进行排序，这是双指针法的前提
        nums.sort()
        n = len(nums)
        # 初始化答案为前三个数的和（避免使用inf，更直观）
        ans = nums[0] + nums[1] + nums[2]
        
        # 外层循环，固定第一个数
        for i in range(n - 2):
            # 跳过重复的i值，避免重复计算
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 初始化双指针
            left, right = i + 1, n - 1
            
            # 计算当前i下的最小可能三数之和（即i加上后面两个最小数）
            min_sum = nums[i] + nums[left] + nums[left + 1]
            # 如果最小和已经大于等于target，后续的和只会更大，可以直接比较并跳过
            if min_sum >= target:
                if abs(min_sum - target) < abs(ans - target):
                    ans = min_sum
                continue
            
            # 计算当前i下的最大可能三数之和（即i加上后面两个最大数）
            max_sum = nums[i] + nums[right - 1] + nums[right]
            # 如果最大和已经小于等于target，后续的和只会更小，可以直接比较并跳过
            if max_sum <= target:
                if abs(max_sum - target) < abs(ans - target):
                    ans = max_sum
                continue
            
            # 双指针遍历中间可能的组合
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # 如果正好等于target，直接返回（这是最接近的情况）
                if current_sum == target:
                    return target
                
                # 更新最接近的和
                if abs(current_sum - target) < abs(ans - target):
                    ans = current_sum
                
                # 根据当前和与target的关系移动指针
                if current_sum < target:
                    left += 1
                    # 跳过重复的left值
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # 跳过重复的right值
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        # 返回最终找到的最接近的和
        return ans