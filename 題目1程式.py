# -*- coding: utf-8 -*-
"""
#國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]，請用一個函數來將學生的成績修正。
#作者：黃威棋
#日期:2023-08-26
"""

def fix_grades(incorrect_grades, correct_grades):
    fixed_grades = []
    for incorrect_grade in incorrect_grades:
        correct_grade = correct_grades[incorrect_grades.index(incorrect_grade)]
        fixed_grades.append(correct_grade)
    return fixed_grades

incorrect_grades = [35, 46, 57, 91, 29]
correct_grades = [53, 64, 75, 19, 92]

fixed_grades = fix_grades(incorrect_grades, correct_grades)
print(fixed_grades)











