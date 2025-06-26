#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   152_Maximum_Product_Subarray.py
@Time    :   2025/04/28 10:09:29
@Author  :   rj
@Version :   1.0
@Desc    :   乘积最大子数组
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        思路：
        本题是一个动态规划问题，要求返回一个子数组的最大乘积。

        难点在于：
        - 数组中可能包含负数，会使最小值变成最大值，最大值变成最小值；
        - 所以必须同时维护当前的最大乘积（max_product）和最小乘积（min_product）；

        状态转移：
        - 对于每个元素 nums[i]，它可能成为：
            1. 当前子数组的起点（自己本身）
            2. 接在前面最大乘积后面（max_product * nums[i]）
            3. 接在前面最小乘积后面（min_product * nums[i]）
        - 所以：
            max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
            min_product = min(nums[i], max_product * nums[i], min_product * nums[i])
        - 由于会修改 max_product，因此更新前先交换 max/min，如果 nums[i] 为负。

        时间复杂度：O(n)
        空间复杂度：O(1)
        """

        # 初始化最大乘积、最小乘积和结果为第一个元素
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        # 遍历数组，从第二个元素开始更新 max_product 和 min_product
        for i in range(1, len(nums)):
            num = nums[i]

            # 如果当前数字是负数，交换最大和最小乘积
            # 因为负数乘以前面的最小值可能变成最大值
            if num < 0:
                max_product, min_product = min_product, max_product

            # 当前位置的最大乘积：要么是当前数字本身，要么是乘以前面的最大乘积
            max_product = max(num, max_product * num)
            # 同理，更新当前位置的最小乘积
            min_product = min(num, min_product * num)

            # 更新全局最大值
            result = max(result, max_product)

        return result
