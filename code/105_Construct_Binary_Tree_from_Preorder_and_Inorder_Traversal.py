#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.py
@Time    :   2025/05/09 17:08:59
@Author  :   rj
@Version :   1.0
@Desc    :   从前序与中序遍历序列构造二叉树
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 使用字典存储中序遍历中每个节点的索引位置，以便快速查找
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        # 创建一个迭代器，用于遍历前序遍历数组
        pre_iter = iter(preorder)

        def helper(in_start, in_end):
            # 如果当前子树为空，返回 None
            if in_start > in_end:
                return None

            # 获取前序遍历的当前根节点
            root_val = next(pre_iter)
            root = TreeNode(root_val)  # 创建该根节点

            # 在中序遍历中找到当前根节点的位置
            root_pos = inorder_map[root_val]

            # 递归构建左子树和右子树
            # 左子树范围是 [in_start, root_pos - 1]
            root.left = helper(in_start, root_pos - 1)
            # 右子树范围是 [root_pos + 1, in_end]
            root.right = helper(root_pos + 1, in_end)

            return root

        # 调用 helper 函数构建树
        return helper(0, len(inorder) - 1)
