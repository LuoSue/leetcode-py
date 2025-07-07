#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   088_Merge_Sorted_Array.py
@Time    :   2025/07/07 11:46:26
@Author  :   rj
@Version :   1.0
@Desc    :   合并两个有序数组
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        不返回值，直接在 nums1 原地合并两个有序数组。
        nums1 的长度为 m + n，其中前 m 个元素为有效数字，后 n 个元素为预留空间。
        nums2 的长度为 n，存储 n 个有序的元素。
        """
        # 初始化三个指针：
        # p1 指向 nums1 的最后一个有效元素
        # p2 指向 nums2 的最后一个元素
        # p 指向 nums1 的最后一个位置（用于放置当前最大值）
        p1, p2, p = m - 1, n - 1, m + n - 1

        # 从后往前比较 nums1 和 nums2 中的元素，将较大值放到 nums1 的末尾
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # 将 nums1[p1] 放到 nums1[p]
                p1 -= 1  # 向前移动 nums1 指针
            else:
                nums1[p] = nums2[p2]  # 将 nums2[p2] 放到 nums1[p]
                p2 -= 1  # 向前移动 nums2 指针
            p -= 1  # 向前移动合并指针

        # 如果 nums2 还有剩余元素，说明这些元素比 nums1 中的所有元素都小，直接复制到 nums1 前面
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
