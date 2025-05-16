#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   239_Sliding_Window_Maximum.py
@Time    :   2025/04/29 11:27:50
@Author  :   rj
@Version :   1.0
@Desc    :   滑动窗口最大值
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        使用双端队列高效解决滑动窗口最大值问题

        核心思路：
        1. 维护一个双端队列，存储的是数组元素的索引，且队列中的索引对应的元素是单调递减的
        2. 这样队列头部始终是当前窗口最大值的索引
        3. 每次窗口滑动时：
           - 移除滑出窗口的旧元素
           - 移除队列中所有小于新元素的元素（因为它们不可能再成为最大值）
           - 添加新元素
           - 记录当前窗口的最大值（队列头部）

        时间复杂度：O(n) - 每个元素最多进出队列一次
        空间复杂度：O(k) - 队列最多存储k个元素
        """
        # 双端队列：存储的是索引，且对应元素单调递减
        dq = deque()
        result = []

        for i in range(len(nums)):
            # 1. 移除滑出窗口的元素（从左侧）
            # 当队列头部索引等于i-k时，说明该元素已经不在当前窗口内
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2. 维护队列单调性（从右侧）
            # 移除所有小于当前元素的索引，因为它们不可能再成为最大值
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. 将当前元素索引加入队列
            dq.append(i)

            # 4. 当窗口形成时（i >= k-1），记录当前最大值
            # 队列头部始终是当前窗口最大值的索引
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
