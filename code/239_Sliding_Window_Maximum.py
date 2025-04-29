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
        # 使用双端队列来存储窗口内的索引
        dq = deque()
        # 用于存储结果的列表
        result = []
        
        # 遍历输入的数组
        for i in range(len(nums)):
            # 移除滑出窗口的元素
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # 移除队列中所有小于当前元素的索引
            # 因为这些元素不可能再成为窗口中的最大值
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # 将当前元素的索引添加到队列中
            dq.append(i)
            
            # 当i >= k - 1时，表示窗口已经形成，开始记录结果
            if i >= k - 1:
                # 队列的头部是当前窗口的最大值索引
                result.append(nums[dq[0]])
        
        # 返回结果列表
        return result
