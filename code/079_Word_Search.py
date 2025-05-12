#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   079_Word_Search.py
@Time    :   2025/05/12 09:43:37
@Author  :   rj
@Version :   1.0
@Desc    :   单词搜索
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        m, n = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False

            # 记录当前字符的位置，避免重复使用
            temp = board[x][y]
            board[x][y] = "#"  # 进行标记

            # 向四个方向搜索
            found = (
                dfs(x + 1, y, index + 1)
                or dfs(x - 1, y, index + 1)
                or dfs(x, y + 1, index + 1)
                or dfs(x, y - 1, index + 1)
            )

            # 恢复原来的字符
            board[x][y] = temp

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
