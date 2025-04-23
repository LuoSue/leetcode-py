#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1011_Capacity_To_Ship_Packages_Within_D_Days.py
@Time    :   2025/04/23 10:46:15
@Author  :   rj 
@Version :   1.0
@Desc    :   在 D 天内送达包裹的能力
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 船的最小运载能力至少要等于最重的包裹，
        # 否则无法将所有包裹运输；最大能力为所有包裹总重量（一次运完）
        left = max(weights)
        right = sum(weights)
        
        # 判断在给定的运载能力下是否可以在指定天数内完成运输
        def canShip(capacity):
            current = 0  # 当前这一天已装载的总重量
            days_needed = 1  # 所需天数，初始为1天
            for w in weights:
                # 如果当前包裹加上后超出容量，则新的一天开始
                if current + w > capacity:
                    days_needed += 1
                    current = w  # 新一天开始，重新装载当前包裹
                else:
                    current += w  # 当前包裹加入当天运输
                # 如果天数超过限制，说明此容量不够
                if days_needed > days:
                    return False
            return True  # 在限制天数内完成运输
        
        # 二分查找最小满足条件的运载能力
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                # 如果可以在mid容量下完成运输，尝试更小容量
                right = mid
            else:
                # 否则需要增加容量
                left = mid + 1
        
        return left  # left最终即为最小满足条件的运载能力
