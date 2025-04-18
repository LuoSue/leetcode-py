#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1652_Defuse_the_Bomb.py
@Time    :   2025/04/18 16:27:21
@Author  :   rj 
@Version :   1.0
@Desc    :   拆炸弹
"""

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # 获取输入数组的长度
        n = len(code)
        # 初始化结果数组，初始值全为0
        result = [0] * n

        # 如果k等于0，所有元素都应该是0，直接返回结果
        if k == 0:
            return result

        # 遍历code数组的每一个元素
        for i in range(n):
            total = 0  # 用于存储当前索引位置的加密结果

            # 如果k是正数，从当前位置的下一个元素开始，向右取k个元素相加
            if k > 0:
                for j in range(1, k + 1):
                    # 使用取模运算确保循环访问数组（环状数组）
                    total += code[(i + j) % n]

            # 如果k是负数，从当前位置的前一个元素开始，向左取|k|个元素相加
            if k < 0:
                for j in range(1, 1 - k):  # 注意范围是1到|k|（即1-k）
                    # 使用(n + i - j) % n确保索引始终为正且在有效范围
                    total += code[(i - j + n) % n]

            # 将计算结果保存到对应的位置
            result[i] = total

        # 返回加密后的数组
        return result
