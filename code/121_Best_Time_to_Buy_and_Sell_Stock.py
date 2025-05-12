#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   121_Best_Time_to_Buy_and_Sell_Stock.py
@Time    :   2025/05/12 22:30:13
@Author  :   rj
@Version :   1.0
@Desc    :   买卖股票的最佳时机
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化最低价格为无穷大
        min_cost = float("inf")
        # 初始化最大利润为0
        max_profit = 0

        # 遍历股票价格列表
        for price in prices:
            # 更新最大利润：当前价格与最低价格之差
            max_profit = max(max_profit, price - min_cost)
            # 更新最低价格
            min_cost = min(min_cost, price)

        # 返回最大利润
        return max_profit
