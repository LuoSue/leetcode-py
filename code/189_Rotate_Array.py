#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   189_Rotate_Array.py
@Time    :   2025/04/29 11:50:04
@Author  :   rj
@Version :   1.0
@Desc    :   轮转数组
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  # 获取数组的长度
        k = k % n  # 确保k在0到n-1之间，防止k大于数组长度

        # 定义一个反转子数组的函数
        def f(start, end, nums):
            while start < end:
                # 交换start和end位置的元素
                nums[start], nums[end] = nums[end], nums[start]
                start += 1  # start指针右移
                end -= 1  # end指针左移

        # 反转整个数组
        f(0, n - 1, nums)
        # 反转前k个元素
        f(0, k - 1, nums)
        # 反转剩余的n-k个元素
        f(k, n - 1, nums)
