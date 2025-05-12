#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   215_Kth_Largest_Element_in_an_Array.py
@Time    :   2025/05/12 17:49:01
@Author  :   rj
@Version :   1.0
@Desc    :   数组中的第K个最大元素
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 创建一个大小为 k 的最小堆（堆顶元素是当前堆中最小的）
        min_heap = []

        # 遍历数组中的每个元素
        for num in nums:
            # 如果堆的大小还没到 k，直接将当前元素加入堆中
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                # 如果当前元素比堆顶元素大，说明它可能是前 k 大的元素之一
                # 把堆顶元素弹出，加入当前元素，保持堆的大小为 k
                if num > min_heap[0]:
                    heapq.heappushpop(min_heap, num)

        # 遍历完成后，堆顶元素就是第 k 大的元素
        return min_heap[0]
