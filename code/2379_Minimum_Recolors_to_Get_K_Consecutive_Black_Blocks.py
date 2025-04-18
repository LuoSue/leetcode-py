#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2379_Minimum_Recolors_to_Get_K_Consecutive_Black_Blocks.py
@Time    :   2025/04/18 14:27:46
@Author  :   rj 
@Version :   1.0
@Desc    :   得到 K 个黑块的最少涂色次数
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 初始化窗口内白块数量：统计前 k 个字符中 'W' 的数量
        white_count = sum(1 for i in range(k) if blocks[i] == 'W')
        # 初始化最小操作次数为当前窗口中的白块数量
        min_operation = white_count

        # 使用滑动窗口遍历剩余部分
        for i in range(k, len(blocks)):
            # 右边进入窗口的字符是白块，增加白块计数
            if blocks[i] == 'W':
                white_count += 1
            # 左边移出窗口的字符是白块，减少白块计数
            if blocks[i - k] == 'W':
                white_count -= 1
            # 记录最小的操作次数
            min_operation = min(min_operation, white_count)

        # 返回最小的涂色次数
        return min_operation
