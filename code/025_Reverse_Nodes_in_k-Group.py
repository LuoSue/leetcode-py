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
        :param head: 链表头节点
        :param k: 每组翻转的节点数
        :return: 翻转后的链表头节点
        """

        # 计算链表长度
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = getLength(head)  # 获取链表总长度

        dummy = ListNode(0)  # 创建虚拟头节点，方便处理边界情况
        dummy.next = head
        prev_group_end = dummy  # 指向前一个已翻转组的最后一个节点，初始指向虚拟头节点

        while length >= k:  # 只要剩余节点数大于等于k就继续处理
            curr = prev_group_end.next  # 当前组的起始节点
            next_group_start = curr  # 保存下一组的起始节点（翻转后变为当前组的尾节点）

            # 翻转当前 k 个节点
            prev = None
            for _ in range(k):
                next_node = curr.next  # 保存下一个节点
                curr.next = prev  # 反转当前节点的指针
                prev = curr  # 移动prev指针
                curr = next_node  # 移动curr指针

            # 连接翻转后的部分
            prev_group_end.next = prev  # 上一组的尾节点指向当前组翻转后的头节点
            next_group_start.next = curr  # 当前组翻转后的尾节点指向下一组的头节点

            # 更新 prev_group_end 为当前组的末尾（即翻转前的起始节点）
            prev_group_end = next_group_start

            length -= k  # 剩余长度减去 k

        return dummy.next  # 返回虚拟头节点的下一个节点（实际头节点）

    def reverseKGroupRecursive(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        """
        递归法：每 k 个节点一组翻转链表
        :param head: 链表头节点
        :param k: 每组翻转的节点数
        :return: 翻转后的链表头节点
        """

        # 翻转 start 到 end 之间的节点（不包括 end）
        def reverseLinkedList(start, end):
            prev = None
            current = start
            while current != end:
                next_node = current.next  # 保存下一个节点
                current.next = prev  # 反转当前节点的指针
                prev = current  # 移动prev指针
                current = next_node  # 移动current指针
            return prev  # 返回翻转后的头节点

        count = 0
        node = head
        # 检查剩余节点是否足够 k 个
        while node and count < k:
            node = node.next
            count += 1

        if count == k:  # 如果剩余节点足够k个
            # 翻转前 k 个节点（从head到node）
            reversed_head = reverseLinkedList(head, node)
            # 递归翻转剩余部分，并接到当前部分后面
            head.next = self.reverseKGroupRecursive(node, k)
            return reversed_head  # 返回当前组翻转后的头节点

        # 不足 k 个节点，直接返回头节点
        return head
