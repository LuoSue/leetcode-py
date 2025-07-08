#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   380_Insert_Delete_GetRandom_O(1).py
@Time    :   2025/07/08 14:18:16
@Author  :   rj
@Version :   1.0
@Desc    :   O(1) 时间插入、删除和获取随机元素
"""

import random


class RandomizedSet:
    def __init__(self):
        # 初始化哈希表和数组
        self.val_to_index = {}  # 记录元素值到索引的映射
        self.nums = []  # 存储元素的列表

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False  # 已存在，不能插入
        # 插入到末尾，并记录其索引
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False  # 不存在，不能删除

        # 获取要删除元素的索引
        index_to_remove = self.val_to_index[val]
        last_val = self.nums[-1]

        # 将最后一个元素移到要删除的位置
        self.nums[index_to_remove] = last_val
        self.val_to_index[last_val] = index_to_remove

        # 删除最后一个元素
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # 随机返回一个元素
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
