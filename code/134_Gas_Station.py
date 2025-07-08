#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   134_Gas_Station.py
@Time    :   2025/07/08 14:53:00
@Author  :   rj
@Version :   1.0
@Desc    :   加油站（贪心算法）
             在一圈加油站中寻找一个起点，使得汽车能够绕行一圈
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total_tank 表示总的油量盈余（总加油 - 总花费）
        # current_tank 表示当前起点到当前位置的油量盈余
        # starting_station 表示尝试的起始加油站索引
        total_tank, current_tank, starting_station = 0, 0, 0

        for i in range(len(gas)):
            # 当前加油站的油量盈余 = 加油量 - 花费油量
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            # 如果当前油量不足以到达下一个加油站，则说明不能从当前起点到当前位置
            if current_tank < 0:
                # 将起点设置为下一个加油站
                starting_station = i + 1
                # 重置当前油量盈余
                current_tank = 0

        # 如果总油量盈余 >= 0，说明存在解，返回起点索引；否则返回 -1
        return starting_station if total_tank >= 0 else -1
