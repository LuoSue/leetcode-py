#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   208_Implement_Trie_(Prefix_Tree).py
@Time    :   2025/05/11 15:27:50
@Author  :   rj
@Version :   1.0
@Desc    :   实现 Trie (前缀树)
"""


class TrieNode:
    def __init__(self):
        # 子节点字典，用来存储每个字符对应的子节点
        self.children = {}
        # 标记当前节点是否是一个单词的结尾
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # 初始化Trie树，根节点不存储字符，只作为起始节点
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 插入一个单词
        node = self.root
        for char in word:
            # 如果当前字符不在子节点中，则添加新的节点
            if char not in node.children:
                node.children[char] = TrieNode()
            # 移动到下一个节点
            node = node.children[char]
        # 标记最后一个字符节点为单词的结尾
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # 查找是否存在一个完全匹配的单词
        node = self._search(word)
        # 如果找到了该单词的结尾节点，则返回True，否则返回False
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # 查找是否存在以给定前缀开头的单词
        return self._search(prefix) is not None

    def _search(self, prefix: str) -> TrieNode:
        # 辅助方法，用于查找给定前缀的最后一个节点
        node = self.root  # 从根节点开始
        for char in prefix:
            # 如果当前字符不在子节点中，返回None
            if char not in node.children:
                return None
            # 移动到下一个节点
            node = node.children[char]
        # 返回前缀的最后一个节点
        return node
