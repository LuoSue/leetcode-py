#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   023_Merge_k_Sorted_Lists.py
@Time    :   2025/05/06 10:59:33
@Author  :   rj
@Version :   1.0
@Desc    :   合并 K 个升序链表
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 使用优先队列（最小堆）存储节点值及其对应链表索引
        heap = []
        # 将每个链表的头节点加入堆中
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(
                    heap, (node.val, i, node)
                )  # (节点值, 链表索引, 节点对象)

        # 创建虚拟头节点，方便处理结果链表
        dummy = ListNode()
        current = dummy  # 当前指针，用于构建结果链表

        # 不断从堆中取出最小元素，接到结果链表上
        while heap:
            val, i, node = heapq.heappop(heap)  # 弹出堆顶最小节点
            current.next = node  # 将最小节点接到当前链表后面
            current = current.next  # 移动当前指针到最新节点
            if node.next:
                # 如果当前节点还有下一个节点，将其加入堆中
                heapq.heappush(heap, (node.next.val, i, node.next))

        # 返回合并后的链表（去掉虚拟头节点）
        return dummy.next

    def mergeKListsDivideAndConquer(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # 如果链表数组为空，直接返回 None
        if not lists:
            return None
        # 如果链表数组中只有一个链表，直接返回它
        if len(lists) == 1:
            return lists[0]

        # 将链表数组分成两半，递归分别合并
        mid = len(lists) // 2
        left = self.mergeKListsDivideAndConquer(lists[:mid])  # 合并左半部分
        right = self.mergeKListsDivideAndConquer(lists[mid:])  # 合并右半部分

        # 合并左右两部分得到的链表
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 创建虚拟头节点，便于构造新链表
        dummy = ListNode()
        current = dummy  # 当前指针，用于构建新链表

        # 逐节点比较两个链表，将较小的节点接到新链表后面
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next  # l1 向后移动
            else:
                current.next = l2
                l2 = l2.next  # l2 向后移动
            current = current.next  # 当前指针向后移动

        # 当一个链表遍历完后，将另一个链表剩下的部分直接接上去
        current.next = l1 if l1 else l2

        # 返回合并后的链表（去掉虚拟头节点）
        return dummy.next
