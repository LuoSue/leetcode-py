#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   169_Majority_Element.py
@Time    :   2025/05/12 22:59:36
@Author  :   rj
@Version :   1.0
@Desc    :   多数元素
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 初始化候选答案和计数器
        ans, count = 0, 0

        # 遍历每个数字
        for num in nums:
            # 如果计数器为0，更新候选答案为当前数字
            if count == 0:
                ans = num
            # 如果当前数字与候选答案相同，计数器加1；否则计数器减1
            count += 1 if ans == num else -1

        # 返回候选答案
        return ans
