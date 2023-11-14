
# region Домашка: ******************************************************************

# КЕГЭ № 5268 (Уровень: Средний) (С. Якунин)
# Дмитрий составляет слова, переставляя буквы в слове АМФИБРАХИЙ.
# Сколько различных слов, содержащих ИИФАА или ААФИИ, может составить Дмитрий?

'''
from itertools import permutations
my_set = set()
for x in permutations('АМФИБРАХИЙ'):
    slovo = ''.join(x)
    if 'ИИФАА' in slovo or 'ААФИИ' in slovo:
        my_set.add(slovo)
print(len(my_set))
'''
'''
from itertools import permutations
words = permutations('АМФИБРАХИЙ')
k = set()
for w in words:
    word = ''.join(w)
    if 'ИИФАА' in word or 'ААФИИ' in word:
        k.add(word)
print(len(k))
'''


# print('02 20 04 40 06 60 24 42 26 62 46 64 13 31 15 51 17 71 35 53 37 73 57 75'.split())

# # КЕГЭ № 4320 (Уровень: Средний)
# # Сколько существует восьмеричных шестизначных чисел, в которых все цифры различны,
# # никакие две чётные или две нечётные цифры не стоят рядом и десятичная запись которых делится на 5?
'''
from itertools import permutations
count = 0
for x in permutations('01234567', 6):
    num = ''.join(x)
    if int(num, 8) % 5 == 0:
        if all(pair not in num for pair in '02 20 04 40 06 60 24 42 26 62 46 64 13 31 15 51 17 71 35 53 37 73 57 75'.split()):
            if num[0] != '0':
                count += 1
print(count)



from itertools import permutations
PAIRS = []
for x in permutations('01234567', 2):
    if (x[0] in '0246' and x[1] in '0246') or (x[0] in '1357' and x[1] in '1357'):
        PAIRS.append(''.join(x))

count = 0
for x in permutations('01234567', 6):
    num = ''.join(x)
    if int(num, 8) % 5 == 0:
        if all(pair not in num for pair in PAIRS):
            if num[0] != '0':
                count += 1
print(count)
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Создание своих функций в Пайтон
'''
M = [1, 2, 3]
print(sum(M))
print(max(M))

print(max(1, 2, 3))
# print(sum(1, 2, 3))
'''

'''
def my_sum(*args):
    """
    print(type(args))  # <class 'tuple'>
    print(args)  # (1, 2, 3)
    """
    summ = 0
    for x in args:
        summ += x
    return summ


print(my_sum(1, 2, 3))
'''

'''
def NOD(x, y):
    r = 1
    for j in range(1, min(x, y)+1):
        if x % j == 0 and y % j == 0:
            r = j
    return r


print(NOD(3, 14))
print(NOD(15, 45))
'''


# Тип 25 №27852
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [185311; 185330], числа, имеющие ровно четыре различных натуральных делителя.
# Для каждого найденного числа запишите эти четыре делителя в четыре
# соседних столбцана экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
def Divisors(x: int):
    divisors = []
    for j in range(1, x+1):
        if x % j == 0:
            divisors.append(j)
    return divisors

for n in range(185311, 185330+1):
    divisors = Divisors(n)
    if len(divisors) == 4:
        print(*divisors)
'''

# Тип 16 №4724
# Алгоритм вычисления значения функции F(n).
# где n — натуральное число, задан следующими соотношениями:
#
# F(1) = 1;
# F(n) = F(n-1) * (n+1), при n > 1.
#
# Чему равно значение функции F(5)? В ответе запишите только натуральное число.
'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) * (n+1)

print(F(5))
'''
# Ответ: 360


# Тип 16 №6779
# Алгоритм вычисления значений функций F(n) и G(n), где n — натуральное число, задан следующими соотношениями:
#
# F(1) = 1;
# G(1) = 1;
#
# F(n) = F(n – 1) – G(n – 1),
# G(n) = F(n–1) + G(n – 1), при n ≥ 2
#
# Чему равно значение величины F(5)/G(5)?
# В ответе запишите только натуральное число.
'''
def F(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) + G(n - 1)

def G(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) + G(n - 1)

