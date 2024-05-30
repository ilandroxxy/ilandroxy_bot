# region Домашка: ************************************************************


# endregion Домашка: *********************************************************


# region Урок: ************************************************************

# Циклы for и while в python:


# Цикл for отвечает за запросы: "повтори n раз", "пробеги от числа a до b"
# Циклы for при работе с функцией range()
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 - четные
print()

for i in range(1, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 1 3 5 7 9 - нечетные
print()

for i in range(3, 10, 3):  # range(START=2, STOP=10-1, STEP=3)
    print(i, end=' ')  # 3 6 9 - кратные 3
print()

# n = int(input())
# for i in range(n, 109, n):  # range(START=2, STOP=10-1, STEP=3)
#     print(i, end=' ')  # кратные n
# print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10 - четные
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1 0 перебор в обратном порядке
print()
'''


# Работа цикла for с списками/кортежами:
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(M[0])  # a
print(M[1])  # b
print(len(M))  # Возвращает длину списка - 5

# пробегаем элементы списка через их индексы
for i in range(len(M)):  # range(START=0, STOP=5-1, STEP=1)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

# пробегаем элементы списка напрямую
for x in M:
    print(x, end=' ')  # a b c d e
print()

# пробегаем элементы списка напрямую, которые являются гласными
for x in M:
    if x in 'ae':
        print(x, end=' ')  # a e 
print() 

# пробегаем элементы списка через их индексы и меняем их
for i in range(len(M)):
    M[i] = M[i] * i
    print(i, M[i], M)
    # 0  ['', 'b', 'c', 'd', 'e']
    # 1 b ['', 'b', 'c', 'd', 'e']
    # 2 cc ['', 'b', 'cc', 'd', 'e']
    # 3 ddd ['', 'b', 'cc', 'ddd', 'e']
    # 4 eeee ['', 'b', 'cc', 'ddd', 'eeee']
# ['', 'b', 'cc', 'ddd', 'eeee']
'''


# Цикл while отвечает за запросы: "повторяй, пока условие верно", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2  # START
while i <= 10:  # STOP
    print(i, end=' ')  # 2 5 6 8 10
    i += 2  # STEP
'''

# Переводы в base-ую систему счисления
'''
x = 8
R = []
while x > 0:
    R.append(x % 2)
    x //= 2
R.reverse()
print(R)  # [1, 0, 0, 0]
'''


# № 6021 ФИПИ 03.02.23 (Уровень: Базовый) Значение арифметического выражения
'''
x = 5 * 216**155 + 4 * 36**156 - 4 * 6**157 - 2023
base = 6
R = []  # Это создание пустого списка
while x > 0:
    R.append(x % base)  # .append() - добавляем новый элемент в конец списка R
    x //= base
R.reverse()  # .reverse() - разворачиваем элементы списка
print(R.count(0))  # .count() - возвращает кол-во вхождений элемента в список

x = 5 * 216**155 + 4 * 36**156 - 4 * 6**157 - 2023
R = []
while x > 0:
    R.append(x % 6)
    x //= 6
print(R.count(0))
'''

# Примитивная программа перевода в base систему счисления
'''
x = int(input('Введите число для перевода в base систему счисления: '))
base = int(input('Введите систему счисления base: '))
R = []
while x > 0:
    R.append(x % base)
    x //= base
R.reverse()
print(R)  # [1, 0, 0, 0]


x = int(input('Введите число для перевода в base систему счисления: '))
base = int(input('Введите систему счисления base: '))
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
r = ''
while x > 0:
    r += alphabet[x % base]
    x //= base
r = r[::-1]
print(r)  # 1000

'''
# [7, 4, 13, 3, 8, 24, 16, 9] -> 74D38OG9


# Бесконечный цикл необходим для создания консольных программ
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

while True:
    case = input('\n\ncase 1: Перевод из 10-ой в base систему счисления\n'
                 'case 2: \n'
                 'case 3: \n'
                 'case 0: exit \n'
                 'case: ')

    if case == '0':
        break

    elif case == '1':
        x = int(input('Введите число для перевода в base систему счисления: '))
        old_x = x
        base = int(input('Введите систему счисления base: '))
        r = ''
        while x > 0:
            r += alphabet[x % base]
            x //= base
        r = r[::-1]
        print(f'Число {old_x} перевели в {base}-ую систему счисления и получили: {r}')
'''


# Пример решения базового 25 номера ЕГЭ
'''
from fnmatch import *
for x in range(98591, 10**10, 98591):
    if fnmatch(str(x), '5?2*3?3?'):
        print(x)
        # 52253230
        # 5024493133
        # 5125253135
        # 5226013137
        # 5326773139
        # 5524053730
        # 5624813732
        # 5725573734
        # 5826333736
        # 5927093738

print(type('5?2*3?3?'))  # <class 'str'>
'''
# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************

# Герман = []
# КЕГЭ = []
# на следующем уроке:
