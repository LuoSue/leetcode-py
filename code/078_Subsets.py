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
        
        :param nums: 包含不重复元素的整数数组
        :return: 所有可能的子集列表
        """
        # 初始化结果列表和当前路径
        result = []
        path = []
        n = len(nums)

        # 定义回溯函数
        def dfs(i: int):
            """
            深度优先搜索回溯函数
            
            :param i: 当前考虑的元素索引
            """
            # 当遍历完所有元素时，将当前路径加入结果
            if i == n:
                result.append(path[:])  # 使用切片复制当前路径
                return
            
            # 不选择当前元素，直接进入下一个元素
            dfs(i + 1)
            
            # 选择当前元素
            path.append(nums[i])  # 将当前元素加入路径
            dfs(i + 1)            # 进入下一个元素
            path.pop()            # 回溯：移除当前元素，恢复状态

        # 从索引0开始回溯
        dfs(0)

        # 返回所有子集
        return result

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        """
        生成所有可能的子集（幂集）。
        
        :param nums: 包含不重复元素的整数数组
        :return: 所有可能的子集列表
        """
        # 初始化结果列表和当前路径
        result = []
        path = []
        n = len(nums)

        # 定义回溯函数
        def dfs(i: int):
            """
            深度优先搜索回溯函数
            
            :param i: 当前可选择的起始元素索引
            """
            # 将当前路径加入结果（每个节点都代表一个有效子集）
            result.append(path[:])
            
            # 从当前索引开始遍历后续元素
            for j in range(i, n):
                # 选择当前元素
                path.append(nums[j])
                # 递归处理下一个位置，起始索引为j+1（避免重复使用同一元素）
                dfs(j + 1)
                # 回溯：移除当前元素，尝试下一个可能的选择
                path.pop()

        # 从索引0开始回溯
        dfs(0)

        # 返回所有子集
        return result