#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   135_Candy.py
@Time    :   2025/07/08 15:04:18
@Author  :   rj
@Version :   1.0
@Desc    :   分发糖果：每个孩子至少分一个糖果，评分高的孩子必须比相邻的孩子分得多。
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)  # 孩子数量
        candies = [1] * n  # 初始化，每个孩子先分一个糖果

        # 从左到右：如果当前孩子评分比左边高，就比左边多分一个糖果
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # 从右到左：如果当前孩子评分比右边高，且糖果数不比右边多，就更新为比右边多一个
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)  # 返回糖果总数

    def candy_optimized(self, ratings: List[int]) -> int:
        """
        空间优化版本：不使用额外数组，只维护总糖果数和上升/下降坡长度。
        """
        n = len(ratings)
        if n <= 1:
            return n

        total = 1  # 第一个孩子先分1个
        up = 0  # 当前上升坡长度
        down = 0  # 当前下降坡长度
        peak = 0  # 上一次上升的峰值长度

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                # 上坡，更新上升长度，重置下坡
                up += 1
                peak = up
                down = 0
                total += 1 + up
            elif ratings[i] == ratings[i - 1]:
                # 平坡，重置所有坡
                up = down = peak = 0
                total += 1
            else:
                # 下坡
                up = 0
                down += 1
                total += 1 + down - (1 if down <= peak else 0)
                # 如果下降长度超过了上升峰值，说明峰值那个人分少了，需要补一个

        return total
