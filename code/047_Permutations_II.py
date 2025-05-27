#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   047_Permutations_II.py
@Time    :   2025/05/27 23:16:20
@Author  :   rj
@Version :   1.0
@Desc    :   全排列 II
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used, result):
            if len(path) == len(nums):
                result.append(path[:])  # 添加当前排列的副本
                return

            for i in range(len(nums)):
                # 跳过已使用的元素
                if used[i]:
                    continue

                # 剪枝：如果当前元素和前一个元素相同，且前一个没有被使用，跳过，避免重复
                # 跳过同层相同、前一个没用的元素
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # 做选择
                used[i] = True
                path.append(nums[i])

                # 递归
                backtrack(path, used, result)

                # 回溯
                path.pop()
                used[i] = False

        nums.sort()  # 排序是去重的前提
        used = [False] * len(nums)
        result = []

        backtrack([], used, result)
        return result
