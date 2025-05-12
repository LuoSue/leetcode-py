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
        result = []

        # 回溯函数
        def backtrack(path):
            # 当path的长度等于nums的长度时，说明找到一个完整的排列
            if len(path) == len(nums):
                result.append(path[:])  # 将当前路径复制一份加入结果
                return

            # 遍历所有数字
            for num in nums:
                if num not in path:  # 如果num不在当前路径中，才选择它
                    path.append(num)  # 做选择
                    backtrack(path)  # 递归调用
                    path.pop()  # 撤销选择，回溯

        # 调用回溯函数
        backtrack([])
        return result
