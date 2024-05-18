# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 16382 ЕГКР 27.04.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

from functools import *
@lru_cache(None)
def F(n):
    if n <= 3:
        return 2025
    if n > 3:
        return 3 * (n-1) * F(n-2)

print(F(2027)/F(2023))
'''
#  [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
'''
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n < 7:
        return 7
    if n >= 7 and n % 3 != 0:
        return 5 - F(n-1)
    if n >= 7 and n % 3 == 0:
        return 3 + F(n-1)

print(F(3015))
'''

'''
def F(n):
    if n == 3:
        return 1
    if n > 3:
        return 5 * F(n-1) + 6 * G(n-1) - 3*n + 8

def G(n):
    if n == 3:
        return 1
    if n > 3:
        return 6 * F(n-1) + 5*G(n-1) + 3

print(F(9) + G(9))
'''
# Ответ: 3312821


# № 12779 (Уровень: Средний)
'''
def F(n):
    if n >= 3000:
        return n
    if n < 3000:
        return n + x + F(n+2)


for x in range(-1000, 1000):
    if F(2984) - F(2988) == 5916:
        print(x)
'''

# № 16387 ЕГКР 27.04.24 (Уровень: Базовый)
'''
def F(a, b):
    if a >= b or a == 16:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(2, 9) * F(9, 18))
'''


# № 11841 (Уровень: Базовый)
'''
def F(a, b):
    if a <= b or a == 20:
        return a == b
    return F(a-2, b) + F(a-3, b) + F(a // 5, b)


print(F(41, 10) * F(10, 5))
'''

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Тимур = [1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = [16, 23]
# на следующем уроке:
