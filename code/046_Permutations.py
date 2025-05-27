#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   046_Permutations.py
@Time    :   2025/05/12 09:30:50
@Author  :   rj
@Version :   1.0
@Desc    :   全排列
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯函数，用于递归构造全排列
        def backtrack(nums, path, used, result):
            # 当 path 长度等于 nums 长度时，表示找到一个完整排列
            if len(path) == len(nums):
                result.append(path[:])  # 添加当前排列的副本
                return

            for i in range(len(nums)):
                if used[i]:
                    continue  # 跳过已经使用过的元素

                # 做选择
                used[i] = True
                path.append(nums[i])

                # 递归继续选择下一个元素
                backtrack(nums, path, used, result)

                # 撤销选择（回溯）
                path.pop()
                used[i] = False

        used = [False] * len(nums)  # 标记每个元素是否使用过
        result = []  # 存储最终结果

        backtrack(nums, [], used, result)  # 初始化回溯
        return result
