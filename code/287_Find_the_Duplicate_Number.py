#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   287_Find_the_Duplicate_Number.py
@Time    :   2025/05/12 23:02:29
@Author  :   rj
@Version :   1.0
@Desc    :   寻找重复数
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        使用 Floyd 判圈算法（龟兔赛跑算法）寻找数组中的重复数字。

        思路：
        给定数组 nums 长度为 n+1，元素值在 1 到 n 之间，说明一定存在重复数字。
        我们可以将数组视作一个链表：
        - 数组索引代表链表节点位置。
        - 数组元素值代表链表节点指向的下一个节点位置。

        因为存在重复数字，链表中必定存在环。

        算法步骤：
        1. 使用快慢指针找环：
           - 慢指针每次走一步，快指针每次走两步。
           - 当两指针相遇时，说明进入环内。

        2. 找环入口（重复数字）：
           - 将慢指针重新置于起点。
           - 慢指针和快指针每次走一步，再次相遇的位置即为环入口。

        返回值：
        重复数字，即环入口节点的值。
        """
        # 初始化慢指针和快指针
        slow = nums[0]
        fast = nums[0]

        # 移动慢指针每次一步，快指针每次两步
        while True:
            slow = nums[slow]  # 慢指针走一步
            fast = nums[nums[fast]]  # 快指针走两步
            if slow == fast:  # 如果慢指针和快指针相遇，表示进入了环形
                break

        # 找到环的起点（重复的数字）
        slow = nums[0]  # 将慢指针重新置为起点
        while slow != fast:
            slow = nums[slow]  # 慢指针一步一步走
            fast = nums[fast]  # 快指针一步一步走

        return slow  # 当慢指针和快指针相遇时，即为重复的数字
