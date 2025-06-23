#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   131_Palindrome_Partitioning.py
@Time    :   2025/05/12 09:45:54
@Author  :   rj
@Version :   1.0
@Desc    :   分割回文串
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub_str: str):
            return sub_str == sub_str[::-1]

        def backtrack(start: int, path: list):
            if start == len(s):  # 如果到达字符串的末尾，说明找到了一种分割方案
                result.append(path[:])  # 复制当前路径，添加到结果中
                return

            for end in range(start, len(s)):
                substr = s[start : end + 1]  # 获取当前的子串
                if is_palindrome(substr):
                    path.append(substr)  # 如果是回文串，将其加入当前路径
                    backtrack(end + 1, path)  # 递归处理剩余的字符串
                    path.pop()  # 回溯，撤销上一步的选择

        backtrack(0, [])
        return result
