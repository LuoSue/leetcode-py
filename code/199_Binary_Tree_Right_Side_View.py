#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   199_Binary_Tree_Right_Side_View.py
@Time    :   2025/05/08 17:25:11
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树的右视图
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideViewIterative(self, root: Optional[TreeNode]) -> List[int]:
        # 如果树为空，返回空列表
        if not root:
            return []

        result = []  # 用于存储右视图的结果
        queue = deque([root])  # 使用队列进行层序遍历

        while queue:
            level_size = len(queue)  # 当前层的节点数

            for i in range(level_size):
                node = queue.popleft()  # 弹出当前节点

                # 如果是当前层的最后一个节点，将其值添加到结果列表中
                if i == level_size - 1:
                    result.append(node.val)

                # 如果左子树存在，将左子节点加入队列
                if node.left:
                    queue.append(node.left)
                # 如果右子树存在，将右子节点加入队列
                if node.right:
                    queue.append(node.right)

        return result  # 返回右视图的结果

    def rightSideViewRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, level):
            # 如果当前节点为空，返回
            if not node:
                return

            # 如果当前层还没有元素，说明这是该层的第一个节点，加入右视图
            if level == len(result):
                result.append(node.val)

            # 先递归右子树，再递归左子树，确保优先访问右子树
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        # 从根节点开始深度优先遍历
        dfs(root, 0)
        return result
