#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2187_Minimum_Time_to_Complete_Trips.py
@Time    :   2025/04/18 11:04:09
@Author  :   rj 
@Version :   1.0
@Desc    :   完成旅途的最少时间
"""

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 判断在给定时间 t 下，是否能完成至少 totalTrips 趟旅程
        def can_finish(t):
            trips = 0
            for t_i in time:
                trips += t // t_i
            return trips >= totalTrips

        # 二分搜索范围：1 到 最快的车全程跑完所有行程所需的时间
        left, right = 1, min(time) * totalTrips
        result = right  # 初始化为最大值

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                result = mid  # 找到一个可能的最小时间
                right = mid - 1  # 尝试更小时间
            else:
                left = mid + 1  # 时间太短，旅程不够多

        return result