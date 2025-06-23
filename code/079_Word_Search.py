#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   079_Word_Search_Optimized.py
@Time    :   2025/05/12 09:43:37
@Author  :   rj
@Version :   1.1
@Desc    :   单词搜索 - 优化版
"""

from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        # 提前剪枝：如果 word 中的某个字符比 board 中的数量还多，直接返回 False
        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)
        for c in word_counter:
            if word_counter[c] > board_counter.get(c, 0):
                return False

        # 方向数组：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x: int, y: int, index: int) -> bool:
            # 所有字符都匹配，返回 True
            if index == len(word):
                return True
            # 越界或不匹配，返回 False
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False

            temp = board[x][y]
            board[x][y] = "#"  # 标记已访问

            for dx, dy in directions:
                if dfs(x + dx, y + dy, index + 1):
                    board[x][y] = temp  # 提前恢复，减少回溯路径
                    return True

            board[x][y] = temp  # 恢复现场
            return False

        # 遍历所有起点
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
