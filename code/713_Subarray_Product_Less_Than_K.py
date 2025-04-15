#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   713_Subarray_Product_Less_Than_K.py
@Time    :   2025/04/15 17:41:03
@Author  :   rj 
@Version :   1.0
@Desc    :   乘积小于 K 的子数组
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 处理边界情况：如果k<=1，由于所有数都是正整数，乘积不可能小于1或更小的k
        if k <= 1:
            return 0
        
        left = 0  # 滑动窗口的左边界
        ans = 0  # 结果计数器
        min_product = 1  # 当前窗口内数字的乘积

        # 使用滑动窗口法，右边界right逐步向右移动
        for right, x in enumerate(nums):
            min_product *= x  # 将当前数字乘入窗口乘积

            # 当乘积超过或等于k时，移动左边界直到乘积小于k
            while min_product >= k:
                min_product /= nums[left]  # 移除左边界的数字
                left += 1  # 左边界右移
            
            # 每次右边界移动后，新增的满足条件的子数组数量为 right - left + 1
            # 这些子数组都是以right结尾的子数组
            ans += right - left + 1
        
        return ans