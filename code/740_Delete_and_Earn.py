#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   740_Delete_and_Earn.py
@Time    :   2025/07/15 17:57:00
@Author  :   rj
@Version :   1.0
@Desc    :   删除并获得点数
"""

from typing import List


class Solution:
    # 动态规划方法，解决类似"打家劫舍"问题
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0  # f0表示不抢劫当前房屋时的最大点数，f1表示抢劫当前房屋时的最大点数
        for num in nums:
            f0, f1 = f1, max(f1, f0 + num)  # 更新状态，选择不抢劫或者抢劫当前房屋
        return f1  # 返回最大点数

    def deleteAndEarn(self, nums: List[int]) -> int:
        # 计算每个数出现的总点数，temp数组记录每个数的总点数
        temp = [0] * (max(nums) + 1)  # 根据输入数组的最大值创建一个临时数组
        for x in nums:
            temp[x] += x  # 累加每个数字对应的总点数
        return self.rob(temp)  # 通过rob方法，计算最大点数
