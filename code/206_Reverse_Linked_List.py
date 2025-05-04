#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   206_Reverse_Linked_List.py
@Time    :   2025/05/04 11:37:21
@Author  :   rj
@Version :   1.0
@Desc    :   反转链表
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归方式反转链表
        """
        # 如果链表为空或只有一个节点，直接返回 head
        if not head or not head.next:
            return head

        # 递归反转子链表
        new_head = self.reverseListRecursive(head.next)
        # 将当前节点的 next 的 next 指向当前节点
        head.next.next = head
        # 当前节点断开原来的 next
        head.next = None

        return new_head

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代方式反转链表
        """
        pre = None  # 前一个节点
        cur = head  # 当前节点

        while cur is not None:
            next_node = cur.next  # 保存下一个节点
            cur.next = pre        # 当前节点指向前一个节点，实现局部反转
            pre = cur             # 更新前一个节点为当前节点
            cur = next_node       # 移动到下一个节点

        return pre  # pre 最终指向新的头节点
