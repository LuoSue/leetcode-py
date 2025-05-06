#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   019_Remove_Nth_Node_From_End_of_List.py
@Time    :   2025/05/06 10:29:28
@Author  :   rj
@Version :   1.0
@Desc    :   删除链表的倒数第 N 个结点
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建一个虚拟头结点，指向链表头，便于处理删除头结点的情况
        dummy = ListNode(0, head)
        slow = fast = dummy

        # fast 指针先向前移动 n 步
        for _ in range(n):
            fast = fast.next

        # fast 和 slow 同时移动，直到 fast 到达链表末尾
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 删除 slow.next 指向的节点，即倒数第 n 个节点
        slow.next = slow.next.next

        # 返回新的头结点
        return dummy.next
