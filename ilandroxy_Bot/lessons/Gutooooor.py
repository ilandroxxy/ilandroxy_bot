# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
"""
x = 5  # способ обращаться к данным в памяти компьютера

# Типы данных переменных

a = 5  # int (integer) - целочисленные

b = 5.0  # float (число с плавающей точкой)

c = '5'  # str (string) - символы, слова, предложения, пунктуация..

'''
print(a + b)
print(a * 4, c * 4)
print(c + a)  # TypeError: can only concatenate str (not "int") to str
'''
d1 = True  # bool (Boolean)
d2 = False

print(4 < 10)  # True

print(a, b, c)  # 5 5.0 5
print(type(c))  # <class 'str'>
"""

# Типы данных коллекций
'''
# i  0  1  2
A = [1, 2, 3, 4, '5', True, [1, 2, 3]]  # list() - список
print(len(A))  # 7

A = list()  # список
A = []  # пустой список
print(len(A))  # 0

B = (1, 2, 3)  # tuple() - кортеж
B = ()

S = {1, 2, 3}  # set() - множество
S = set()


d = {}
print(type(d))  # <class 'dict'>
D = {1: 'one', 2: 'two', 3: 'three'}
print(D[1])  # one
'''

'''
M = [2, '2', 2.0, True, 3+4, '3' * 4, 7/2, 4 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'one', 2: 'two', 3: 'three'}]
for x in M:
    print(x, type(x))
'''

# Конвертирование типов данных
'''
a = 5
print(a, type(a))

a = str(a)
print(a, type(a))

a = float(a)
print(a, type(a))

a = int(a)
print(a, type(a))

A = [1, 2, 3, 1, 2, 3]
print(A, type(A))

A = set(A)
print(A, type(A))

A = tuple(A)
print(A, type(A))

A = list(A)
print(A, type(A))
'''


# Ввод данных с клавиатуры:

'''
name = input('Введите свое имя: ')  # функция ввода строки с клавиатуры
print(name)
'''


'''
def NOD(a, b):
    result = 1
    for j in range(1, min(a, b)+1):
        if a % j == 0 and b % j == 0:
            result = j
    return result


a = int(input('a: '))
b = int(input('b: '))
print(NOD(a, b))
'''


# Работа с текстами через print()
'''
weather = input('Какая сегодня погода?: ')
temperature = int(input('Сколько сегодня градусов?: '))
# Сегодня классная погода, wetaher, а температура 24 градуса!
print('Сегодня классная погода,', weather, ', а температура', temperature, ' градуса!')
print('Сегодня классная погода, ' + weather + ', а температура' + str(temperature) + ' градуса!')
print('Сегодня классная погода, {}, а температура {} градуса!'.format(weather, temperature))
print(f'Сегодня классная погода, {weather}, а температура {temperature} градуса!')
'''

# Поговорить про библиотеки на экзамене
'''
import math
print(math.sqrt(4))

import math as m   # самый приоритетный, потому что можно подглядывать
print(m.gcd(36, 48))

from math import gcd, sqrt
print(gcd(36, 48))

from math import *
print(fabs(-5))
'''

# Список библиотек:
'''
import math
import itertools
import functools
import sys
import turtle
import fnmatch  # 25 номер работа с масками
import string

print(string.ascii_uppercase)
'''


# Базовая арифметика
'''
a = 7
b = 2
print(f'{a} + {b} = {a+b} \n'
      f'{a} - {b} = {a-b} \n'
      f'{a} * {b} = {a*b} \n')

print(f'{a} / {b} = {a/b} - Вещественное деление\n' 
      f'{a} // {b} = {a//b} - Целочисленное деление\n'
      f'{a} % {b} = {a%b} - Остаток от деления\n')

print(f'Возведите число 2 в степень 4: {2**4}')
print(f'Возьмите квадратный корень числа 16: {16**(0.5)}')
print(f'Возьмите кубический корень числа 16: {16**(1/3)}')

m = 5
n = 4.0
print(m * n, m + n, m - n)

s = '5*'
print(s + '67')  # 5*67
print(s * 4)  # 5*5*5*5*
'''

# endregion Урок: ******************************************************************


# todo: Полина = []
# todo:  КЕГЭ  = []
# на прошлом уроке: Обсудили базовую теорию языка Пайтон: типы данных , конвертацию, ввод с клавиатуры, f-строки, библиотеки, арифметические действия
# на следующем уроке:
