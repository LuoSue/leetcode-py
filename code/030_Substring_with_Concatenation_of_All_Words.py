#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   030_Substring_with_Concatenation_of_All_Words.py
@Time    :   2025/08/04 14:30:59
@Author  :   rj
@Version :   1.0
@Desc    :   串联所有单词的子串
"""

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 如果字符串或单词列表为空，直接返回空列表
        if not s or not words:
            return []

        word_len = len(words[0])  # 每个单词的长度（假设都相同）
        word_count = len(words)  # 单词的个数
        result = []  # 结果列表，用于存储符合要求的起始索引

        word_freq = Counter(words)  # 统计每个单词出现的频率

        # 有 word_len 种可能的起始点（从0到word_len-1），确保覆盖所有子串
        for i in range(word_len):
            left = i  # 滑动窗口左边界
            sub_freq = Counter()  # 当前窗口中的单词频率

            # 右指针每次向右移动一个单词长度
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]  # 当前扫描到的单词

                if word in word_freq:
                    sub_freq[word] += 1  # 当前窗口中该单词出现次数加1

                    # 如果某个单词的数量超过了要求，就收缩窗口直到满足条件
                    while sub_freq[word] > word_freq[word]:
                        left_word = s[left : left + word_len]
                        sub_freq[left_word] -= 1
                        left += word_len

                    # 如果当前窗口包含的单词数等于所需单词总数，则记录起始索引
                    if (right - left) // word_len + 1 == word_count:
                        result.append(left)

                        # 为了寻找下一个可能的解，继续收缩窗口
                        left_word = s[left : left + word_len]
                        sub_freq[left_word] -= 1
                        left += word_len
                else:
                    # 如果遇到的单词不在目标词中，清空窗口状态，重新开始
                    sub_freq.clear()
                    left = right + word_len

        return result
