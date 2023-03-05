
# region Домашка: ******************************************************************

# Тип 15 № 19067
# (x + 2y < A) ∨ (y > x) ∨ (x > 30)
'''
def fun(x, y, A):
    return (x + 2 * y < A) or (y > x) or (x > 30)

sps = []
for A in range(1, 1000):
    if all(fun(x, y, A) for x in range(100) for y in range(100)):
        sps.append(A)
print(min(sps))
'''
# ответ 91


# Тип 15 № 38949
# x & 85 = 0 → (x & 54 ≠ 0 → x & А ≠ 0)
'''
def fun(x):
    # return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))
    R = x & 85 == 0
    T = x & 54 != 0
    P = x & A != 0
    return R <= (T <= P)

sps = []
for A in range(0, 1000):
    if all(fun(x) for x in range(0, 1000)):
        sps.append(A)
print(min(sps))
'''
# Ответ: 34



# Тип 15 № 40731
# (x∈Q)→(¬(x∈P)→ ¬((x∈Q)∧¬(x∈A)))
#   ¬(x∈P) ---> (not P)
'''
def fun(x):
    A = a1 <= x <= a2
    P = 19 <= x <= 84
    Q = 4 <= x <= 51
    return Q <= ((not P) <= (not(Q and (not A))))

sps = []
M = [i/4 for i in range(0*4, 100*4)]
for a1 in M:
    for a2 in M:
        if all(fun(x) for x in M):
            sps.append(a2 - a1)
print(min(sps))  # 14.75 - нужно округлить 
'''
# Ответ: 15



# '''Тип 15 № 45249
# def fun(n, m):
#     return n % m == 0
# sps = []
# for A in range(1, 100):
#     if all((fun(x, 3) <= (not fun(x, 5))) or (x + A >= 90) for x in range(1, 100)):
#         sps.append(A)
# print(sps)
# ответ 75
# '''


# '''Тип 15 № 18499
# def fun(m, n):
#     return (2 * m + 3 * n > 40) or ((m < A) and (n <= A))
# sps = []
# for A in range(1, 100):
#     if all(fun(m, n) for m in range(0, 100) for n in range(0, 100)):
#         sps.append(A)
# print(min(sps))
# ответ 21
# '''


# Тип 15 № 9321
# ¬ДЕЛ(x, А) → (¬ДЕЛ(x, 21) ∧¬ ДЕЛ(x, 35))
'''
def ost(n, m):
    return n % m == 0

def fun(x):
    return (not ost(x, A)) <= ((not ost(x, 21)) and (not ost(x, 35)))

sps = []
for A in range(1, 10000):
    if all(fun(x) for x in range(1, 10000)):
        sps.append(A)
print(max(sps))
'''

'''
def f(x):
    return (x % A != 0) <= ((x % 21 != 0) and (x % 35 != 0))

sps = []
for A in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        sps.append(A)
print(max(sps))
'''
# Ответ: 7


'''Тип 15 № 39244
def fun(x, A):
    return (x&105 == 0) <= ((x&58 != 0) <= (x&A != 0))
sps = []
for A in range(100):
    if all(fun(x, A) for x in range(100)):
        sps.append(A)
print(min(sps))
ответ 18
'''


# Тип 15 № 46973
# (x∈Q)→(((x∈P)≡(x∈Q))∨(¬(x∈P)→(x∈A)))
'''
def fun(x):
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))

sps = []
M = [i/4 for i in range(50*4, 150*4)]
for a1 in M:
    for a2 in M:
        if all(fun(x) for x in M):
            sps.append(a2 - a1)
print(min(sps))  # 22.75  - округляем
'''
# Ответ: 23



'''Тип 15 № 29125
def fun(x, y, A):
    return (4 * x + 3 * y < A) or (x > y) or (y > 13)
sps = []
for A in range(100):
    if all(fun(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        sps.append(A)
print(min(sps))
ответ 92
'''

# ¬ДЕЛ(x, А) → (¬ДЕЛ(x, 21) ∧¬ ДЕЛ(x, 35))

