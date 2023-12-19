
# region Домашка: ******************************************************************
'''
from itertools import product
num = 1
R = []
for s in product(sorted('ПЯТЬДНЕЙ'), repeat=4):
    slovo = ''.join(s)
    if 'Я' not in slovo and 'Е' not in slovo:
        if len(slovo) == len(set(slovo)):  # все буквы различны
            R.append(num)
    num += 1
print(max(R))
'''
# Ответ: 3428

'''
from itertools import permutations
count = set()
for s in permutations('СОТОЧКА'):
    slovo = ''.join(s)
    if any(pair in slovo for pair in 'ОО ОА АО'.split()):
        count.add(slovo)
print(len(count))
'''
# Ответ: 1800

'''
from itertools import product
num = 1
R = []
for s in product(sorted('БАРШ'), repeat=5):
    slovo = ''.join(s)
    # if slovo.count('Б') + slovo.count('Р') + slovo.count('Ш') <= 3:
    if len([x for x in slovo if x in 'БРШ']) <= 3:
        if len(set(slovo)) == 4:
            R.append(num)
    num += 1
print(max(R))
'''
# Ответ: 913

'''
from itertools import permutations
count = set()
for s in permutations('АМФИБРАХИЙ'):
    slovo = ''.join(s)
    if 'ИИФАА' in slovo or 'ААФИИ' in slovo:
        count.add(slovo)
print(len(count))
'''


# Тип 16 №4660
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
#
# F(1) = 1
# F(2) = 2
# F(n) = (F(n–1) − F(n–2)) * n, при n >2
#
# Чему равно значение функции F(8)?
# В ответе запишите только натуральное число.
'''
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return (F(n - 1) - F(n - 2)) * n

print(F(8))
'''

# Разобраться КЕГЭ № 1363 в чем проблема ДЗ 8.3 (4 задача) +
# region

# КЕГЭ № 1363 Джобс 16.05.2021 (Уровень: Сложный)
# Сколько существует четных пятеричных чисел длиной 6, начинающихся с цифры 3?
'''
from itertools import product
count = 0
for s in product('01234', repeat=6):
    slovo = ''.join(s)
    if slovo[0] == '3' and slovo[0] != '0':
        if sum([int(x) for x in slovo]) % 2 == 0:
            count += 1
print(count)
'''
# Примечание: Четность числа в нечетной системе счисления определеяется четностью суммы ее цифр

# Ответ: 1562
# endregion

# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# todo: Разобрать с функтулс
# Тип 16 №48464
# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:
# F(0) = 0;
# F(n) = F(n − 1) + n.
#
# Укажите количество таких чисел n из интервала 765 432 010 ≤ n ≤ 1 542 613 234,
# для которых F(n) не делится без остатка на 3.
'''
import sys
sys.setrecursionlimit(100000000)

def F(n):
    if n == 0:
        return 0
    return F(n - 1) + n


cnt = 0
for n in range(765_432_010, 1_542_613_234+1):
    if F(n) % 3 != 0:
        cnt += 1
print(cnt)
'''
# RecursionError: maximum recursion depth exceeded



# Тип 16 №35990
# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное
# число, задан следующими соотношениями:

# F(0) = 0;
# F(n) = F(n / 2), если n > 0 и при этом чётно;
# F(n) = 1 + F(n − 1), если n нечётно.
#
# Сколько существует таких чисел n, что 1 ≤ n ≤ 500 и F(n) = 3?
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

cnt = 0
for n in range(1, 500+1):
    if F(n) == 3:
        cnt += 1
print(cnt)
'''
# Ответ: 84


# Тип 16 60258
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
# F(n)=n при n>2024;
# F(n)= n * F(n+1), если n≤2024.

# Чему равно значение выражения F(2022) / F(2024)?
'''
def F(n):
    if n > 2024:
        return n
    if n <= 2024:
        return n * F(n+1)

print(F(2022) / F(2024))
'''
# Ответ: 4090506



# Тип 16 №59757
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(n)=10, при n<11;
# F(n)=n+F(n−1), если n≥11.
#
# Чему равно значение выражения F(2024)−F(2022)
'''
import sys
sys.setrecursionlimit(100000)
def F(n):
    if n < 11:
        return 10
    if n >= 11:
        return n+F(n-1)

print(F(2024) - F(2022))
'''
# Отвте: 4047


# Тип 23 №60265
# 1. Прибавить 1
# 2. Умножить на 2
# 3. Возвести в квадрат
# Сколько существует программ, для которых при исходном
# числе 2 результатом является число 20,
# при этом траектория вычислений не содержит числа 11?
'''
def F(a, b):
    if a > b or a == 11:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b) + F(a**2, b)


print(F(2, 20))


def F(a, b):
    if a >= b or a == 11:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a**2, b)

print(F(2, 20))
'''
# Ответ: 37

# todo Варя Разобрать задачу https://inf-ege.sdamgia.ru/problem?id=40732
'''
import sys
sys.setrecursionlimit(100000)
def F(n):
    if n == 0:
        return n
    if n > 0 and n % 3 == 2:
        return F((n - 1) + 1)
    if n > 0 and n % 3 < 2:
        return F((n - n % 3) / 3)
for n in range(1, 1000):
    if F(n) == 6:
        print(n)
        exit()
'''
# endregion Урок: ******************************************************************


# Варя = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке: 16, 23, 15
