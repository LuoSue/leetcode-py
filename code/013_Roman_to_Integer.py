#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   013_Roman_to_Integer.py
@Time    :   2025/07/09 14:13:54
@Author  :   rj
@Version :   1.0
@Desc    :   罗马数字转整数
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # 定义罗马数字与整数的映射表
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0  # 存放最终的整数值
        prev_value = 0  # 记录上一个字符对应的整数值，用于判断加减关系

        # 从右向左遍历字符串（便于处理减法情况）
        for ch in reversed(s):
            current = roman_map[ch]  # 当前字符对应的整数值

            # 如果当前值小于上一个值，说明是减法组合（如 IV、IX 等）
            if current < prev_value:
                total -= current
            else:
                # 否则为正常加法
                total += current

            # 更新上一个值为当前值
            prev_value = current

        return total
