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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currentSum):
            if not node:
                return 0

            # 更新当前路径的累积和
            currentSum += node.val

            # 统计累积和中有多少个满足条件的路径
            count = prefixSums[currentSum - targetSum]

            # 将当前累积和记录到哈希表中
            prefixSums[currentSum] += 1

            # 递归遍历左子树和右子树
            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)

            # 回溯时，移除当前路径的累积和
            prefixSums[currentSum] -= 1

            return count

        # 哈希表存储累积和及其出现的次数
        prefixSums = defaultdict(int)
        # 初始条件：表示从根节点到当前节点的路径和为0
        prefixSums[0] = 1

        return dfs(root, 0)
