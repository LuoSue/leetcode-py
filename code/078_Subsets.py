#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   078_Subsets.py
@Time    :   2025/05/12 09:34:40
@Author  :   rj
@Version :   1.0
@Desc    :   子集
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        生成所有可能的子集（幂集）。
        :param nums: 一个包含唯一元素的整数数组
        :return: 所有可能的子集列表
        """
        # 定义结果列表
        results = []

        # 定义回溯函数
        def backtrack(start, path):
            # 将当前路径添加到结果中
            results.append(path[:])
            # 遍历数组中的每个元素
            for i in range(start, len(nums)):
                # 选择当前元素，并递归调用回溯函数，探索下一个元素
                path.append(nums[i])
                backtrack(i + 1, path)
                # 撤销选择，即回溯
                path.pop()

        # 从索引0开始回溯
        backtrack(0, [])

        # 返回所有子集
        return results
