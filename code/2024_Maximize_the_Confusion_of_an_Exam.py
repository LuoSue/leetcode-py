#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2024_Maximize_the_Confusion_of_an_Exam.py
@Time    :   2025/04/20 14:49:22
@Author  :   rj 
@Version :   1.0
@Desc    :   考试的最大困扰度
"""



class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        # 定义一个函数来计算最多改k个字符能得到的最长连续target字符
        def getMaxConsecutive(target: str) -> int:
            left = 0
            count = 0  # 记录需要修改的字符数
            max_length = 0
            
            # 滑动窗口
            for right in range(n):
                # 如果当前字符不是目标字符，需要修改，count加1
                if answerKey[right] != target:
                    count += 1
                
                # 如果需要修改的次数超过k，缩小窗口
                while count > k:
                    if answerKey[left] != target:
                        count -= 1
                    left += 1
                
                # 更新最大长度
                max_length = max(max_length, right - left + 1)
            
            return max_length
        
        # 分别计算全改为'T'和全改为'F'的最大长度，取较大值
        return max(getMaxConsecutive('T'), getMaxConsecutive('F'))