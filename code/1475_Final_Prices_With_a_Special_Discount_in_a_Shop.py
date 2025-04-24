#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1475_Final_Prices_With_a_Special_Discount_in_a_Shop.py
@Time    :   2025/04/24 11:52:22
@Author  :   rj
@Version :   1.0
@Desc    :   商品折扣后的最终价格
"""

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        # 初始化结果数组，长度与 prices 相同，初始值为0
        result = [0] * n

        # 用于存储索引的单调栈（栈中保存的是候选折扣的商品索引）
        stack = []

        # 从后往前遍历商品价格列表
        for i in range(n - 1, -1, -1):
            # 如果栈顶对应的价格大于当前价格，则不能作为折扣，出栈
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()

            # 如果栈不为空，栈顶价格可以作为当前商品的折扣
            if stack:
                result[i] = prices[i] - prices[stack[-1]]
            else:
                # 否则当前商品无折扣
                result[i] = prices[i]

            # 将当前商品索引入栈，作为左侧商品的候选折扣
            stack.append(i)

        return result
