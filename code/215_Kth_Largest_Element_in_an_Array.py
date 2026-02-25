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
        # 目标索引：第k大的元素在排序后数组中的位置是 len(nums) - k
        target = len(nums) - k

        def quick_select(left, right):
            # 如果区间只有一个元素，直接返回该元素
            if left >= right:
                return nums[left]

            # 随机选择一个基准元素，避免最坏情况
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            # 三路划分：
            # lt 指向小于基准的区域的末尾
            # i 是当前遍历指针
            # gt 指向大于基准的区域的起始位置
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    # 将小于基准的元素交换到左边
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    # 将大于基准的元素交换到右边
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    # 等于基准的元素，继续遍历
                    i += 1

            # 现在数组被划分为三部分：[left, lt-1] < pivot, [lt, gt] = pivot, [gt+1, right] > pivot
            # 如果目标索引在等于基准的区域内，直接返回基准值
            if target >= lt and target <= gt:
                return nums[lt]
            # 如果目标索引在左边，递归处理左区间
            elif target < lt:
                return quick_select(left, lt - 1)
            # 如果目标索引在右边，递归处理右区间
            else:
                return quick_select(gt + 1, right)

        # 开始快速选择
        return quick_select(0, len(nums) - 1)
