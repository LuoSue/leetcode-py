#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   031_Next_Permutation.py
@Time    :   2025/05/12 23:01:45
@Author  :   rj
@Version :   1.0
@Desc    :   下一个排列
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Step 1: 从右往左找到第一个下降点
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # 存在下降点
            # Step 2: 找到比 nums[i] 大的最小值
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i] 和 nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: 反转 nums[i+1:] 使其变为升序
        nums[i + 1 :] = nums[i + 1 :][::-1]
