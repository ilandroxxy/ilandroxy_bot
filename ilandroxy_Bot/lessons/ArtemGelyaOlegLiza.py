
# region Домашка: ******************************************************************

# Напишите программу, в которой рассчитывается сумма
# и произведение цифр положительного трёхзначного числа.
'''
num = input()  # трёхзначное
a = int(num[0])
b = int(num[1])
c = int(num[2])
print(f'Сумма цифр числа {num}: {a + b + c}')
print(f'Произведение цифр числа {num}: {a * b * c}')
'''

'''
a, b, c = [int(x) for x in input()]
print(f'Сумма цифр числа: {a + b + c}')
print(f'Произведение цифр числа: {a * b * c}')
'''

'''
num = int(input())     # 345
a = num // 100
b = (345 // 10) % 10
c = num % 10
print(f'Сумма цифр числа: {a + b + c}')
print(f'Произведение цифр числа: {a * b * c}')
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Какие библиотеки будем использовать при подготовке
'''
import math
import turtle  # для решения 6-го номера
import ipaddress  # для решения 13-го номера
import fnmatch  # для решения 25-го номера
import os
import functools  # могут пригодиться при решении 16-го номера
import itertools  # 8, 24, 17, 9
import string

print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''


# Как правильно использовать библиотеки в Пайтон
'''
import math  # Плюсы: что через math. можно посмотреть содержимое библиотеки, придется везде тоскать с собой math.
print(math.sqrt(16))

import math as m  # По факту - мы просто переименовали библиотеку
print(m.sqrt(16))

from math import sqrt, log, pow  # подключаем только необходимые нам функции
print(sqrt(16))

from math import *  # * - это оператор раскрытия, то есть достаем сразу все функции
print(factorial(5))
'''


'''
import math as m
print(m.sqrt(16))

print(m.factorial(5))
# 1. Навести курсов на функцию и использовать сочетание клавиш (cmd) ctrl + B

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

print(print.__doc__)
'''


weather = 'облачно'
temperature = 24
print(f'Сегодня, отличная погодна, {weather}, а температура {temperature} градусов!')

# Базовая арифметика
'''
a = 7
b = 2
print(f'{a} + {b} = {a+b} \n'
      f'{a} - {b} = {a-b} \n'
      f'{a} * {b} = {a*b}')

print()  # в функции print() присутствует один символ "\n"

print(f'{a} / {b} = {a/b} - Обыкновенное вещественное деление (дроби) \n'
      f'{a} // {b} = {a//b} - Целочисленное деление, то есть взятие только целой части\n'
      f'{a} % {b} = {a%b}')

print()

print(f'Возведите число {a} в степень {b}: {a} ** {b} = {a**b} \n'
      f'Возьмем квадратный корень от 16: 16 ** (1/2) = {16 ** (1/2)} \n'
      f'Возьмем кубический корень от 27: 27 ** (1/3) = {27 ** (1/3)}')
import math as m
print(m.sqrt(16))
'''

'''
n = int(input('Введите число n: '))
if n % 2 == 0:
      print('Число четное')
else:
      print('Нечетное ')
'''

# Поиск делителей числа:
'''
num = int(input('num: '))
divisors = []
for j in range(1, num+1):
      if num % j == 0:
            divisors.append(j)
print(divisors)  # [1, 2, 3, 4, 6, 8, 12, 24]
'''

# Вводится пятизначное число и нужно разбить его на цифры
# Пример: 83587 = 8 3 5 8 7
'''
num = 83587
a = num // 10000
b = (num // 1000) % 10
c = (num % 1000) // 100
d = (num % 100) // 10
e = num % 10
print(a, b, c, d, e)
'''


# Условные операторы (ветвление): if, elif, else
'''
x = -5
y = 6

if x > 0 and y > 0:  # if (если)
      print('Первая четверть')
elif x < 0 and y > 0:
      print('Вторая четверть')
elif x < 0 and y < 0:  # elif (иначе если)
      print('Третья четверть')
elif x > 0 and y < 0:
      print('Четваря четверть')
else:  # else (иначе)
      print('Лежит на оси.')
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
    elif y < 0:
        print('Третья четверть')
    else:  
        print('Лежит на оси')
'''

# Логические связки: and, or, not
'''
a = 7
b = 7
c = -5
if a > 0 and b > 0 and c > 0:
    print(1)
elif (a > 0 or b > 0) and c > 0:
    print(2)
else:
    print(3)
'''

'''
flag = True
print(not flag)  # False

M = []
while flag:  # пока flag == True
    print(M)
    x = int(input('x: '))
    if x == 0:
        flag = False  # exit()
    M.append(x)
'''


# Соберем мини калькулятор
'''
while True:
    try:
        a = int(input('\n\na: '))
        s = input('s: ')
        b = int(input('b: '))

        if s == '+':
            print(f'{a} + {b} = {a+b}')
        elif s == '-':
            print(f'{a} - {b} = {a-b}')
        elif s == '*':
            print(f'{a} * {b} = {a*b}')
        elif s == '/':
            print(f'{a} / {b} = {a/b}')
    except Exception as e:
        print(f'Что-то пошло не так, ошибка: {e}')
'''
# ZeroDivisionError: division by zero


# endregion Урок: ******************************************************************


# todo: GOAL = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:  # Циклы и разбор 2-го номера
