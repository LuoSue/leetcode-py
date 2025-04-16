#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2300_Successful_Pairs_of_Spells_and_Potions.py
@Time    :   2025/04/16 14:11:47
@Author  :   rj 
@Version :   1.0
@Desc    :   咒语和药水的成功对数
"""

import bisect
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Step 1: 对药水数组进行排序
        potions.sort()
        
        # Step 2: 定义一个函数计算每个咒语成功组合的药水数目
        result = []
        for spell in spells:
            # 使用整数除法来计算所需的最小药水强度
            required = (success + spell - 1) // spell
            
            # 使用二分查找找到第一个满足 potion >= required 的位置
            idx = bisect.bisect_left(potions, required)
            
            # 计算成功组合的药水数量
            result.append(len(potions) - idx)
        
        return result