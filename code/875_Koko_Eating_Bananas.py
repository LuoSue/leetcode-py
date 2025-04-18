#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   875_Koko_Eating_Bananas.py
@Time    :   2025/04/18 10:58:56
@Author  :   rj 
@Version :   1.0
@Desc    :   爱吃香蕉的珂珂
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 定义一个函数判断给定速度 speed 是否能在 h 小时内吃完所有香蕉
        def can_finish(speed):
            hours = 0  # 总共花费的小时数
            for pile in piles:
                # 每堆香蕉吃完需要的时间是 向上取整(pile / speed)
                # 可用 (pile + speed - 1) // speed 替代 math.ceil
                hours += (pile + speed - 1) // speed
            return hours <= h  # 判断是否在时间限制内吃完

        # 二分查找的左右边界
        left, right = 1, max(piles)
        result = right  # 初始化结果为最大值（最坏情况下每小时吃最多）

        # 开始二分查找
        while left <= right:
            mid = (left + right) // 2  # 当前尝试的速度
            if can_finish(mid):
                # 如果能吃完，说明速度可以更小，尝试左半边
                result = mid
                right = mid - 1
            else:
                # 吃不完，说明速度太慢，尝试右半边
                left = mid + 1

        return result  # 返回最小可行的速度