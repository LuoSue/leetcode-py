#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   023_Merge_k_Sorted_Lists.py
@Time    :   2025/05/06 10:59:33
@Author  :   rj
@Version :   1.0
@Desc    :   合并 K 个升序链表
"""

from heapq import heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # 将所有链表的头节点加入最小堆
        for node in lists:
            if node:
                heappush(min_heap, node)

        dummy = ListNode(-1)  # 哑节点
        curr = dummy

        while min_heap:
            node = heappop(min_heap)  # 取出最小值节点
            curr.next = node
            curr = node  # 移动指针

            if node.next:
                heappush(min_heap, node.next)  # 将下一个节点加入堆

        return dummy.next
