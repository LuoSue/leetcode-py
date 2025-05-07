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
    def copy_list_with_random_pointers(
        self, head: "Optional[Node]"
    ) -> "Optional[Node]":
        """
        方法一：在原链表中插入复制节点，再分离出新链表
        """
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
                )  # 新节点的 random 指向原 random 节点的下一个（即新节点）
            cur = cur.next.next  # 移动到下一个原节点

        # 3. 拆分链表，将复制链表从原链表中分离出来
        dummy = Node(0)  # 哨兵节点，方便操作
        copy_cur = dummy
        cur = head
        while cur:
            copy_cur.next = cur.next  # 提取复制节点
            copy_cur = copy_cur.next  # 移动到下一个复制节点
            cur.next = cur.next.next  # 恢复原链表的 next 指针
            cur = cur.next  # 移动到下一个原节点

        return dummy.next

    def copy_list_with_hashmap(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        方法二：使用哈希表记录原节点和复制节点的对应关系
        """
        if not head:
            return None

        # 创建哈希表，存储原节点到新节点的映射
        old_to_new = {}

        # 第一步：复制节点并填充哈希表
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)  # 复制节点
            cur = cur.next

        # 第二步：设置 next 和 random 指针
        cur = head
        while cur:
            if cur.next:
                old_to_new[cur].next = old_to_new[cur.next]
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]
