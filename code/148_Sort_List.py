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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或只有一个节点，直接返回
        if not head or not head.next:
            return head

        # 找到链表中点（使用快慢指针法）
        def getMiddle(node):
            slow = node
            fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # 合并两个有序链表（递归实现）
        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            if left.val < right.val:
                left.next = merge(left.next, right)
                return left
            else:
                right.next = merge(left, right.next)
                return right

        mid = getMiddle(head)  # 找到中点
        nextToMid = mid.next  # 中点后的第一个节点
        mid.next = None  # 将链表从中间断开

        left = self.sortList(head)  # 递归排序左半部分
        right = self.sortList(nextToMid)  # 递归排序右半部分

        return merge(left, right)  # 合并排序后的左右两部分
