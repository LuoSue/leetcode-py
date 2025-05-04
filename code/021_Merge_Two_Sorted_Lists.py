#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   021_Merge_Two_Sorted_Lists.py
@Time    :   2025/05/04 11:57:36
@Author  :   rj
@Version :   1.0
@Desc    :   合并两个有序链表
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点的值
        self.next = next  # 指向下一个节点的指针

class Solution:
    def mergeTwoLists_iterative(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        方法一：迭代法
        使用虚拟头节点，逐一比较两个链表当前节点的值，把较小的接到新链表上。
        """
        cur = dum = ListNode(0)  # 虚拟头节点，cur 用于构造新链表

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2  # 将 list2 当前节点接到 cur 后
                list2 = list2.next  # list2 前进一步
            else:
                cur.next = list1  # 将 list1 当前节点接到 cur 后
                list1 = list1.next  # list1 前进一步
            cur = cur.next  # cur 前进一步

        # 处理剩余节点（其中一个链表已经为空）
        cur.next = list1 if list1 else list2

        # 返回合并后的链表（跳过虚拟头节点）
        return dum.next

    def mergeTwoLists_recursive(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        方法二：递归法
        每次比较两个链表当前节点的值，递归决定下一步怎么接。
        """
        if list1 is None:
            return list2  # list1 为空，直接返回 list2
        if list2 is None:
            return list1  # list2 为空，直接返回 list1

        if list1.val < list2.val:
            # list1 当前值小，递归合并 list1.next 和 list2
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            # list2 当前值小，递归合并 list1 和 list2.next
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2

