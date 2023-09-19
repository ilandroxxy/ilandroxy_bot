
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Использование библиотек при подготовке

# Список библиотек, которые мы будем использовать в процессе подготовки
'''
import math
import ipaddress  # для 13-го номера
import itertools  # для 8, 24, 17, 9
import turtle  # для 6-го номера
import fnmatch  # для 25-го номера
import functools
import os  # могут пригодиться в 16-ом номере, чтобы увеличить глубину рекурсии
import string

print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''


# Как использовать и подключать библиотеки?
'''
import math  # через math. мы можем посмотреть на содержимое библиотеки, но везде придется таскать за собой math.
print(math.sqrt(16))

import math as m  # аналогичный пример, но math переименовали в m или любую другую переменную
print(m.sqrt(16))

from math import sqrt, log, factorial  # подключаем только необходимые нам функции
print(sqrt(16))

from math import *  # * - это оператор раскрытия, то есть подключаем все функции разом!
print(sqrt(16))
'''


# Что делать, если не помнишь что делает та или иная функция
'''
import math as m
print(m.factorial(5))  # 120

# 1.
# Навести курсор на функцию и зажать комбинацию клавиш (cmd) ctrl + B

# 2.
print(m.factorial.__doc__)  # Find n!. Raise a ValueError if x is negative or non-integral.

# 3.
print(help(m.factorial))
# Help on built-in function factorial in module math:
# 
# factorial(n, /)
#     Find n!.
#     
#     Raise a ValueError if x is negative or non-integral.
# 
# None
'''

# Условные операторы (ветвление): if, elif, else
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:  # if (если)
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:  # elif (иначе если) 
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else (иначе)
    print('Лежит на оси. ')
'''


# Каскадные условные операторы (вложенность)
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0 and y > 0
        print('Первая четверть')
    else:  # x > 0 and y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <= 0 and y > 0
        print('Вторая четверть')
    else:  # x <= 0 and y <= 0
        print('Третья четверть')
'''


# Условные связки: and, or, not
'''
# and - гарантирует, что все условия выполнимы

# or - хотя бы одно из условий должно выполняться

a = 7
b = -8
if a > 0 or b > 0:
    print(True)


flag = True
print(not flag)  # False (просто инверсия)

M = []
while flag:  # пока flag == True
    print(M)
    x = int(input('x: '))
    if x == 0:
        flag = False
    M.append(x)
'''

# Сачок для ловли ошибок
'''
while True:
    try:
        a = int(input('\n\na: '))
        s = input('s: ')
        b = int(input('b: '))
        if s == '+':
            print(f'{a} + {b} = {a+b}')
        elif s == '-':
            print(f'{a} - {b} ={a-b}')
        elif s == '*':
            print(f'{a} * {b} = {a*b}')
        elif s == '/':
            print(f'{a} / {b} = {a/b}')
        else:
            print('Введите корректный символ операции: +, -, *, /')
    except Exception as e:
        print(f'Поймали ошибку: {e}')
'''
# ZeroDivisionError: division by zero

# endregion Урок: ******************************************************************


# todo: Екатерина = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
