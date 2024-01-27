# region Домашка: ******************************************************************

# КЕГЭ № 5268 (Уровень: Средний) (С. Якунин)
#
# Дмитрий составляет слова, переставляя буквы в слове АМФИБРАХИЙ.
# Сколько различных слов, содержащих ИИФАА или ААФИИ, может составить Дмитрий?
'''
from itertools import permutations
count = set()
for v in permutations('АМФИБРАХИЙ'):
    slovo = ''.join(v)
    if 'ИИФАА' in slovo or 'ААФИИ' in slovo:
        count.add(slovo)
print(len(count))
'''
# Ответ: 1440

# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************


# Тип 12 №13544
# Ниже приведена программа для исполнителя Редактор.

#     ПОКА нашлось (19) ИЛИ нашлось (299) ИЛИ нашлось (3999)
#         заменить (19, 2)
#         заменить (299, 3)
#         заменить (3999, 1)
#
# На вход этой программе подаётся строка длины 94, состоящая из цифры 3,
# за которой следуют 93 идущих подряд цифр 9.
#
# Какая строка получится в результате применения программы к этой строке?
'''
s = '3' + '9' * 93
while '19' in s or '299' in s or '3999' in s:
    s = s.replace('19', '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print(s)
'''
# Ответ: 1


# Тип 12 №46970
# Дана программа для редактора:
#
# ПОКА НЕ нашлось (00)
#     заменить (01, 210)
#     заменить (02, 3101)
#     заменить (03, 2012)

#
# Известно, что исходная строка начиналась с нуля и заканчивалась нулём,
# а между ними содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка, содержащая 70 единиц, 56 двоек и 23 тройки.
# Сколько цифр было в исходной строке?
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
                print(x+y+z+2)
'''
# Ответ: 40


# Тип 16 №4692
# Алгоритм вычисления значения функции F(n). где n — натуральное число, задан следующими соотношениями:
# F(1) = 1;
# F(n) = F(n-1) * (n+1), при n >1.
# Чему равно значение функции F(4)? В ответе запишите только натуральное число.
'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) * (n+1)

print(F(4))
'''
# Ответ: 80


# Тип 16 №39245
# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:
# F(0) = 0;
# F(n) = F(n / 2), если n > 0 и при этом чётно;
# F(n) = 1 + F(n − 1), если n нечётно.

# Сколько существует таких чисел n, что 1 ≤ n ≤ 900 и F(n) = 9?
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)


count = 0
for n in range(1, 900):
    if F(n) == 9:
        count += 1
print(count)
'''
# Ответ: 3


# Тип 16 №4656
# Алгоритм вычисления значения функции F(n) и G(n),
# где n – натуральное число, задан следующими соотношениями:
#
# F(1) = 0
# F(n) = F(n–1) + n, при n >1
#
# G(1) = 1
# G(n) = G(n–1) * n, при n >1
#
# Чему равно значение функции F(5) + G(5)?
# В ответе запишите только натуральное число.
'''
def F(n):
    if n == 1:
        return 0
    if n > 1:
        return F(n-1) + n

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return G(n-1) * n

print(F(5) + G(5))
'''
# Ответ: 134


# Тип 16 №47220
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
# F(n)=1 при n=1;
# F(n)=n·F(n−1), если n>1.
#
# Чему равно значение выражения F(2023) / F(2020)?
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n-1)


print(F(2023) / F(2020))

# Письменное решение: 
# F(2023) = 2023 * F(2022)
# F(2022) = 2022 * F(2021)
# F(2021) = 2021 * F(2020) / F(2020)
print(2023 * 2022 * 2021)
'''


# Ответ: 8266912626

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


# Тип 23 №9808
# 1. Прибавить 1
# 2. Умножить на 2
# Сколько существует программ, для которых при исходном числе 2 результатом является число 31
# и при этом траектория вычислений содержит число 15 и не содержит числа 22?
'''
def F(a, b):  # a - старт и траектория по которой будем двигаться, а b - стоп на котором будем останавливаться
    if a > b or a == 22:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b)


print(F(2, 15) * F(15, 31))

# Вариант 2
def F(a, b):
    if a >= b or a == 22:
        return a == b
    return F(a+1, b) + F(a*2, b)


print(F(2, 15) * F(15, 31))
'''
# Ответ: 13


# Тип 23 №58224
# 1. Вычти 1;
# 2. Найди целую часть от деления на 2.

# При исходном числе 45 результатом является число 3,
# и при этом траектория вычислений содержит число 15 и не содержит 5.
# Сколько таких программ существует?
'''
def F(a, b):
    if a <= b or a == 5:
        return a == b
    return F(a-1, b) + F(a // 2, b)

print(F(45, 15) * F(15, 3))
'''
# Ответ: 170

# endregion Урок: *************************************************************


# Славик = [2.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 16.1, 23.1]
# КЕГЭ  = []
# на следующем уроке:
