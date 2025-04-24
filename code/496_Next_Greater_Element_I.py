#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   496_Next_Greater_Element_I.py
@Time    :   2025/04/24 14:04:58
@Author  :   rj
@Version :   1.0
@Desc    :   下一个更大元素 I
"""

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 创建一个字典，用于记录 nums2 中每个元素的下一个更大元素
        next_gt = {}
        # 单调栈，存储 nums2 中元素的索引，栈顶元素对应的值是当前遍历中最小的可能是“下一个更大元素”的候选者
        stack = []
        n = len(nums2)

        # 从 nums2 的末尾向前遍历
        for i in range(n - 1, -1, -1):
            # 当栈非空，且栈顶元素小于当前元素时，弹出栈顶元素
            # 因为它不可能是当前元素的“下一个更大元素”
            while stack and nums2[stack[-1]] < nums2[i]:
                stack.pop()
            # 如果栈非空，栈顶元素就是当前元素的“下一个更大元素”
            if stack:
                next_gt[nums2[i]] = nums2[stack[-1]]
            else:
                # 否则，没有比当前元素更大的元素，记录为 -1
                next_gt[nums2[i]] = -1
            # 当前元素入栈
            stack.append(i)

        # 对于 nums1 中的每一个元素，查找其在 nums2 中的“下一个更大元素”
        return [next_gt[num] for num in nums1]
