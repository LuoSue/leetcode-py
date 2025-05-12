#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   051_N-Queens.py
@Time    :   2025/05/12 09:48:06
@Author  :   rj 
@Version :   1.0
@Desc    :   N 皇后
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 回溯函数，参数依次为：当前处理的行、已占用的列、主对角线、副对角线、当前棋盘状态
        def backtrack(row, cols, diag1, diag2, current_solution):
            # 如果所有行都放置了皇后，说明找到一个可行解
            if row == n:
                # 将当前棋盘状态加入结果集（每行转为字符串）
                result.append([''.join(row) for row in current_solution])
                return
            
            # 遍历当前行的每一列，尝试放置皇后
            for col in range(n):
                # 检查当前位置是否在已占用的列、主对角线、副对角线上
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # 冲突，跳过
                
                # 做出选择：放置皇后
                cols.add(col)                  # 标记列已被占用
                diag1.add(row - col)          # 标记主对角线已被占用
                diag2.add(row + col)          # 标记副对角线已被占用
                current_solution[row][col] = 'Q'  # 在棋盘上放置皇后
                
                # 递归进入下一行，继续放置皇后
                backtrack(row + 1, cols, diag1, diag2, current_solution)
                
                # 撤销选择：回溯
                cols.remove(col)              # 取消列标记
                diag1.remove(row - col)       # 取消主对角线标记
                diag2.remove(row + col)       # 取消副对角线标记
                current_solution[row][col] = '.'  # 移除棋盘上的皇后
        
        result = []  # 存储所有可行解
        # 初始化棋盘，n 行 n 列，全部填入 '.'
        current_solution = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()    # 记录已放置皇后的列
        diag1 = set()   # 记录主对角线（row - col）
        diag2 = set()   # 记录副对角线（row + col）
        
        # 从第 0 行开始回溯搜索
        backtrack(0, cols, diag1, diag2, current_solution)
        return result   # 返回所有的解决方案
