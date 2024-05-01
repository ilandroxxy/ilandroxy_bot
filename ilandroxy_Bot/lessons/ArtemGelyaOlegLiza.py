
# region Домашка: *********************************************************************

# endregion Домашка: ******************************************************************

# region Урок: *********************************************************************
'''
print('n k m l')
for n in 0, 1:
    for k in 0, 1:
        for m in 0, 1:
            for l in 0, 1:
                F = (not n) or (k and (not m)) or (l == m)
                if not F:
                    print(n, k, m, l)
                    # n k m l
                    # 1 0 0 1
                    # 1 0 1 0
                    # 1 1 1 0
'''
import shlex

'''
for n in range(1, 1000):
    s = f'{n:b}'
    if n % 2 == 0:
        s = '1' + s + '1'
    else:
        s += '10'
    r = int(s, 2)
    if r > 179:
        print(n)
        break
'''

'''
from turtle import *
lt(90)
tracer(0)
m = 20

for _ in range(2):
    fd(12 * m)
    rt(90)
    fd(19 * m)
    rt(90)

up()

fd(4 * m)
rt(90)
fd(6 * m)
lt(90 * m)

down()

color('green')

for _ in range(4):
    fd(12 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(2, 'red')


done()
'''

'''
pixels = 1079 * 1919
colors = 7999   # i -> 13
print(2**13)
i = 13
I = pixels * i  # бит на одну картинку
I = I * 199
print(I / 19_999_999)
'''
'''
from itertools import *
num = 0
for s in product("АЁРТШ", repeat=5):
    slovo = ''.join(s)
    num += 1
    if slovo.count('А') <= 1 and 'ЁЁ' not in slovo:
        print(num, slovo)
        break
'''


# Определите количество строк таблицы,
# содержащих числа, для которых выполнены все условия:
# четыре числа строки можно разбить на две пары чисел с равными суммами
# максимальное число строки меньше суммы трёх оставшихся чисел
# сумма чисел в строке чётна
'''
from itertools import permutations
cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
        if max(M) < (M[0] + M[1] + M[2]):
            if sum(M) % 2 == 0:
                cnt += 1
print(cnt)
'''

'''
symbols = 7
print(2**13)
i = 14  # 2**13 < 8198 < 2**14
bit = symbols * i
print(bit / 8)  # 12.25
byte = 13
print((byte * 20240) / (2 ** 10))
'''

'''
s = '7' * 47
while '2222' in s or '7777' in s:
    if '2222' in s:
        s = s.replace('2222', '77', 1)
    else:
        s = s.replace('7777', '22', 1)
print(s)
'''

'''
from ipaddress import *
net = ip_network('114.179.203.128/255.255.255.192', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 3 == 0:
        cnt += 1
print(cnt)
'''

'''
from string import *
alphabet = digits + ascii_uppercase
for x in alphabet[:29]:
    A = int(f'42{x}158', 29)
    B = int(f'16{x}234', 29)
    if (A + B) % 28 == 0:
        print((A + B) // 28)
'''
'''
def F(a1, a2, x):
    B = 74 <= x <= 194
    C = 152 <= x <= 223
    A = a1 <= x <= a2
    return ((not A) and B) <= (B <= (not C))


R = []
M = [x / 4 for x in range(70*4, 225*4)]
for a1 in M:
    for a2 in M:
        if all(F(a1, a2, x) for x in M):
            R.append(a2 - a1)
print(min(R))
'''
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n <= 12:
        return 1
    if n > 12:
        return F(n-1) + n - 2

print(F(2024) - F(2020))
'''

'''
from functools import *

@lru_cache(None)
def F(n):
    if n < 3:
        return n
    if n > 2 and n % 2 != 0:
        return F(n-1) + F(n-2) + 1
    if n > 2 and n % 2 == 0:
        return sum([F(i) for i in range(1, n)])

print(F(38))
'''
# 9182657279

'''
from functools import *
S = set()

@lru_cache(None)
def F(a, k):
    if k == 68:
        S.add(a)
        return 0
    return F(a+3, k+1) + F(a-2, k+1)


F(1, 0)
print(len(S))
'''
# Ответ: 69

'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if x % 21 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x > max(A) or y > max(A):
        R.append(x + y)
print(len(R), min(R))
'''

'''
def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a * 2, b)

print(F(3, 6) * F(6, 12) * F(12, 16))
'''

