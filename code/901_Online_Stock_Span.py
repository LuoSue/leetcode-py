#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   901_Online_Stock_Span.py
@Time    :   2025/04/24 14:18:21
@Author  :   rj
@Version :   1.0
@Desc    :   股票价格跨度
"""


class StockSpanner:
    def __init__(self):
        # 使用一个栈来保存元组，格式为 (price, span)
        # price 表示某一天的股价，span 表示该价格的跨度
        self.stack = []

    def next(self, price: int) -> int:
        # 初始化今天的跨度为 1（至少包括今天）
        span = 1

        # 如果栈不为空，且栈顶价格小于等于当前价格
        # 说明这些日子的股价都小于或等于今天的价格，可以累加跨度
        while self.stack and self.stack[-1][0] <= price:
            # 弹出栈顶元素并将其跨度累加到当前跨度上
            _, prev_span = self.stack.pop()
            span += prev_span

        # 将当前价格及其跨度压入栈中
        self.stack.append((price, span))

        # 返回今天的跨度
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
