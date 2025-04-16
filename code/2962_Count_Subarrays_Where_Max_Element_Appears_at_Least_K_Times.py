#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2962_Count_Subarrays_Where_Max_Element_Appears_at_Least_K_Times.py
@Time    :   2025/04/16 10:09:37
@Author  :   rj 
@Version :   1.0
@Desc    :   统计最大元素出现至少 K 次的子数组
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 找到数组中的最大值
        max_val = max(nums)
        n = len(nums)
        count = 0  # 记录满足条件的子数组数量
        left = 0  # 左指针初始化
        max_count = 0  # 当前窗口中 max_val 出现的次数

        # 枚举每个子数组的右端点
        for right in range(n):
            # 如果当前元素是最大值，则增加出现次数
            if nums[right] == max_val:
                max_count += 1
            
            # 当 max_val 出现次数达到 k 时，更新结果
            while max_count >= k:
                # 从当前 left 到 right 的所有子数组都满足条件
                # 因为我们固定了左边界 left，右边界可以从 right 扩展到数组末尾
                count += n - right
                
                # 移动左指针，缩小窗口，更新 max_count
                if nums[left] == max_val:
                    max_count -= 1
                left += 1

        # 返回满足条件的子数组数量
        return count