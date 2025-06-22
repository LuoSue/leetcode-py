#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   124_Binary_Tree_Maximum_Path_Sum.py
@Time    :   2025/05/11 15:11:47
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树中的最大路径和
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")  # 全局最大路径和

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # 递归计算左右子树的最大路径和，如果小于0就舍弃
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # 当前节点作为路径顶点时的最大路径和
            current_max = node.val + left_max + right_max

            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, current_max)

            # 返回当前节点对父节点的最大贡献
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum
