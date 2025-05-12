#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   072_Edit_Distance.py
@Time    :   2025/05/12 22:57:03
@Author  :   rj
@Version :   1.0
@Desc    :   编辑距离
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # 优化空间：只需要两行dp数组
        prev = list(range(n + 1))
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            curr[0] = i  # 当前行的第一列，代表把word1前i个字符变为空字符串
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = (
                        min(
                            prev[j],  # 删除
                            curr[j - 1],  # 插入
                            prev[j - 1],  # 替换
                        )
                        + 1
                    )
            # 将当前行赋值给prev，进行下一轮迭代
            prev, curr = curr, prev

        # 最终结果在prev[n]中
        return prev[n]
