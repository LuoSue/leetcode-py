#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1004_Max_Consecutive_Ones_III.py
@Time    :   2025/04/16 10:00:51
@Author  :   rj 
@Version :   1.0
@Desc    :   最大连续1的个数 III
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        找到包含最多k个0的最长连续1子数组的长度
        
        使用滑动窗口算法：
        1. 维护一个窗口[left, right]，窗口内最多包含k个0
        2. 当0的个数超过k时，移动左指针缩小窗口
        3. 始终记录满足条件的最大窗口大小
        
        参数:
            nums: 二进制数组，包含0和1
            k: 允许包含的最大0的个数
            
        返回:
            满足条件的最大子数组长度
        """
        left = 0           # 滑动窗口的左边界
        count = 0          # 记录当前窗口中0的个数
        max_len = 0       # 记录满足条件的最大窗口长度

        # 遍历数组，right表示滑动窗口的右边界
        for right in range(len(nums)):
            # 如果当前数字是0，增加计数
            if nums[right] != 1:
                count += 1
            
            # 当窗口中0的个数超过k时，需要移动左边界
            while count > k:
                # 如果左边界的数字是0，减少计数
                if nums[left] != 1:
                    count -= 1
                left += 1  # 移动左边界

            # 更新最大窗口长度（当前窗口大小是right - left + 1）
            max_len = max(max_len, right - left + 1)

        return max_len