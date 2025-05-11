#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   236_Lowest_Common_Ancestor_of_a_Binary_Tree.py
@Time    :   2025/05/11 15:07:32
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树的最近公共祖先
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 如果根节点为空，说明没找到公共祖先，返回None
        if not root:
            return None
        # 如果根节点就是p或q，那么这个根节点就是最近公共祖先
        if root == p or root == q:
            return root

        # 递归查找左子树中的公共祖先
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归查找右子树中的公共祖先
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果在左子树和右子树中都找到了祖先节点，说明当前节点是最近公共祖先
        if left and right:
            return root

        # 如果只在左子树或右子树中找到，返回该子树的祖先节点
        return left if left else right
