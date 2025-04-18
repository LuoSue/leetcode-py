#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2563_Count_the_Number_of_Fair_Pairs.py
@Time    :   2025/04/18 10:46:38
@Author  :   rj 
@Version :   1.0
@Desc    :   统计公平数对的数目
"""

import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # 先对数组进行排序，以便后续使用二分查找
        nums.sort()
        n = len(nums)
        res = 0  # 用于统计公平数对的总数

        # 遍历每一个元素 nums[i]，从前往后找
        for i in range(n - 1):
            # 目标是找出满足条件的 j（j > i）：
            # lower <= nums[i] + nums[j] <= upper
            # 转化为：lower - nums[i] <= nums[j] <= upper - nums[i]
            # 在排序后的数组中用二分法查找满足这个区间的 j

            # 左边界：第一个大于等于 lower - nums[i] 的 j 的位置
            left = bisect.bisect_left(nums, lower - nums[i], i + 1)
            # 右边界：第一个大于 upper - nums[i] 的 j 的位置（不包含该位置）
            right = bisect.bisect_right(nums, upper - nums[i], i + 1)
            # 满足条件的 j 的数量为 right - left
            res += right - left

        return res