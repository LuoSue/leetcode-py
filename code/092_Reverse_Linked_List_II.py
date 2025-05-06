#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   092_Reverse_Linked_List_II.py
@Time    :   2025/05/06 15:27:56
@Author  :   rj
@Version :   1.0
@Desc    :   反转链表 II
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Step 1: 移动 pre 到 left 的前一个节点
        for _ in range(left - 1):
            pre = pre.next

        # Step 2: 从 left 到 right 进行反转（头插法）
        curr = pre.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = pre.next
            pre.next = temp

        return dummy.next
