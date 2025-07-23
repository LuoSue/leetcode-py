#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   494_Target_Sum.py
@Time    :   2025/07/23 11:27:40
@Author  :   rj
@Version :   1.0
@Desc    :   目标和
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 数组元素总和
        total_sum = sum(nums)

        # 如果 (total_sum + target) 不是偶数，或者目标值绝对值比总和还大，则无法找到合法方案
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0

        # 转换为子集和问题：寻找子集，使其和为 subset_sum
        # subset_sum = (P - N) + (P + N) / 2 = (target + total_sum) / 2
        subset_sum = (total_sum + target) // 2

        # 初始化一维动态规划数组 dp，其中 dp[i] 表示和为 i 的子集个数
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # 和为 0 只有 1 种方式（不选任何数）

        # 遍历数组中的每个数字
        for num in nums:
            # 倒序遍历是为了保证每个 num 只被使用一次（0/1 背包）
            for j in range(subset_sum, num - 1, -1):
                # 状态转移：将当前 num 加入到和为 j - num 的方案中
                dp[j] += dp[j - num]

        # 返回最终的结果：和为 subset_sum 的子集个数
        return dp[subset_sum]
