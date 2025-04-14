#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   049_Group_Anagrams.py
@Time    :   2025/04/14 22:36:00
@Author  :   rj 
@Version :   1.0
@Desc    :   字母异位词分组 - 给定一个字符串数组，将字母异位词组合在一起。
             字母异位词指字母相同，但排列不同的字符串。
"""

from typing import List


class Solution:
    """
    使用哈希表来分组字母异位词的解决方案
    
    基本思路：
    1. 字母异位词排序后会得到相同的字符串
    2. 使用这个排序后的字符串作为哈希表的键
    3. 将原始字符串存储在对应键的值列表中
    4. 最后返回哈希表中所有值列表的集合
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 创建一个空字典来存储分组结果
        # key: 排序后的字符串（字母异位词的统一标识）
        # value: 具有相同字母组成的原始字符串列表
        anagrams_set = {}
        
        # 遍历输入字符串列表中的每个字符串
        for s in strs:
            # 对当前字符串进行排序，作为字母异位词的统一标识
            # 例如："eat" -> "aet", "tea" -> "aet"
            sorted_s = ''.join(sorted(s))
            
            # 如果这个排序后的字符串不在字典中，初始化一个空列表
            if sorted_s not in anagrams_set:
                anagrams_set[sorted_s] = []
            
            # 将原始字符串添加到对应键的值列表中
            anagrams_set[sorted_s].append(s)
        
        # 返回字典中所有值列表的集合（即分组结果）
        return list(anagrams_set.values())