#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2302_Count_Subarrays_With_Score_Less_Than_K.py
@Time    :   2025/04/16 10:31:11
@Author  :   rj 
@Version :   1.0
@Desc    :   统计得分小于 K 的子数组数目
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        统计所有子数组得分严格小于 k 的子数组数量
        
        子数组得分定义为：子数组的和 × 子数组的长度
        
        使用滑动窗口算法：
        1. 维护一个窗口 [left, right]，保证窗口内所有子数组得分 < k
        2. 当窗口不满足条件时，移动左指针缩小窗口
        3. 对于每个有效窗口，计算以 right 结尾的满足条件的子数组数量
        
        参数:
            nums: 输入数组
            k: 得分阈值
            
        返回:
            满足条件的子数组总数
        """
        left = 0           # 滑动窗口左边界
        count = 0           # 满足条件的子数组计数
        windows_sum = 0     # 当前窗口内元素的和

        # 遍历数组，right为滑动窗口右边界
        for right, x in enumerate(nums):
            windows_sum += x  # 将当前元素加入窗口和

            # 当窗口得分(和×长度) >= k 时，需要缩小窗口
            while windows_sum * (right - left + 1) >= k:
                windows_sum -= nums[left]  # 从和中移除左边界元素
                left += 1                 # 移动左边界

            # 以right结尾的满足条件的子数组数量为窗口长度
            # 因为这些子数组都满足得分 < k 的条件
            count += right - left + 1

        return count