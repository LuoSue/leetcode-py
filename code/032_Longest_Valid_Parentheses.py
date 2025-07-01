#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   032_Longest_Valid_Parentheses.py
@Time    :   2025/04/28 10:28:44
@Author  :   rj
@Version :   1.0
@Desc    :   最长有效括号
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        动态规划思路：
        定义 dp[i] 表示以 s[i] 结尾的最长有效括号子串的长度。
        初始状态：dp[i] = 0（默认无有效括号）

        状态转移：
        只有当 s[i] == ')' 时才可能产生有效子串：
        1. 如果 s[i-1] == '('，即遇到 "()"：
           - 则 dp[i] = dp[i-2] + 2 （i >= 2 时加上前面的有效子串）

        2. 如果 s[i-1] == ')'，即形如 "...))"，需要检查前面是否存在匹配的 '('：
           - 令 prev = i - dp[i-1] - 1
           - 如果 s[prev] == '('，则可以将 s[prev:i] 组成有效括号
           - dp[i] = dp[i-1] + 2 + dp[prev-1]（若 prev >= 1，否则加 0）

        最终在遍历中不断更新最大长度 max_len

        时间复杂度：O(n)
        空间复杂度：O(n)
        """

        n = len(s)
        if n == 0:
            return 0

        # dp[i] 表示以 s[i] 结尾的最长有效括号子串的长度
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ")":  # 只在遇到右括号时，才可能组成有效括号
                if s[i - 1] == "(":
                    # 形如 "()"，可以直接构成一对
                    # 如果前面还有有效括号，则加上它们的长度
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    # 形如 "))"，前面还有一个匹配的 "("
                    # s[i - dp[i - 1] - 1] 是当前 ')' 的匹配 '('
                    # 再加上更前面的有效长度
                    dp[i] = (
                        dp[i - 1]
                        + 2
                        + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                    )

                # 更新最大长度
                max_len = max(max_len, dp[i])

        return max_len

    def longestValidParentheses_stack(self, s: str) -> int:
        """
        栈解法思路：
        使用一个栈保存括号的索引位置，用来匹配有效括号。

        初始在栈中压入 -1，作为基准点（哨兵）：
        - 如果当前字符是 '('，将其索引压入栈；
        - 如果是 ')'，弹出栈顶元素：
            - 如果栈变空，说明当前右括号无法匹配，入栈当前索引作为新起点；
            - 如果栈非空，当前 i - stack[-1] 即为一个有效括号子串的长度。

        遍历过程中不断更新最大长度。

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        max_len = 0
        stack = [-1]  # 哨兵，代表一个虚拟起点

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # 当前右括号无法配对，更新起点
                    stack.append(i)
                else:
                    # 当前右括号匹配成功，更新最大长度
                    max_len = max(max_len, i - stack[-1])

        return max_len
