

# region Тип 15 № 34538 Обратите внимание на задание с интервалами
'''
# На числовой прямой даны два отрезка: Р = [30, 45] и Q = [40, 55].
# Какова наименьшая возможная длина интервала A, что обе приведённые ниже формулы истинны при любом значении переменной х:
#
# ( ¬(x ∈ A) → (¬(x ∈ P)) ) и ((x ∈ Q)→ (x ∈ A))


def F(x, a1, a2):
    return ((not(a1 <= x <= a2)) <= ((not(30 <= x <= 45)))) and ((40 <= x <= 55) <= (a1 <= x <= a2))

A = []
for a1 in range(1, 100):
    for a2 in range(1, 100):
        flag = True
        for x in range(1, 1000):
            if F(x, a1, a2) == False:
                flag = False
                break
        if flag == True:
            A.append(a2-a1)
            print(a2 - a1)
print(min(A))
'''
# Ответ: 25.
# endregion Тип 15 № 34538

# region Тип 15 № 40731 Обратите внимание на задание с отрезками
'''
# На числовой прямой даны два отрезка: P=[19;84] и Q=[4;51].
# Укажите наименьшую возможную длину такого отрезка A, для которого формула
#
# (x ∈ Q)→( ¬(x ∈ P)→ ¬((x ∈ Q)∧ ¬(x ∈ A)))
#
# тождественно истинна (т.е. принимает значение 1 при любом значении переменной х).

def F(x, a1, a2):
    return (4 <= x <= 51) <= ((not(19 <= x <= 84)) <= (not((4 <= x <= 51) and (not(a1 <= x <= a2)))))

A = []
for a1 in range(1, 1000):
    for a2 in range(1, 1000):
        flag = True
        for x in range(1, 1000):
            if F(x, a1, a2) == False:
                flag = False
                break
        if flag == True:
            A.append(a2 - a1)
            print(a2 - a1)
print(min(A) + 1)
'''
# endregion Тип 15 № 40731 Обратите внимание на задание с отрезками

# region Тип 15 № 7763 Обратите внимание на задание с промежутками
'''
# На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23]. Укажите наибольшую возможную длину промежутка A, для которого формула
#
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
#
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

def F(x, a1, a2):
    return ((5 <= x <= 30) == (14 <= x <= 23)) <= (not(a1 <= x <= a2))

A = []
for a1 in range(1, 100):
    for a2 in range(1, 100):
        flag = True
        for x in range(1, 100):
            if F(x, a1, a2) == False:
                flag = False
                break
        if flag == True:
            A.append(a2 - a1)
            print(a2 - a1)
print(max(A) + 1)
'''
# Ответ: 9
# endregion Тип 15 № 7763 Обратите внимание на задание с промежутками


# region Тип 15 № 9699  P = [4, 15] и Q = [12, 20]
# '''
# # На числовой прямой даны два отрезка: P = [4, 15] и Q = [12, 20].
# #
# # Укажите наименьшую возможную длину отрезка A, для которого выражение
# #
# # ((x ∈ P) ∧ (x ∈ Q)) → (x ∈ A)
# #
# # тождественно истинно, то есть принимает значение 1 при любом значении переменной х.
#
# def F(a1, a2, x):
#     return ((4 <= x <= 15) and (12 <= x <= 20)) <= (a1 <= x <= a2)
#
# M = []
# for a1 in range(1, 100):
#     for a2 in range(1, 100):
#         flag = True
#         for x in range(1, 100):
#             if F(a1,a2,x) == False:
#                 flag = False
#                 break
#         if flag == True:
#             M.append(a2-a1)
#
# print(min(M))
# '''
# # Ответ 3
# endregion # Тип 15 № 9699

# region Тип 15 № 34506  m & n
'''
# Для какого наименьшего неотрицательного целого числа А формула
#
# x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной х)?




def F(A, x):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))


M = []
for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        if F(A, x) == False:
            flag = False
            break
    if flag == True:
        M.append(A)
print(min(M))
'''
# Ответ: 8
# endregion Тип 15 № 345

# region Тип 15 № 33094  ДЕЛ(n, m)
"""
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
#
# Для какого наибольшего натурального числа А формула
#
# (A < 50) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 18)))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

def F(x, A):
    return (A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 18 != 0)))

for A in range(1000, -1, -1):
    flag = True
    for x in range(1, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
"""
# Ответ: 45
# endregion Тип 15 № 33094

# region Тип 15 № 29125
"""
# Для какого наименьшего целого неотрицательного числа А выражение
#
# (4x + 3y < A) ∨ (x > y) ∨ (y > 13)
#
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?

def F(x, y, A):
    return (4*x + 3*y < A) or (x > y) or (y > 13)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if F(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
"""
# Ответ: 92
# endregion Тип 15 № 29125

# region Тип 15 № 47219 ДЕЛ(n, m)
"""
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
#
# Для какого наименьшего натурального числа А формула
# (ДЕЛ(x, 2) → ¬ДЕЛ(x, 3)) \/ (x + A ≥ 100)
#
# тождественно истинна (т.е. принимает значение 1) при любом натуральном значении переменной х?


def F(x, A):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)

M = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
"""
# Ответ: 94
# endregion Тип 15 № 47219 ДЕЛ(n, m)

