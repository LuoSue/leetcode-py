#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   034_Find_First_and_Last_Position_of_Element_in_Sorted_Array.py
@Time    :   2025/04/16 11:24:16
@Author  :   rj 
@Version :   1.0
@Desc    :   在排序数组中查找元素的第一个和最后一个位置
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        在排序数组nums中查找target的第一个和最后一个位置
        如果target不存在，返回[-1, -1]
        时间复杂度: O(log n)
        """
        
        def find_left(nums, target):
            """
            使用二分查找找到target的最左位置
            :param nums: 排序数组
            :param target: 要查找的目标值
            :return: target的最左索引，如果不存在返回-1
            """
            left, right = -1, len(nums)
            res = -1  # 初始化结果为-1，表示未找到

            while left <= right:
                mid = (left + right) // 2  # 计算中间位置

                if nums[mid] >= target:
                    right = mid  # 向左半部分继续搜索
                    if nums[mid] == target:
                        res = mid  # 更新结果为当前找到的target位置
                else:
                    left = mid  # 向右半部分继续搜索

            return res

        def find_right(nums, target):
            """
            使用二分查找找到target的最右位置
            :param nums: 排序数组
            :param target: 要查找的目标值
            :return: target的最右索引，如果不存在返回-1
            """
            left, right = -1, len(nums)
            res = -1  # 初始化结果为-1，表示未找到

            while left <= right:
                mid = (left + right) // 2  # 计算中间位置

                if nums[mid] <= target:
                    left = mid  # 向右半部分继续搜索
                    if nums[mid] == target:
                        res = mid  # 更新结果为当前找到的target位置
                else:
                    right = mid  # 向左半部分继续搜索

            return res

        # 如果最左位置没找到，说明target不存在于数组中
        if find_left(nums, target) == -1:
            return [-1, -1]

        # 返回最左和最右位置
        return [find_left(nums, target), find_right(nums, target)]