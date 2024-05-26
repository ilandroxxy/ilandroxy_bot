# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# № 16382 ЕГКР 27.04.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n <= 3:
        return 2025
    if n > 3:
        return 3 * (n-1) * F(n-2)

print(F(2027) / F(2023))
'''
# Ответ: 36905616

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


# № 13297 Открытый курс "Слово пацана" (Уровень: Базовый)
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
        return 6 * F(n-1)+5*G(n-1) + 3

print(F(9) + G(9))
'''
# 3312821

# № 7655 Вариант от ChatGPT (Уровень: Средний)
'''
from functools import *
@lru_cache(None)
def F(n):
    if n < 2025:
        return n**2
    if 2025 <= n < 2050:
        return 2 * F(n-1) - F(n-2) + n
    if 2050 <= n <= 2100:
        return F(n-1) + 2 * F(n-2) + 3 * F(n-3)
    if n > 2100:
        return 2 * F(n-1) + F(n-2) + n

print(str(F(2020) + F(2200))[-7:])
'''
# 5098903

'''
def F(a, b):
    if a > b or a == 16:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(2, 9) * F(9, 18))


def F(a, b):
    if a >= b or a == 16:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(2, 9) * F(9, 18))
'''

'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-1, b) + F(a-2, b) + F(a//4, b)

print(F(26, 20) * F(20, 3))
'''
# Ответ: 34749


def F(x, A):
    #       ¬ДЕЛ(x, А)   → ( ДЕЛ(x, 28)   →   ¬ДЕЛ(x, 49) )
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))


for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)



# endregion Урок: ***************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Сева = [1, 2, 3, 4, 6, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25]
# КЕГЭ  = [16, 15 (без отрезков), 23]
# на следующем уроке: 8, 9, 12, 17, 24, 25
