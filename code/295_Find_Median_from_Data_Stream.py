#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   295_Find_Median_from_Data_Stream.py
@Time    :   2025/05/12 17:53:02
@Author  :   rj
@Version :   1.0
@Desc    :   数据流的中位数
"""

import heapq


class MedianFinder:
    def __init__(self):
        # 最大堆：保存较小的一半数字
        self.max_heap = []  # Python heapq 默认是最小堆，所以存储负数来模拟最大堆
        # 最小堆：保存较大的一半数字
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 首先加入最大堆（负数以模拟最大堆）
        heapq.heappush(self.max_heap, -num)

        # 将最大堆的最大值移到最小堆
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # 保证两个堆的平衡，最小堆不允许比最大堆大
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # 如果最大堆比最小堆多一个元素
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # 否则两个堆的大小相等，返回两个堆的平均值
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
