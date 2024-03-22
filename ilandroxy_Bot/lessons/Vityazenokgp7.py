# region Домашка: ******************************************************************
import shlex

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Теория списков list()
# - Может хранить в себе неограниченное кол-во элементов разных типов данных
# - Каждый элемент имеет порядковый номер - индекс
# - Индексы мы можем считать слева-направо с 0 или справа-налево с -1
# - Элементы списка можно изменять и удалять через индексы

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

# Работа с списками через циклы
'''
for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']


for x in M:  # перебор напрямую
    print(x, end=' ')  # a b c d e
print()


A = [1, 2, 1, 2, 1, 23, 13, 13, 21, 321, 23, 12, 32, 3]
for x in A:
    if x % 2 == 0:
        print(x, end=' ')  # 2 2 12 32
print()
'''


# Срезы элементов списка
# START STOP STEP
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0])  # a
print(M[2:4])  # ['c', 'd']
print(M[:4])  # ['a', 'b', 'c', 'd']
print(M[2:])  # ['c', 'd', 'e']
print(M[:])  # ['a', 'b', 'c', 'd', 'e']
print(M[::])  # ['a', 'b', 'c', 'd', 'e']
print(M[0::2])  # ['a', 'c', 'e']  - все элементы на четных индексах
print(M[1::2])  # ['b', 'd'] - все элементы на нечетных индексах
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a'] - в обратном порядке (аналог .reverse)

# Такие срезы часто встречаются в 5 номерах
print(M[2:])  # начиная со второго по индексы (то есть с 3-го) или все элементы кроме первых двух
print(M[-2:])  # последние два элементы 
print(M[:-2])  # все элементы кроме последних двух
'''

# i  0  1  2  3  4  5
M = [1, 2, 3, 4, 5, 5]

# Функции списков
'''
print(len(M))  # кол-во элементов 6
print(sum(M))  # сумма элементов 20
print(max(M))
print(min(M))
print(set(M))  # {1, 2, 3, 4, 5} - убирает копии элементов
print(sorted(M))  # [1, 2, 3, 4, 5, 5] - по возрастанию
print(sorted(M, reverse=True))  # [5, 5, 4, 3, 2, 1]  # по убыванию
'''

# Методы списков (методы это частный случай функции для типа данных)
'''
M.append(8)  # - добавление нового элемента в конец списка
M.append(9)
# M += [8, 9]  # справа добавить несколько элементов
# M = [8, 9] + M  # слева добавить несколько элементов
print(M)  # [1, 2, 3, 4, 5, 5, 8, 9]


# Метод .reverse() изменяет порядок элементов в списке на обратный. Пример: 
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Вывод: [4, 3, 2, 1]

# Можно записать по другому через срез:
my_list = [1, 2, 3, 4]
my_list = my_list[::-1]
print(my_list)  # Вывод: [4, 3, 2, 1]


# Метод .count() возвращает количество вхождений заданного элемента в список. Пример:
my_list = [1, 2, 2, 3, 4, 2]
count_of_twos = my_list.count(2)
print(count_of_twos)  # Вывод: 3


# Метод .remove() удаляет первое вхождение указанного элемента из списка. Пример:
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)  # первая найденная двойка
print(my_list)  # Вывод: [1, 3, 2, 4]

# Можно удалить элемент через его индекс используя del:
my_list = [1, 2, 3, 2, 4]
del my_list[1]  # индекс удаляемого элемента
print(my_list)  # Вывод: [1, 3, 2, 4]


# Метод .index() возвращает индекс первого вхождения заданного элемента в списке. Пример:
my_list = [1, 2, 3, 2, 4]
index_of_two = my_list.index(2)
print(index_of_two)  # Вывод: 1


# Метод .sort() сортирует элементы списка по возрастанию (по умолчанию) 
# или в обратном порядке, если передан аргумент reverse=True. Пример:
my_list = [4, 1, 3, 2]
my_list.sort()
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list.sort(reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]


# Скажу честно я не любитель этого метода, считаю, что удобнее будет использовать функцию sorted():
my_list = [4, 1, 3, 2]
my_list = sorted(my_list)
print(my_list)  # Вывод: [1, 2, 3, 4]

my_list = sorted(my_list, reverse=True)
print(my_list)  # Вывод: [4, 3, 2, 1]
'''


# Генераторы списков (списочные выражения)
"""
print([x for x in range(0, 10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([x for x in range(0, 10, 2)])  # [0, 2, 4, 6, 8]

print([x for x in range(0, 10) if x % 2 == 0])  # [0, 2, 4, 6, 8]

print([x ** 2 for x in range(0, 10) if x % 2 == 0])  # [0, 4, 16, 36, 64]

# Заполнить список числами с клавиатуры:
'''
M = []
n = int(input('Введите длину списка М: '))
for _ in range(n):
    x = int(input('x: '))
    M.append(x)
print(M)
'''

print([int(x) for x in input('Введите числа через пробел: ').split()])
"""

'''
# Считывание файла для 17 номера:
M = [int(x) for x in open('17.txt')]
print(M)

# Считывание файла для 9 номера:

for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    print(M)
'''


# Тип 24 №59847
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых пара символов W встречается ровно 100 раз.
'''
s = open('24.txt').readline().split('WW')
maxi = 0
for i in range(len(s)-100):
    r = 'WW'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''

# Строки почти полностью аналогичны спискам, но менять элементы строки нельзя

# Срезы - полностью аналогичны спискам
'''
s = 'abcde'

for i in range(len(s)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(s[i], end=' ')  # a b c d e
print()

for x in s:  # перебор напрямую
    print(x, end=' ')  # a b c d e
print()


A = '1321323123312412412341'
for x in A:
    if x in '02468':
        print(x, end=' ')  # 2 2 2 2 4 2 4 2 4 
print()
'''

# Функции строк
'''
s = '21312313'
print(len(s))  # 8
print(max(s))  # 3
print(min(s))  # 1
print(set(s))  # {'1', '2', '3'}
print(len(set(s)))  # 3 - кол-во различных элементов строки

print(sorted(s))  # ['1', '1', '1', '2', '2', '3', '3', '3']
print(sorted(s, reverse=True))  # ['3', '3', '3', '2', '2', '1', '1', '1']

print(len('-100'))  # 4
'''

# Методы строк:
'''
s = 'abcdaea'

print(s.count('a'))  # 3
print(s.index('a'))  # 0 - индекс вхождения первого найденного
print(s.rindex('a'))  # 6 - индекс вхождения последнего найденного

s = s.replace('a', '*')  # заменили все 'a' на '*'
print(s)  # *bcd*e*

s = s.replace('*', 'a', 2)  # заменили 'a' на '*' первые два найденных
print(s)  # abcdae*

for x in 'uy21g31yu2g3':
    # if x.isdigit():
    #     print(x, end=' ')  # 2 1 3 1 2 3
    if x.isalpha():
        print(x, end=' ')  # u y g y u g
print()

ip = '192.12.43.19'
print(ip.split('.'))  # ['192', '12', '43', '19']

print([int(x) for x in ip.split('.')])  # [192, 12, 43, 19]

IP = ip.split('.')   # ['192', '12', '43', '19']
NEW_IP = ','.join(IP)  
print(NEW_IP)  # 192,12,43,19
'''
# endregion Урок: **********************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Михаил = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
