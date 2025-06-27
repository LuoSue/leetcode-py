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
        原地将 nums 修改为其下一个字典序排列（即最小的“比当前大的排列”）。
        如果不存在更大的排列，则将其变为最小的排列（升序）。

        核心思想：
        1. 从后向前查找第一个「下降点」i，使得 nums[i] < nums[i+1]，
           表明 nums[i+1:] 是当前前缀下的最大排列（即单调递减）。
        2. 若找到这样的 i，从后向前找到第一个 j，使得 nums[j] > nums[i]，
           说明 nums[j] 是「比 nums[i] 大的最小数」，交换两者即可让整体变大。
        3. 为了使变大的幅度最小，我们将 i+1 之后的部分（仍为降序）翻转为升序，
           得到字典序最小的“变大”结果。

        举例说明：
        nums = [1, 3, 5, 4, 2]
        → i = 1（3 < 5）
        → j = 3（4 > 3）
        → 交换：nums = [1, 4, 5, 3, 2]
        → 翻转后缀：nums = [1, 4, 2, 3, 5]
        """

        n = len(nums)
        i = n - 2

        # Step 1: 从后往前找到第一个 nums[i] < nums[i+1] 的位置
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: 再从后往前找到第一个大于 nums[i] 的位置 j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: 交换 nums[i] 与 nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: 将 nums[i+1:] 反转为升序，得到字典序最小的后缀
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
