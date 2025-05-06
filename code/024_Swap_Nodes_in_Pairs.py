#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   024_Swap_Nodes_in_Pairs.py
@Time    :   2025/05/06 10:35:37
@Author  :   rj
@Version :   1.0
@Desc    :   两两交换链表中的节点
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点的值
        self.next = next  # 指向下一个节点的指针


class Solution:
    def swapPairsIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代法：两两交换链表中的节点
        """
        dummy = ListNode(0, head)  # 哑节点，用于简化头节点的操作
        current = dummy  # 当前指针

        # 当存在下一对可交换的节点时进入循环
        while current.next and current.next.next:
            first = current.next  # 第一个节点
            second = current.next.next  # 第二个节点

            # 交换这两个节点
            first.next = second.next
            second.next = first
            current.next = second

            # 将当前指针向后移动两位，为下一轮交换做准备
            current = first

        # 返回新的头节点（跳过哑节点）
        return dummy.next

    def swapPairsRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归法：两两交换链表中的节点
        """
        # 如果不足两节点，则直接返回当前节点
        if not head or not head.next:
            return head

        first = head  # 第一个节点
        second = head.next  # 第二个节点

        # 递归交换后续节点
        first.next = self.swapPairsRecursive(second.next)
        second.next = first

        # 返回交换后的新头节点
        return second
