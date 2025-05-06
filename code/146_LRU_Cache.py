#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   146_LRU_Cache.py
@Time    :   2025/05/06 11:09:13
@Author  :   rj
@Version :   1.0
@Desc    :   LRU 缓存
"""


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 哈希表，存储 key 到节点的映射
        self.head = Node()  # 哑节点，既作为头又作为尾（循环双向链表）
        self.head.prev = self.head.next = self.head

    # 将节点添加到头部（最近使用）
    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 从链表中移除节点
    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    # 获取缓存的值，如果存在则移动到头部
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # 先移除
            self._add_to_head(node)  # 再放到头部
            return node.value
        return -1  # 不存在返回 -1

    # 插入或更新缓存
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # 先移除旧节点
            node.value = value  # 更新值
            self._add_to_head(node)  # 再放到头部
        else:
            if len(self.cache) >= self.capacity:
                lru = self.head.prev  # 最近最少使用节点（尾节点）
                self._remove(lru)  # 移除它
                del self.cache[lru.key]  # 从哈希表删除
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)  # 新节点放到头部
