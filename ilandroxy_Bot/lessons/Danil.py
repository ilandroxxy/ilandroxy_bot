# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# 7 №11226
'''
a = 2
b = 4000  # Гц
c = 7 * 8

T = 56 * 60  # время передачи в сек
I = 86000 * T  # бит
t = I / (a * b * c)
print(t / 60)
'''
# Ответ: 11


# 8 №11227
'''
s = sorted('ЛОГАРИФМ')
num = 0
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if num % 2 == 0:
                        if slovo[:2] != 'ЛМ':
                            if slovo.count('И') >= 2:
                                cnt += 1
print(cnt)
'''
# Ответ: 1288


# 9 №11228
'''
from itertools import *
summa = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    copied_2 = [x for x in M if M.count(x) == 2]
    copied_3 = [x for x in M if M.count(x) == 3]
    if len(copied_3) == 3 and len(copied_2) == 4:
        if any(sum(p[:2]) % 2 != 0 and sum(p[2:]) % 2 != 0 for p in permutations(M[:4])):
            summa += sum(M)
print(summa)
'''

# 11 №11230
'''
symbols = 17
alphabet = 21  # 16 <= 21 <= 32
i = 5  # бит на один символ
bit = symbols * i
print(bit / 8)  # 10.625 -> 11
byte = 11
dop = 485
I = 4096 * (byte + dop)
print(I / (2**10))
'''
# 1984
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
    summa = sum(map(int, s))
    R.append(summa)
print(min(R))
'''
'''
from ipaddress import *
net = ip_network('192.168.31.80/255.255.255.240', 0)
maxi = 0
for ip in net:
    s = f'{ip:b}'
    maxi = max(maxi, s.count('1'))
print(maxi)
'''


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
# 739259957
# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Данил = [1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: 7, 8, 9
