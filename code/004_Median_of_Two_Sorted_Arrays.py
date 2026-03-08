#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   004_Median_of_Two_Sorted_Arrays.py
@Time    :   2025/05/12 14:54:20
@Author  :   rj
@Version :   1.0
@Desc    :   寻找两个正序数组的中位数
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的那个数组，以减少二分查找的范围
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # 核心思想：分割点
        # 对 nums1 和 nums2 各"切一刀"，将两个数组分成左右两半：
        #   nums1: left_1 | right_1   （分割点 i，左边有 i 个元素，取值范围 [0, m]）
        #   nums2: left_2 | right_2   （分割点 j，左边有 j 个元素，取值范围 [0, n]）
        #
        # 分割点 i=0 表示 nums1 全部在右半，i=m 表示 nums1 全部在左半
        # 因此二分的搜索空间是 m+1 个切割位置，right 初始化为 m 而非 m-1
        #
        # 目标：找到一组 (i, j) 使得：
        #   1. 左边总元素数 == 右边总元素数（奇数时左边多一个）
        #      即：i + j == (m + n + 1) // 2
        #   2. 左边最大值 <= 右边最小值
        #      即：max(left_1, left_2) <= min(right_1, right_2)
        # 满足以上两点，中位数就在左右边界处
        left, right = 0, m

        while left <= right:
            # i 是 nums1 的分割点，j 是 nums2 的分割点，使得左边元素数量等于右边元素数量（或多一个）
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # 处理边界情况，避免越界
            maxLeft1 = float("-inf") if i == 0 else nums1[i - 1]  # nums1 左边最大值
            minRight1 = float("inf") if i == m else nums1[i]  # nums1 右边最小值

            maxLeft2 = float("-inf") if j == 0 else nums2[j - 1]  # nums2 左边最大值
            minRight2 = float("inf") if j == n else nums2[j]  # nums2 右边最小值

            # 满足中位数条件：左边最大值 <= 右边最小值
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # 如果总长度是奇数，中位数是左边较大的那个
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # 如果总长度是偶数，中位数是左右两个中间值的平均数
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            # 如果 nums1 左边最大值太大，说明 i 选得太右了，需要往左移动
            elif maxLeft1 > minRight2:
                right = i - 1
            # 如果 nums2 左边最大值太大，说明 i 选得太左了，需要往右移动
            else:
                left = i + 1
