#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   611_Valid_Triangle_Number.py
@Time    :   2025/04/15 16:27:06
@Author  :   rj 
@Version :   1.0
@Desc    :   有效三角形的个数
"""

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()  # 先排序，以便使用双指针
        n = len(nums)
        ans = 0  # 统计有效三角形数量

        # 从最大的数开始，倒序遍历（固定最大的边 nums[k]）
        for k in range(n - 1, 1, -1):
            i = 0  # 左指针
            j = k - 1  # 右指针（指向比 nums[k] 小的最大数）
            
            while i < j:
                # 检查是否能构成三角形：nums[i] + nums[j] > nums[k]
                if nums[i] + nums[j] > nums[k]:
                    # 如果成立，则 nums[i], nums[j], nums[k] 可以组成三角形
                    # 并且 nums[i+1], nums[i+2], ..., nums[j-1] 和 nums[j], nums[k] 也能组成三角形
                    # 所以共有 j - i 个新组合
                    ans += j - i
                    j -= 1  # 尝试更小的 nums[j]
                else:
                    # 不满足条件，说明 nums[i] 太小，需要增大
                    i += 1
        return ans