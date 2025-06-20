#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   148_Sort_List.py
@Time    :   2025/05/06 10:54:07
@Author  :   rj
@Version :   1.0
@Desc    :   排序链表
"""

from typing import Optional


# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点值
        self.next = next  # 下一个节点指针


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或只有一个节点，直接返回
        if not head or not head.next:
            return head

        # Step 1: 均分链表为两半
        left, right = self.splitList(head)

        # Step 2: 对两半分别排序
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        # Step 3: 排序好的两半合并为一个链表
        return self.merge(left_sorted, right_sorted)

    def splitList(self, head: ListNode) -> tuple[ListNode, ListNode]:
        # 使用快慢指针找到中点，slow最后停在左半部分的尾部
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # prev 就是中点左侧最后一个节点，断开连接
        mid = slow
        if prev:
            prev.next = None

        return head, mid

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2  # 接上剩余部分
        return dummy.next
