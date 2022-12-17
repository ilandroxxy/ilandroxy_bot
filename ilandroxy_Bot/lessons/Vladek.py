
# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not y)) <= ((z <= (not w)) and (w <= y))
                print(x, y, z, w, F)
'''

# 5
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]

    for _ in range(3):
        m = int(s, 2)
        summ = sum([int(i) for i in str(m)])
        if summ % 2 != 0:
            s += '1'
        else:
            s += '0'

    r = int(s, 2)
    if r > 1028:
        M.append(r)
print(min(M))
'''
# Ответ: 1035

# 14
'''
s = 'ВЕРОНИКА'
s1 = 'ЕОИА'
s2 = 'ВРНК'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        summ_glas = 0
                        summ_sogl = 0
                        for x in temp:
                            if x in s1:
                                summ_glas += 1
                            else:
                                summ_sogl += 1
                        if summ_glas > summ_sogl:
                            print(temp)
                            count += 1
print(count)
'''
# Ответ: 90112

# 14
'''
for x in range(2, 37+1):
    A = [1, 2, 3, x]
    B = [4, x, 5, 9]
    A.reverse()
    B.reverse()

    a, b = 0, 0
    for i in range(4):
        a += A[i] * 37 ** i
        b += B[i] * 37 ** i

    if (a + b) % 36 == 0:
        print((a + b) // 36)
        break
'''


'''
def F(x, y, A):
    Q = 144 % x == 0
    W = x % y == 0
    R = (x + y) > 100
    T = (A - x) > y
    return (Q <= (not W)) or R or T

for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break
'''
# Ответ: 97




# Тип 15 № 13364
'''
# На числовой прямой даны два отрезка: P = [130; 171] и Q = [150; 185]. Укажите наименьшую возможную длину такого отрезка A, что формула
#
# (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
#
# истинна при любом значении переменной х, т.е. принимает значение 1 при любом значении переменной х.

def F(x):
    P = 130 <= x <= 171
    Q = 150 <= x <= 185
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

L = [i/4 for i in range(100*4, 200*4)]


M = []
for a1 in L:
    for a2 in L:
        if all(F(x) for x in L) == True:
            M.append(a2-a1)
print(min(M))
'''


'''
from functools import *
@lru_cache()
def F(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n > 1:
        return F(n-1) - F(n-2) + 3*n

print(F(40))
'''


'''
from functools import *
@lru_cache(None)
def F(n):
    if n == 0:
        return 0
    else:
        return F(n // 10) + (n % 10)

count = 0
for n in range(237_567_892, 1_134_567_009):
    if F(n) > F(n+1):
        count += 1
print(count)
'''



# Тип 25 № 38959
# Пусть M(N)— произведение 5 наименьших различных натуральных делителей натурального числа N, не считая единицы. Если у числа N меньше 5 таких делителей, то M(N) считается равным нулю.
#
# Найдите 5 наименьших натуральных чисел, превышающих 200000000, для которых0<M(N)<N. В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.
'''
def D(n):
    dl = set()
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
            if len(dl) > 10:
                return sorted(dl)
    return sorted(dl)

k = 0
for n in range(200000000+1, 300000000):
    dl = D(n)
    if len(dl) > 5:
        M = dl[0] * dl[1] * dl[2] * dl[3] * dl[4]
        if 0 <= M <= n:
            print(M)
            k += 1
            if k == 5:
                break
'''
# Ответ:
# 1728
# 21632
# 1260
# 1152
# 4127787


# Тип 25 № 27852
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [185311;185330], числа, имеющие ровно четыре различных натуральных делителя.
# Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки. Делители в строке должны следовать в порядке возрастания.
#
# Например, в диапазоне [12;14] ровно четыре различных натуральных делителя имеет число 14, поэтому для этого диапазона вывод на экране должна содержать следующие значения:

'''
def F(x):
    dl = set()
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            dl.add(j)
            dl.add(x // j)
            if len(dl) > 4:
                return dl
    return sorted(dl)

for x in range(185311, 185330 + 1):
    dl = F(x)
    if len(dl) == 4:
        print(*dl)
'''

# Ответ:
# 1 2 92657 185314
# 1 47 3943 185321
# 1 241 769 185329
# endregion Урок: ******************************************************************


# todo: Владек = [2, 5, 8, 12, 14+, 15, 16, 23, 25.1], на следующем уроке: 25 номер на Mки, маски, N = 2**m*3**n