#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   139_Word_Break.py
@Time    :   2025/04/27 22:36:27
@Author  :   rj
@Version :   1.0
@Desc    :   单词拆分
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        动态规划思路：
        定义 dp[i] 表示字符串 s 的前 i 个字符 s[:i] 是否可以被字典中的单词拆分组成。
        初始状态：dp[0] = True，空字符串可被拆分。

        状态转移：
        对每个位置 i（从1到n），
            尝试从 i 的前面某个位置 j 拆分，
            如果 dp[j] 是 True，且 s[j:i] 是字典中的单词，
            那么 dp[i] 也为 True。

        通过这个过程，dp[n] 即表示整个字符串 s 是否可被拆分。

        优化：
        由于单词有最大长度 max_len，可以缩小 j 的遍历区间，减少不必要的检查。
        """

        # 将单词列表转换为集合，加快查找速度
        word_set = set(wordDict)
        # 获取字典中最长单词的长度，减少不必要的遍历
        max_len = max(len(word) for word in word_set) if word_set else 0
        n = len(s)
        # 初始化动态规划数组，dp[i]表示s[:i]是否可以被拆分成字典中的单词
        dp = [False] * (n + 1)
        dp[0] = True  # 空字符串可以被拆分

        # 遍历字符串的每个位置
        for i in range(1, n + 1):
            # 优化：只需要检查i-max_len到i之间的子串
            start = max(0, i - max_len)
            for j in range(start, i):
                # 如果s[:j]可以拆分，且s[j:i]在字典中，则s[:i]也可以拆分
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # 找到一种拆分方式即可，不需要继续检查
        # 返回整个字符串是否可以被拆分
        return dp[n]
