#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   001_Two_Sum.py
@Time    :   2025/04/14 22:20:02
@Author  :   rj
@Version :   1.0
@Desc    :   两数之和 - 给定一个整数数组 nums 和一个整数目标值 target，
             请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
"""

from typing import List


class Solution:
    """
    使用哈希表来优化查找效率的解决方案

    基本思路：
    1. 我们需要找到两个数 a 和 b，使得 a + b = target
    2. 对于每一个当前数字 b = nums[i]，我们需要检查是否存在 a = target - b 在之前已经出现过
    3. 使用哈希表来存储已经遍历过的数字及其索引，可以实现O(1)时间的查找
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个空哈希表来存储值到索引的映射
        # key: 数组中的数字
        # value: 该数字对应的索引
        hash_table = {}

        # 遍历数组，i是索引，num是当前数字
        for i, num in enumerate(nums):
            # 计算当前数字所需的补数（即target - num）
            complement = target - num

            # 检查补数是否已经在哈希表中
            if complement in hash_table:
                # 如果存在，返回当前索引和补数的索引
                return [i, hash_table[complement]]

            # 如果补数不存在，将当前数字及其索引存入哈希表
            hash_table[num] = i

        # 理论上根据题目描述总会有一个解，所以这里不需要return
        # 但为了代码完整性，可以返回空列表或抛出异常
        return []
