#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2266_Count_Number_of_Texts.py
@Time    :   2025/07/11 17:46:37
@Author  :   rj
@Version :   1.0
@Desc    :   统计打字方案数
"""


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7  # 取模防止结果过大
        n = len(pressedKeys)  # 输入的字符串长度
        dp = [0] * (n + 1)  # dp[i] 表示前 i 个字符的打字方案数
        dp[0] = 1  # 空字符串只有一种打字方案

        # 每个数字最多能连续按的次数：'7' 和 '9' 是 4 次，其他是 3 次
        max_press = {"2": 3, "3": 3, "4": 3, "5": 3, "6": 3, "7": 4, "8": 3, "9": 4}

        # 从第 1 个字符开始遍历
        for i in range(1, n + 1):
            ch = pressedKeys[i - 1]  # 当前第 i 个字符（下标从 0 开始）
            limit = max_press[ch]  # 当前字符最多可连续按的次数

            # 向前最多查 limit 位，看这些连续字符是否都是当前字符
            for j in range(1, limit + 1):
                # 确保索引合法并且 pressedKeys[i-j:i] 是 j 个相同的 ch
                if i - j >= 0 and pressedKeys[i - j : i] == ch * j:
                    dp[i] += dp[i - j]  # 加上以这些 j 个字符为结尾的方案数
                    dp[i] %= MOD  # 取模防止溢出

        return dp[n]  # 返回整个字符串的总方案数
