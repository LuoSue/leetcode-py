#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   347_Top_K_Frequent_Elements.py
@Time    :   2025/05/12 17:50:18
@Author  :   rj
@Version :   1.0
@Desc    :   前 K 个高频元素
"""

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 使用哈希表统计每个数字出现的频率
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # 构建一个最小堆，堆中存储的是 (频率, 数字) 的元组
        # 保证堆的大小不超过 k
        min_heap = []
        for num, count in freq.items():
            if len(min_heap) < k:
                # 如果堆的大小小于 k，直接入堆
                heapq.heappush(min_heap, (count, num))
            else:
                # 如果当前元素频率比堆顶元素高，替换堆顶
                if count > min_heap[0][0]:
                    heapq.heappop(min_heap)  # 弹出频率最低的元素
                    heapq.heappush(min_heap, (count, num))  # 加入当前高频元素

        # 从堆中取出元素，只返回数字部分
        return [num for (count, num) in min_heap]
