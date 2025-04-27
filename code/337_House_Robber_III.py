#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   337_House_Robber_III.py
@Time    :   2025/04/27 11:19:07
@Author  :   rj
@Version :   1.0
@Desc    :   打家劫舍 III - 二叉树版
"""

from typing import Optional

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 深度优先搜索函数，返回一个元组 (抢当前节点的最大值, 不抢当前节点的最大值)
        def dfs(node):
            if not node:
                return (0, 0)  # (抢劫当前节点的金额, 不抢劫当前节点的金额)
            
            # 递归处理左子树和右子树
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 抢劫当前节点：当前节点的值 + 不抢劫左右子节点的最大值
            rob_current = node.val + left[1] + right[1]
            
            # 不抢劫当前节点：左右子节点可以抢或不抢，取最大值
            not_rob_current = max(left[0], left[1]) + max(right[0], right[1])
            
            return (rob_current, not_rob_current)

        # 执行深度优先搜索并获取结果
        result = dfs(root)
        
        # 返回两种情况的最大值：抢或不抢当前根节点
        return max(result[0], result[1])
