#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   160_Intersection_of_Two_Linked_Lists.py
@Time    :   2025/04/30 17:50:53
@Author  :   rj
@Version :   1.0
@Desc    :   相交链表
"""

from typing import Optional


# 定义链表节点
class ListNode:
    def __init__(self, x):
        self.val = x  # 节点值
        self.next = None  # 下一个节点指针


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # 初始化两个指针，分别指向链表A和链表B的头部
        p_a, p_b = headA, headB

        # 当两个指针相遇时，说明找到了交点；否则继续遍历
        while p_a != p_b:
            # 如果p_a指向链表A的节点，则继续向下一个节点移动
            if p_a:
                p_a = p_a.next
            # 否则将p_a指向链表B的头部
            else:
                p_a = headB

            # 如果p_b指向链表B的节点，则继续向下一个节点移动
            if p_b:
                p_b = p_b.next
            # 否则将p_b指向链表A的头部
            else:
                p_b = headA

        # 返回相交节点，如果没有交点则返回None
        return p_a
