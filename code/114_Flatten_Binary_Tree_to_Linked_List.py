#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   114_Flatten_Binary_Tree_to_Linked_List.py
@Time    :   2025/05/09 16:40:04
@Author  :   rj
@Version :   1.0
@Desc    :   二叉树展开为链表
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    head = None

    def flattenByPostOrder(self, root: Optional[TreeNode]) -> None:
        """
        逆先序遍历法：不返回任何值，直接就地修改root。
        通过逆先序遍历将右子树、左子树依次连接成链表。
        """
        if root is None:
            return
        # 先递归展开右子树，再递归展开左子树
        self.flattenByPostOrder(root.right)
        self.flattenByPostOrder(root.left)
        # 当前节点的左子树置空，将右子树接到当前节点的右侧
        root.left = None
        root.right = self.head
        self.head = root  # 更新head为当前节点

    def flattenByRearranging(self, root: Optional[TreeNode]) -> None:
        """
        重新排列法：不返回任何值，直接就地修改root。
        通过修改节点的指向，将左子树调整到右子树上，保持链表结构。
        """
        if root is None:
            return None
        # 递归处理左子树和右子树，得到左右子树的尾节点
        left_tail = self.flattenByRearranging(root.left)
        right_tail = self.flattenByRearranging(root.right)
        # 如果左子树存在，将左子树接到右子树上
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        # 返回右子树的尾节点，若右子树为空，则返回左子树的尾节点，若都为空则返回当前节点
        return right_tail or left_tail or root

    def flattenByInPlace(self, root: Optional[TreeNode]) -> None:
        """
        就地修改法：不返回任何值，直接就地修改root。
        通过遍历节点，并将左子树移动到右子树上，保持链表结构。
        """
        curr = root
        while curr:
            if curr.left:
                # 找到左子树的最右节点
                prev = curr.left
                while prev.right:
                    prev = prev.right
                # 将右子树接到最右节点
                prev.right = curr.right
                # 将左子树移到右边
                curr.right = curr.left
                curr.left = None
            # 移动到下一个节点
            curr = curr.right
