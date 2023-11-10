# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Работа с комментариями
'''
# - Однострочный комментарий

"""
- Многострочный комментарий
"""
# todo Не могу понять зачем нужна переменная А
'''

# region Тут задача номер 1
# тут код задачи
a = 5
# endregion Тут задача номер 1


X = 5  # переменная - это удобный способ связи данных с ячейкой памяти
print(type(X))  # <class 'int'>

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(type(2+2))  # <class 'int'>

b = 5.0  # float (число с плавающей точкой) - вещественные/дробные числа
print(7 / 2)   # 3.5
print(4 / 2)   # 2.0

c = '5'  # str (string) - строчный тип данных, хранит в себе: символы, слова, текста и тд
print(a * 4, c * 4)  # 20 5555  # строчка при умножении на целое число - дублируется

d1 = True  # bool (Boolean)
d2 = False
print(4 < 10)  # True - 4 меньше чем 10? 
'''

# Типы данных коллекций (последовательностей)
'''
A = [1, 2, 3]  # list (Список)
# Списки хранят неограниченное кол-во элементов, разных типов данных
# Каждый элемент списка имеет порядковый номер - индекс
# Индексы могут считаться слева-направо начиная с 0 или справа-налево начиная с -1
# В списках можно менять элементы через индексы

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка: {M[0]} \n'
      f'Последний элемент списка: {M[-1]}')
# Первый элемент списка: a
# Последний элемент списка: e


B = (1, 2, 3)  # tuple (Кортеж)
# Полностью идентичны спискам, кроме: менять элементы кортежа нельзя

C = {1, 2, 3, 2, 3}  # set (Множество)
# В множестве все элементы различны - копии удаляются
print(C)  # {1, 2, 3}
# Запись 122233 содержит три различные цифры: 1, 2 и 3.
print(len(set('122233')))  # 3

D = {'один': 'one', 'два': 'two', 'три': 'three'}  # dict (Словарь)
# Элементы словаря состоят из двух частей: ключ и значение элемента
# Доступ к значению элемента осуществляется через ключ

print(D['один'])  # one
D['два'] = 2
print(D)  # {'один': 'one', 'два': 2, 'три': 'three'}
print(D.keys())  # dict_keys(['один', 'два', 'три'])
print(D.values())  # dict_values(['one', 2, 'three'])
for key, value in D.items():
    print(key, value)
    # один one
    # два 2
    # три three
'''

# Конвертация типов данных
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)
print(a, type(a))  # 5 <class 'str'>
# ValueError: invalid literal for int() with base 10: '5.0'

a = float(a)
print(a, type(a))  # 5 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>

A = [1, 2, 3, 1, 2, 3]
print(A, type(A))  # [1, 2, 3, 1, 2, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 3, 1, 2, 3) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)  # [1, 2, 3] <class 'list'>
print(A, type(A))
'''

# Ввод данных с клавиатуры
'''
a = input('Введите: ')
print(a, type(a))  # <class 'str'>

x = int(input('Введите целое число: '))
print(x, type(x))  # <class 'int'>
'''

# Работа с выводом функции print() через f-строки
'''
weather = 'облачно'
temperature = int(input('Введите температуру: '))
# Сегодня облачно, а температура 24 градуса!
print("Сегодня ", weather, ", а температура ", temperature, " градуса!")
print("Сегодня " + weather + ", а температура " + str(temperature) + " градуса!")
print("Сегодня {}, а температура {} градуса!".format(weather, temperature))
print(f"Сегодня {weather}, а температура {temperature} градуса!")
'''

# Базовая арифметика
'''
a = 7
b = 2
print(f'{a} + {b} = {a + b} \n'
      f'{a} - {b} = {a - b} \n'
      f'{a} * {b} = {a * b}')

print()  # В любой функции print() есть переход на новую строку '\n'

print(f'{a} / {b} = {a / b} - Вещественное деление (результат всегда float)\n'
      f'{a} // {b} = {a // b} - Целочисленное деление (взятие только лишь целой части)\n'
      f'{a} % {b} = {a % b} - Остаток от деления (в виде обыкновенное дроби)')

x = 7
if x % 2 == 0:
    print('Четное ')
else:
    print('Нечетное ')

print()

import math  # встроенная библиотека с математическими формулами
print(math.sqrt(16))  # Квадратный корень числа

print(f'Возведите число {a} в степень {b}:   {a} ** {b} = {a**b} \n'
      f'Возьмите квадратный корень от числа 16:   16 ** (1/2) = {16 ** (1/2)} \n'
      f'Возьмите кубический корень от числа 27:   27 ** (1/3) = {27 ** (1/3)}')
'''

# endregion Урок: ******************************************************************


# Тимур = []
# КЕГЭ  = []
# на следующем уроке:
