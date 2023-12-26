# region Домашка: ******************************************************************

# Тип 14 №48388
# Операнды арифметического выражения записаны в системах счисления с основаниями 12 и 14:
# x231y_12 + 78x98y_14
#
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 99.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 99
# и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:12]:
    for y in alphabet[:12]:
        A = int(f'{x}231{y}', 12)
        B = int(f'78{x}98{y}', 14)
        if (A + B) % 99 == 0:
            print((A + B) // 99)
            exit()
'''
# Ответ: 41428


# КЕГЭ № 4964 (Уровень: Средний)
# Операнды арифметического выражения записаны в системах счисления с основаниями 21.
# 12yx9_21 + 36y99_21
#
# В записи чисел переменными x и y обозначены неизвестные цифры из алфавита 21-ричной системы счисления.
# Определите наименьшее значение x, при которых значение данного арифметического выражения кратно 18_10
# при любом значении y. Для найденного значения x вычислите частное от деления значения арифметического
# выражения на 18_10 при y=5 и укажите его в ответе в десятичной системе счисления
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:21]:
    if all((int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)) % 18 == 0 for y in alphabet[:21]):
        print((int(f'12{5}{x}9', 21) + int(f'36{5}99', 21)) // 18)
        exit()
'''


# КЕГЭ № 6845 (Уровень: Средний)
# В системе счисления с основанием p выполняется равенство
# 1x77 + xx77 = y0yy
#
# Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p.
# Определите значение числа yxyx_p и запишите это значение в десятичной системе счисления.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(8, 36):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'1{x}77', p) + int(f'{x}{x}77', p) == int(f'{y}0{y}{y}', p):
                print(int(f'{y}{x}{y}{x}', p))
'''


# КЕГЭ № 8002 (Уровень: Базовый) (Л. Шастин)
# Операнды арифметического выражения записаны в системе счисления с основанием 18.
#
# 77968х11_18 + 4x213_18
#
# В записи чисел переменной х обозначена неизвестная цифра из алфавита 18-ричной системы счисления.
# Определите наибольшее значение х, при котором значение данного арифметического выражения кратно 7.
# Для найденного значения х вычислите частное от деления значения арифметического выражения на 7
# и укажите его в ответе в десятичной системе счисления.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alphabet[:18]:
    A = int(f'77968{x}11', 18)
    B = int(f'4{x}213', 18)
    if (A + B) % 7 == 0:
        R.append((A + B) // 7)
print(max(R))
'''


# КЕГЭ № 227 (Уровень: Базовый)
# Сколько единиц в двоичной записи числа 4**2015 + 2**2015 - 15?
'''
x = 4**2015 + 2**2015 - 15
n = 2
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M.count(1))
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Разобраться со степенью Лиза #разобрал
# region
# Тип 14 №58481
# В системе счисления с основанием p выполняется равенство 12 * 34 = xy**2.
# Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p.
# Определите значение числа yx_p и запишите это значение в десятичной системе счисления.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(5, 36):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'12', p) * int(f'34', p) == int(f'{x}{y}', p) ** 2:  # тут не корректное условие, должно быть (xy)**2
                print(int(f'{y}{x}', p))
'''
# endregion


# Тип 16 №4653
# Последовательность чисел Люка задается рекуррентным соотношением:
# F(1) = 2
# F(2) = 1
# F(n) = F(n–2) + F(n–1), при n >2, где n – натуральное число.
#
# Чему равно десятое число в последовательности Люка?
'''
def F(n):
    if n == 1:  # F(1) = 2
        return 2
    if n == 2:
        return 1
    if n > 2:
        return F(n-2) + F(n-1)

print(F(10))
'''
# Ответ: 76


# Тип 16 №4657
# Алгоритм вычисления значения функции F(n) и G(n),
# где n – натуральное число, задан следующими соотношениями:
# F(1) = 1
# F(n) = 2 * G(n–1) + 5 * n, при n >1
#
# G(1) = 1
# G(n) = F(n–1) + 2 * n, при n >1
#
# Чему равно значение функции F(4) + G(4)?
'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * G(n-1) + 5 * n

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) + 2 * n

print(F(4) + G(4))
'''
# Ответ: 89


# Тип 16 №36871
# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число,
# задан следующими соотношениями:
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

cnt = 0
for n in range(1, 1000+1):
    if F(n) == 3:
        cnt += 1
print(cnt)
'''
# Ответ: 120


# Тип 16 №59841
# Задан алгоритм вычисления функции F(n), где n — натуральное число:
#
# F(n) = 7, при n< 7;
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
        return 2*n+F(n-1)


print(F(2024) - F(2022))

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# F(2024) = 2*2024 + F(2023)
# F(2023) = 2*2023 + F(2022) -  F(2022)
print(2*2024 + 2*2023)
'''
# Ответ: 8094

# endregion Урок: ******************************************************************


# Лиза = [2.1, 6.1, 8.1, 12.1, 14.1, 16.1]
# КЕГЭ  = []
# на следующем уроке:
