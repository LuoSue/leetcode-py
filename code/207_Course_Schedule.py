#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   207_Course_Schedule.py
@Time    :   2025/05/11 15:26:24
@Author  :   rj 
@Version :   1.0
@Desc    :   课程表
"""

from collections import deque
from typing import List

# 定义解决方案类
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 邻接表，用于存储每门课的先修课程
        adj_list = [[] for _ in range(numCourses)]
        # 记录每门课程的入度（即先修课程的数量）
        indegree = [0] * numCourses

        # 根据先修课程的关系填充邻接表和入度数组
        for course, prereq in prerequisites:
            indegree[course] += 1  # 课程的入度增加
            adj_list[prereq].append(course)  # 先修课程指向当前课程

        # 初始化队列，将入度为0的课程（没有先修课程的课程）加入队列
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        process = 0  # 记录已经处理的课程数

        # 广度优先搜索（BFS）处理课程
        while queue:
            current = queue.popleft()  # 弹出队列中的课程
            process += 1  # 处理一门课程

            # 遍历当前课程的所有后续课程
            for next in adj_list[current]:
                indegree[next] -= 1  # 将后续课程的入度减1
                # 如果某门课程的入度变为0，说明它可以被学习，加入队列
                if indegree[next] == 0:
                    queue.append(next)
        
        # 如果已处理的课程数量等于总课程数，返回True，否则返回False
        return process == numCourses