# region Тип 15 № 36028  P=[17,54] и Q=[37,83]
"""
# На числовой прямой даны два отрезка: P=[17,54] и Q=[37,83]. Какова наименьшая возможная длина интервала A, что формула
#
# (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

def F(x, a1, a2):
    return (17 <= x <= 54) <= (((37 <= x <= 83) and (not(a1 <= x <= a2))) <= (not(17 <= x <= 54)))

M = []
for a1 in range(1, 1000):
    for a2 in range(1, 1000):
        flag = True
        for x in range(1, 1000):
            if F(x, a1, a2) == False:
                flag = False
                break
        if flag == True:
            M.append(a2 - a1)
            print(min(M))
"""
# Ответ: 17
# endregion Тип 15 № 36028

# region Тип 15 № 34513  m & n
"""
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Для какого наименьшего неотрицательного целого числа А формула
#
# x & 33 = 0 → (x & 45≠0 → x & А ≠ 0)
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной х)?

# вариант 1
def F(A, x):
    return (x & 33 == 0) <= ((x & 45 != 0) <= (x & A != 0))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(F(A, x)):
            flag = False
            break
    if flag == True:
        print(A)
        break

# вариант 2
for A in range(64):
    flag = True
    for x in range(64):
        if not((x & 33 == 0) <= ((x & 45 != 0) <= (x & A != 0))):
            flag = False
    if flag:
        print(A)
        break
"""
# Ответ: 12
# endregion Тип 15 № 34513  m & n

# region Тип 15 № 18594
'''
# Для какого наименьшего целого неотрицательного числа A выражение
#
# (2m + 3n > 43) ∨ (m < A) ∨ (n ≤ A)
#
# тождественно истинно при любых целых неотрицательных m и n?

for A in range(1, 1000):
    flag = True
    for m in range(1, 1000):
        for n in range(1, 1000):
            if not( (2*m + 3*n > 43) or (m < A) or (n <= A) ):
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
'''
# Ответ: 9
# endregion Тип 15 № 18594

# region Тип 15 № 34517
'''
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
#
# Так, например, 12&6 = 1100_2 & 0110_2 = 0100_2 = 4.
#
# Для какого наибольшего целого числа А формула
# х&А != 0 → (x&10 = 0 → х&3 != 0)
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной x)?
def F(x, A):
    return (x&A != 0) <= ((x&10 == 0) <= (x&3 != 0))  # & - сложение бинарный чисел

for A in range(1000, 0, -1):
    flag = True
    for x in range(1, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''
# Ответ: 11
# endregion Тип 15 № 34517

# region Тип 15 № 16821
'''
# Для какого наименьшего целого неотрицательного числа A выражение
#
# (3x + 4y ≠ 70) ∨ (A > x) ∨ (A > y)
#
# тождественно истинно при любых целых неотрицательных x и y?


def F(x, y, A):
    return ((3 * x + 4 * y) != 70) or (A > x) or (A > y)

for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if F(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
'''
# Ответ: 11
# endregion Тип 15 № 16821

# region Тип 15 № 34545
'''
# На числовой прямой даны два отрезка: P = [12, 62] и Q = [32, 92].
#
# Какова наименьшая возможная длина интервала A, что формула
#
# (¬(x ∈ А) ∧ (x ∈ Q)) → (x ∈ P)
#
# тождественно истинна, т.е. принимает значение 1 при любом значении переменной х.

def F(a1, a2, x):
    return ((not(a1 <= x <= a2)) and (32 <= x <= 92)) <= (12 <= x <= 62)

M = []
for a1 in range(1, 100):
    for a2 in range(1, 100):
        flag = True
        for x in range(1, 100):
            if F(a1, a2, x) == False:
                flag = False
                break
        if flag == True:
            M.append((a2-a1) + 1)
print(min(M))
'''
# Ответ: 30
# endregion Тип 15 № 34545

# region Тип 15 № 15803 сложное задание с отрезками
'''
# На числовой прямой задан отрезок A. Известно, что формула
#
# ((x ∈ A) → (x2 ≤ 100)) ∧ ((x2 ≤ 64) → (x ∈ A))
#
# тождественно истинна при любом вещественном x.
# Какую наибольшую длину может иметь отрезок A?

M = []
for a1 in range(-100, 100):
    for a2 in range(a1 + 1, 100):
        flag = True
        for x in range(-100, 100):
            if not(((a1 <= x <= a2) <= (x**2 <= 100)) and ((x**2 <= 64) <= (a1 <= x <= a2))):
                flag = False
                break
        if flag == True:
            print(a2-a1)
            M.append(a2 - a1)
print(f'Максимальное: {max(M)}')
'''
# Ответ: 20
# endregion Тип 15 № 15803

# region Тип 15 № 34537
"""
# На числовой прямой даны три отрезка: P = [10,15], Q = [10,20] и R=[5,15]. Какова наименьшая возможная длина интервала A, что формулы
#
# (x ∈ A) → (x ∈ P) и (x ∈ Q) → (x ∈ R)
#
# тождественно равны, то есть принимают равные значения при любом значении переменной х (за исключением, возможно, конечного числа точек).


def F(a1, a2, x):
    return ((a1 <= x <= a2) <= (10 <= x <= 15)) == ((10 <= x <= 20) <= (5 <= x <= 15))  # вместо и -> ==, потому что: тождественно равны

M = []
for a1 in range(1, 1000):
    for a2 in range(a1+1, 1000):
        flag = True
        for x in range(1, 1000):
            if not(F(a1,a2,x)):
                flag = False
                break
        if flag == True:
            M.append((a2-a1) + 1)  # Какова наименьшая возможная длина интервала A
            print(M, a2, a1)
print(min(M))
"""
# Ответ: 5
# endregion Тип 15 № 34537
