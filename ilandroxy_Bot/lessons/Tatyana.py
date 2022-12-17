

# region Домашка:  **************************************************

# Задание 15 № 39244
'''
def F(x, A):
    B = x & 105 == 0
    C = x & 58 != 0
    D = x & A != 0
    return B <= (C <= D)
for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''

# № 34542
'''
def F(x, a1, a2):
    A = a1 <= x <= a2
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    return (P <= (not(Q))) <= (not(A))
liner = [i/4 for i in range(1*4, 60*4)]
print(liner)
M = []
for a1 in liner:
    for a2 in liner:
        if all(F(x, a1, a2) == True for x in liner):
            M.append(a2 - a1)
print(max(M))
'''

# № 27303
'''
def F(x, y, A):
    return (4 * x + 3 * y < A) or (y <= x) or (13 <= y)
for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break
'''

# № 18720
'''
def F(x, y, A):
    return (x * y < A) or (x < y) or (12 <= x)
for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break
'''

# Площадь и длина
'''
# import math
# def get_circle(R):
#     return 2 * math.pi * R,  math.pi * R ** 2
# R = float(input('Введите длину радиуса '))
# print(get_circle(R))


from math import *
def get_circle(R):
    return 2 * pi * R, pi * R ** 2
R = float(input('Введите длину радиуса '))
print(get_circle(R))
'''

# Is a Number Prime?
'''
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
n = int(input('Введите число '))
print(is_prime(n))
'''

# Делители 1
'''
def get_factors(num):
    M = []
    for i in range(1, num + 1):
        if num % i == 0:
            M.append(i)
    return M
n = int(input('Введите число '))
print(get_factors(n))
'''


'''
def FIO(last_name, first_name, daddy_name):
    return f'{last_name[0]}.{first_name[0]}.{daddy_name[0]}.'

name = input('Введите ФИО:').split()
print(FIO(name[0], name[1], name[2]))
'''


'''
def FIO(name):
    name = name.upper()
    M = name.split()
    return f'{M[0][0]}.{M[1][0]}.{M[2][0]}.'

name = input('Введите ФИО: ')

print(FIO(name))
'''




# endregion Домашка: **************************************************


# region Урок:  **************************************************

#ДЗ или написать свою функцию для вычислений:
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
print(14 & 4)


# Тип 15 № 39244
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
#
# Так, например, 14 & 5 = 11102 & 01012 = 01002 = 4. Для какого наименьшего неотрицательного целого числа А формула
#
# (x & 105 = 0) → ((x & 58 ≠ 0) → (x & А ≠ 0))
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

'''
def Con(m, n):
    M = bin(m)[2:]
    N = bin(n)[2:]

    while len(M) != len(N):  # добавляем незначащие нули
        if len(M) < len(N):
            M = '0' + M
        else:
            N = '0' + N

    r = ''
    for i in range(len(M)):
        if M[i] == '1' and N[i] == '1':
            r += '1'
        else:
            r += '0'

    result = int(r, 2)
    return result

def F(x, A):
    Q = Con(x, 105) == 0
    W = x & 58 != 0
    R = Con(x, A) != 0
    return Q <= (W <= R)

for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''


# Тип 5 № 33475
'''
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. В конец записи (справа) дописывается вторая справа цифра двоичной записи.
# 3. В конец записи (справа) дописывается вторая слева цифра двоичной записи.
# 4. Результат переводится в десятичную систему.

# При каком наименьшем числе N в результате работы алгоритма получится R>180?
# В ответе запишите это число в десятичной системе счисления.

for n in range(2, 1000):
    s = bin(n)[2:]
    s += s[-2]
    s += s[1]
    r = int(s, 2)
    if r > 180:
        print(n)
        break
        '''
# Ответ: 46

# Тип 5 № 28542
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится троичная запись числа N.
# 2. В конец записи (справа) дописывается остаток от деления числа N на 3.
# 3. Результат переводится из троичной системы в десятичную и выводится на экран.
#
# Какое наименьшее четырёхзначное число может появиться на экране в результате работы автомата?

# Вариант 1
'''
for n in range(1, 1000):
    x = n

    M = []
    while x > 0:
        M.append(x % 3)
        x //= 3
    M.reverse()

    M.append(n % 3)

    r = 0
    M.reverse()
    for i in range(0, len(M)):
        r += M[i] * 3 ** i

    if 1000 <= r < 10000:
        print(r)
        break
'''


'''
def systems(x, n):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    M = []
    while x > 0:
        M.append(alphabet[x % n])
        x //= n
    M.reverse()
    r = ''.join(M)
    return r

for n in range(1, 1000):
    s = systems(n, 3)
    s += str(n % 3)
    r = int(s, 3)
    if 1000 <= r < 10000:
        print(r)
        break
'''
# Ответ: 1003




# endregion Урок:  **************************************************


# todo: Татьяна = [2, 5, 8, 12, 14+, 15.1, 16, 23], на следующем уроке: Переходим к 25