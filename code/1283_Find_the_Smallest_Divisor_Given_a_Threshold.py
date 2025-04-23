#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1283_Find_the_Smallest_Divisor_Given_a_Threshold.py
@Time    :   2025/04/23 10:10:17
@Author  :   rj 
@Version :   1.0
@Desc    :   使结果不超过阈值的最小除数
"""

from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 初始化二分查找的左右边界
        left, right = 1, max(nums)

        # 使用二分查找来找满足条件的最小除数
        while left < right:
            # 取中间值作为当前尝试的除数
            mid = (left + right) // 2

            # 计算所有数字除以当前除数后的向上取整之和
            # (num + mid - 1) // mid 是等价于 math.ceil(num / mid)
            total = sum((num + mid - 1) // mid for num in nums)

            # 如果总和超过阈值，说明除数太小，需要增大
            if total > threshold:
                left = mid + 1
            else:
                # 否则说明当前除数可行，尝试更小的除数
                right = mid

        # 返回最小满足条件的除数
        return left
