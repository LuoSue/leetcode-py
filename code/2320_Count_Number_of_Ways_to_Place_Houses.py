#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2320_Count_Number_of_Ways_to_Place_Houses.py
@Time    :   2025/07/15 17:49:43
@Author  :   rj
@Version :   1.0
@Desc    :   统计放置房子的方式数目
"""

MOD = 10**9 + 7  # 由于答案可能很大，取余 MOD 防止结果溢出


class Solution:
    def countHousePlacements(self, n: int) -> int:
        # 如果 n 为 0，表示没有地块，只有一种放置方式：不放房子
        if n == 0:
            return 1

        # a 表示前一个地块（位置）不放房子的方式数，b 表示前一个地块放房子的方式数
        a, b = 1, 2  # 第 1 个地块：不放房子；第 2 个地块：两种选择

        # 从第 3 个地块开始，逐步计算放置房子的方式数
        for _ in range(2, n + 1):
            # 更新 a 和 b：当前地块的放置方式数目是前两地块数目的和
            a, b = b, (a + b) % MOD  # a 更新为 b，b 更新为 a + b 的和取模

        # 最终返回结果，b 表示一侧放置房子的方式数目，乘以自身表示两侧分别放置的方式数目
        return (b * b) % MOD  # 最终返回两侧放置房子的方式数目
