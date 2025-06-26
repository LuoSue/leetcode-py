#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   148_Sort_List_Combined.py
@Time    :   2025/06/26
@Author  :   rj
@Version :   2.0
@Desc    :   链表排序：递归版和迭代版（常数空间）合并实现
"""

from typing import Optional


# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # ========================== 递归版归并排序 ==========================

    def sortListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 拆分链表
        left, right = self.splitList(head)

        # 分别排序
        left_sorted = self.sortListRecursive(left)
        right_sorted = self.sortListRecursive(right)

        # 合并两个已排序的链表
        return self.merge(left_sorted, right_sorted)

    def splitList(self, head: ListNode) -> tuple[ListNode, ListNode]:
        # 快慢指针找到中点
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 断开链表
        mid = slow
        if prev:
            prev.next = None

        return head, mid

    # ========================== 迭代版归并排序（O(1) 空间） ==========================

    def sortListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 计算链表长度
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        size = 1

        # 子链表从 size=1 开始翻倍合并
        while size < length:
            prev, curr = dummy, dummy.next

            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)

                merged_head, merged_tail = self.merge(left, right)
                prev.next = merged_head
                prev = merged_tail

            size <<= 1  # size *= 2

        return dummy.next

    def split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        """
        从 head 开始切 size 个节点，返回剩余部分的头节点
        """
        for i in range(size - 1):
            if head and head.next:
                head = head.next
            else:
                break

        rest = head.next if head else None
        if head:
            head.next = None
        return rest

    # ========================== 公共合并方法 ==========================

    def merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
        """
        合并两个有序链表，返回合并后链表的头尾节点
        """
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        # 移动 tail 到末尾
        while tail.next:
            tail = tail.next

        return dummy.next, tail
