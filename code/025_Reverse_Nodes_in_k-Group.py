#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   025_Reverse_Nodes_in_k-Group.py
@Time    :   2025/05/06 10:44:46
@Author  :   rj
@Version :   1.0
@Desc    :   每 k 个节点一组翻转链表
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点的值
        self.next = next  # 指向下一个节点的指针


class Solution:
    def reverseKGroupIterative(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        """
        迭代法：每 k 个节点一组翻转链表
        """

        # 计算链表长度
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = getLength(head)

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while length >= k:
            curr = prev_group_end.next  # 当前组的起始节点
            next_group_start = curr  # 保存下一组的起始节点

            # 翻转当前 k 个节点
            prev = None
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # 连接翻转后的部分
            prev_group_end.next = prev
            next_group_start.next = curr

            # 更新 prev_group_end 为当前组的末尾
            prev_group_end = next_group_start

            length -= k  # 剩余长度减去 k

        return dummy.next

    def reverseKGroupRecursive(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        """
        递归法：每 k 个节点一组翻转链表
        """

        # 翻转 start 到 end 之间的节点（不包括 end）
        def reverseLinkedList(start, end):
            prev = None
            current = start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        count = 0
        node = head
        # 检查剩余节点是否足够 k 个
        while node and count < k:
            node = node.next
            count += 1

        if count == k:
            # 翻转前 k 个节点
            reversed_head = reverseLinkedList(head, node)
            # 递归翻转剩余部分，并接到当前部分后面
            head.next = self.reverseKGroupRecursive(node, k)
            return reversed_head

        # 不足 k 个节点，直接返回头节点
        return head
