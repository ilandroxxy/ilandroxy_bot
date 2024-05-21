# region Домашка: ************************************************************

# КЕГЭ № 10577 (Уровень: Базовый)
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети.
# Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.
#
# Два узла, находящиеся в одной сети, имеют IP-адреса 165.112.200.70 и 165.112.175.80.
# Найдите наибольшее возможное количество единиц в двоичной записи маски подсети.
'''
from ipaddress import *
maxi = 0
for mask in range(32+1):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        # print(net1, mask, net1.netmask)
        maxi = max(maxi, mask)
print(maxi)
'''
# Ответ: 17

# endregion Домашка: *********************************************************


# region Урок: ************************************************************

'''
# Вариант 1
s = '0123456'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if num[0] != '0':  # if a != '0':
                                chet = [x for x in num if x in '0246']
                                if len(chet) == 2:
                                    cnt += 1
print(cnt)

# Вариант 2
from itertools import *
cnt = 0
for s in product('0123456', repeat=7):
    num = ''.join(s)
    if num[0] != '0': 
        chet = [x for x in num if x in '0246']
        if len(chet) == 2:
            cnt += 1
print(cnt)
'''

'''
from math import prod
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = sorted([x for x in M if M.count(x) == 1])
    if len(copied) == 2 and len(not_copied) == 5:
        print(copied, not_copied)
        if prod(not_copied[:3]) > prod(copied):
            cnt += 1
print(cnt)
'''

'''
# Вариант 1
x = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
cnt = 0
while x > 0:
    if x % 25 > 10:
        cnt += 1
    x //= 25
print(cnt)

# Вариант 2
x = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
print(len([a for a in M if a > 10]))
'''


'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''
# Ответ: 196

'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n <= 3:
        return 2025
    if n > 3:
        return 3 * (n-1) * F(n-2)

print(F(2027) / F(2023))

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
'''
# 36905616.0 -> 36905616

'''
from functools import *

@lru_cache(None)
def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * f(n-2) - f(n-1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * f(n-1) + f(n-2) - 2

print(f(170))
'''
# Ответ: 3596910688800

'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if str(x)[-2:] == '21' and len(str(abs(x))) == 5]
R = []  # Будем складывать суммы пар (то есть искать наибольшую сумму и кол-во пар)
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A and y not in A) or (y in A and x not in A):
        if (x**2 + y**2) >= max(A) ** 2:
            R.append(x+y)
print(len(R), max(R))
'''
# Ответ: 74 103365

'''
s = open('24.txt').readline()
count = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] in ('KLMN', 'LMNK', 'MNKL', 'NKLM'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 3
print(maxi)
'''
# Ответ: 182

# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Максим = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ = [16]
# на следующем уроке:
