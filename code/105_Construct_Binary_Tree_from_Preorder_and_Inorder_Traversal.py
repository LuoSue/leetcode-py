#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.py
@Time    :   2025/05/09 17:08:59
@Author  :   rj
@Version :   1.0
@Desc    :   从前序与中序遍历序列构造二叉树（优化版）
"""

from typing import List, Optional


# 定义二叉树节点结构
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 将中序遍历值与其索引构建哈希表，便于 O(1) 查找根节点位置
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # 使用前序遍历构建树，定义一个迭代器代替索引变量，更高效
        pre_iter = iter(preorder)

        # 辅助递归函数：构建中序范围在 [in_start, in_end] 的子树
        def helper(in_start, in_end):
            # 若当前子树区间非法，返回空节点
            if in_start > in_end:
                return None

            # 前序遍历中当前的根节点值（递归中每次前进一步）
            root_val = next(pre_iter)
            root = TreeNode(root_val)

            # 从哈希表中查找该值在中序中的位置
            root_pos = inorder_map[root_val]

            # 递归构建左子树：中序区间为 [in_start, root_pos - 1]
            root.left = helper(in_start, root_pos - 1)

            # 递归构建右子树：中序区间为 [root_pos + 1, in_end]
            root.right = helper(root_pos + 1, in_end)

            # 返回当前构建好的树节点
            return root

        # 初始构造整棵树，范围为整个中序遍历区间
        return helper(0, len(inorder) - 1)
