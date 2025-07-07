#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   274_H-Index.py
@Time    :   2025/07/07 15:47:21
@Author  :   rj
@Version :   1.0
@Desc    :   H 指数
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)  # 论文总数
        counter = [0] * (
            n + 1
        )  # 创建一个计数数组，索引表示引用次数，值表示有多少篇论文引用次数为该索引

        # 遍历每篇论文的引用次数
        for c in citations:
            if c >= n:
                # 如果引用次数大于等于 n，统一归为 n（因为 h 最大不会超过 n）
                counter[n] += 1
            else:
                # 否则统计该引用次数对应的论文数量
                counter[c] += 1

        total = 0  # total 表示引用次数大于等于 i 的论文总数
        # 从 n 到 0 倒序遍历，找最大满足条件的 h
        for i in range(n, -1, -1):
            total += counter[i]  # 累加引用次数 ≥ i 的论文篇数
            if total >= i:
                # 找到最大的 i 满足至少有 i 篇论文引用次数 ≥ i
                return i

        return 0  # 没有满足条件的 h，返回 0
