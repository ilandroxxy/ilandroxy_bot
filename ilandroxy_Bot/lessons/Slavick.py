
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# x = 5   # переменные - это способ хранить данные и обращаться к ним по имени
# print(x, type(x))  # 5 <class 'int'>

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные заначения

b = 5.0  # float (число с плавающей точкой) - дроби/вещественные числа
print(7 / 2)  # 3.5

c = '5'  # str (string) - строковый тип данных для хранения символов, слов, текста
print(a * 4, c * 4)   # 20 5555
print('hello, ' + 'world!')  # hello, world!
# print('5' + 34) - TypeError: can only concatenate str (not "int") to str

d1 = True  # bool (Boolean) - Булева алгебра (Математическая логика)
d2 = False
print(4 < 10)  # Спрашиваю 4 меньше чем 10? # True
'''

# Типы данных коллекций/последовательностей
'''
A = [1, 2, 3]  # list (список)
A = []  # пустой список
# Вмещает неограниченное кол-во элементов разных типов данных
# Каждый элемент списка имеет порядковый номер - индекс
# Индексы считаются слева начиная с 0 или спарава начиная с -1
# Через индекс мы можем брать элементы списка или изменять их

B = (1, 2, 3)  # tuple (кортеж)
B = ()  # пустой кортеж
# Через индекс мы можем брать элементы списка, но менять элементы нельзя

C = {1, 2, 3}  # set (множество)
C = set()  # пустое множество
# В множествах нет повторяющихся элементов - то есть копии будут удаляться

D = {}  # пустой словарь
D = {1: 'one', 2: 'two', 3: 'three'}
# Элементы в словаре состоят из двух частей: ключ и значение
# То есть доступ к значению осуществляется по ключу
print(D[1])  # one
D[1] = 10000
print(D)  # {1: 10000, 2: 'two', 3: 'three'}
print(D.keys())   # dict_keys([1, 2, 3])
print(D.values())  # dict_values([10000, 'two', 'three'])
for key, value in D.items():
    print(key, value)
    # 1 10000
    # 2 two
    # 3 three
'''

'''
M = [2, 2.0, '2', True, 2+2, 7/2, '2' * 3, 4 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'one', 2: 'two', 3: 'three'}]
for elem in M:
    print(elem, type(elem))
    # 5 <class 'int'>
    # 2 <class 'int'>
    # 2.0 <class 'float'>
    # 2 <class 'str'>
    # True <class 'bool'>
    # 4 <class 'int'>
    # 3.5 <class 'float'>
    # 222 <class 'str'>
    # True <class 'bool'>
    # [1, 2, 3] <class 'list'>
    # (1, 2, 3) <class 'tuple'>
    # {1, 2, 3} <class 'set'>
    # {1: 'one', 2: 'two', 3: 'three'} <class 'dict'>
'''

# Конвертация типов данных
'''
a = 5
print(a, type(a))   # 5 <class 'int'>

a = str(a)
print(a, type(a))  # 5 <class 'str'>

a = float(a)
print(a, type(a))   # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>

A = [1, 2, 3, 1, 2, 3]
print(A, type(A))  # [1, 2, 3, 1, 2, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 3, 1, 2, 3) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3] <class 'list'>
'''

# Ввод данных с клавиатуры
'''
x = input('Введите: ')  # input() - ввод строки с клавиатуры
print(x, type(x))

n = int(input('Введите число: '))
print(n, type(n))
'''

# Работа с выводом функции print() через f-строки
'''
weather = 'облачно'
temperature = int(input('Введите температуру: '))
# "Сегодня облачно, а температура 24 градуса!"
print("Сегодня ", weather, ", а температура ", temperature, " градуса!")
print("Сегодня " + weather + ", а температура " + str(temperature) + " градуса!")
print("Сегодня {}, а температура {} градуса!".format(weather, temperature))
print(f"Сегодня {weather}, а температура {temperature} градуса!")
'''

# Базовая арифметика
'''
a = 7
b = 2

print(f'{a} + {b} = {a+b} \n'
      f'{a} - {b} = {a-b} \n'
      f'{a} * {b} = {a*b}')

print()  # в каждом print() есть переход на новую строку '\n'

print(f'{a} / {b} = {a/b} - вещественное деление \n'
      f'{a} // {b} = {a//b} - целочисленное деление (без округлений) \n'
      f'{a} % {b} = {a%b} - остаток от деления (от обыкновенной дроби) ')

print()

import math
print(math.sqrt(16))  # 4.0

print()

print(f'Возведите число {a} в степень {b}: {a} ** {b} = {a**b} \n'
      f'Квадратный корень от числа 16: 16 ** (1/2) = {16**(1/2)} \n'
      f'Кубический корень от числа 27: 27 ** (1/3) = {27 ** (1/3)}')
'''

chas = int(input())
minut = int(input())
interval = int(input())

chasminut = chas * 60 + minut + interval
chasitog = chasminut // 60
minutitog = chasminut % 60

if chasitog // 24 > 0:
    print(chasitog % 24, minutitog, sep=":")
    # print(chasitog - 24 * (chasitog // 24), minutitog, sep=":")
else:
    print(chasitog, minutitog, sep=":")



# endregion Урок: ******************************************************************


# todo: Славик = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
