#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   994_Rotting_Oranges.py
@Time    :   2025/05/11 15:24:45
@Author  :   rj
@Version :   1.0
@Desc    :   腐烂的橘子 - 多源 BFS 解法
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])  # 获取网格行列数
        queue = deque()  # 队列用于 BFS 扩散腐烂橘子
        fresh_count = 0  # 新鲜橘子的计数器

        # Step 1: 初始化 - 统计新鲜橘子数量，并记录所有腐烂橘子的坐标
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  # 腐烂橘子入队，作为 BFS 的多个起点
                elif grid[r][c] == 1:
                    fresh_count += 1  # 统计新鲜橘子数量

        # 如果没有新鲜橘子，直接返回 0 分钟
        if fresh_count == 0:
            return 0

        minutes = 0  # 记录腐烂过程所需分钟数
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 四个方向：上、下、左、右

        # Step 2: BFS 扩散过程，每轮代表 1 分钟
        while queue and fresh_count:
            minutes += 1  # 进入新的一分钟
            for _ in range(len(queue)):  # 处理当前分钟所有腐烂橘子
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  # 邻居坐标
                    # 如果邻居是新鲜橘子，则腐烂它
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # 标记为腐烂
                        fresh_count -= 1  # 新鲜橘子数 -1
                        queue.append((nr, nc))  # 加入下一轮腐烂队列

        # Step 3: 若还有新鲜橘子未腐烂，返回 -1；否则返回分钟数
        return minutes if fresh_count == 0 else -1
