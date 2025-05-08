#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   102_Binary_Tree_Level_Order_Traversal.py
@Time    :   2025/05/08 16:49:35
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树的层序遍历
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 如果根节点为空，返回空列表
        if not root:
            return []

        # 使用队列来进行层序遍历
        queue = deque([root])
        result = []  # 存储结果的列表

        while queue:
            # 当前层的节点数量
            level_length = len(queue)
            level_value = []  # 当前层的节点值

            # 遍历当前层的所有节点
            for _ in range(level_length):
                node = queue.popleft()  # 从队列中取出节点
                level_value.append(node.val)  # 记录当前节点的值

                # 如果左子树存在，加入队列
                if node.left:
                    queue.append(node.left)
                # 如果右子树存在，加入队列
                if node.right:
                    queue.append(node.right)

            # 将当前层的值添加到结果中
            result.append(level_value)

        # 返回所有层的遍历结果
        return result
