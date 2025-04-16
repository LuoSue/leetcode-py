#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2537_Count_the_Number_of_Good_Subarrays.py
@Time    :   2025/04/16 09:40:18
@Author  :   rj 
@Version :   1.0
@Desc    :   统计好子数组的数目
"""

from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 使用哈希表记录当前窗口中每个元素的出现次数
        count = defaultdict(int)
        left = 0  # 滑动窗口的左边界
        total_pairs = 0  # 当前窗口内的相同元素对数
        result = 0  # 最终结果，即好子数组的数目
        
        for right in range(n):
            x = nums[right]
            # 新加入的元素x可以与之前所有x形成新的相同对
            # 所以total_pairs增加count[x]（即之前x的出现次数）
            total_pairs += count[x]
            # 更新x的出现次数
            count[x] += 1
            
            # 当窗口内的相同对数满足k时，尝试移动左边界以缩小窗口
            while total_pairs >= k:
                y = nums[left]
                # 移动左边界前，需要减少y的计数，并相应减少total_pairs
                # 因为y被移出窗口，所以之前与y配对的相同对会减少count[y]-1个
                count[y] -= 1
                total_pairs -= count[y]
                left += 1
            
            # 当前窗口[left, right]不满足total_pairs >= k
            # 所以所有以right结尾的子数组[left_prev, right]（left_prev < left）都满足条件
            # 共有left个这样的子数组（left_prev从0到left-1）
            result += left
        
        return result