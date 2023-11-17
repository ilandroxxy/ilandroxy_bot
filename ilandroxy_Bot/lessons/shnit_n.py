# region Домашка: ************************************************************

# КЕГЭ № 8158 /dev/inf 05.23 (Уровень: Базовый) (А. Рогов)
# Операнды арифметического выражения записаны в системе счисления с основанием 15.
#
# 1x51_15 − 3x2_15
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
# Определите наибольшее значение x, при котором значение данного выражения кратно 4.
# Для найденного x вычислите частное от деления данного выражения на 4
# и запишите его в ответе в десятичной системе счисления.
# Основание системы счисления указывать не нужно.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[14:0:-1]:
    A = int(f'1{x}51', 15)
    B = int(f'3{x}2', 15)
    if (A - B) % 4 == 0:
        print((A - B) // 4)
        break
'''


# КЕГЭ № 5632 (Уровень: Средний) (М. Ишимов)
#
# Операнды арифметического выражения записаны в системе счисления с основанием 21.
#
# 32yxA_21 + 16y18_21
#
# В записи чисел переменными х и у обозначены две неизвестные цифры из алфавита 21-ричной системы счисления.
# Определите наименьшее значение х, при котором значение данного арифметического выражения кратно 12
# при любом нечётном значении у. Для найденного значения х вычислите частное от деления значения
# арифметического выражения на 12 при у = 7 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:21]:
    flag = True
    for y in alphabet[1:21:2]:
        if (int(f'32{y}{x}A', 21) + int(f'16{y}18', 21)) % 12 != 0:
            flag = False
            break
    if flag == True:
        print((int(f'32{7}{x}A', 21) + int(f'16{7}18', 21)) // 12)
        break
'''
# Ответ: 71524

# endregion Домашка: ************************************************************

# region Урок: ************************************************************


# Оформление выводов в консоль через функцию print() и f-строку
# "Сегодня облачно, а температура 24 градуса!"
'''
weather = 'облачно'
temperature = int(input('Введите температуру: '))
print("Сегодня ", weather, ", а температура ", temperature, " градуса!")
print("Сегодня " + weather + ", а температура " + str(temperature) + " градуса!")
print("Сегодня {}, а температура {} градуса!".format(weather, temperature))
print(f"Сегодня {weather}, а температура {temperature} градуса!")
'''
# TypeError: can only concatenate str (not "int") to str


# Тип коллекций в Пайтон: списки list()
# - В списке может храниться неограниченное кол-во элементов разных типов данных
# - Все элементы списка имеют свой порядковый номер: индексы
# - Индексы считаются слева-направо начиная с 0 или срава-налево начиная с -1
# - Элеметы списка можно изменять через их индексы

'''
# i         0    1    2    3    4
M: list = ['a', 'b', 'c', 'd', 'e']
# -i       -5   -4   -3   -2   -1

print(f'Первый элемент списка: {M[0]} \n'
      f'Последний элемент списка: {M[-1]}')

# Первый элемент списка: a
# Последний элемент списка: e

# Меням элементы через их индексы
M[1] = 'B'
M[-2] = 'D'
print(M)   # ['a', 'B', 'c', 'D', 'e']
'''

# Срезы списков и строк
'''
# i         0    1    2    3    4
M: list = ['a', 'b', 'c', 'd', 'e']

print(M[1:3])   # ['b', 'c']
print(M[:3])  # ['a', 'b', 'c']
print(M[2:])  # ['c', 'd', 'e']
print(M[:])  # ['a', 'b', 'c', 'd', 'e']
print(M[::2])  # ['a', 'c', 'e']
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a']

# i  01234
s = 'abcde'
print(s[1:3])   # bc
print(s[:3])  # abc
print(s[2:])  # cde
print(s[:])  # abcde
print(s[::2])  # ace
print(s[::-1])  # edcba
'''

# Функции строк и списков
'''
M = [1, 5, 6, 4, 7, 5]
print(len(M))   # 6 - функция len() возвращает длину списка / строки (то есть кол-во элементов)
print(sum(M))  # 28 - выводит сумму элементов списка (со строкой не работает)
print(max(M))  # 7 - выводит максимальный элемент
print(min(M))  # 1 - выводит минимальный элемент

print(set(M))  # {1, 4, 5, 6, 7}
# множество - не может хранить копий элементов

print(sorted(M))  # [1, 4, 5, 5, 6, 7]
print(sorted(M, reverse=True))  # [7, 6, 5, 5, 4, 1]

s = '67234abcd'
print(sorted(s))  # ['2', '3', '4', '6', '7', 'a', 'b', 'c', 'd']
'''

# Методы списков (это частный случай функций, но для одного определенного объекта)
'''
M = [1, 5, 6, 4, 7, 5]

print(M.count(5))  # 2 - возвращает кол-во вхождений элемента в список
print(M.index(5))  # 1 - возвращает индекс первого найденного элемента

M.append(8)  # добавить элемент в конец списка
M.append(9)
print(M)  # [1, 5, 6, 4, 7, 5, 8, 9]

M.sort()
print(M)    # [1, 4, 5, 5, 6, 7, 8, 9]

M.reverse()
print(M)  # [9, 8, 7, 6, 5, 5, 4, 1]
'''

# Методы строк
'''
s = '23123123123123'

print(s.count('2'))
print(s.index('2'))
print(s.rindex('2'))  # 12 - выводить индекс последнего найденного элемента


s = s.replace('2', '*')
print(s)  # *31*31*31*31*3
s = s.replace('*', '2', 3)
print(s)  # 231231231*31*3

for x in '2312uih32u1i3':
    if x.isdigit():  # Работаем только с цифрами в строке
        print(x, end=' ')  # 2 3 1 2 3 2 1 3
print()

id = '193.123.56.7'
print(id.split('.'))  # ['193', '123', '56', '7']

ID = [int(x) for x in id.split('.')]
print(ID)  # [193, 123, 56, 7]

new_id = ','.join(id.split('.'))
print(new_id)  # 193,123,56,7
'''

# Генераторы списков
'''
M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x**2 for x in range(10)]
print(M)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]

import random
M = [random.randint(0, 100) for _ in range(10)]
chet = [x for x in M if x % 2 == 0]
nechet = [x for x in M if x % 2 != 0]
print(M, chet, nechet)

M = [int(x) for x in input('Введите числа через пробел: ').split() if x.isdigit()]
print(M)
# Введите числа через пробел: 123 ujhnoijio 123
# [123, 123]


# Сумма цифр строки: 
s = '12134567865'
print(sum([int(x) for x in s if x.isdigit()]))  # 48
'''

# endregion Урок: ************************************************************


# Никита = [14.1]
# КЕГЭ = []
# на следующем уроке: