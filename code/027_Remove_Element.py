#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   027_Remove_Element.py
@Time    :   2025/07/07 14:06:57
@Author  :   rj
@Version :   1.0
@Desc    :   移除元素
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k 记录非目标元素应放置的位置
        k = 0
        for x in nums:
            # 如果当前元素不是要移除的 val，则保留
            if x != val:
                nums[k] = x  # 将该元素移动到 nums[k] 位置
                k += 1  # k 前进一位
        # 最终 k 即为新数组的长度（不包含 val 的元素个数）
        return k
