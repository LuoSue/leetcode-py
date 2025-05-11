#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   994_Rotting_Oranges.py
@Time    :   2025/05/11 15:24:45
@Author  :   rj
@Version :   1.0
@Desc    :   腐烂的橘子
"""

from collections import deque
from typing import List


# 定义解决方案类
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # 获取网格的行数和列数
        queue = deque()  # 用于存储腐烂橘子的位置
        fresh = 0  # 新鲜橘子的数量
        time = 0  # 腐烂所需的时间

        # 初始化队列和新鲜橘子计数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:  # 如果是腐烂橘子
                    queue.append((i, j))  # 将腐烂橘子的坐标加入队列
                elif grid[i][j] == 1:  # 如果是新鲜橘子
                    fresh += 1  # 新鲜橘子计数加1

        # 如果没有新鲜橘子，直接返回0（即没有腐烂的过程）
        if fresh == 0:
            return 0

        # 四个方向：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 开始腐烂过程，直到所有新鲜橘子腐烂或队列为空
        while queue and fresh > 0:
            # 处理当前层的所有腐烂橘子
            for _ in range(len(queue)):
                x, y = queue.popleft()  # 弹出队列中的腐烂橘子坐标
                for dx, dy in directions:  # 遍历四个方向
                    nx, ny = x + dx, y + dy  # 计算新坐标
                    # 检查新坐标是否在网格内，并且是新鲜橘子
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # 将新鲜橘子腐烂
                        queue.append((nx, ny))  # 将新腐烂的橘子加入队列
                        fresh -= 1  # 新鲜橘子数量减1
            time += 1  # 腐烂过程结束，时间增加1

        # 如果所有新鲜橘子都腐烂了，返回腐烂的时间
        # 否则，返回-1，表示有新鲜橘子永远无法腐烂
        return time if fresh == 0 else -1
