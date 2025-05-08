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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
