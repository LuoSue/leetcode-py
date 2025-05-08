#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   108_Convert_Sorted_Array_to_Binary_Search_Tree.py
@Time    :   2025/05/08 16:57:12
@Author  :   rj
@Version :   1.0
@Desc    :   将有序数组转换为二叉搜索树
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # 找到中间索引
        mid = len(nums) // 2

        # 创建根节点
        root = TreeNode(nums[mid])

        # 递归构建左子树和右子树
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root
