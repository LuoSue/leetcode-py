#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   098_Validate_Binary_Search_Tree.py
@Time    :   2025/05/08 17:01:57
@Author  :   rj
@Version :   1.0
@Desc    :   验证二叉搜索树
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST_traversal(self, root: Optional[TreeNode]) -> bool:
        # 用于记录前一个节点的值，初始化为负无穷
        self.prev = float("-inf")
        # 标记是否是有效的二叉搜索树
        self.is_valid = True

        def inorder(node):
            # 递归中序遍历函数
            if not node or not self.is_valid:
                return
            inorder(node.left)  # 先遍历左子树
            # 如果当前节点的值小于等于前一个节点的值，说明不是二叉搜索树
            if node.val <= self.prev:
                self.is_valid = False
                return
            # 更新前一个节点的值
            self.prev = node.val
            inorder(node.right)  # 再遍历右子树

        inorder(root)  # 从根节点开始中序遍历
        return self.is_valid  # 返回是否是有效的二叉搜索树

    def isValidBST_recursive(self, root: TreeNode) -> bool:
        # 递归法：验证节点值是否在合适的范围内
        def isValid(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True  # 如果节点为空，说明是有效的
            # 如果当前节点的值不在合法范围内，则返回 False
            if node.val <= lower or node.val >= upper:
                return False
            # 递归验证左子树和右子树，左子树的值应该小于当前节点，右子树的值应该大于当前节点
            return isValid(node.left, lower, node.val) and isValid(
                node.right, node.val, upper
            )

        return isValid(root)  # 从根节点开始递归验证
