#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   416_Partition_Equal_Subset_Sum.py
@Time    :   2025/04/28 10:15:47
@Author  :   rj 
@Version :   1.0
@Desc    :   分割等和子集
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 计算所有元素的总和
        total_sum = sum(nums)
        
        # 如果总和是奇数，无法平分成两个子集
        if total_sum % 2 != 0:
            return False
        
        # 目标子集和为总和的一半
        target = total_sum // 2
        
        # 创建一个一维动态规划数组
        # dp[i] 表示是否存在子集的和为 i
        dp = [False] * (target + 1)
        dp[0] = True  # 和为0的子集始终存在（空集）
        
        # 遍历数组中的每个数
        for num in nums:
            # 倒序更新dp数组，避免同一个数被多次使用
            for j in range(target, num - 1, -1):
                # 更新当前和 j 是否可以由已有子集加上 num 得到
                dp[j] = dp[j] or dp[j - num]
        
        # 返回是否可以找到和为 target 的子集
        return dp[target]
