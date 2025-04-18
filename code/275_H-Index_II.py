#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   275_H-Index_II.py
@Time    :   2025/04/18 10:52:08
@Author  :   rj 
@Version :   1.0
@Desc    :   H 指数 II
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 定义二分查找的左右边界
        # h 指数的可能范围是 0 到 len(citations)
        left = 1
        right = len(citations) + 1  # 注意这里是开区间 [left, right)

        while left < right:
            mid = (left + right) // 2  # 取中间值作为候选 h 值
            # 检查 citations[-mid] 是否 >= mid
            # citations[-mid] 相当于从末尾往前数第 mid 个数
            # 举个例子：[-1] 是最后一个，[-2] 是倒数第二个
            # 如果倒数第 mid 个引用数 >= mid，说明至少有 mid 篇论文被引用了至少 mid 次
            if citations[-mid] >= mid:
                # 说明还可能有更大的 h 值，往右边继续找
                left = mid + 1
            else:
                # mid 太大了，不满足条件，往左边找
                right = mid

        # 最后 left 会停在第一个不满足条件的位置
        # 所以要返回 left - 1，才是最大的满足条件的 h 值
        return left - 1