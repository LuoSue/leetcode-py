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
        n = len(s)
        if n == 0:
            return 0
        
        # dp[i] 表示以 s[i] 结尾的最长有效括号子串的长度
        dp = [0] * n
        max_len = 0
        
        for i in range(1, n):
            if s[i] == ')':  # 只在遇到右括号时，才可能组成有效括号
                if s[i - 1] == '(':
                    # 形如 "()"，可以直接构成一对
                    # 如果前面还有有效括号，则加上它们的长度
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    # 形如 "))" 且前面有匹配的 "("
                    # dp[i - 1] 是前一个 ')' 结尾的有效长度
                    # s[i - dp[i - 1] - 1] 是与当前 ')' 匹配的 '('
                    # 再加上更前面 dp[i - dp[i - 1] - 2] 的长度
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                
                # 更新最大长度
                max_len = max(max_len, dp[i])
        
        return max_len
