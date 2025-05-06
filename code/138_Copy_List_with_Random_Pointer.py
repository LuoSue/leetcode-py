#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   138_Copy_List_with_Random_Pointer.py
@Time    :   2025/05/06 10:47:39
@Author  :   rj
@Version :   1.0
@Desc    :   随机链表的复制
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # 1. 在原链表中插入复制节点
        cur = head
        while cur:
            new_node = Node(cur.val)  # 创建新节点
            new_node.next = cur.next  # 新节点指向当前节点的下一个节点
            cur.next = new_node  # 当前节点指向新节点
            cur = new_node.next  # 移动到下一个原节点

        # 2. 复制 random 指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = (
                    cur.random.next
                )  # 新节点的 random 指向原 random 节点的下一个（即对应的新节点）
            cur = cur.next.next  # 移动到下一个原节点

        # 3. 拆分链表，将复制链表从原链表中分离出来
        dummy = Node(0)
        copy_cur = dummy
        cur = head
        while cur:
            copy_cur.next = cur.next  # 提取复制节点
            copy_cur = copy_cur.next  # 移动到下一个复制节点
            cur.next = cur.next.next  # 恢复原链表的 next 指针
            cur = cur.next  # 移动到下一个原节点

        return dummy.next
