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
