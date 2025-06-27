#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   046_Permutations.py
@Time    :   2025/05/12 09:30:50
@Author  :   rj
@Version :   1.0
@Desc    :   全排列 - 回溯法求所有不含重复数字的全排列
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存储所有排列结果
        used = [False] * len(nums)  # 用于标记元素是否使用过

        # 回溯函数：path 表示当前构建的排列路径
        def backtrack(path: List[int]):
            if len(path) == len(nums):
                res.append(path[:])  # 收集一个完整排列的拷贝
                return

            for i in range(len(nums)):
                if used[i]:
                    continue  # 跳过已经使用的数字

                # 做选择
                used[i] = True
                path.append(nums[i])

                # 递归继续构造下一个数字
                backtrack(path)

                # 撤销选择（回溯）
                path.pop()
                used[i] = False

        backtrack([])  # 从空路径开始回溯
        return res
