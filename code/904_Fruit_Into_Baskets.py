#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   904_Fruit_Into_Baskets.py
@Time    :   2025/04/20 13:44:22
@Author  :   rj 
@Version :   1.0
@Desc    :   水果成篮 - 给定一个整数数组，表示树上从左到右的水果种类，找出可以收集的最多水果数量（只能用两个篮子，每个篮子只能收集一种水果）。
"""

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 窗口左边界
        left = 0
        # 最大水果数
        max_count = 0
        # 用于记录当前窗口中每种水果的数量
        fruits_count = defaultdict(int)
        
        # 枚举窗口右边界
        for right, fruit in enumerate(fruits):
            # 将当前水果加入窗口（更新其计数）
            fruits_count[fruit] += 1
            
            # 如果当前窗口中水果种类超过2种，则移动左边界收缩窗口
            while len(fruits_count) > 2:
                # 左边界的水果数量减少
                fruits_count[fruits[left]] -= 1
                # 如果某种水果的数量为0，从字典中移除
                if fruits_count[fruits[left]] == 0:
                    del fruits_count[fruits[left]]
                # 左边界右移
                left += 1
            
            # 更新最大水果数
            max_count = max(max_count, right - left + 1)
        
        return max_count
