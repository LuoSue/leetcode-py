#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   300_Longest_Increasing_Subsequence.py
@Time    :   2025/04/27 23:10:21
@Author  :   rj
@Version :   1.0
@Desc    :   最长递增子序列
"""

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划思路：
        定义 dp[i] 表示以 nums[i] 结尾的最长递增子序列的长度。
        状态转移：
            对每个 nums[i]，向前寻找所有 j < i 且 nums[j] < nums[i] 的位置，
            令 dp[i] = max(dp[i], dp[j] + 1)
        最终答案是 max(dp)，即所有 dp[i] 中的最大值。

        时间复杂度：O(n^2)
        空间复杂度：O(n)
        """
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLISGreedy(self, nums: List[int]) -> int:
        """
        贪心 + 二分查找思路（也称为 Patience Sorting）：
        使用一个数组 tails，其中 tails[i] 表示长度为 i+1 的递增子序列的最小末尾元素。

        遍历数组 nums：
        - 对于每个 num，在 tails 中用二分查找找第一个 >= num 的位置 idx；
        - 如果 idx == len(tails)，说明 num 比所有尾巴都大，直接 append；
        - 否则，替换 tails[idx] 为 num（贪心地选更小的尾部元素）。

        tails 的长度即为最长递增子序列的长度。

        时间复杂度：O(n log n)，因为每次二分查找 + 最多 n 次 append
        空间复杂度：O(n)，用于 tails 数组
        """
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)
