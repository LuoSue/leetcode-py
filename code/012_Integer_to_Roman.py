#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   012_Integer_to_Roman.py
@Time    :   2025/07/09 14:23:21
@Author  :   rj
@Version :   1.0
@Desc    :   整数转罗马数字
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        # 定义一个从大到小排列的数字与对应罗马数字的映射
        val_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        res = ""

        # 遍历所有的数字-罗马字符对
        for value, symbol in val_map:
            # 如果当前数字小于等于num，则不断使用它
            while num >= value:
                res += symbol  # 添加对应的罗马字符
                num -= value  # 减去对应的值

        return res
