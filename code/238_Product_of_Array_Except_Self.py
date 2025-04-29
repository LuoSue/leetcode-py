#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   238_Product_of_Array_Except_Self.py
@Time    :   2025/04/29 11:51:19
@Author  :   rj
@Version :   1.0
@Desc    :   除自身以外数组的乘积
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # 获取数组的长度
        ans = [1] * n  # 初始化结果数组，每个元素初始为1
        pre = 1  # 用于存储从左到右的前缀积

        # 第一次遍历：计算每个位置左边所有元素的乘积
        for i in range(n):
            ans[i] = pre  # 当前ans[i]存储的是当前位置左边所有元素的乘积
            pre *= nums[i]  # 更新pre为当前位置的乘积，pre存储的是从左到当前位置的乘积

        suf = 1  # 用于存储从右到左的后缀积
        # 第二次遍历：计算每个位置右边所有元素的乘积，并与ans中的前缀积相乘
        for j in range(n - 1, -1, -1):
            ans[j] *= suf  # 当前ans[j]存储的是左边和右边所有元素的乘积
            suf *= nums[j]  # 更新suf为当前位置的乘积，suf存储的是从右到当前位置的乘积

        return ans  # 返回最终结果
