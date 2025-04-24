#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1512_Number_of_Good_Pairs.py
@Time    :   2025/04/24 11:30:50
@Author  :   rj 
@Version :   1.0
@Desc    :   好数对的数目
"""

from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        # 创建一个字典用于记录每个数字出现的次数，初始值为0
        count = defaultdict(int)
        
        # 遍历数组中的每个数字
        for num in nums:
            # 当前数字之前已经出现的次数，即为当前数字能组成的“好数对”的数量
            ans += count[num]
            # 更新当前数字出现的次数
            count[num] += 1
        
        # 返回总的“好数对”数量
        return ans
