# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
R = []
for n in range(1, 1000):
    s = bin(n)[2:]  # s = f'{n:b}'
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
pixels = 1280*960
I = (920 * 2**13)  # бит
I = I + I * 0.15
print(I / pixels)  # 6.133 -> 6
i = 7

print(2**i)
'''
# Ответ: 128


'''
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
import math
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = sorted([x for x in M if M.count(x) == 1])
    if len(copied) == 2 and len(not_copied) == 5:
        if math.prod(not_copied[:3]) > math.prod(copied):
            cnt += 1
print(cnt)
'''

'''
maxi = 0
for n in range(4, 10000):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum(map(int, s))
    if maxi < summa:
        maxi = summa
        print(maxi)
'''

'''
from ipaddress import *
net = ip_network('112.208.0.0/255.255.128.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 11 == 0:
        cnt += 1
print(cnt)
'''

'''
x = 4*3125**2019 + 3*625**2020 -2*125**2021 +25**2022 -4*5**2023 - 2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
M.reverse()
print(len([i for i in M if i > 10]))
'''


M = [int(x) for x in open('17.txt')]
D = [x for x in M if str(x)[-2:] == '21' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i:i+2]
    if (x in D) != (y in D):
        if (x**2 + y**2) >= max(D) ** 2:
            R.append(x + y)
print(len(R), max(R))

# 74 103365


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Лера = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 12, 14, 15, 16, 23]
# на следующем уроке: повторять все номера кодом, 7, 11
