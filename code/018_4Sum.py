#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   18_4Sum.py
@Time    :   2025/04/15 16:09:25
@Author  :   rj 
@Version :   1.0
@Desc    :   四数之和
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 首先对数组进行排序，这是多指针解法的基础
        nums.sort()
        n = len(nums)
        result = []  # 存储最终结果的列表

        # 第一层循环，固定第一个数
        for i in range(n - 3):
            # 跳过重复的第一个数，避免重复解
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 提前终止条件1：当前i及后续最小的三个数之和已经大于target
            # 由于数组已排序，后续所有组合都会更大，可以直接结束整个循环
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            
            # 提前终止条件2：当前i及最大的三个数之和仍然小于target
            # 说明这个i太小，跳过继续尝试更大的i
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            # 第二层循环，固定第二个数
            for j in range(i + 1, n - 2):
                # 跳过重复的第二个数
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 提前终止条件3：当前i,j及后续最小的两个数之和已经大于target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                
                # 提前终止条件4：当前i,j及最大的两个数之和仍然小于target
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                # 初始化双指针
                left = j + 1
                right = n - 1

                # 双指针遍历寻找符合条件的组合
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum > target:
                        # 和太大，需要减小，右指针左移
                        right -= 1
                    elif current_sum < target:
                        # 和太小，需要增大，左指针右移
                        left += 1
                    else:
                        # 找到符合条件的组合，加入结果列表
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # 跳过左侧重复元素
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1  # 移动到下一个不同元素
                        
                        # 跳过右侧重复元素
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1  # 移动到下一个不同元素
        
        return result