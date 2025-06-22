#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   437_Path_Sum_III.py
@Time    :   2025/05/09 17:16:33
@Author  :   rj
@Version :   1.0
@Desc    :   路径总和 III
"""

from collections import defaultdict
from typing import Optional

# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 哈希表记录前缀和出现的次数
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # 初始化：前缀和为 0 的路径出现过 1 次

        self.count = 0  # 用于统计符合条件的路径数量

        def dfs(node, current_sum):
            if not node:
                return  # 递归终止条件：到达空节点

            # 当前路径的前缀和
            current_sum += node.val

            # 查找是否存在一段前缀和使得 current_sum - prefix = targetSum
            # 即有多少个前缀和为 current_sum - targetSum 的路径
            self.count += prefix_sum[current_sum - targetSum]

            # 记录当前前缀和的次数（进入下一层递归前）
            prefix_sum[current_sum] += 1

            # 递归处理左右子树
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # 回溯：当前路径结束，撤销当前前缀和的记录，避免影响其他路径
            prefix_sum[current_sum] -= 1

        # 从根节点开始递归
        dfs(root, 0)

        return self.count  # 返回总路径数

