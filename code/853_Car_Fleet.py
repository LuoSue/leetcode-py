#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   853_Car_Fleet.py
@Time    :   2025/04/24 14:31:30
@Author  :   rj 
@Version :   1.0
@Desc    :   车队
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 将汽车的位置信息和速度信息组合成元组 (position, speed)，并按照位置从大到小排序
        # 这样可以确保我们从最接近终点的车开始处理
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        
        # 用一个栈来记录车队到达终点所需的时间
        # 栈中的每个元素代表一个独立车队的到达时间（从终点往回看）
        stack = []
        
        for pos, spd in cars:
            # 计算当前车辆从当前位置开到终点所需要的时间
            time = (target - pos) / spd
            
            if not stack:
                # 栈为空，当前车是第一个车队
                stack.append(time)
            else:
                # 如果当前车到达终点的时间大于栈顶（前车）时间，说明无法追上前面的车队，形成新车队
                if time > stack[-1]:
                    stack.append(time)
                # 否则当前车会追上前面的车队，加入已有车队（不入栈）

        # 栈的长度就是车队的数量
        return len(stack)
