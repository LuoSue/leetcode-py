#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   322_Coin_Change.py
@Time    :   2025/04/27 22:31:25
@Author  :   rj 
@Version :   1.0
@Desc    :   零钱兑换
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        使用动态规划解决零钱兑换问题，找到组成目标金额的最少硬币数
        
        :param coins: 可用的硬币面额列表
        :param amount: 目标金额
        :return: 组成目标金额的最少硬币数，如果无法组成则返回-1
        """
        # 初始化动态规划数组，dp[i]表示组成金额i所需的最少硬币数
        # 初始值设为amount + 1，相当于一个较大的值（因为最多需要amount个1元硬币）
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 金额为0时不需要任何硬币
        
        # 遍历从1到amount的所有金额
        for i in range(1, amount + 1):
            # 对于每个金额，尝试所有可用的硬币面额
            for coin in coins:
                # 如果当前硬币面额小于等于当前金额i，则可以考虑使用该硬币
                if coin <= i:
                    # 更新dp[i]为使用当前硬币后的最小硬币数（dp[i - coin] + 1）
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 如果dp[amount]的值没有被更新（仍然为初始值amount + 1），说明无法组成目标金额，返回-1
        # 否则返回dp[amount]
        return dp[amount] if dp[amount] <= amount else -1