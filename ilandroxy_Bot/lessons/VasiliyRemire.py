
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

'''
a = 2
b = 4000  # Гц
c = 7 * 8
# t - ?
# I - ?

T = 56 * 60
U = 86000  # бит/с
I = U * T

t = I / (a * b * c)  # сек
print(t / 60)  # 10.75
'''
# Ответ: 11


'''
R = []
for n in range(4, 2000):
    s = '3' * n + '5'
    while '23' in s or '5333' in s or '33333' in s:
        if '23' in s:
            s = s.replace('23', '3', 1)
        if '5333' in s:
            s = s.replace('5333', '32', 1)
        if '33333' in s:
            s = s.replace('33333', '55', 1)
    # summa = sum(map(int, s))
    summa = sum(int(x) for x in s)
    R.append(summa)
print(min(R))
'''
# Ответ: 10

'''
from ipaddress import *
maxi = 0
net = ip_network('192.168.31.80/255.255.255.240', 0)
for ip in net:
    s = f'{ip:b}'
    maxi = max(maxi, s.count('1'))
print(maxi)
'''
# Ответ: 16

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:26]:
    A = int(f'27{x}98876', 26)
    B = int(f'26{x}51', 26)
    C = int(f'15{x}47', 26)
    D = int(f'62{x}5', 26)
    if (A + B + C + D) % 25 == 0:
        print((A + B + C + D) // 25)
'''
# Ответ: 739259957

'''
def F(x, A):
    B = 120 <= x <= 130
    return (B <= (x % 7 != 0)) or (A > 2*x)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
        break
'''


# № 16262 Джобс 03.05.24 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return C <= (((not A) and B) <= (not C))


R = []
M = [x / 4 for x in range(10*4, 120*4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 43.0 -> 43, 43.2 -> 43, 43.7 -> 48
'''
# Ответ: 43

'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n <= 6:
        return n
    if n > 6:
        return 2*n + 3 + F(n-1)

print(F(6188) - F(6185))

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
'''
# Ответ: 37131

'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if len(str(abs(x))) == 2]
B = [x for x in M if len(str(abs(x))) == 4 and str(x)[-1] == '1']
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if len([p for p in (x, y, z) if p > min(A) ** 2]) == 2:
        if (x * y * z) % max(B) == 0:
            R.append(abs(x) + abs(y) + abs(z))
print(len(R), max(R))
'''

'''
def F(a, b, c: str):
    if a > b:
        return 0
    if a == b:
        return 1
    if c == 'B':
        return F(a + 2, b, 'A') + F(a * 3, b, 'C')
    return F(a+2, b, 'A') + F(a**2, b, 'B') + F(a * 3, b, 'C')

print(F(2, 64, ''))
'''

'''
s = open('24.txt').readline()
for a in 'ABCD':
    s = s.replace(a, ' ')
print(max([len(x) for x in s.split()]))
'''

'''
from fnmatch import *
for x in range(2919, 10**10, 2919):
    if fnmatch(str(x), '9*253?74'):
        print(x, x // 2919)
'''


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Василий = [1, 2, 3, 4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [3, 13, 14, 15]
# на следующем уроке:
