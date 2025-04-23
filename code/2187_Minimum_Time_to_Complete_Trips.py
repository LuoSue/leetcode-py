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
        # 最短可能时间为1，最长时间为最慢的司机做完所有旅程所需的时间
        left, right = 1, min(time) * totalTrips

        # 使用二分查找，寻找能够完成所有旅程所需的最小时间
        while left < right:
            mid = (left + right) // 2  # 当前猜测的时间
            total = 0  # 当前猜测时间内可以完成的总旅程数

            # 计算在mid时间内，每个司机最多可以完成多少旅程
            for t in time:
                total += mid // t
                # 如果已经超过所需旅程数，可以提前结束
                if total >= totalTrips:
                    break

            # 如果能完成所需旅程数，则尝试缩小右边界
            if total >= totalTrips:
                right = mid
            # 否则需要更长的时间，调整左边界
            else:
                left = mid + 1

        # 最小的可行时间即为结果
        return left
