#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   543_Diameter_of_Binary_Tree.py
@Time    :   2025/05/08 16:41:39
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树的直径
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    对于树中的每一个节点，以该节点为根的子树的直径要么是左子树的直径，要么是右子树的直径，
    要么是穿过该节点的最长路径（即左子树的最大深度 + 右子树的最大深度 + 1）。
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 初始化直径，初始值为0
        self.diameter = 0

        def height(node):
            # 递归函数，计算当前节点的高度
            if not node:
                return 0
            # 递归计算左子树和右子树的深度
            left_depth = height(node.left)
            right_depth = height(node.right)
            # 更新树的直径，选择最大值
            self.diameter = max(self.diameter, left_depth + right_depth)

            # 返回当前节点的高度
            return max(left_depth, right_depth) + 1

        # 从根节点开始计算
        height(root)
        # 返回计算得到的二叉树直径
        return self.diameter
