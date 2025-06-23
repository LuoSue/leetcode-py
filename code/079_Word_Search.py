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
        rows, cols = len(board), len(board[0])

        # 1. 剪枝：统计 board 上每个字符的出现频率
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        for c in word_count:
            # 如果某个字符在 word 中出现次数 > board 中的次数，提前返回 False
            if word_count[c] > board_count.get(c, 0):
                return False

        # 2. 搜索优化：从 word 中较不常见的字符开始搜索，提升剪枝效率
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]  # 反转单词，提高搜索效率

        # 3. 定义 DFS 搜索函数
        def dfs(i, j, k):
            # 当前格子字符与 word[k] 不匹配，剪枝
            if board[i][j] != word[k]:
                return False
            # 所有字符已匹配，成功
            if k == len(word) - 1:
                return True

            # 暂存当前字符并标记为已访问
            tmp = board[i][j]
            board[i][j] = "#"  # 使用特殊标记防止重复访问

            # 四个方向搜索：上、下、左、右
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                # 如果新位置合法且未被访问
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] != "#":
                    if dfs(ni, nj, k + 1):
                        return True  # 匹配成功

            # 回溯：还原当前格子的值
            board[i][j] = tmp
            return False  # 当前路径匹配失败

        # 4. 遍历整个网格寻找起点
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # 起始字符匹配
                    if dfs(i, j, 0):  # 开始 DFS 搜索
                        return True

        return False  # 所有路径都没匹配成功
