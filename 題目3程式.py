#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
#請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?
#作者:黃威棋
#日期：2023-08-26
"""

def last_person_position(n):
    if n == 1:
        return 1
    else:
        return (last_person_position(n - 1) + 3 - 1) % n + 1

n = int(input("請輸入人數 n (0-100)："))

if 0 <= n <= 100:
    last_person = last_person_position(n)
    print(f"最後留下的同事是第 {last_person} 順位。")
else:
    print("請輸入有效的人數範圍。")