print(F(5) / G(5))
'''
# Ответ: 1


# Тип 16 №36871
# Алгоритм вычисления значения функции F(n),
# где n — целое неотрицательное число, задан следующими соотношениями:
#
# F(0) = 0;
# F(n) = F(n / 2), если n > 0 и при этом чётно;
# F(n) = 1 + F(n − 1), если n нечётно.
#
# Сколько существует таких чисел n, что 1 ≤ n ≤ 1000 и F(n) = 3?
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)


count = 0
for n in range(1, 1000+1):
    if F(n) == 3:
        count += 1
print(count)

# Вариант 2
print(len([n for n in range(1, 1000+1) if F(n) == 3]))
'''
# Ответ: 120


# Тип 16 №59841
# Задан алгоритм вычисления функции F(n), где n— натуральное число:
#
# F(n)=7, при n<7;
# F(n)=2n+F(n−1), если n≥7.
#
# Чему равно значение функции F(2024)−F(2022)?
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 7:
        return 7
    if n >= 7:
        return 2*n + F(n-1)


print(F(2024) - F(2022))
# RecursionError: maximum recursion depth exceeded

# F(2024) = 2*2024 + F(2023)
# F(2023) = 2*2023 + F(2022)  -  F(2022)
print(2*2024 + 2*2023)
'''
# Ответ: 8094


# Тип 23 №59768
# 1. Прибавить 1
# 2. Прибавить 2
# 3. Умножить на 3

# Сколько существует программ, для которых при исходном числе 3 результатом является число 25,
# и при этом траектория вычислений содержит число 10 и не содержит число 17?
'''
def F(a, b):
    if a > b or a == 17:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)


print(F(3, 10) * F(10, 25))


def F(a, b):
    if a >= b or a == 17:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)


print(F(3, 10) * F(10, 25))
'''
# Ответ: 6006


# Тип 23 №61403
# A. Прибавить 1
# B. Умножить на 2
# C. Возвести в квадрат
#
#  Сколько существует программ, которые преобразуют исходное число 3 в число 25
#  и при этом траектория вычислений не содержит числа 14?
'''
def F(a, b):
    if a >= b or a == 14:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a**2, b)


print(F(3, 25))
'''
# Ответ: 26


# Тип 23 №58214
# 1. Вычти 1;
# 2. Найди целую часть от деления на 3.

# Сколько существует программ, для которых при исходном числе 67 результатом является число 5,
# и при этом траектория вычислений содержит число 33?
'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a-1, b) + F(a//3, b)

print(F(67, 33) * F(33, 5))
'''
# Ответ: 20

'''
def my_bit_conuction(x, y):
    x_2 = bin(x)[2:]
    y_2 = bin(y)[2:]
    print(x_2, y_2)
    while len(x_2) != len(y_2):
        if len(x_2) < len(y_2):
            x_2 = '0' + x_2
        else:
            y_2 = '0' + y_2

    r = ''
    for i in range(len(x_2)):
        if x_2[i] == '1' and y_2[i] == '1':
            r += '1'
        else:
            r += '0'
    return int(r, 2)

print(my_bit_conuction(14, 5))
'''



# Тип 15 №9804
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
#
# Так, например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
#
# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)
#
# тождественно истинна (т. е. принимает значение 1 при любом неотрицательном целом значении переменной x)?
'''
def F(x, A):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(0, 1000):
    flag = True
    for x in range(0, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break


# Вариант 2

def F(x, A):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(0, 1000):
    if all(F(x, A) for x in range(0, 10000)):
        print(A)
        break


# Вариант 3
def F(x, A):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))

R = []
for A in range(0, 1000):
    if all(F(x, A) for x in range(0, 10000)):
        R.append(A)
print(min(R))

# Вариант 4
print(min([A for A in range(0, 1000) if all(((x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))) for x in range(0, 10000))]))
'''


# Тип 15 №28554
# Для какого наибольшего целого неотрицательного числа А выражение
#
# (x*y < 140) ∨ (y > A) ∨ (x > A)
#
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?

def F(x, y, A):
    return (x*y < 140) or (y > A) or (x > A)

R = []
for A in range(0, 1000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        R.append(A)
print(max(R))

# endregion Урок: ******************************************************************


# GOAL = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 16.2, 23.1]
# КЕГЭ  = []
# на следующем уроке:
