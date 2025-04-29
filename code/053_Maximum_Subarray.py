#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   053_Maximum_Subarray.py
@Time    :   2025/04/29 11:47:28
@Author  :   rj 
@Version :   1.0
@Desc    :   最大子数组和 (Maximum Subarray Problem)
"""

from typing import List  # 导入List类型，用于指定输入列表的类型

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 如果输入列表为空，返回0
        if not nums:
            return 0
        
        # 初始化当前最大值current_max和最终最大值final_max为数组的第一个元素
        current_max = final_max = nums[0]

        # 从第二个元素开始遍历数组
        for i in range(1, len(nums)):
            # 更新当前子数组的最大和，要么选择从当前元素开始一个新子数组，要么选择继续扩展当前子数组
            current_max = max(nums[i], current_max + nums[i])
            
            # 如果当前的子数组和大于最终最大值，更新最终最大值
            final_max = max(final_max, current_max)

        # 返回找到的最大子数组和
        return final_max
