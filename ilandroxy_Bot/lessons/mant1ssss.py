
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

X = 5  # переменная в программирование - это способ обращаться к данными, которые мы в ней храним

# Типы данных переменных:
'''
a: int = 5  # int (integer) - целочисленные значения

b: float = 5.0  # float (число с плавающей точкой) - вещественные числа (дроби)
print(7 / 2)  # 3.5 - Питон сам понимает, какой тип данных нужно принять

c: str = '5'  # str (string) - строчный тип данных, необходим для хранения символов, букв, слов, текстов..
print(a*4, c*4)  # 20 5555
# print(c + 4)  # TypeError: can only concatenate str (not "int") to str

d1: bool = True  # bool (Boolean) - Математическая логика (СНГ) - Булева Алгебра.
d2: bool = False
print(4 < 10)  # True

print(type(d1))  # <class 'bool'> - проверить тип данных
'''

# Типы данных коллекций:
'''
A: list = [1, 2, 3]  # list - список

B: tuple = (1, 2, 3)  # tuple - кортеж

C: set = {1, 2, 3}  # set - множество (не может иметь копий числа)

D: dict = {1: 'один', 2: 'два', 3: 'три'}  # dict - словарь
print(D[2])  # 'два'
D[2] = 'ДВА'
print(D)  # {1: 'один', 2: 'ДВА', 3: 'три'}
print(D.keys())  # dict_keys([1, 2, 3])
print(D.values())  # dict_values(['один', 'ДВА', 'три'])

for key, value in D.items():
    print(key, value)

    # 1 один
    # 2 ДВА
    # 3 три
'''


'''
M = [2, 2.0, '2', True, 2+2, 7/2, '2'*4, 4<10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: 'два', 3: 'три'}]
for elem in M:
    print(elem, type(elem))

# 2 <class 'int'>
# 2.0 <class 'float'>
# 2 <class 'str'>
# True <class 'bool'>
# 4 <class 'int'>
# 3.5 <class 'float'>
# 2222 <class 'str'>
# True <class 'bool'>
# [1, 2, 3] <class 'list'>
# (1, 2, 3) <class 'tuple'>
# {1, 2, 3} <class 'set'>
# {1: 'один', 2: 'два', 3: 'три'} <class 'dict'>
'''

# Конвертация типов данных
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)  # При переводен из строк надо обращать внимание на лишние символы!
print(a, type(a))  # 5 <class 'str'>   #

a = float(a)
print(a, type(a))  # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # print(a, type(a))  # 5.0 <class 'float'>


A = [1, 2, 3, 1, 2, 3]
print(A, type(A))  # [1, 2, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 3) <class 'tuple'>

A = set(A)  # сет отбросит все повторяющиеся значения!
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3] <class 'list'>
'''


# Ввод данных с клавиатуры
'''
s = input('Введите строку: ')  # функция input() - вводит именно строку с клавиатуры
print(s, type(s))  # <class 'str'>

n = int(input('Введите число: '))
print(n, type(n))  # <class 'int'>
'''

# Работа с текстовой функцией print()
# Задача написать строчку: "Сегодня классная погода, облачно, а температура 24 градуса!"
'''
weather = 'облачно'
temperature = int(input("Введите температуру: "))
print('Сегодня классная погода,', weather, ', а температура', temperature, 'градуса!')
print('Сегодня классная погода, ' + weather + ', а температура ' + str(temperature) + ' градуса!')
print('Сегодня классная погода, {}, а температура {} градуса!'.format(weather, temperature))
print(f'Сегодня классная погода, {weather}, а температура {temperature} градуса!')
'''


# Базовая арифметика в Python:
a = 7
b = 2
print(f'{a} + {b} = {a+b}\n'
      f'{a} - {b} = {a-b}\n'
      f'{a} * {b} = {a*b}')

print()  # в любом принте есть один '\n' для перехода на новую строку

print(f'{a} / {b} = {a/b} - обычное вещественное деление (дробное)\n'
      f'{a} // {b} = {a//b} - целочисленное деление\n'
      f'{a} % {b} = {a%b} - остаток от деления (от обыкновенное дроби)')

print()

print(f'Возвести число {a} в степень {b}: {a} ** {b} = {a ** b}\n'
      f'Взять квадратный корень от 16: 16 ** (1/2) = {16 ** (1/2)}\n'
      f'Взять кубический корень от 27: 27 ** (1/3) = {27 ** (1/3)}')

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




# endregion Урок: ******************************************************************


# todo: Марк = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке: