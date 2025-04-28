#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   152_Maximum_Product_Subarray.py
@Time    :   2025/04/28 10:09:29
@Author  :   rj 
@Version :   1.0
@Desc    :   乘积最大子数组
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:       
        # 最大乘积数组
        max_product = nums[0]
        # 最小乘积数组
        min_product = nums[0]
        # 结果
        result = nums[0]
        
        # 遍历数组，从第二个元素开始更新 max_product 和 min_product
        for i in range(1, len(nums)):
            num = nums[i]
            
            # num < 0 会出现负数结果，交换最大乘积与最小乘积
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            result = max(result, max_product)
        
        return result