

# region Домашка:  **************************************************

'''
# Тип 5 № 28681
for n in range(128, 256):
    s = bin(n)[2:]
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    if n - int(s, 2) == 105:
        print(n)
'''

# Тип 16 № 7273
'''
def F(x):
    if x == 1:
        return 1
    if x > 1:
        return F(x - 1) * (2 * x + 1)
print(F(4))
'''

# № 5458
'''
def F(x):
    if x <= 2:
        return 2
    if x > 2:
        return F(x - 1) + 2 * F(x - 2)
print(F(5))
'''

# № 5554
'''
def F(x):
    if x <= 2:
        return x + 1
    if x > 2:
        return F(x - 1) + 3 * F(x - 2)
print(F(4))
'''

# Тип 23 № 45257
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 2, b) + F(a * 2, b)
print(F(1, 18) * F(18, 52))
'''

# № 13633
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a * 2, b) + F(a * 3, b)
print(F(2, 15) * F(15, 30))
'''

# № 18828
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 3, b) + F(a * 3, b)
print(F(4, 10) * F(10, 17) * F(17, 23))
'''

# endregion Домашка: **************************************************


# region Урок:  **************************************************

# Тип 15 № 9320
'''
# Для какого наименьшего натурального числа А формула
# ДЕЛ(x, А) → (ДЕЛ(x, 21) + ДЕЛ(x, 35))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

def F(x, A):
    return (x % A == 0) <= ((x % 21 == 0) or (x % 35 == 0))  # ДЕЛ(x, А) → (ДЕЛ(x, 21) + ДЕЛ(x, 35))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''
# Ответ: 21




# Тип 15 № 26990
'''
# Для какого наибольшего целого неотрицательного числа A выражение
# (x > A) ∨ (y > A) ∨ (2y + x < 110)
# тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?

def F(x, y, A):
    return (x > A) or (y > A) or (2*y + x < 110)

for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if F(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
'''
# Ответ: 36



# Тип 15 № 34508
'''
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
#
# x & 29 ≠ 0 → (x & 12 = 0 → x & А ≠ 0)
#
# тождественно истинна (то есть принимает значение 1 при любом неотрицательном целом значении переменной х)?

def F(x, A):
    Q = x & 29 != 0
    W = x & 12 == 0
    R = x & A != 0
    return Q <= (W <= R)
    # return (x & 29 != 0) <= ((x & 12 == 0) <= (x & A != 0))

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
# Ответ: 17



# Тип 15 № 34535
# На числовой прямой даны три отрезка: P = [10, 40], Q = [5, 15] и R = [35, 50].
# Какова наименьшая возможная длина промежутка A, что формула
# ( (x ∈ А) ∨ (x ∈ P) ) ∨ ((x ∈ Q)→ (x ∈ R))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

# Вариант 1 -> плохой вариант для работы с отрезками, потому что ошибается на +- 1
'''
def F(x, a1, a2):
    A = a1 <= x <= a2
    P = 10 <= x <= 40
    Q = 5 <= x <= 15
    R = 35 <= x <= 50
    return (A or P) or (Q <= R)
    # return ((a1 <= x <= a2) or (10 <= x <= 40)) or ((5 <= x <= 15) <= (35 <= x <= 50))

M = []
for a1 in range(0, 60):
    for a2 in range(0, 60):
        flag = True
        for x in range(0, 100):
            if F(x, a1, a2) == False:
                flag = False
                break
        if flag == True:
            M.append(a2 - a1)
print(min(M))
'''

# Вариант 2
'''
def F(x):
    A = a1 <= x <= a2
    P = 10 <= x <= 40
    Q = 5 <= x <= 15
    R = 35 <= x <= 50
    return (A or P) or (Q <= R)

liner = [i/4 for i in range(1*4, 60*4)]
print(liner)

M = []
for a1 in liner:
    for a2 in liner:
        if all(F(x) == True for x in liner):
            M.append(a2 - a1)
print(min(M))
'''
# Ответ: 5

# 3.8  # round(3.8) --> 4
# 3.3  # round(3.3) --> 3

# 3.8  #  int(3.8) + 1 --> 3 + 1 = 4
# 3.3  #  int(3.3) + 1 --> 3 + 1 = 4



# Тип 15 № 7763
'''
# На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23]. Укажите наибольшую возможную длину промежутка A, для которого формула
#
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
#
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

def F(x):
    A = a1 <= x <= a2
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    return (P == Q) <= (not A)

liner = [i/4 for i in range(1*4, 60*4)]
print(liner)

M = []
for a1 in liner:
    for a2 in liner:
        if all(F(x) == True for x in liner):
            M.append(a2 - a1)
print(max(M))
'''
# Ответ: 9


# Тип 15 № 47012
''' 
# На числовой прямой даны два отрезка: P=[69;91] и Q=[77;114]. Укажите наименьшую возможную длину такого отрезка A, для которого формула
#
# (x∈P)→(¬((x∈P)≡(x∈Q))∨((x∈Q)→(x∈A)))
#
# тождественно истинна (т.е. принимает значение 1 при любом значении переменной х).

def F(x):
    A = a1 <= x <= a2
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    return P <= ((not(P == Q)) or (Q <= A))

liner = [i/4 for i in range(50*4, 120*4)]
print(liner)

M = []
for a1 in liner:
    for a2 in liner:
        # flag = True
        # for x in liner:
        #     if F(x) == False:
        #         flag = False
        #         break
        # if flag == True:
        #     M.append(a2 - a1)
        if all(F(x) == True for x in liner):
            M.append(a2 - a1)
print(min(M))
'''
# Ответ: 14

# endregion Урок:  **************************************************


# todo: Татьяна = [2, 5, 8, 12, 14+, 15.1, 16, 23], на следующем уроке: Вопросы по 15 номеру, Разбираем задачи на отрезки и множества