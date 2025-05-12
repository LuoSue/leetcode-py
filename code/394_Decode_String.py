#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   394_Decode_String.py
@Time    :   2025/05/12 17:47:30
@Author  :   rj
@Version :   1.0
@Desc    :   字符串解码
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # 处理多位数字
            elif char == "[":
                # 将当前字符串和数字入栈
                stack.append(current_str)
                stack.append(current_num)
                # 重置当前字符串和数字
                current_str = ""
                current_num = 0
            elif char == "]":
                # 弹出数字和字符串，进行解码
                num = stack.pop()
                prev_str = stack.pop()
                current_str = prev_str + current_str * num  # 重复并拼接
            else:
                # 普通字符，直接添加到当前字符串
                current_str += char

        return current_str
