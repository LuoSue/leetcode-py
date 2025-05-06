#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   002_Add_Two_Numbers.py
@Time    :   2025/05/06 10:26:32
@Author  :   rj
@Version :   1.0
@Desc    :   两数相加
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点的值
        self.next = next  # 指向下一个节点的指针


class Solution:
    def addTwoNumbersIterative(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        迭代法：将两个链表表示的数字相加，返回结果链表
        """
        dummy = ListNode()  # 哨兵节点，用于简化操作
        current = dummy  # 当前指针
        carry = 0  # 进位

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # 取 l1 当前节点值，如果为空则取 0
            val2 = l2.val if l2 else 0  # 取 l2 当前节点值，如果为空则取 0

            total_sum = val1 + val2 + carry  # 当前位总和
            carry = total_sum // 10  # 更新进位
            current.next = ListNode(total_sum % 10)  # 创建新节点存放当前位

            current = current.next  # 移动到下一个节点
            if l1:
                l1 = l1.next  # l1 前进
            if l2:
                l2 = l2.next  # l2 前进

        return dummy.next  # 返回去掉哨兵节点后的链表

    def addTwoNumbersRecursive(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0
    ) -> Optional[ListNode]:
        """
        递归法：将两个链表表示的数字相加，返回结果链表
        """
        if l1 is None and l2 is None:
            return (
                ListNode(carry) if carry else None
            )  # 递归结束，如果有进位则创建新节点

        if l1 is None:
            l1, l2 = l2, l1  # 确保 l1 非空，简化后续处理

        carry += l1.val + (l2.val if l2 else 0)  # 当前位和进位相加
        l1.val = carry % 10  # 更新 l1 当前节点值为当前位数字
        l1.next = self.addTwoNumbersRecursive(
            l1.next, l2.next if l2 else None, carry // 10
        )  # 递归处理下一位
        return l1  # 返回当前链表节点
