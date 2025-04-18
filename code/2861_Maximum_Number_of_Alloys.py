#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2861_Maximum_Number_of_Alloys.py
@Time    :   2025/04/18 11:08:33
@Author  :   rj 
@Version :   1.0
@Desc    :   最大合金数
"""

from typing import List


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        # 判断是否可以用第 machine_index 台机器制造 alloy_count 份合金
        def can_make(machine_index, alloy_count):
            total_cost = 0  # 记录总花费
            for i in range(n):
                # 每种金属总共需要的量
                need = composition[machine_index][i] * alloy_count
                # 需要购买的量 = 需要的 - 库存，不足才买
                buy = max(0, need - stock[i])
                # 计算费用
                total_cost += buy * cost[i]
                # 如果超过预算，直接返回 False
                if total_cost > budget:
                    return False
            # 所有金属都满足预算，返回 True
            return True

        # 对某台机器，使用二分查找找出它最多能制造的合金数
        def max_alloy_for_machine(machine_index):
            left, right = 0, 10**9  # 左右边界为 0 和一个很大的数
            while left < right:
                mid = (left + right + 1) // 2
                if can_make(machine_index, mid):
                    left = mid  # 可以制造，尝试更多
                else:
                    right = mid - 1  # 不行，减小数量
            return left  # 最终 left 就是该机器能制造的最大数量

        res = 0  # 最终结果
        # 遍历每台机器，取最大值
        for i in range(k):
            res = max(res, max_alloy_for_machine(i))
        return res