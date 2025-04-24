#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   503_Next_Greater_Element_II.py
@Time    :   2025/04/24 14:10:30
@Author  :   rj
@Version :   1.0
@Desc    :   下一个更大元素 II
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 初始化结果数组，默认为 -1，表示没有下一个更大元素
        ans = [-1] * n
        # 使用栈保存“可能还没找到下一个更大元素”的元素下标
        stack = []

        # 遍历两倍长度的数组，模拟环形数组（循环一次等于遍历两次数组）
        for i in range(2 * n):
            # nums[i % n] 用来模拟环形访问
            while stack and nums[stack[-1]] < nums[i % n]:
                # 如果当前元素比栈顶元素大，那么当前元素是栈顶元素的“下一个更大元素”
                current = stack.pop()
                ans[current] = nums[i % n]
            # 只有前 n 个索引才入栈，避免重复处理
            if i < n:
                stack.append(i)

        return ans

