import useful as u
# print(u.OrelReshka())
# region Домашка: ************************************************************

# Тип 14 № 27385
# Сколько различных цифр содержит эта запись?
'''
x = 343**5 + 343**4 + 49**6 - 7**13 - 21
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M)
print(len(set(M)))
'''
# Ответ: 4


# Тип 14 № 38589
'''
x = 3 * 4**38 + 2 * 4**23 + 4**20 + 3 * 4**5 + 2 * 4 ** 4 + 1
M = []
while x > 0:
    M.append(x % 16)
    x //= 16
M.reverse()
print(M.count(0))
'''
# Ответ: 15


# Тип 16 № 6459
# Алгоритм вычисления значения функции F(n),
# где n — натуральное число, задан следующими соотношениями:
#
# F(n) = 2 при n ≤ 2;
# F(n) = 3 × F(n − 1) − F(n − 2) при n> 2.
'''
def F(n):
    if n <= 2:
        return 2
    if n > 2:
        return 3 * F(n - 1) - F(n - 2)

print(F(6))
'''
# Ответ: 68


# Тип 25 № 55821
'''
from fnmatch import *
for x in range(273, 10 ** 8, 273):
    if fnmatch(str(x), "12??36*1"):
        print(x, x//273)
'''
# Ответ:
# 1271361 4657
# 12633621 46277
# 12663651 46387
# 12693681 46497


# Тип 23 № 40739
'''
def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(1, 8) * F(8, 15))
'''
# Ответ: 651

# endregion Домашка: ************************************************************


# region Урок: ************************************************************

# Теория циклов в языке Python (for, while)
# Повтори n раз, Повтори пока выполняется условие, Бесконечные циклы

# Цикл for: Повтори n раз
'''
for i in range(10+1):  # range() - функция диапазона, бежим от START до STOP с шагом STEP
    print(i, end=' ')  # range(START = 0, STOP = 10-1, STEP = 1)
print()

for i in range(2, 10+1):
    print(i, end=' ')
print()

for i in range(2, 10+1, 2):
    print(i, end=' ')
print()

for i in range(10, 0-1, -1):
    print(i, end=' ')
print()


# i   0    1    2    3    4
L = ['a', 'b', 'c', 'd', 'e']    # list() - список
print(len(L))

for i in range(0, len(L)):
    print(L[i], end=' ')  # через for-ик можно пробегать элементы список/строк/кортежей и тд (по индексам)
print()

for x in L:
    print(x, end=' ')  # можно пробегать элементы списка напрямую через переменную х
print()


S = 'abcde'  # str() - строка
for i in range(0, len(S)):
    print(S[i], end=' ')
print()

for x in S:
    print(x, end=' ')
print()


s = 'abcd'
for a in s:  # вложенные циклы (или каскадные циклы) 
    for b in s:
        print(a, b)
'''

# Цикл while (цикл с условием "ПОКА условие выполняется"):

for i in range(2, 10+1, 2):
    print(i, end=' ')
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()

# Перевод из 10-ной в n-ную систему счисления
'''
x = int(input('Введите 10-ное число для перевода: '))
n = int(input('Введите n-ную систему счисления: '))
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)
'''

# Тип 5 № 16882
# Автомат обрабатывает натуральное число N (0 ≤ N ≤ 255) по следующему алгоритму:
# 1. Строится восьмибитная двоичная запись числа N.
# 2. Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
# 3. Полученное число переводится в десятичную запись.
# 4. Из нового числа вычитается исходное, полученная разность выводится на экран.
#
# Пример. Дано число N = 13. Алгоритм работает следующим образом.
# 1. Восьмибитная двоичная запись числа N: 00001101.
# 2. Все цифры заменяются на противоположные, новая запись 11110010.
# 3. Десятичное значение полученного числа 242.
# 4. На экран выводится число 242 − 13 = 229.
#
# Какое число нужно ввести в автомат, чтобы в результате получилось 111?
'''
for n in range(0, 255+1):
    s = bin(n)[2:]
    while len(s) < 8:  # 1. Строится восьмибитная двоичная запись числа N.
        s = '0' + s

    s = s.replace('1', '*')
    s = s.replace('0', '1')  # 2. Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
    s = s.replace('*', '0')

    r = int(s, 2)  # 3. Полученное число переводится в десятичную запись.

    result = r - n  # 4. Из нового числа вычитается исходное, полученная разность выводится на экран.

    if result == 111:
        print(n)
'''
# Ответ: 72

# Простой пример бесконечного цикла
'''
k = 0
while True:
    print(k)
    k += 1
'''


'''
import random
import time

password = 'qwerty'
count = 0
pas = input('Введите пароль от учетной записи: ')
while True:

    if pas == password:
        print('Добро пожаловать!')
        break
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        x = int(input(f'Пройдите проверку на робота:\n'
                      f'Сколько будет {a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка на робота пройдена успешно!\n')
        else:
            print('Проверка не пройдена, попробуйте через 5 минут.')
            time.sleep(5*60)
    pas = input('Неверный пароль, попробуйте снова: ')
'''
# endregion Урок: ************************************************************


# todo: Евгений = []
# на прошлом уроке: Рассмотрели домашку по номерам: 14, 16, 23, 25 и полностью разобрали теорию по циклам
# на следующем уроке: Разбираем домашку по циклам и 2 номера.
