#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   200_Number_of_Islands.py
@Time    :   2025/05/11 15:19:00
@Author  :   rj
@Version :   1.0
@Desc    :   岛屿数量
"""

from typing import List


class Solution:
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            queue = [(i, j)]
            # 将当前陆地标记为已访问（即变为 '0'）
            grid[i][j] = "0"
            # 方向数组，表示上下左右四个方向
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            # 开始广度优先搜索
            while queue:
                x, y = queue.pop()
                # 遍历四个方向
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # 检查是否越界以及是否为陆地
                    if (
                        0 <= nx < len(grid)
                        and 0 <= ny < len(grid[0])
                        and grid[nx][ny] == "1"
                    ):
                        grid[nx][ny] = "0"  # 标记为已访问
                        queue.append((nx, ny))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # 遇到陆地
                    count += 1  # 岛屿数量加 1
                    bfs(i, j)  # 广度优先搜索，标记相连的所有陆地为水

        return count

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        if not grid:  # 如果输入为空，直接返回 0
            return 0

        def dfs(i, j):
            # 如果索引越界或遇到水（'0'），则返回
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] == "0"
            ):
                return
            # 将当前陆地（'1'）标记为已访问（改为 '0'，避免重复访问）
            grid[i][j] = "0"
            # 向上下左右四个方向继续深度优先搜索
            dfs(i + 1, j)  # 下
            dfs(i - 1, j)  # 上
            dfs(i, j + 1)  # 右
            dfs(i, j - 1)  # 左

        count = 0  # 记录岛屿数量的计数器
        # 遍历整个网格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果遇到陆地（'1'）
                if grid[i][j] == "1":
                    count += 1  # 岛屿数量加 1
                    dfs(i, j)  # 使用 DFS 搜索整座岛屿，将其所有陆地标记为水（'0'）

        return count  # 返回岛屿的数量
