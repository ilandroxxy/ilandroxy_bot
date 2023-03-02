
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 23 № 15117 i

# У исполнителя есть две команды, которым присвоены номера:
#
# 1. Прибавить 1
# 2. Прибавить 2

# Сколько существует программ, которые преобразуют исходное число 3 в число 20 и
# при этом траектория вычислений содержит число 9 и не содержит числа 15?
'''
def F(a, b):
    if a > b or a == 15:  #  не содержит числа 15
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b)

print(F(3, 9) * F(9, 20))  # содержит число 9
'''
# Ответ: 520


# Тип 23 № 6508
# У исполнителя Прибавитель две команды, которым присвоены номера:
#
# 1. прибавь 1,
# 2. увеличь старшую цифру числа на 1.

#  Сколько есть программ, которые число 15 преобразуют в число 37?
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+10, b)

print(F(15, 37))
'''
# Ответ: 20


# Тип 16 № 6459
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(n) = 2 при n ≤ 2;
# F(n) = 3 × F(n − 1) − F(n − 2) при n> 2.
#
# Чему равно значение функции F(6)? В ответе запишите только натуральное число.
'''
def F(n):
    if n <= 2:
        return 2
    if n > 2:
        return 3 * F(n - 1) - F(n - 2)

x = F(6)
print(x)

print(F(6))
'''
# Ответ: 68


# Тип 16 № 6893 i
# Алгоритм вычисления значений функций F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(1) = 1; F(2) = 2; F(3) = 3;
#
# F(n) = F(n − 3)*n при n >3
#
# Чему равно значение функции F(10)? В ответе запишите только натуральное число.
'''
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n > 3:
        return F(n - 3) * n

print(F(10))
'''
# Ответ: 280


# Тип 16 № 36871
# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:
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

# Вариант 1
count = 0
for n in range(1, 1000+1):  # 1 ≤ n ≤ 1000
    if F(n) == 3:
         count += 1
print(count)

# Вариант 2
print(len([n for n in range(1, 1000+1) if F(n) == 3]))
'''
# Ответ: 120

# Тип 16 № 47220 i
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(n)=1 при n=1;
# F(n) = n * F(n−1), если n > 1.
#
# Чему равно значение выражения F(2023) / F(2020)?
'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n-1)

print(F(2023) / F(2020))  # RecursionError: maximum recursion depth exceeded
'''
# print(2023 * 2022 * 2021)
# Ответ: 8266912626


# Тип 16 № 4656 i
# Алгоритм вычисления значения функции F(n) и G(n), где n – натуральное число, задан следующими соотношениями:
#
# F(1) = 0
# F(n) = F(n–1) + n, при n >1
#
# G(1) = 1
# G(n) = G(n–1) * n, при n >1
#
# Чему равно значение функции F(5) + G(5)?
'''
def F(n):
    if n == 1:
        return 0
    if n > 1:
        return F(n-1) + n
    
def G(n):
    if n == 1:
        return 1
    if n > 1:
        return G(n-1) * n

print(F(5) + G(5))
'''
# Ответ: 134


# № 5954 (Уровень: Базовый)
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
#
# F(n) = 1 при n = 1;
# F(n) = n × F(n − 1), если n > 1.
#
#  Чему равно значение выражения (F(2023) - F(2022)) / F(2020)?
# Раскроем скобки: (F(2023) / F(2020)) - (F(2022) / F(2020))

# F(2023) = 2023 * F(2022)
# F(2022) = 2022 * F(2021)
# F(2021) = 2021 * F(2020)

# F(2022) = 2022 * F(2021)
# F(2021) = 2021 * F(2020)

# print((2023 * 2022 * 2021) - (2022 * 2021))
# 8262826164


# № 4739 (Уровень: Средний)
# (А. Куканова) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:

# F(n) = n − 10000 при n > 10000;
# F(n) = F(n + 1) + F(n + 2), если 1 ≤ n ≤ 10000.

# Чему равно значение выражения F(12345) × (F(10) − F(12)) / F(11) + F(10101)?

def F(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return F(n + 1) + F(n + 2)

print(F(12345))
print(F(10101))

# F(12345) × (F(10) − F(12)) / F(11) + F(10101)
# 2345 × (F(10) − F(12)) / F(11) + 101
# 2345 × (F(11) + F(12) − F(12)) / F(11) + 101
# 2345 × (F(11) + ...) / F(11) + 101
# 2345 × 1 + 101
# Ответ: 2446

# endregion Урок: ******************************************************************


# todo: Всеволод = [2, 5.1, 8, 12, 14, 15, 16, 23]
# на прошлом уроке: Разобрали 16, 23 номера. В том числе на аналитическое решение.
# на следующем уроке:
