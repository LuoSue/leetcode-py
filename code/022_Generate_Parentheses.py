#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   022_Generate_Parentheses.py
@Time    :   2025/05/12 09:41:54
@Author  :   rj
@Version :   1.0
@Desc    :   括号生成
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s, left, right):
            # 终止条件：当左括号和右括号都等于n时，说明已经生成了一个有效组合
            if left == n and right == n:
                result.append(s)
                return

            # 如果左括号数量小于n，可以添加一个左括号
            if left < n:
                backtrack(s + "(", left + 1, right)

            # 如果右括号数量小于左括号，可以添加一个右括号
            if right < left:
                backtrack(s + ")", left, right + 1)

        # 从空字符串开始回溯
        backtrack("", 0, 0)
        return result
