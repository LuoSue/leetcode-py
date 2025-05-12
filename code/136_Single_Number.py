#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   136_Single_Number.py
@Time    :   2025/05/12 22:57:48
@Author  :   rj 
@Version :   1.0
@Desc    :   只出现一次的数字
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 初始化结果为0
        res = 0
        
        # 对每个数字进行异或操作
        for n in nums:
            res ^= n  # 如果一个数字出现两次，异或结果会归零，最终剩下的就是只出现一次的数字
        
        # 返回最终结果
        return res
