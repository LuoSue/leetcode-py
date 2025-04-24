#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   475_Heaters.py
@Time    :   2025/04/24 10:40:03
@Author  :   rj 
@Version :   1.0
@Desc    :   供暖器
"""

import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        找到覆盖所有房屋的最小加热半径。

        Args:
            houses: 一个包含房屋位置的列表。
            heaters: 一个包含供暖器位置的列表。

        Returns:
            覆盖所有房屋的最小加热半径。
        """
        heaters.sort()  # 对供暖器的位置进行排序，这对于使用二分查找至关重要
        max_radius = 0  # 初始化最大半径为 0

        for house in houses:  # 遍历每个房屋的位置
            # 使用 bisect_left 找到排序后的 heaters 列表中第一个大于或等于 house 的元素的索引
            left = bisect.bisect_left(heaters, house)
            min_dist = float('inf')  # 初始化最小距离为无穷大

            # 如果找到了一个大于或等于 house 的供暖器
            if left < len(heaters):
                min_dist = min(min_dist, heaters[left] - house)  # 计算该供暖器到房屋的距离

            # 如果在找到的供暖器的左边还有一个供暖器（即 left > 0）
            if left > 0:
                min_dist = min(min_dist, house - heaters[left - 1])  # 计算前一个供暖器到房屋的距离

            # 更新最大半径，确保能够覆盖当前房屋
            max_radius = max(max_radius, min_dist)

        return max_radius  # 返回覆盖所有房屋所需的最小加热半径