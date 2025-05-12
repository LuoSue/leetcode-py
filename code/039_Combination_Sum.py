#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   039_Combination_Sum.py
@Time    :   2025/05/12 09:40:20
@Author  :   rj 
@Version :   1.0
@Desc    :   组合总和
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # 回溯函数
        def backtrack(start, target, current_combination):
            if target == 0:  # 目标达成
                result.append(current_combination[:])  # 保存当前的组合
                return
            if target < 0:  # 超过目标值，剪枝
                return
            
            # 遍历候选数，进行递归
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])  # 选择当前元素
                # 由于可以重复选择同一元素，递归时仍然从当前位置 i 开始
                backtrack(i, target - candidates[i], current_combination)
                current_combination.pop()  # 回溯，撤销选择
        
        # 从第一个元素开始，目标为target，当前组合为空
        backtrack(0, target, [])
        
        return result