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
        # 递归终止条件：当链表为空或只剩下一个节点时，直接返回该节点作为新的头节点
        if not head or not head.next:
            return head

        # 递归反转剩余链表，new_head 是反转后的新头节点
        new_head = self.reverseListRecursive(head.next)

        head.next.next = head  # 将当前节点的 next 指向当前节点，完成反转
        head.next = None

        return new_head  # 返回反转后的新头节点

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代方式反转链表
        """
        pre = None  # 前一个节点
        cur = head  # 当前节点

        while cur is not None:
            next_node = cur.next  # 保存下一个节点
            cur.next = pre  # 当前节点指向前一个节点，实现局部反转
            pre = cur  # 更新前一个节点为当前节点
            cur = next_node  # 移动到下一个节点

        return pre  # pre 最终指向新的头节点
