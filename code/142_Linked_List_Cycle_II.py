#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   142_Linked_List_Cycle_II.py
@Time    :   2025/05/04 11:51:04
@Author  :   rj
@Version :   1.0
@Desc    :   环形链表 II
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x  # 节点的值
        self.next = None  # 指向下一个节点的指针

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        检测链表是否有环，并返回环的入口节点。
        使用快慢指针法（Floyd 判圈法）：
        1. 第一次相遇后，一个指针从头开始，一个指针留在相遇点。
        2. 两个指针以相同速度前进，再次相遇的地方即为环的入口。
        
        :param head: 链表头节点
        :return: 如果有环，返回环入口节点；否则返回 None
        """
        slow = fast = head  # 初始化快慢指针

        # 第一步：判断是否有环（快慢指针相遇）
        while fast and fast.next:
            slow = slow.next          # 慢指针走一步
            fast = fast.next.next     # 快指针走两步

            if slow == fast:
                # 有环，准备寻找入口
                temp = head

                # 第二步：寻找环的入口节点
                while temp != fast:
                    temp = temp.next
                    fast = fast.next
                return temp  # 返回环入口节点

        # 无环，返回 None
        return None