# Тип 15 № 9321
'''
for A in range(1, 10000):
    if all(((x % A != 0) <= ((x % 21 != 0) and (x % 35 != 0))) for x in range(1, 10000)):
        print(A)

# Вариант 2
print(max([A for A in range(1, 10000) if all(((x % A != 0) <= ((x % 21 != 0) and (x % 35 != 0))) for x in range(1, 10000))]))
'''
# Ответ: 7

# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************


# Тип 23 № 3627
# У исполнителя Увеличитель две команды, которым присвоены номера:

# 1. прибавь 2,
# 2. умножь на 3.
#
# Сколько есть программ, которые число 1 преобразуют в число 31?

'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+2, b) + F(a*3, b)

print(F(1, 31))
'''


'''
d = True
print(int(d))
# Вариант 2
def F(a, b):
    if a >= b:
        return int(a == b)
    else:
        return F(a+2, b) + F(a*3, b)

print(F(1, 31))
'''
# Ответ: 12



# Тип 23 № 23920 i

# 1. Прибавить 1
# 2. Умножить на 2

# Сколько существует программ, для которых при исходном числе 1 результатом является число 21
# и при этом траектория вычислений содержит число 10 и не содержит числа 18?
'''
def F(a, b):
    if a >= b or a == 18:  # не содержит числа 18
        return int(a == b)
    else:
        return F(a+1, b) + F(a*2, b)

print(F(1, 10) * F(10, 21))
'''
# Ответ: 14


# Тип 16 № 6423 i
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:

# F(n) = n − 1 при n ≤ 2;
#
# F(n) = 3 × F(n − 1) − F(n − 2) при n> 2.
# Чему равно значение функции F(6)? В ответе запишите только натуральное число.
'''
def F(n):
    if n <= 2:  # при n ≤ 2
        return n - 1  # F(n) = n − 1
    if n > 2:  # при n> 2
        return 3 * F(n - 1) - F(n - 2)  # F(n) = 3 × F(n − 1) − F(n − 2)

print(F(6))
'''
# Ответ: 55

# Тип 16 № 39245 i
# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:
#

# F(0) = 0;
# F(n) = F(n / 2), если n > 0 и при этом чётно;
# F(n) = 1 + F(n − 1), если n нечётно.
#
# Сколько существует таких чисел n, что 1 ≤ n ≤ 900 и F(n)=9?
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

count = 0
for n in range(1, 900+1):
    if F(n) == 9:
        count += 1
print(count)
'''
# Ответ: 3


# Тип 16 № 33188 i
# Обозначим через a mod b остаток от деления натурального числа a на натуральное число b. Алгоритм вычисления значения функции F(n), где n  — натуральное число, задан следующими соотношениями:
#
# F(0) = 0;
# F(n) = n + F(n − 3), если n mod 3 = 0, и n > 0;
# F(n) = n + F(n − (n mod 3)), если n mod 3 > 0.
#
# Чему равно значение функции F(22)?
'''
def mod(a, b):
    return a % b

def F(n):
    if n == 0:
        return 0
    if n > 0 and mod(n, 3) == 0:
        return n + F(n - 3)
    if mod(n, 3) > 0:
        return n + F(n - (mod(n, 3)))

print(F(22))
'''
# Ответ: 106


'''
def F(n):
    print(n ** 2)

F(5)  # вызов функции

x = F(5)  # Пытаемся получить возвращаемое значение функции
print(x)  
'''


# Тип 16 № 47220 i
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(n) = 1 при n=1;
# F(n) = n·F(n−1), если n>1.
#
# Чему равно значение выражения F(2023) / F(2020)?

# F(2023) = 2023 * F(2022)
# F(2022)= 2022 * F(2021)
# F(2021) = 2021 * F(2020)  / F(2020)   (сократились)
print(2023 * 2022 * 2021)

# endregion Урок: ******************************************************************


# todo: Сергей = [2, 5, 8, 12, 14, 15, 16, 23]
# на прошлом уроке: Плотно разобрали 16, 23 номера. Особенно хорошо проговорили моменты с рекурсией. Решали и аналитические задачи.
# на следующем уроке:
