
# region Домашка: ******************************************************************

'''
abc = int(input())
a = abc//100
b = (abc - a*100)//10
c = (abc - a*100) % 10
print(f'a: {a}, b: {b}, c: {c}')
print(f'Сумма цифр = {a+b+c}')
print(f'Произведение цифр = {a*b*c}')
'''
# Сумма цифр = 6
# Произведение цифр = 6

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Четыре типа подключения библиотек в Python
'''
import math  # самый базовый способ подключения библиотеки, но придется везде таскать название 
print(math.sqrt(16))

import math as m  # можно сократить название библиотеки - поменять ее имя
print(m.sqrt(16))  

from math import sqrt, pow  # импортируем только определенные нужные нам методы из библиотеки
print(sqrt(16))

from math import *  # оператор раскрытия * - достает все методы из библиотеки
print(sqrt(16))
'''

# Список библиотек, которые мы будем использовать на экзамене:
'''
import os
import functools

import itertools
import math
import turtle
import fnmatch
import string

print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''

# Импортируем свою библиотеку
'''
import useful

import useful as u
print(u.OrelReshka())
'''

# Условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:  # if - если
    print('Первая четверть')
elif x > 0 and y < 0:  # elif - иначе если
    print('Четвертая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
else:  # else - иначе
    print('Лежит на осях')
'''

# Каскадные условия
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


# Условные связки:
# and - все условия должны выполняться
# or - хотя бы одно из условий должно выполняться
# not - инверсия - меняет значение на противоположное
'''
flag = True
print(not flag)  # False
'''

'''
flag = True
M = []
while flag:
    x = int(input('x: '))

    if x == 0:
        flag = False
    else:
        M.append(x)
        print(M)
'''


# Мини калькулятор:
'''
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

if s == '+':
    print(f'{a} {s} {b} = {a + b}')
'''


'''
import random
import time

pas = 'qwerty'
password = input('Введите ваш пароль: ')
count = 0
while True:
    if count == 2:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        x = int(input(f'Решите пример: {a} + {b} = '))
        if x == a + b:
            print('Проверка пройдена успешна!')
            count = 0
        else:
            print('Повторите попытку через 5 минут.')
            time.sleep(5*60)

    if pas == password:
        print('Welcome!')
        break
    password = input('Неверный пароль, попробуйте снова: ')
    count += 1
'''

# endregion Урок: ******************************************************************


# todo: Марк = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
