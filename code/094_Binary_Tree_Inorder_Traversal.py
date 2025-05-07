#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   094_Binary_Tree_Inorder_Traversal.py
@Time    :   2025/05/07 17:25:04
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树的中序遍历
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # 用于存储中序遍历的结果

        # 定义递归的深度优先搜索（DFS）函数
        def dfs(root):
            if not root:
                return  # 如果节点为空，直接返回
            dfs(root.left)  # 先递归遍历左子树
            result.append(root.val)  # 访问当前节点（中序遍历的“中”）
            dfs(root.right)  # 再递归遍历右子树

        dfs(root)  # 从根节点开始进行 DFS
        return result  # 返回最终的中序遍历结果

    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # 用于存储中序遍历的结果
        stack = []  # 用栈模拟递归过程
        current = root

        # 当栈不为空或当前节点不为空时循环
        while stack or current:
            # 不断将当前节点及其左子树入栈
            while current:
                stack.append(current)
                current = current.left
            # 弹出栈顶节点，访问它
            current = stack.pop()
            result.append(current.val)
            # 转向右子树
            current = current.right

        return result  # 返回最终的中序遍历结果
