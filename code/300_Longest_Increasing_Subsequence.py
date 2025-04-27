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
        # 如果输入列表为空，返回0
        if not nums:
            return 0
        # 初始化dp数组，dp[i]表示以nums[i]结尾的最长递增子序列的长度
        dp = [1] * len(nums)
        # 遍历数组
        for i in range(1, len(nums)):
            for j in range(i):
                # 如果前面的元素小于当前元素，更新dp[i]
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # 返回dp数组中的最大值，即最长递增子序列的长度
        return max(dp)

    def lengthOfLISGreedy(self, nums: List[int]) -> int:
        # tails数组用于存储每个长度的递增子序列的最小尾元素
        tails = []
        for num in nums:
            # 使用二分查找确定num应该放置的位置
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                # 如果num比tails所有元素都大，直接追加到tails末尾
                tails.append(num)
            else:
                # 否则，用当前num替换掉tails中第一个大于等于num的元素
                tails[idx] = num
        # tails的长度就是最长递增子序列的长度
        return len(tails)
