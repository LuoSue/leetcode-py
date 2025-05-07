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


# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点值
        self.next = next  # 下一个节点指针


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或只有一个节点，直接返回
        if not head or not head.next:
            return head

        # 找到链表中点（使用快慢指针法）
        def getMiddle(node):
            slow = node  # 慢指针
            fast = node  # 快指针
            # 当 fast 和 fast.next 都存在时继续遍历
            while fast.next and fast.next.next:
                slow = slow.next  # 慢指针走一步
                fast = fast.next.next  # 快指针走两步
            return slow  # 返回中点节点

        # 合并两个有序链表（递归实现）
        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            # 比较左右链表当前节点值，较小的接到结果链表上
            if left.val < right.val:
                left.next = merge(left.next, right)
                return left
            else:
                right.next = merge(left, right.next)
                return right

        mid = getMiddle(head)  # 找到链表中点
        nextToMid = mid.next  # 中点后的第一个节点
        mid.next = None  # 将链表从中间断开

        # 递归排序左半部分
        left = self.sortList(head)
        # 递归排序右半部分
        right = self.sortList(nextToMid)

        # 合并排序后的左右两部分
        return merge(left, right)
