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
        """
        将字符串分割成若干子串，使得每个子串都是回文串。
        返回所有可能的分割方案。
        
        :param s: 输入字符串
        :return: 所有可能的分割方案，每个方案是一个字符串列表
        """
        result = []  # 存储所有可能的分割方案
        path = []    # 存储当前正在构建的分割方案
        n = len(s)   # 字符串长度

        def dfs(i: int):
            """
            深度优先搜索回溯函数
            
            :param i: 当前待分割的起始位置
            """
            # 如果已经处理到字符串末尾，说明找到了一个完整的分割方案
            if i == n:
                result.append(path[:])  # 将当前方案加入结果集
                return

            # 从起始位置i开始，尝试所有可能的结束位置j
            for j in range(i, n):
                # 获取从i到j的子串（包含两端）
                t = s[i : j + 1]
                
                # 检查子串是否为回文串（正反读相同）
                if t == t[::-1]:
                    # 如果是回文串，将其加入当前分割方案
                    path.append(t)
                    # 递归处理剩余部分，下一个起始位置为j+1
                    dfs(j + 1)
                    # 回溯：移除当前子串，尝试下一个可能的分割点
                    path.pop()

        # 从字符串起始位置0开始回溯
        dfs(0)
        
        return result