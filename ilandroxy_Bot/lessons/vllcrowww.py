# region Домашка: ******************************************************************
'''
import turtle as t
t.left(90)
t.speed(100)
l = 40

t.forward(120 * l)

for i in range(8):
    t.forward(4 * l)
    t.right(60)
t.up()
for x in range(0, 15):
    for y in range(-7, 12):
        t.goto(x * l, y * l)
        t.dot(3, 'red')
t.done()
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип коллекции список list()
# - Содержат в себе неограниченное кол-во элементов разных типов данных
# - У каждого элемента списка есть свой порядковый номер - индекс
# - Индексы могут считаться слева-направо начиная с 0 или справа-налево начиная с -1
# - Элементы списков можно изменять через их индексы (в отличие от строк и кортежей)
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']  # list - список 
T = ('a', 'b', 'c', 'd', 'e')  # tuple - кортеж
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка: {M[0]} \n'
      f'Последний элемент списка: {M[-1]}')
'''


# Как можно взаимодействовать со списками через циклы
'''
for x in M:  # Просто пробегаем каждый элемент списка
    print(x, end=' ')
print()

for i in range(len(M)):   # [0, 5-1]
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    if M[i] in 'ae':
        M[i] = M[i].upper()  # Гласные буквы сделать большими 
print(M)  # ['A', 'b', 'c', 'd', 'E']
'''

# Срезы списков (строк/кортежей)
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

print(M[1:3])  # ['b', 'c']
print(M[:3])  # ['a', 'b', 'c']
print(M[2:])  # ['c', 'd', 'e']
print(M[::2])  # ['a', 'c', 'e']
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a'] аналог метода .reverse()

s = 'abcde'
print(s[::-1])  # edcba
'''

# Функции списков
'''
M = [2, 4, 2, 6, 7, 1]

print(len(M))  # 6 - возвращает длину списка (кол-во элементов)
print(sum(M))  # 22 - возвращает сумму элементов списка (но элементы должны быть числами)
print(max(M))  # 7
print(min(M))  # 1

print(set(M))  # {1, 2, 4, 6, 7}
print(len(set(M)))  # 5 - "Все элементы должны быть различны", "Сколько различных элементов в списке"

print(sorted(M))  # [1, 2, 2, 4, 6, 7]  - аналог метода .sort
print(sorted(M, reverse=True))  # [7, 6, 4, 2, 2, 1]

s = '0123456789DBCA'
print(sorted(s))  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D']
'''


# Методы списков (Методы - это частный случай функций, методы работают с определенным типом данных)
'''
M = [2, 4, 2, 6, 7, 1]

print(M.count(2))  # 2 - Возвращает кол-во вхождений элемента в список
print(M.index(2))  # 0 - Возвращает индекс первого вхождения элемента

M.append(8)  # Добавляет один элемент в конец списка
print(M)  # [2, 4, 2, 6, 7, 1, 8]

M = M + [9, 10, 11]
print(M)  # [2, 4, 2, 6, 7, 1, 8, 9, 10, 11]

M = [-1, -2, 0] + M
print(M)  # [-1, -2, 0, 2, 4, 2, 6, 7, 1, 8, 9, 10, 11]

M.sort()
print(M)  # [-2, -1, 0, 1, 2, 2, 4, 6, 7, 8, 9, 10, 11]

M.reverse()  # Просто развернули элементы списка 
print(M)  # [11, 10, 9, 8, 7, 6, 4, 2, 2, 1, 0, -1, -2]
'''

# Функции строк
'''
s = '242671'

print(len(s))  # 6 - возвращает длину списка (кол-во элементов)
print(max(s))  # 7
print(min(s))  # 1

print(set(s))  # {'2', '4', '1', '6', '7'}
print(len(set(s)))  # 5 - "Все элементы должны быть различны", "Сколько различных элементов"

print(sorted(s))  # ['1', '2', '2', '4', '6', '7']
print(sorted(s, reverse=True))  # ['7', '6', '4', '2', '2', '1']
'''

# Методы строк
'''
s = '2426712728'

print(s.count('2'))
print(s.index('2'))
print(s.rindex('2'))  # 8 - выводит правый крайний элемент строки

s = s.replace('2', '*')  # Заменил все двойки на *
print(s)  # *4*671*7*8

s = s.replace('*', '2', 2)  # Заменил две первые * на двойки (слева-направо)
print(s)  # 242671*7*8

s = 'dfhjg324fedgkj324'
alpha = []
digit = []
for x in s:
    if x.isalpha():
        alpha.append(x.upper())
    elif x.isdigit():
        digit.append(int(x))
print(digit, alpha)

ip = '240.23.67.9'
print(ip.split('.'))  # ['240', '23', '67', '9']

IP = [int(x) for x in ip.split('.')]
print(IP)  # [240, 23, 67, 9]

old_ip = ip.split('.')
new_ip = ','.join(old_ip)
print(new_ip)  # '240,23,67,9'
'''

# Генераторы списков
'''
M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x**2 for x in range(10)]
print(M)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]

# Найдите сумму цифр строки s = 'ewkle23k23123j4'
print(sum([int(x) for x in 'ewkle23k23123j4' if x.isdigit()]))  # 20


# Введите список целых чисел с клавиатуры
M = [int(x) for x in input('Введите числа через пробел: ').split() if x.isdigit()]
print(M)
# Введите числа через пробел: jhuih 234 234 327887         1238721              129308
# [234, 234, 327887, 1238721, 129308]
'''

# endregion Урок: ******************************************************************


# Марго = [2.1, 6.1]
# КЕГЭ  = []
# на следующем уроке:
