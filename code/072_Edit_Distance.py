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
        """
        | 操作类型 | 状态转移               | 含义                                                                      |
        | ---- | ------------------ | ----------------------------------------------------------------------- |
        | 删除   | `dp[i-1][j] + 1`   | 删除 `word1[i-1]`，问题变为 `word1[0..i-2]` 转换成 `word2[0..j-1]`                |
        | 插入   | `dp[i][j-1] + 1`   | 在 `word1` 末尾插入 `word2[j-1]`，问题变为 `word1[0..i-1]` 转换成 `word2[0..j-2]`    |
        | 替换   | `dp[i-1][j-1] + 1` | 替换 `word1[i-1]` 为 `word2[j-1]`，问题变为 `word1[0..i-2]` 转换成 `word2[0..j-2]` |

        动态规划思路：
        本题求两个字符串之间的最小编辑距离（最少操作次数），允许操作包括：
        - 插入一个字符
        - 删除一个字符
        - 替换一个字符

        状态定义：
        - dp[i][j] 表示将 word1 的前 i 个字符转换为 word2 的前 j 个字符所需的最小操作数。

        状态转移：
        - 若 word1[i - 1] == word2[j - 1]，则 dp[i][j] = dp[i - 1][j - 1]
        - 否则：
            dp[i][j] = min(
                dp[i - 1][j],     # 删除：从 word1 删除一个字符
                dp[i][j - 1],     # 插入：在 word1 插入一个字符
                dp[i - 1][j - 1]  # 替换：替换 word1 的当前字符
            ) + 1

        初始化：
        - dp[0][j] = j：将空串变成 word2 的前 j 个字符，需要插入 j 次
        - dp[i][0] = i：将 word1 的前 i 个字符变成空串，需要删除 i 次

        空间优化：
        - 注意每次 dp[i][j] 只依赖于上一行（i-1）和当前行的前一列（j-1），
        - 所以可以用滚动数组，仅保留两行（prev 和 curr）

        时间复杂度：O(m * n)
        空间复杂度：O(n)
        """

        m, n = len(word1), len(word2)

        # 初始化第一行：将空字符串变成 word2 所需的操作次数
        prev = list(range(n + 1))  # dp[0][j] = j
        curr = [0] * (n + 1)  # 当前行 dp[i][*]

        for i in range(1, m + 1):
            curr[0] = i  # dp[i][0] = i，将 word1 的前 i 个字符变为空串

            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 字符相等，不需要操作
                    curr[j] = prev[j - 1]
                else:
                    # 字符不同，取三种操作中的最小值加一
                    curr[j] = (
                        min(
                            prev[j],  # 删除 word1[i - 1]
                            curr[j - 1],  # 插入 word2[j - 1]
                            prev[j - 1],  # 替换
                        )
                        + 1
                    )

            # 滚动数组：交换 prev 和 curr，为下一轮做准备
            prev, curr = curr, prev

        # 最终编辑距离在 dp[m][n]，也就是 prev[n] 中
        return prev[n]
