#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   101_Symmetric_Tree.py
@Time    :   2025/05/08 09:36:05
@Author  :   rj
@Version :   1.0
@Desc    :   对称二叉树
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """迭代方法判断二叉树是否对称
        Args:
            root: 二叉树根节点
        Returns:
            bool: 如果树是对称的返回True，否则返回False
        """
        if not root:
            return True

        # 使用双端队列存储需要比较的节点对
        queue = deque([(root.left, root.right)])

        while queue:
            # 取出需要比较的左右节点
            l_node, r_node = queue.popleft()

            # 如果两个节点都为空，继续检查下一对
            if not l_node and not r_node:
                continue

            # 如果只有一个节点为空或节点值不同，返回False
            if not l_node or not r_node or l_node.val != r_node.val:
                return False

            # 将对应的子节点对加入队列（左子树的左节点与右子树的右节点比较，左子树的右节点与右子树的左节点比较）
            queue.append((l_node.left, r_node.right))
            queue.append((l_node.right, r_node.left))

        return True

    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        """递归方法判断二叉树是否对称
        Args:
            root: 二叉树根节点
        Returns:
            bool: 如果树是对称的返回True，否则返回False
        """

        def isMirror(l_node, r_node):
            """辅助函数，检查两棵子树是否镜像对称
            Args:
                l_node: 左子树节点
                r_node: 右子树节点
            Returns:
                bool: 如果子树镜像对称返回True，否则返回False
            """
            # 如果两个节点都为空，返回True
            if not l_node and not r_node:
                return True
            # 如果只有一个节点为空或节点值不同，返回False
            if not l_node or not r_node or l_node.val != r_node.val:
                return False
            # 递归检查左子树的左节点与右子树的右节点，以及左子树的右节点与右子树的左节点
            return isMirror(l_node.left, r_node.right) and isMirror(
                l_node.right, r_node.left
            )

        if not root:
            return False
        # 从根节点的左右子树开始检查
        return isMirror(root.left, root.right)
