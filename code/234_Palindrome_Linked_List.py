#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   234_Palindrome_Linked_List.py
@Time    :   2025/05/04 11:40:18
@Author  :   rj
@Version :   1.0
@Desc    :   回文链表
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: 使用快慢指针找到中间节点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: 反转链表后半部分
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: 比较前半部分和反转后的后半部分
        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
