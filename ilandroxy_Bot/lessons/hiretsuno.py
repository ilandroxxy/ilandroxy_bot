# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# - однострочный комментарий

"""
'''
- многострочные комментарии
'''
"""

# print('Я читал сегодня "Война и мир"')

X = 5  # переменная - это способ взаимодействия с данными через их имя

# Типы данных
'''
a = 5  # int (integer) - целочисленные
print(type(6 + 4))  # <class 'int'>

b = 5.0  # float (число с плавающей точкой)
print(4 / 2)  # 2.0

c = '5'  # str (string) - хранит в себе любые символы, слова, предложения
print(a * 4, c * 4)  # 20 5555 - строки дублируются при умножении на числа

d1 = True
d2 = False  # bool  (Boolean) - Булева Алгбера (математическая логика)
print(4 < 10)  # True
'''

# Типы данных коллекций
'''
A = [1, 2, 3]  # list (список)

B = (1, 2, 3)  # tuple (кортеж)
# менять элементы нельзя

C = {1, 2, 3}  # set (множество)
# не может хранить копии элементов - удаляет копии

D = {1: 'one', '2': 'two', 3: 'three', 'список': [1, 2, 3]}  # dict (словарь)
# элементы словаря состоят из двух частей: ключ и значение
# доступ к значению осуществляется через ключ
# ключи не могут повторяться
print(D['список'])  # [1, 2, 3]
D[1] = '100'
print(D)  # {1: '100', '2': 'two', 3: 'three', 'список': [1, 2, 3]}
print(D.keys())  # dict_keys([1, '2', 3, 'список'])
print(D.values())  # dict_values(['100', 'two', 'three', [1, 2, 3]])
print(D.items())  # dict_items([(1, '100'), ('2', 'two'), (3, 'three'), ('список', [1, 2, 3])])

for key, value in D.items():
    print(key, value)
    # 1 100
    # 2 two
    # 3 three
    # список [1, 2, 3]


M = [1, '2', 5.7, True, 4+5, '4' * 4, 7/2, 4 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'one', 2: 'two', 3: 'three',}]
for elem in M:
    print(elem, type(elem))
    # 1 <class 'int'>
    # 2 <class 'str'>
    # 5.7 <class 'float'>
    # True <class 'bool'>
    # 9 <class 'int'>
    # 4444 <class 'str'>
    # 3.5 <class 'float'>
    # True <class 'bool'>
    # [1, 2, 3] <class 'list'>
    # (1, 2, 3) <class 'tuple'>
    # {1, 2, 3} <class 'set'>
    # {1: 'one', 2: 'two', 3: 'three'} <class 'dict'>
'''

# Конвертирование типов
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)
print(a, type(a))  # 5 <class 'str'>
# ValueError: invalid literal for int() with base 10: '5.0'

a = float(a)
print(a, type(a))  # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>

A = [1, 2, 3, 2, 3]
print(A, type(A))  # [1, 2, 3, 2, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 3, 2, 3) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3] <class 'list'>
'''

# Ввод данных с клавиатуры
'''
x = input('Введите символ: ')  # - ввод с клавиатуры строки
print(type(x))   # <class 'str'>

x = int(input('Введите число: '))
print(type(x))   # <class 'int'>
'''


# Работа с выводом текста и переменных в консоль через f-строки
'''
weather = 'облачно'
temperature = int(input('Введите температуру: '))
# 'Сегодня отличная погода - облачно, а температура 24 градуса!'
print('Сегодня отличная погода -', weather, ', а температура ', temperature, ' градуса!')
print('Сегодня отличная погода - ' + weather + ', а температура ' + str(temperature) + ' градуса!')
print('Сегодня отличная погода - {}, а температура {} градуса!'.format(weather, temperature))
print(f'Сегодня отличная погода - {weather}, а температура {temperature} градуса!')
'''


# Базовая арифметика
'''
a = 7
b = 2

print(f'{a} + {b} = {a+b} \n'
      f'{a} - {b} = {a-b} \n'
      f'{a} * {b} = {a*b}')

