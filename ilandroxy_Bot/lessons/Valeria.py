# На следующий урок: системы счисления + 14 номер

# Home work 6.10
# Задание 2 № 29109
'''
# Логическая функция F задаётся выражением ((z → w) ∨ (y ≡ w))∧((x∨z) ≡ y).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

# Решение:

print('z w y x')
for z in range(2):
    for w in range(2):
        for y in range(2):
            for x in range(2):
                F = ((z <= w) or (y == w)) and ((x or z) == y)
                if F == True:
                    print(z, w, y, x, F)
'''
# Ответ: zyxw



# Задание 2 № 15912
# Логическая функция F задаётся выражением ((x → y ) ≡ (z → w)) ∨ (x ∧ w).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

# Решение:
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) == (z <= w)) or (x and w)
                if F == False:
                    print(x, y, z, w, F)
'''
# Ответ: zyxv

# Negatives, Zeros and Positives
# Решение:
'''
n = int(input())
A = [int(input()) for _ in range(n)]
N = []
Z = []
P = []
for i in A:
    if i < 0:
        N.append(i)
    elif i == 0:
        Z.append(i)
    else:
        P.append(i)
# B = N + Z + P
# for b in B:
#    print(b, '\n')
print(*N)

print(*Z)

print(*P)
'''

'''
n = int(input())
A = [int(input()) for _ in range(n)]

for i in A:
    if i < 0:
        print(i, end=" ")
print()

for i in A:
    elif i == 0:
        print(i, end=" ")
print()

for i in A:
    if i == 0:
        print(i, end=" ")
print()

for i in A:
    if i > 0:
        print(i, end=" ")
print()
'''



# Список четных
# Решение:

'''
n = int(input())
if n < 2:
    print('Error')
#print([i for i in range(2, n + 1, 2)])
A = [i for i in range(2, n + 1) if i % 2 == 0]  # Списочное выражение
print(A)
'''

'''
n = int(input())
A = []
for i in range(1, n+1):
    if i % 2 == 0:
        A.append(i)
print(A)
'''



# Символы всех строк
# Решение:
'''
n = int(input())
STR = ""
for _ in range(n):
    STR += input()
    
A = [i for i in STR]
print(A)



n = int(input())
M = []
for _ in range(n):
    for i in input():
        M.append(i)
print(M)
'''


'''

import math  # подключить библиотеку к файлу

x = math.factorial(5)
print(x)

print(math.pow(4, 2))


import math as m  # сократить имя билиотеки

x = m.factorial(5)
print(x)

print(m.pow(4, 2))

from math import gcd, lcm  # вытащить только определенные методы из библиотеки

print(gcd(24, 12))
print(lcm(24, 12))

from math import *  # подключить сразу все методы без использования math.

print(sqrt(16))
print(factorial(6))
'''

# Способ самим посчитать факториал
'''
x = int(input('x: '))
factorial = 1
while x > 0:
    factorial *= x
    x -= 1
print(factorial)

def Factorial(x):
    factorial = 1
    while x > 0:
        factorial *= x
        x -= 1
    return factorial

print(Factorial(5))
'''

# Ввод списков с клавиатуры
B = [int(i) for i in input().split()]   # Сплит - это метод убирающий пробелы из строки
print(B)

A = [int(input()) for _ in range(int(input()))]
print(A)

n = int(input())
M = []
for i in range(n):
    M.append(int(input()))
print(M)


