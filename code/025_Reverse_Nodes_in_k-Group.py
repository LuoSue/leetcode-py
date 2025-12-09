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

        # 计算链表总长度 n
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # p0 是前一个已反转/处理完的子链表的尾部（或初始的虚拟头节点）
        # dummy 是虚拟头节点，便于处理头节点的改变
        p0 = dummy = ListNode(0, head)
        # pre 用于子链表反转时，作为前一个节点
        pre = None
        # cur 用于子链表反转时，作为当前节点
        cur = head

        # 只要剩余节点数 n 大于等于 k，就进行 k 个一组的反转
        while n >= k:
            n -= k  # 剩余节点数减少 k

            # 1. 反转当前 k 个节点
            # pre_next 用于记录当前子链表反转后的尾部（即反转前的头部），
            # 这样我们在反转结束后，可以用它来连接下一段未反转的链表
            # 在进入 for 循环前，我们知道 nxt 实际上是当前反转段的第一个节点 (p0.next)，
            # 它的 next 指针在反转后会指向下一段未反转的链表头 cur

            for _ in range(k):
                nxt = cur.next  # 记录下一个节点
                cur.next = pre  # 反转指向：当前节点指向前一个节点
                pre = cur  # pre 向前移动到当前节点
                cur = nxt  # cur 向前移动到下一个节点

            # 此时：
            # - pre 是反转后子链表的头部（即反转前的第 k 个节点）
            # - cur 是下一段未反转链表的头部（即反转前的第 k+1 个节点）
            # - p0.next 是反转前子链表的头部（即反转后的尾部）

            # 2. 连接链表
            # nxt 记录当前反转段的尾部（即反转前的头部 p0.next）
            nxt = p0.next

            # 将当前反转段的尾部（反转前的头部）连接到下一段未反转链表的头部 (cur)
            nxt.next = cur

            # 将前一个已处理完的子链表的尾部 (p0) 连接到当前反转段的头部 (pre)
            p0.next = pre

            # 移动 p0 到当前反转段的尾部（即 nxt），准备下一轮反转
            p0 = nxt
            # 重置 pre，为下一轮 k 个节点反转做准备
            pre = None

        # 循环结束后，返回虚拟头节点的下一个节点，即新链表的头节点
        return dummy.next

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
