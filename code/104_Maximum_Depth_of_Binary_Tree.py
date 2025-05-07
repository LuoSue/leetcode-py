#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   104_Maximum_Depth_of_Binary_Tree.py
@Time    :   2025/05/07 17:39:38
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树的最大深度
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归写法：计算二叉树的最大深度
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 如果节点为空，高度为0
        # 递归计算左子树和右子树的最大高度
        left_height = self.maxDepthRecursive(root.left)
        right_height = self.maxDepthRecursive(root.right)
        # 当前节点的最大高度 = 左右子树最大高度中的较大值 + 1（算上当前节点）
        return max(left_height, right_height) + 1

    # 迭代写法：使用队列进行层序遍历（BFS）计算最大深度
    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # 如果节点为空，高度为0

        queue = deque([root])  # 初始化队列，加入根节点
        depth = 0  # 初始化深度为0

        while queue:
            depth += 1  # 每遍历一层，深度+1

            # 遍历当前层的所有节点
            for _ in range(len(queue)):
                node = queue.popleft()  # 弹出队首节点

                # 将下一层的节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth  # 返回最大深度
