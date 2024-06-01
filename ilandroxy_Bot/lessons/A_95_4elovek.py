# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# № 15330 Досрочная волна 2024 (Уровень: Базовый)
'''
def F(x, a1, a2):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return C <= (((not A) and B) <= (not C))


R = []
M = [x / 4 for x in range(10 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2-a1)
print(min(R))
'''

# № 12469 (Уровень: Базовый)
'''
def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))

R = []
M = [x / 4 for x in range(2*4, 120*4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 22
'''
'''
maxi = 0
for n in range(4, 100):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum(map(int, s))
    maxi = max(maxi, summa)
print(maxi)
'''

'''
s = '8' * 45
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '88', 1)
    else:
        s = s.replace('8888', '11', 1)
print(s)  # 888
'''

'''
x = 4*3125**2019 + 3*625**2020 -2*125**2021+25**2022-4*5**2023-2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
print(len([i for i in M if i > 10]))  # 3030
'''
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:27]:
    A = int(f'123{x}24', 27)
    B = int(f'135{x}78', 27)
    if (A + B) % 26 == 0:
        print((A + B) // 26)
'''
# 1213206

'''
from fnmatch import *
for x in range(98591, 10**10, 98591):
    if fnmatch(str(x), '5?2*3?3?'):
        print(x, x // 98591)
'''


# № 13868 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '112?57*4'):
        summa = sum(map(int, str(x)))
        if summa % 2 != 0:
            print(x, x//2024)
'''


# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
'''
def prime(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

from fnmatch import *
for x in range(10**7):
    if fnmatch(str(x), '3?1111*'):
        if prime(x):
            print(x)
'''

'''
R = []
for n in range(1, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + f'{x:b}'
    r = int(s, 2)
    if r >= 195:
        R.append(r)
print(min(R))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    result = ''
    while num > 0:
        result += alphabet[num % base]
        num //= base
    return result[::-1]


R = []
for n in range(1, 1000):
    s = convert(n, 4)
    if n % 3 == 0:
        s = s[-1] + s[1:-1] + s[0] + '1'
    else:
        s = s + str(n % 3)
    r = int(s, 4)
    if r <= 340:
        R.append(r)
print(max(R))
'''

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    result = ''
    while num > 0:
        result += alphabet[num % base]
        num //= base
    return result[::-1]


for n in range(1, 1000):
    s = convert(n, 2)
    print(s)
    if n % 2 == 0:
        s = s + s[-2:]
    else:
        s = '1' + s + '0'
    print(s)
    R = int(s, 2)

    if R < 100:
        print(n)

# endregion Урок: ***************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Сева = [1, 2, 3, 4, 6, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25]
# КЕГЭ  = [5, 12, 14, 15, 16, 23, 25]
# на следующем уроке: 8, 9, 17, 24