'''
s = open('24.txt').readline()
for a in 'AEOU':
     s = s.replace(a, 'A')
for a in 'KLMN':
    s = s.replace(a, 'M')
while 'MM' in s or 'AA' in s:
    s = s.replace('MM', 'M M').replace('AA', 'A A')
print(max([len(x) for x in s.split()]))


# Вариант 2
s = open('24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if (s[i] in 'AEOU' and s[i+1] in 'KLMN') or (s[i+1] in 'AEOU' and s[i] in 'KLMN'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '10*2024?'):
        print(x // 2024)
'''

# ABSBDBSADBASBABDSBADBSABDASB
# A ABSBDBSA ADBA ASBA ABDSBA ADBSA ABDA ASB  maxi = 8
# ABSBDBSADBASBABDSBADBSABDASB
# AB BSBDB BSADB BASBAB BDSB BADB BSAB BDASB B maxi = 8
# ABSBDBSADBASBABDSBADBSABDASB
# ABSBD DBSAD DBASBABD DSBAD DBSABD DASB maxi = 8
# ABSBDBSADBASBABDSBADBSABDASB
'''
s = open('24.txt').readline()
maxi = 0
for a in 'ABCDEFGHIJKLM':
    s = s.replace(a, f'{a} {a}')
    maxi = max(maxi, max([len(x) for x in s.split()]))
    s = s.replace(f'{a} {a}', a)

print(maxi)
'''
# Ответ: 322

'''
def F(a, b):
    if a <= b or a == 12 or a == 15:
        return a == b
    if a % 2 == 0:
        return F(a // 2, b)
    if a % 3 == 0:
        return F(a // 3, b)
    return F(a - 1, b) 

print(F(19, 1))

'''
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if str(x)[-3:] == '538']
R = []
for i in range(len(M)-3):
    x, y, z, w = M[i:i+4]
    lenght = [len(str(abs(a))) for a in (x, y, z, w)]
    if 2 <= lenght.count(5) < 4:
        krat_3 = [a for a in (x, y, z, w) if a % 3 == 0]
        krat_7 = [a for a in (x, y, z, w) if a % 7 == 0]
        if len(krat_3) > len(krat_7):
            if max(A) < (x + y + z + w) < max(A) * 2:
                R.append(x + y + z + w)
print(len(R), max(R))
'''



# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo Разобрать новые 22 номера № 12474 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый)

# todo Тип 24 №55641
'''
f = open('24.txt').readlines()пш
li = []
for j in f:
    st = ''
    for x, y in zip(j, j[1:]):
        if x == 'T':
            st += y
    maxi = max(st.count(i) for i in set(st))
    for s in set(st):
        if st.count(s) == maxi:
            li += [s]
print(max(li.count(l) for l in set(li)))
'''


# todo - Разобрать Тип 13 №64943
# Узлы с IP -адресами 202.3.20.24 и 202.3.27.11 находятся в одной сети.
# Укажите наименьшее возможное количество принадлежащих этой сети IP-адресов,
# в двоичной записи которых чётное число единиц.
'''
from ipaddress import *
mini = 10**9
for mask in range(32+1):
    cnt = 0
    net1 = ip_network(f'202.3.20.24/{mask}', 0)
    net2 = ip_network(f'202.3.27.11/{mask}', 0)
    if net1 == net2:
        for ip in net1:
            s = f'{ip:b}'
            if s.count('1') % 2 == 0:
                cnt += 1
    maxi = max(maxi, cnt)
    print(maxi)
'''
# Ответ: 2048


# todo Разобрать задачку https://stepik.org/lesson/1231755/step/9?unit=1245338
# (А.Богданов) В файле содержится последовательность натуральных чисел.
# Рассматриваются все пары элементов, в которых только один элемент чётный,
# и между элементами пары есть ровно один элемент и он кратен минимальному
# четному элементу из всех элементов последовательности.
# Найти количество таких пар и пару с минимальной суммой.
'''
M = [int(i) for i in open('17.txt')]
n = min([i for i in M if i % 2 == 0])  # минимальному четному элементу из всех элементов последовательности
B = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        z = M[M.index(x) + 1]
        if M.index(y) - M.index(x) == 2:
            if (x % 2 == 0) != (y % 2 == 0):
                if z % n == 0:
                    B.append(x + y)
print(len(B), min(B))
'''
#  0  1  2  3  4
# [4, 5, 6, 7, 8]

'''
M = [int(i) for i in open('17.txt')]
n = min([i for i in M if i % 2 == 0])  # минимальному четному элементу из всех элементов последовательности
count = 0
mini = 9999999
r = ''
for i in range(len(M) - 2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x % 2 == 0) != (z % 2 == 0):
        if y % n == 0:
            count += 1
            if mini > x + z:
                mini = x + z
                r = [x, y]
print(count, r)
'''


# endregion Разобрать: *************************************************************


# GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:



