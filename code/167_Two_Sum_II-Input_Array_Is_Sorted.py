#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   167_Two_Sum_II-Input_Array_Is_Sorted.py
@Time    :   2025/04/15 15:09:26
@Author  :   rj
@Version :   1.0
@Desc    :   两数之和 II - 输入有序数组
             LeetCode 167题：给定一个已按照升序排列的整数数组numbers，
             从数组中找出两个数满足相加之和等于目标数target。
             函数应该返回这两个数的下标值index1和index2，其中index1必须小于index2。
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        使用双指针法在有序数组中查找两数之和等于目标值
        
        参数:
            numbers: 已排序的整数数组
            target: 目标和
            
        返回:
            两个数的下标(从1开始计数)，以列表形式返回
        """
        # 初始化双指针：low指向数组开头，high指向数组末尾
        low, high = 0, len(numbers) - 1

        while low < high:
            # 计算当前两个指针指向的元素之和
            temp = numbers[low] + numbers[high]

            if temp > target:
                # 如果和大于目标值，需要减小和，因此将high指针左移
                high -= 1
            elif temp < target:
                # 如果和小于目标值，需要增大和，因此将low指针右移
                low += 1
            else:
                # 找到和等于目标值的情况，返回两个指针的位置(题目要求从1开始计数)
                return [low + 1, high + 1]
        
        # 理论上题目保证有解，所以不会执行到这里
        return [-1, -1]