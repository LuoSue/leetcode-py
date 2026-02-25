#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   215_Kth_Largest_Element_in_an_Array.py
@Time    :   2025/05/12 17:49:01
@Author  :   rj
@Version :   1.1
@Desc    :   数组中的第K个最大元素
"""

import heapq
import random
from typing import List


class Solution:
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        # 创建一个大小为k的最小堆（堆顶元素是当前堆中最小的）
        # 这样堆中始终保存着最大的k个元素，堆顶就是第k大的元素
        min_heap = []

        # 遍历数组中的每个元素
        for num in nums:
            # 将当前元素加入堆中
            heapq.heappush(min_heap, num)
            # 如果堆的大小超过k，说明堆中元素多于k个
            if len(min_heap) > k:
                # 弹出堆顶元素（当前堆中最小的元素）
                # 保持堆的大小始终为k，且堆中元素是当前遍历过的元素中最大的k个
                heapq.heappop(min_heap)

        # 遍历完成后，堆顶元素就是第k大的元素
        # 因为堆中保存的是最大的k个元素，堆顶是这k个中最小的
        return min_heap[0]

    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        # 第k大的元素在排序后数组中的索引是 len(nums) - k
        # 例如：[3,2,1,5,6,4], k=2, 排序后[1,2,3,4,5,6], 第2大的元素5的索引是4 = 6-2
        target = len(nums) - k

        def quick_select(left, right):
            # 随机选择基准元素，避免最坏情况
            pivot_index = random.randint(left, right)
            # 将基准元素交换到最右边
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 基准值
            pivot = nums[right]
            # i指向小于等于基准值的区域的右边界
            i = left

            # 遍历[left, right-1]区间
            for j in range(left, right):
                # 如果当前元素小于等于基准值
                if nums[j] <= pivot:
                    # 将其交换到左侧区域
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            # 将基准值放到正确位置（所有小于等于它的元素在左边）
            nums[i], nums[right] = nums[right], nums[i]

            # 如果基准值的位置正好是目标位置，直接返回
            if i == target:
                return nums[i]
            # 如果基准值位置小于目标位置，说明第k大的元素在右半部分
            elif i < target:
                return quick_select(i + 1, right)
            # 如果基准值位置大于目标位置，说明第k大的元素在左半部分
            else:
                return quick_select(left, i - 1)

        # 开始快速选择
        return quick_select(0, len(nums) - 1)