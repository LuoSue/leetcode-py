#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   017_Letter_Combinations_of_a_Phone_Number.py
@Time    :   2025/05/12 09:39:20
@Author  :   rj
@Version :   1.0
@Desc    :   电话号码的字母组合
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 映射表
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        # 回溯函数
        def backtrack(index, current_combination):
            # 如果当前组合的长度等于输入的数字长度，则说明生成了一个有效的组合
            if index == len(digits):
                result.append(current_combination)
                return

            # 当前数字对应的字母
            letters = digit_to_letters[digits[index]]

            # 遍历当前数字对应的每个字母
            for letter in letters:
                # 递归尝试下一个字母
                backtrack(index + 1, current_combination + letter)

        # 从第0个数字开始回溯
        backtrack(0, "")

        return result
