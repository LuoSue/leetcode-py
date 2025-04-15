#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   015_3Sum.py
@Time    :   2025/04/15 11:05:42
@Author  :   rj
@Version :   1.0
@Desc    :   三数之和
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        找出所有三个数之和为0的不重复组合
        
        参数:
            nums: 整数列表
            
        返回:
            所有满足条件的三元组列表
        """
        # 先对数组进行排序，方便后续处理
        nums.sort()
        result = []
        n = len(nums)

        # 遍历数组，固定第一个数
        for i in range(n - 2):
            # 如果第一个数已经大于0，由于数组已排序，后面的数更大，不可能和为0
            if nums[i] > 0:
                break

            # 如果当前数加上最大的两个数仍小于0，说明当前数太小，跳过
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue

            # 跳过重复的第一个数，避免结果重复
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            # 将三数之和问题转化为两数之和问题，固定 i，调整 left 与 right
            left, right = i + 1, n - 1  # 左右指针分别指向剩余部分的开始和结束

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum > 0:
                    # 两数之和太大，右指针左移
                    right -= 1
                elif current_sum < 0:
                    # 两数之和太小，左指针右移
                    left += 1
                else:
                    # 找到满足条件的三元组
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过重复的左元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的右元素
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 移动指针寻找新的组合
                    left += 1
                    right -= 1

        return result