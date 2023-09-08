
# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************

# Поговорить про условные операторы и подключение библиотек к проекту


# Список библиотек, которые мы будем использовать на экзамене:
import math
import os
import functools
import itertools
import fnmatch
import turtle
import string


# Как подключать библиотеки?
'''
import math
print(math.sqrt(16))

import math as m   # переименовали библиотеку
print(m.sqrt(16))

from math import sqrt, pow  # импортировали только определенные методы из библиотеки
print(sqrt(16))

from math import *  # * - это оператор раскрытия, то есть мы импортируем сразу все методы из библиотеки
print(sqrt(16))



import useful
print(useful.OrelReshka())

from useful import *
print(OrelReshka())
'''


# Условные операторы - тема с ветвлениями
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:  # if - если
    print('Первая четверть ')
elif x > 0 and y < 0:  # elif - иначе если
    print('Четвертая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
else:  # else - иначе
    print('Лежит на осях')
'''

# Каскады условных операторов
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

# Логические связки:
# and - все поставленные условия должны выполняться
# not - инверсия (меняет значение логической переменной)
# or - то должно выполняться хотя бы одно из условий
'''
flag = True
print(not flag)  # False
'''

'''
M = []
while flag:
    x = int(input('x: '))

    if x == 0:
        flag = False
    else:
        M.append(x)
        print(M)
'''

'''
M = []
while True:
    x = int(input('x: '))

    if x == 0:
        break
    else:
        M.append(x)
        print(M)
'''

# Задача: найти минимальное число сумма цифр которого равна 64 и число должно быть четным
'''
for num in range(1, 110101001010101):
    summ = sum([int(i) for i in str(num) if i.isdigit()])

    if summ == 64 and num % 2 == 0:
        print(num)  # 29999998
        exit()
'''




# endregion Урок: ************************************************************


# todo: Максим = []
# на прошлом уроке:
# на следующем уроке: Поговорить про условные операторы и подключение библиотек к проекту