print()  # в каждом print() есть переход '\n'

print(f'{a} / {b} = {a/b} - обычное вещественное деление (его результат всегда float) \n'
      f'{a} // {b} = {a//b} - целочисленное деление (всегда int и без округлений, то есть только целая часть) \n'
      f'{a} % {b} = {a%b} - остаток от деления (от обыкновенной дроби) ')

x = 5
if x % 2 == 0:
    print('четное')
else:
    print('нечетное ')

print()

import math
print(math.sqrt(16))  # 4.0

print(f'Возведите число {a} в степень {b}: {a} ** {b} = {a**b} \n'
      f'Квадратный корень от числа 16: 16 ** (1/2) = {16 ** (1/2)} \n'
      f'Кубический корень от числа 27: 27 ** (1/3) = {27 ** (1/3)}')
'''

'''
import useful
print(useful.Who_Is_Name())
'''

# Список библиотек, который мы будем использовать при подготовки
'''
import math
import string
alphabet = string.digits + string.ascii_uppercase
print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

import turtle  # для решения 6-го номера
import fnmatch  # для решения 25-го нмоера 
import ipaddress  # для решения нового 13-го номера 
import sys  # для решения 16-го номера 
import itertools  # может пригодиться в 8, 9, 12, 24, 25
'''


# Как пользоваться библиотеками?
'''
import math  # удобно, что можно заглянуть в список функций, но неудобно, так как везде нужно таскать math
print(math.sqrt(16))

import math as m  # можно переименовать библиотеку в более короткую форму
print(m.sqrt(16))

from math import sqrt, pow, factorial  # импортировать выборочные функции
print(sqrt(16))

from math import *  # импортировать сразу все функции из библиотеки
print(factorial(5))  # 120
'''


# Условные операторы (ветвление): if, elif, else
'''
x = -5
y = 7
if x > 0 and y > 0:  # if (если)
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть ')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else (иначе)
    print('Лежит на осях')
'''

# Логические связки and, or, not
'''
flag = True
print(not flag)  # False

a = 6
b = -5
if a > 0 and b > 0:
    print('YES 1')
if a > 0 or b > 0:
    print('YES 2')
'''

# Циклы: while и for

# Цикл - некоторое повторяющееся действие

# Цикл for: "повтори n раз", "пробеги от а до б"
'''
for i in range(10):    # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):    # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')   # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):    # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):    # range(START=2, STOP=10+1-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):    # range(START=10, STOP=0+1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 \
print()

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for i in range(len(M)):  # len() - функция возвращающая длину списка (кол-во элементов в нем)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e

s = 'abcde'
for i in range(len(s)):
    print(s[i], end=' ')  # a b c d e
print()

# В списках можно менять элементы через индексы, а в строках нет:

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1
s = 'abcde'

for x in M:  # если хотим просто пробежать элементы
    print(x, end=' ')
print()

import random
A = [random.randint(0, 100) for _ in range(10)]

for x in A:
    if x % 2 == 0:
        print(x, end=' ')
print()
'''


# Цикл while: "пока условие верно, делай", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()
'''


# Перевод из 10-ной в n-ную систему счисления
'''
x = int(input('x: '))
n = int(input('n: '))
M = []
while x > 0:
    M.append(x % n)
    x //= n
# M.reverse()
M = M[::-1]
print(M)
'''

'''
k = 1
while True:
    k += 1
    print(k)
'''

'''
import random
import time

answer = ['Пароль неверный, попробуйте снова: ',
          'Неверный пароль, попробуйте снова: ',
          'Пароль неверен, повторите попытку: ']

pas = 'qwerty'
password = input('Введите пароль для проверки: ')
count = 1
while True:
    if pas == password:
        print('Welcome! ')
        break
    password = input(f'{random.choice(answer)}')
    count += 1
    if count == 3:
        print('Подозрительная попытка входа, пройдите проверку на робота ')
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка успешно пройдена')
        else:
            print('Повторите попытку через 5 минут')
            time.sleep(5 * 60)
'''


# endregion Урок: ******************************************************************


# todo: Дарья = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
