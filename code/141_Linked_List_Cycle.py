#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   141_Linked_List_Cycle.py
@Time    :   2025/05/04 11:43:36
@Author  :   rj 
@Version :   1.0
@Desc    :   环形链表
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x  # 节点的值
        self.next = None  # 指向下一个节点的指针

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        判断链表中是否有环。
        使用快慢指针（Floyd 判圈法），如果存在环，快慢指针最终会相遇。
        :param head: 链表头节点
        :return: 如果链表中有环，返回 True；否则返回 False
        """
        slow = fast = head  # 初始化快慢指针，均指向链表头

        while fast and fast.next:  # 只要快指针和快指针的下一个节点不为空，就继续循环
            slow = slow.next          # 慢指针走一步
            fast = fast.next.next     # 快指针走两步

            if slow == fast:
                # 快慢指针相遇，说明链表中存在环
                return True
        
        # 快指针走到链表末尾，说明不存在环
        return False
