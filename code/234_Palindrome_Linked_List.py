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
            return True  # 空链表或单个节点一定是回文

        # Step 1: 使用快慢指针找到链表中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: 反转链表后半部分
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev  # 反转指针
            prev = slow
            slow = next_node

        # Step 3: 比较前半部分和反转后的后半部分
        left, right = head, prev
        while right:  # 只需要比对后半部分长度
            if left.val != right.val:
                return False  # 有不相等的节点，不是回文
            left = left.next
            right = right.next

        return True  # 全部比对成功，是回文
