#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   744_Find_Smallest_Letter_Greater_Than_Target.py
@Time    :   2025/04/22 17:35:27
@Author  :   rj 
@Version :   1.0
@Desc    :   寻找比目标字母大的最小字母
"""

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 二分查找初始化左右指针
        left, right = 0, len(letters)
        # 默认返回第一个字母（当 target 大于等于所有字母时，需要环绕回来）
        res = letters[0]

        while left < right:
            # 计算中间位置
            mid = left + (right - left) // 2

            # 如果中间字母大于目标字母，说明可能是答案，继续在左侧查找
            if letters[mid] > target:
                res = letters[mid]  # 更新当前结果
                right = mid         # 缩小右边界
            else:
                # 如果中间字母小于等于目标字母，继续在右侧查找
                left = mid + 1
        
        # 返回找到的结果（若没找到合适的，返回初始值 letters[0]）
        return res
