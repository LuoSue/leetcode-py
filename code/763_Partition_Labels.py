#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   763_Partition_Labels.py
@Time    :   2025/05/12 22:44:10
@Author  :   rj
@Version :   1.0
@Desc    :   划分字母区间
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: 记录每个字符最后出现的位置
        last_position = {char: idx for idx, char in enumerate(s)}

        partitions = []
        start, end = 0, 0

        # Step 2: 遍历字符串
        for idx, char in enumerate(s):
            # 更新当前部分的结束位置
            end = max(end, last_position[char])

            # 如果当前字符的位置等于部分的结束位置，说明这一部分可以划分完毕
            if idx == end:
                partitions.append(idx - start + 1)  # 记录当前部分的大小
                start = idx + 1  # 更新 start 为下一个部分的起始位置

        return partitions
