#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   056_Merge_Intervals.py
@Time    :   2025/04/29 11:49:09
@Author  :   rj
@Version :   1.0
@Desc    :   合并区间
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 如果只有一个区间，直接返回该区间
        if len(intervals) == 1:
            return intervals

        # 按照区间的起始位置排序
        intervals.sort(key=lambda x: x[0])
        result = []  # 用于存储合并后的区间

        # 遍历所有区间
        for interval in intervals:
            # 如果result为空，或者当前区间的起始位置大于result最后一个区间的结束位置，说明不重叠，直接加入result
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                # 如果当前区间与result最后一个区间有重叠，合并两个区间
                result[-1][1] = max(result[-1][1], interval[1])

        # 返回合并后的所有区间
        return result
