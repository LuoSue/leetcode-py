#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   122_Best_Time_to_Buy_and_Sell_Stock_II.py
@Time    :   2025/07/07 15:40:38
@Author  :   rj
@Version :   1.0
@Desc    :   买卖股票的最佳时机 II（可以多次买卖，但不能同时持有多股）
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # 初始化利润为0
        n = len(prices)  # 获取价格列表长度
        for i in range(1, n):  # 从第2天开始遍历
            # 如果今天的价格高于前一天，就执行“昨天买入今天卖出”的操作
            if prices[i] > prices[i - 1]:
                # 把这部分利润累加到总利润中
                profit += prices[i] - prices[i - 1]
        return profit  # 返回总利润
