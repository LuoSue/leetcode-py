#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   041_First_Missing_Positive.py
@Time    :   2025/04/29 11:53:08
@Author  :   rj
@Version :   1.0
@Desc    :   缺失的第一个正数
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        解题思路：
        本题要求在时间复杂度为 O(n)、空间复杂度为 O(1) 的条件下找到缺失的第一个正整数。
        由于正整数的范围是 1 到 n（数组长度），我们可以将每个数字 nums[i] 放到其应在的位置 nums[nums[i]-1] 上。
        通过原地交换的方式构造一个“哈希映射”关系，使得 nums[i] = i + 1。
        最后再遍历一遍数组，找到第一个 nums[i] != i + 1 的位置 i，即缺失的第一个正整数为 i + 1。
        如果所有位置都满足 nums[i] == i + 1，则说明缺失的数是 n + 1。
        """
        n = len(nums)  # 获取数组的长度

        # 第一次遍历：将每个数字放到对应的位置
        for i in range(n):
            # 当nums[i]在1到n范围内且nums[i]不在正确位置时，交换它到正确的位置
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 交换当前元素和其目标位置上的元素
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 第二次遍历：检查数组中是否有缺失的正整数
        for i in range(n):
            # 如果当前位置的值不等于i+1，说明i+1是缺失的最小正整数
            if nums[i] != i + 1:
                return i + 1

        # 如果没有缺失的正整数，说明最小的缺失正整数是n+1
        return n + 1
