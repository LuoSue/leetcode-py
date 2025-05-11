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
        # 全局变量，记录最大路径和
        max_sum = float("-inf")

        def max_gain(node):
            nonlocal max_sum

            if not node:
                return 0

            # 递归计算左右子树的最大贡献值
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 当前节点的最大路径和
            current_max_path = node.val + left_gain + right_gain

            # 更新全局最大路径和
            max_sum = max(max_sum, current_max_path)

            # 返回当前节点能够向上提供的最大路径和
            return node.val + max(left_gain, right_gain)

        # 从根节点开始递归
        max_gain(root)

        return max_sum
