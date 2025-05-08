#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   230_Kth_Smallest_Element_in_a_BST.py
@Time    :   2025/05/08 17:19:01
@Author  :   rj
@Version :   1.0
@Desc    :   二叉搜索树中第 K 小的元素
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest_traversal(self, root: Optional[TreeNode], k: int) -> int:
        # 初始化计数器和结果变量
        self.count = 0
        self.result = None
        # 调用中序遍历函数
        self.inorder(root, k)
        return self.result

    def inorder(self, node, k):
        # 中序遍历树并查找第 K 小的元素
        if not node or self.result is not None:
            return
        # 遍历左子树
        self.inorder(node.left, k)
        # 访问当前节点
        self.count += 1
        # 如果当前节点是第 K 小元素，保存结果
        if self.count == k:
            self.result = node.val
            return
        # 遍历右子树
        self.inorder(node.right, k)

    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        # 非递归实现：使用栈模拟中序遍历
        stack = []
        current = root
        count = 0

        while current or stack:
            # 先遍历左子树
            while current:
                stack.append(current)
                current = current.left
            # 弹出栈顶元素
            current = stack.pop()
            # 访问当前节点
            count += 1
            # 如果当前节点是第 K 小元素，返回其值
            if count == k:
                return current.val
            # 遍历右子树
            current = current.right
