#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   020_Valid_Parentheses.py
@Time    :   2025/05/12 17:36:58
@Author  :   rj 
@Version :   1.0
@Desc    :   有效的括号
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # 定义左右括号的映射关系，'#' 是哨兵字符，用于防止空栈时出错
        matching_dict = {'(': ')', '{': '}', '[': ']', '#': '#'}
        stack = []

        # 遍历字符串中的每个字符
        for c in s:
            # 如果是左括号，入栈
            if c in matching_dict:
                stack.append(c)
            else:
                # 如果是右括号，尝试弹出栈顶元素；如果栈为空，则用 '#' 代替
                top = stack.pop() if stack else '#'
                # 如果当前右括号不匹配栈顶对应的左括号，说明不合法
                if matching_dict[top] != c:
                    return False

        # 如果栈为空，说明所有括号都匹配成功
        return not stack
