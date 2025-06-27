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

    def sortColors_Dutch_National_Flag(self, nums: List[int]) -> None:
        """
        荷兰国旗问题模板：
        - 将数组分成三段：
            - [0, p0-1]：全是 0（红色）
            - [p0, i-1]：全是 1（白色）
            - [i, p2]：待处理区域
            - [p2+1, end]：全是 2（蓝色）

        扫描规则：
        - nums[i] == 0：交换到前面去（和 p0），p0++, i++
        - nums[i] == 1：跳过，i++
        - nums[i] == 2：交换到后面去（和 p2），p2--，i 不变（因为新换来的数还未处理）
        """

        p0 = 0  # 下一个 0 应该放置的位置
        p2 = len(nums) - 1  # 下一个 2 应该放置的位置
        i = 0  # 当前扫描位置

        while i <= p2:
            if nums[i] == 0:
                # 把当前 0 交换到前面的区域
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1  # 交换后的 nums[i] 是 1 或 0，已经处理过
            elif nums[i] == 2:
                # 把当前 2 交换到后面的区域
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                # i 不加，因为换过来的可能是 0/1/2，需要重新判断
            else:
                # 是 1，留在中间区域
                i += 1
