'''
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)
'''


# Тип 24 № 33526
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

'''
import string
f = open('24.txt', 'r')
s = f.readline()

M = []
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])
print(len(M))

Alphabet = string.ascii_uppercase
maxi = 0
for i in Alphabet:
    if maxi < M.count(i):
        print(i, M.count(i))
        maxi = M.count(i)
'''

'''
import string
f = open('24.txt', 'r')
s = f.readline()

M = []
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])
print(len(M))

Alphabet = string.ascii_uppercase
res = {}  # словарь - тип коллекции dict()
for i in Alphabet:
    res[i] = M.count(i)
print(res)

print(max(res.values()))
for key in res:
    if res[key] == 1517:
        print(key)
'''

'''
import  turtle

while True:
    turtle.getshapes()
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(100)
    turtle.right(120)
'''

# Метод Монте-карло
'''
import random

n = 1000000
k = 0
s0 = 16
for i in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if y**3 - 2*x**2 <= -1 and 2*y + x*83 <= 3:
        k += 1

S = (k/n) * s0  # Площадь фигуры
print(S)
'''

# Тип 15 № 34541
'''
# На числовой прямой даны два отрезка: Р = [3, 38] и Q = [21, 57].
# Какова наибольшая возможная длина интервала A, что логическое выражение
#
# ((х ∈ Q) → (х ∈ Р)) → ¬(х ∈ A)
#
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.

def F(a1, a2, x):
    return ((21 <= x <= 57) <= (3 <= x <= 38)) <= (not(a1 <= x <= a2))

M = []
for a1 in range(0, 100):
    for a2 in range(a1+1, 100):
        flag = True
        for x in range(0, 100):
            if F(a1, a2, x) == False:
                flag = False
                break
        if flag == True:
            M.append(a2-a1)
            print(max(M))
print(max(M)+1)
'''
# Ответ: 19


# Тип 15 № 15803  # Разобрать
'''
# На числовой прямой задан отрезок A. Известно, что формула
#
# ((x ∈ A) → (x**2 ≤ 100)) ∧ ((x**2 ≤ 64) → (x ∈ A))
#
# тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A?


def f(x, a):
    return ((x in a) <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= (x in a))


a = set([i for i in range(-1000, 1000)])

for x in range(-1000, 1000):
    if f(x, a) == False:
        a.remove(x)
print(len(a) - 1)
print(a)
M = []
for a1 in range(-1000, 1000):
    for a2 in range(a1+1, 1000):
        flag = True
        for x in range(0, 100):
            if F(a1, a2, x) == False:
                flag = False
                break
        if flag == True:
            M.append(a2-a1)
print(max(M)+1)
'''

# Тип 15 № 34512
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
#
# Например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
#
# Для какого наименьшего неотрицательного целого числа А формула
#
# x&77 ≠ 0 → (x&12 = 0 → x&А ≠ 0)
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной х)?

'''
def Conunctioun(m, n):
    M = bin(m)
    N = bin(n)
    M = M[2:]
    N = N[2:]


    M = [int(i) for i in M]
    N = [int(i) for i in N]


    while len(M) != len(N):
        if len(M) < len(N):
            M.reverse()
            M.append(0)
            M.reverse()
        else:
            N.reverse()
            N.append(0)
            N.reverse()

    A = []
    for i in range(len(M)):
        if M[i] == 1 and N[i] == 1:
            A.append(1)
        else:
            A.append(0)


    res = 0
    A.reverse()
    for i in range(0, len(A)):
        res += A[i] * 2 ** i
    return res

# x&77 ≠ 0 → (x&12 = 0 → x&А ≠ 0)
def F(x, A):
    return ((Conunctioun(x, 77) == 0) or ((Conunctioun(x, 12) != 0) or (Conunctioun(x, A) != 0)))

M = []
for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        print(F(x, A))
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        M.append(A)
print(max(A))

'''
for A in range(128):
    B = True
    for x in range(128):
        # x&77 ≠ 0 → (x&12 = 0 → x&А ≠ 0)
        if ((x&77==0) or (x&12!=0) or (x&A!=0))==0:
            B=False
    if B:
        print(A)
        break



