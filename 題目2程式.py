# -*- coding: utf-8 -*-
"""
#國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，請寫一個程式計算每個字母(大小寫視為同個字母)出現次數
#作者:黃威棋
#日期：2023-08026
"""

def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1
    return letter_count

text = "Hello welcome to Cathay 60th year anniversary"
letter_counts = count_letters(text)

for letter, count in letter_counts.items():
    print(f"{letter}: {count}")











