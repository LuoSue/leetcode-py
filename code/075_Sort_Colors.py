#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   075_Sort_Colors.py
@Time    :   2025/05/12 23:00:35
@Author  :   rj
@Version :   1.0
@Desc    :   颜色分类
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 初始化三个颜色的计数器
        count0, count1, count2 = 0, 0, 0

        # 遍历数组，统计0, 1, 2的个数
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # 根据计数结果更新原数组
        # 将前count0个元素设为0
        for i in range(count0):
            nums[i] = 0
        # 将接下来的count1个元素设为1
        for i in range(count0, count0 + count1):
            nums[i] = 1
        # 将最后count2个元素设为2
        for i in range(count0 + count1, count0 + count1 + count2):
            nums[i] = 2
