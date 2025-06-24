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
        num_stack = []  # 存储倍数
        str_stack = []  # 存储当前字符串
        current_str = ""  # 当前构造的字符串
        num = 0  # 当前数字

        for ch in s:
            if ch.isdigit():
                # 构建多位数字
                num = num * 10 + int(ch)
            elif ch == "[":
                # 进入新一层，保存当前状态
                num_stack.append(num)
                str_stack.append(current_str)
                num = 0
                current_str = ""
            elif ch == "]":
                # 弹出栈顶，构造新的字符串
                repeat_times = num_stack.pop()
                last_str = str_stack.pop()
                current_str = last_str + current_str * repeat_times
            else:
                # 普通字母
                current_str += ch

        return current_str
