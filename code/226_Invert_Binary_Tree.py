#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   226_Invert_Binary_Tree.py
@Time    :   2025/05/07 22:50:14
@Author  :   rj
@Version :   1.0
@Desc    :   翻转二叉树
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        迭代方式翻转二叉树
        """
        if not root:
            return None

        stack = [root]

        while stack:
            current = stack.pop()
            # 交换当前节点的左右子节点
            current.left, current.right = current.right, current.left

            # 如果左子节点存在，加入栈中
            if current.left:
                stack.append(current.left)
            # 如果右子节点存在，加入栈中
            if current.right:
                stack.append(current.right)

        return root

    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归方式翻转二叉树
        """
        if not root:
            return None

        # 交换当前节点的左右子节点
        root.left, root.right = root.right, root.left

        # 递归翻转左子树
        self.invertTreeRecursive(root.left)
        # 递归翻转右子树
        self.invertTreeRecursive(root.right)

        return root
