# region Домашка:  ******************************************************************************

# Тип 16 № 45250
"""
def F(n):
    if n < 3:
        return 2
    if n % 2 == 0 and n > 2:
        return F(n - 2) + F(n - 1) - n
    if n % 2 != 0 and n > 2:
        return F(n - 1) - F(n - 2) + 2 * n
print(F(32))
#Ответ:3194


"""
# Тип 16 № 5310
"""
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2*F(n-1) + 1
print(F(6))
#Ответ:63
"""

# Тип 16 № 35990
"""
def F(n):
    if n == 0:
        return 0
    if n % 2 == 0 and n > 0:
        return F(n // 2)
    if n % 2 != 0:
        return 1 + F(n - 1)
count = 0
for x in range(1, 500+1):
    if F(x) == 3:
        count += 1
print(count)
# Ответ-84
"""


#Тип 23 № 18828
"""
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 3, y) + f(x * 3, y)
print(f(4, 10) * f(10, 17) * f(17, 23))
#Ответ-324
"""


# Тип 23 № 11318
"""
def f(x, y):
    if x > y or x == 22:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(2, 12) * f(12, 26))
#Ответ-30
"""


# Тип 23 № 18634
"""
def f(x, y):
    if x > y or x == 13:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
print(f(1, 9) * f(9, 15))
# Ответ-159
"""

# endregion Домашка: ******************************************************************************


# region Урок:  ******************************************************************************

# Тип 16 № 47220 i
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(n)=1 при n=1;
# F(n)=n·F(n−1), если n>1.
#
# Чему равно значение выражения F(2023) / F(2020)?
'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n*F(n-1)

print(F(2023) / F(2020))  # RecursionError: maximum recursion depth exceeded in comparison
'''
# print(2023*2021*2020)
# Ответ: 8258735660


# № 5291 /dev/inf 12.2022 (Уровень: Базовый)
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
#
# F(n) = 1 при n < 3;
# F(n) = F(n − 1) + n, если n > 2 и при этом n нечётно;
# F(n) = F(n − 3) + 2 × n, если n > 2 и при этом n чётно.
#
# Чему равно значение выражения F(2048) - F(2041)?

# F(2048) = F(2045) + 2 * 2048
# F(2045) = F(2044) + 2045
# F(2044) = F(2041) + 2 * 2044

# print((2 * 2048) + 2045 + (2 * 2044))
# Ответ: 10229



# № 5168 (Уровень: Средний)
# (Д. Статный) Алгоритм вычисления значения функции F(n),
# где n – натуральное число, задан следующими соотношениями:
#
# F(n) = n, если n ≥ 10 000,
# F(n) = F(n+1) + n**2 – 3(n-1), если n < 10 000 и n – чётное.
# F(n) = F(n+2) + 5*n – (n-1), если n < 10 000 и n – нечётное.
#
# Чему равно значение выражения F(90) - F(99)?

# F(90) = F(91) + 90**2 – 3(90-1)
# F(91) = F(93) + 5*91 – (91-1)
# F(93) = F(95) + 5*93 – (93-1)
# F(95) = F(97) + 5*95 – (95-1)
# F(97) = F(99) + 5*97 – (97-1)

# print((90**2 - 3*(90-1)) + (5*91 - (91-1)) + (5*93 - (93-1)) + (5*95 - (95-1)) + (5*97 - (97-1)))
# Ответ: 9341



# Тип 15 № 33187

# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наибольшего натурального числа А формула
#
# ДЕЛ(90, A) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 15) → ¬ДЕЛ(x, 20)))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

'''
def F(x, A):
    return (90 % A == 0) and ((x % A != 0) <= ((x % 15 == 0) <= (x % 20 != 0)))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        # if not(F(x, A)):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
'''

# Вариант 2
'''
def F(x):
    return (90 % A == 0) and ((x % A != 0) <= ((x % 15 == 0) <= (x % 20 != 0)))

for A in range(1, 1000):
    if all(F(x) for x in range(1, 1000)):
        print(A)
'''
# Ответ: 30



# Тип 15 № 27303 i
# Для какого наименьшего целого неотрицательного числа А выражение
#
# (4x + 3y < A) ∨ (x ≥ y) ∨ (y ≥ 13)
#
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?

# Вариант 1
'''
def F(x, y, A):
    return (4*x + 3*y < A) or (x >= y) or (y >= 13)

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

# Вариант 2
'''
def F(x, y):
    return (4*x + 3*y < A) or (x >= y) or (y >= 13)

for A in range(0, 1000):
    if all(F(x, y) for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break
'''
# Ответ: 81


# Тип 15 № 34510 i
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
#
# x&25 ≠ 0 → (x&9 = 0 → x&А ≠ 0)
#
# тождественно истинна (то есть принимает значение 1 при любом неотрицательном целом значении переменной х)?
'''
def F(x):
    return (x & 25 != 0) <= ((x & 9 == 0) <= (x & A != 0))

for A in range(0, 1000):
    if all(F(x) for x in range(0, 1000)):
        print(A)
        break
'''
# Ответ: 16


# Тип 15 № 13364
# На числовой прямой даны два отрезка: P = [130; 171] и Q = [150; 185].
# Укажите наименьшую возможную длину такого отрезка A, что формула
#
# (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
# истинна при любом значении переменной х, т.е. принимает значение 1 при любом значении переменной х.
'''
def F(x):
    P = 130 <= x <= 171
    Q = 150 <= x <= 185
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))
    # return (130 <= x <= 171) <= (((150 <= x <= 185) and (not(a1 <= x <= a2))) <= (not(130 <= x <= 171)))

M = []
A = [i/5 for i in range(120*5, 200*5)]

for a1 in A:
    for a2 in A:
        if all(F(x) for x in A):
            M.append(a2-a1)
print(min(M))
'''
# Ответ: 21


# Тип 15 № 8666 i
# На числовой прямой даны два отрезка: P = [25; 50] и Q = [32; 47].
# Укажите наибольшую возможную длину промежутка A, для которого формула
#
# (¬ (x  принадлежит  A) → (x  принадлежит  P)) → ((x  принадлежит  A) → (x  принадлежит  Q))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
'''
def F(x):
    P = 25 <= x <= 50
    Q = 32 <= x <= 47
    A = a1 <= x <= a2
    return ((not A) <= P) <= (A <= Q)

M = []
A = [i/5 for i in range(20*5, 60*5)]

for a1 in A:
    for a2 in A:
        if all(F(x) for x in A):
            M.append(a2-a1)
print(max(M))
'''
# Ответ: 15


# Тип 15 № 34542
# На числовой прямой даны два отрезка: P = [1, 39] и Q = [23, 58]. Какова наибольшая возможная длина интервала A, что логическое выражение
# ((x ∈ P) → ¬(x ∈ Q)) → ¬(x ∈ А)
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.
'''
def F(x):
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    A = a1 <= x <= a2
    return (P <= (not Q)) <= (not A)

M = []
A = [i/5 for i in range(0*5, 70*5)]

for a1 in A:
    for a2 in A:
        if all(F(x) for x in A):
            M.append(a2-a1)
print(max(M))
'''
# Ответ: 16

# endregion Урок:  ******************************************************************************


# todo: Ислам = [2, 5, 6, 8, 12, 14+, 15, 16.2, 23]
# на прошлом уроке: Разобрали 16 номер на глубину рекурсии (письменное решение), разобрали все типы 15 номеров
# на следующем уроке: Повторить 15 номер, переходим к 25 номерам.