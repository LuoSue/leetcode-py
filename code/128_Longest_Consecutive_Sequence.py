#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   128_Longest_Consecutive_Sequence.py
@Time    :   2025/04/14 22:48:21
@Author  :   rj
@Version :   1.0
@Desc    :   最长连续序列 - 给定一个未排序的整数数组 nums，
             找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
             要求算法的时间复杂度为 O(n)。
"""

from typing import List


class Solution:
    """
    使用哈希集合实现O(n)时间复杂度的解决方案

    基本思路：
    1. 首先将所有数字存入一个集合，实现O(1)时间的查找
    2. 对于集合中的每个数字，检查它是否是一个连续序列的起点
    3. 如果是起点，则向后查找连续的数字，计算序列长度
    4. 在整个过程中维护遇到的最大序列长度
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        # 将输入列表转换为集合，去除重复元素并实现O(1)查找
        nums_set = set(nums)
        # 初始化最大长度为0
        max_len = 0

        # 遍历集合中的每个数字
        for num in nums_set:
            # 只有当当前数字是一个序列的起点时才进行处理
            # (即num-1不在集合中，说明这是一个新序列的起点)
            if num - 1 not in nums_set:
                cur_num = num  # 当前检查的数字
                cur_len = 1  # 当前序列长度

                # 向后查找连续的数字
                while cur_num + 1 in nums_set:
                    cur_len += 1  # 长度加1
                    cur_num += 1  # 检查下一个数字

                # 更新最大长度
                max_len = max(cur_len, max_len)

        # 返回找到的最大连续序列长度
        return max_len
