#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   208_Implement_Trie_(Prefix_Tree).py
@Time    :   2025/05/11 15:27:50
@Author  :   rj
@Version :   1.0
@Desc    :   实现 Trie (前缀树)
"""


class Node:
    def __init__(self):
        # 子节点字典，用来存储每个字符对应的子节点
        self.son = {}
        # 标记当前节点是否是一个单词的结尾
        self.end = False


class Trie:
    def __init__(self):
        # 初始化Trie树，根节点不存储字符，只作为起始节点
        self.root = Node()

    def insert(self, word: str) -> None:
        # 插入一个单词
        cur = self.root
        for char in word:
            # 如果当前字符不在子节点中，则添加新的节点
            if char not in cur.son:
                cur.son[char] = Node()
            # 移动到下一个节点
            cur = cur.son[char]
        # 标记最后一个字符节点为单词的结尾
        cur.end = True

    def search(self, word: str) -> bool:
        # 查找是否存在一个完全匹配的单词
        cur = self._search(word)
        # 如果找到了该单词的结尾节点，则返回True，否则返回False
        return cur is not None and cur.end

    def startsWith(self, prefix: str) -> bool:
        # 查找是否存在以给定前缀开头的单词
        return self._search(prefix) is not None

    def _search(self, prefix: str) -> Node:
        # 辅助方法，用于查找给定前缀的最后一个节点
        cur = self.root  # 从根节点开始
        for char in prefix:
            # 如果当前字符不在子节点中，返回None
            if char not in cur.son:
                return None
            # 移动到下一个节点
            cur = cur.son[char]
        # 返回前缀的最后一个节点
        return cur
