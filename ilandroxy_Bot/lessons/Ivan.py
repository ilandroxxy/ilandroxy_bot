# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Тип 15 № 33760
'''
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
#
# Для какого наибольшего натурального числа А формула
#
# ДЕЛ(120, A) ∧ (ДЕЛ(x, 36) → (¬ДЕЛ(x, А) → ¬ДЕЛ(x, 45)))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

# Вариант 1
for A in range(10000, 0, -1):
    flag = True
    for x in range(1, 1000):
        if not((120 % A == 0) and ((x % 36 == 0) <= ((x % A != 0) <= (x % 45 != 0)))):
            flag = False
            break
    if flag == True:
        print(A)
        break

# Вариант 2
for A in range(10000, 0, -1):
    flag = True
    for x in range(1, 1000):
        if not((120 % A == 0) and ((x % 36 == 0) <= ((not(x % A == 0)) <= (not(x % 45 == 0))))):
            flag = False
            break
    if flag == True:
        print(A)
        break

# Вариант 3
for A in range(10000, 0, -1):
    flag = True
    for x in range(1, 1000):
        if ((120 % A == 0) and ((x % 36 == 0) <= ((x % A != 0) <= (x % 45 != 0)))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break

# Вариант 4
def F(x, A):
    return (120 % A == 0) and ((x % 36 == 0) <= ((x % A != 0) <= (x % 45 != 0)))

for A in range(10000, 0, -1):
    flag = True
    for x in range(1, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''


# Ответ: 60.


# Тип 15 № 34513
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
#
# Например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
#
# Для какого наименьшего неотрицательного целого числа А формула
#
# x&33 = 0 → (x&45≠0 → x&А ≠ 0)
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной х)?

# Вариант 2
'''
def Con(m, n):
    m = bin(m)[2:]
    n = bin(n)[2:]
    #print(m, n)

    while len(m) != len(n):
        if len(m) < len(n):
            m = '0' + m
        else:
            n = '0' + n
    #print(m, n)

    r = ''
    for i in range(0, len(n)):
        if m[i] == '1' and n[i] == '1':
            r += '1'
        else:
            r += '0'
    #print(r)

    res = int(r, 2)
    return res

# print(Con(14, 5))
def F(x, A):
    return (Con(x, 33) == 0) <= ((Con(x, 45) != 0) <= (Con(x, A) != 0))

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

# Вариант 1
'''
def F(x, A):
    return (x & 33 == 0) <= ((x & 45 != 0) <= (x & A != 0))

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
# Ответ: 12.


# Тип 15 № 18630
'''
# Для какого наименьшего целого неотрицательного числа A выражение
#
# (3m + 4n > 63) ∨ ((m ≤ A) ∧ (n < A))
#
# тождественно истинно при любых целых неотрицательных m и n?

def F(m, n, A):
    return ((3*m + 4*n) > 63) or ((m <= A) and (n < A))

for A in range(0, 1000):
    flag = True
    for m in range(0, 1000):
        for n in range(0, 1000):
            if F(m,n,A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
'''
# Ответ: 21.



# Тип 15 № 34547
'''
# На числовой прямой даны два отрезка: P = [8, 39] и Q = [23, 58].
#
# Какова наименьшая возможная длина интервала A, при которой выражение
#
# ((x ∈ P) ∨ (x ∈ А)) → ((x ∈ Q) ∨ (x ∈ А))
#
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.

def F(a1, a2, x):
    return ((8 <= x <= 39) or (a1 <= x <= a2)) <= ((23 <= x <= 58) or (a1 <= x <= a2))

M = []
for a1 in range(1, 100):
    for a2 in range(1, 100):
        flag = True
        for x in range(1, 100):
            if F(a1, a2, x) == False:
                flag = False
                break
        if flag == True:
            M.append(a2-a1)
print(min(M)+1)
'''
# Ответ: 15





# endregion Урок: ******************************************************************************


# todo: Иван = [2, 5, 8, 12, 13, 14, 16, 17, 23, 24], на следующем уроке: добиваем 17, 24 номера, если останутся вопросы
