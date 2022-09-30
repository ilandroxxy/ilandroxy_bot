# Циклы
# Домашка в файле:
# - ход конем не получилось?
# - как додумался до abs




'''
a = int(input('a: '))
print('Цифра в позиции десятков тысяч равна', a // 10000)
print('Цифра в позиции тысяч равна', (a // 1000) % 10 )
print('Цифра в позиции сотен равна', ((a // 100) % 100) % 10 )
print('Цифра в позиции десятков равна', ((a // 10)% 100) % 10 )
print('Цифра в позиции единиц равна', a % 10)
'''

"""
a = int(input('a: '))
a = str(a)
print('Цифра в позиции десятков тысяч равна', int(a[0]))
print('Цифра в позиции тысяч равна', a[1])
print('Цифра в позиции сотен равна', a[2])
print('Цифра в позиции десятков равна', a[3])
print('Цифра в позиции единиц равна', a[4])
"""


'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a > b > c or a < b < c:
    print(b)
elif b > a > c or b < a < c:
    print(a)
elif a > c > b or a < c < b:
    print(c)
else:
    print('Некоторые из чисел равны')
'''

'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print((a + b + c) - max(a, b, c) - min(a, b, c))
'''


'''
a = int(input('a: '))
if 0 < a <= 60:
    print('Легкий вес')
elif 60 < a <= 64:
    print('Первый полусредний вес')
elif 64 < a <= 69:
    print('Полусредний вес')
'''

'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

f1 = abs(x1 - x2)
f2 = abs(y1 - y2)
if f1 == 1 and f2 == 2:
    print('YES')
elif f1 == 2 and f2 == 1:
    print('YES')
elif x1 == x2 and y1 == y2:
    print('Надо обязательно походить')
else:
    print('NO')
'''

# Библиотеки в Пайтон

#import math
#print(math.fabs(4-7))

#import math as myname
#print(myname.fabs(6-8))

#from math import *
#print(fabs(3-7))

#from math import fabs, sqrt
#print(fabs(4-9))

# import math - математические функции
# import random - методы для радомайзеров
# import datatime - методы для работы с временем
# import sqlite3 - методы для работы с SQL запросами (базы данных)



# Циклы
# 1. Повторяющиеся действие n раз, 2. повторяющееся действие при условии,
# 3. Повторяющееся действие в пробежке от n до m, 4. бесконечный цикл

# Ключевые слова: while, for, break, continue, flag


# Цикл for с индексацией
'''
n = 5
for i in range(n):  # [0, n)
    print(i)

for i in range(2, 10):  # [2, 10)
    print(i)

for i in range(2, 10, 2):  # [2, 10)
    print(i)

for i in range(2, 10+1, 2):  # [2, 10]
    print(i)

for i in range(10, 2-1, -1):  # [10, 2] в убывающем порядке
    print(i)

for i in range(0, 10000000,100000):
    print(i)
'''

# Простой for для прохода по элементам
'''
M = [3, 4, 5, 6, 7]
#    0  1  2  3  4
# print(M[1])

for i in range(0, len(M)):  # [0, 5)
    print(M[i], end=" ")
print()

for x in M:   # такой for пробегает все элементы
    print(x, end=" ")
'''



# while
'''
for i in range(0, 10+1, 2):  # [0, 10] или [0, 11)
    print(i)
# range(START, STOP, STEP)


i = 0   # START
while i <= 10:  # STOP
    print(i)
    i += 2  # STEP
'''

'''
a = int(input('a: '))
print('Цифра в позиции тысяч равна', a // 1000)
print('Цифра в позиции сотен равна', (a // 100) % 10, (a % 1000) // 100)
print('Цифра в позиции десятков равна', (a // 10) % 10)
print('Цифра в позиции единиц равна', a % 10)
'''

# Взять сумму цифр числа
'''
a = int(input('a: '))
summ = 0
while a > 0:
    summ += a % 10
    a = a // 10
    print(a)
print('summ =', summ)
'''


# Перевод в n-ную систему счисления
'''
x = int(input("Введите десятичное число: "))
n = int(input('Введите систему счисления: '))
# Перевести x в 2-ную систему счисления
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)
'''


# Бесконечный цикл

'''
count = 0
while True:
    count += 1
    print(count)
'''

'''
import random

password = 'qwerty'
count = 0
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('welcome')
        break
    print("Пароль неверный! Попробуйте еще")
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f'Проверка на робата, решите задачку:\n'
              f'{a} + {b} = ')
        x = int(input())
        if x == a + b:
            count = 0
            continue
        else:
            print("Аккаунт заблокирован!")
            break
'''


'''
for i in range(0, 100, 2):
    print(i, end=' ')
print('  <--- Вариант 1')

for i in range(0, 100):
    if i % 2 == 0:
        print(i, end=' ')
print('  <--- Вариант 2')

for i in range(0, 100):
    if i % 2 != 0:
        continue
    print(i, end=' ')
print('  <--- Вариант 3')
'''





















