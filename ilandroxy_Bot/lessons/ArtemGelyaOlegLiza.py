
# region Домашка: *********************************************************************

# endregion Домашка: ******************************************************************

# region Урок: *********************************************************************
'''
from math import prod
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = sorted([x for x in M if M.count(x) == 1])
    if len(copied) == 2 and len(not_copied) == 5:
        if prod(not_copied[:3]) > prod(copied):
            cnt += 1
print(cnt)
'''
# Ответ: 293


'''
pixels = 1280 * 960
I = 960 * 2**13  # бит

I = I / 0.85
print(I / pixels)  # i = 7.529, i ->
print(2**7)
'''


'''
s = '4783216434'
summa1 = sum([int(x) for x in s])
print(summa1)

summ2 = sum(map(int, s))
print(summ2)
'''
'''
M = [123, 21,321,3,123, ]
print([x for x in M if x > 10])
'''

'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if str(x)[-2:] == '21' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i:i+2]
    if (x in A) != (y in A):
        if (x**2 + y**2) >= max(A)**2:
            R.append(x + y)
print(len(R), max(R))
'''
# 74 103365


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


# № 12931 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
'''
s = open('24.txt').readline()
count = 4
maxi = 0
for i in range(len(s)-4):
    if s[i:i+5] in ('VWXYZ', 'WXYZV', 'XYZVW', 'YZVWX', 'ZVWXY'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 4
print(maxi)
'''
# Ответ: 40


# № 12254 ЕГКР 16.12.23 (Уровень: Базовый)
'''
s = open('24.txt').readline()
count = 2
maxi = 0
for i in range(len(s)-2):
    if s[i:i+3] in ('RSQ', 'SQR', 'QRS'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)
'''
# Ответ: 54


# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4142
'''
s = open('24.txt').readlines()
maxi = 0
for x in s:
    count = 2
    for i in range(len(x)-2):
        if x[i:i+3] in ('XYZ', 'YZX', 'ZXY'):
            count += 1
            maxi = max(maxi, count)
        else:
            count = 2
print(maxi)
'''

# № 16269 Джобс 03.05.24 (Уровень: Средний)
'''
s = open('24.txt').readline()
for a in 'TUVW':
    s = s.replace(a, ' ')
s = s.replace('XX', '**').replace('YY', '++').replace('ZZ', '--')
for a in "XYZ":
    s = s.replace(a, ' ')
while '++++' in s or '----' in s or '****' in s:
    s = s.replace('****', '** **').replace('++++', '++ ++').replace('----', '-- --')
print(max([len(x) for x in s.split()]))
'''

# № 16269 Джобс 03.05.24 (Уровень: Средний)
'''
s = open('24.txt').readline()
for a in 'TUVW':
    s = s.replace(a, ' ')
for a in 'XYZ':
    while a*4 in s:
        s = s.replace(a*4, f'{a*2} {a*2}')
    while a*3 in s:
        s = s.replace(a*3, f'{a*2} {a*2}')
print(max([len(x) for x in s.split()]))
print(max(map(len, s.split())))
'''

# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов,
# среди которых ровно по одному разу встречаются буквы X и Y.

# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов,
# среди которых ровно по одному разу встречаются буквы X и Y.

s = open('24.txt').readline()
s = s.replace('X', 'X ').replace('Y', 'Y ').split()
maxi = 0
for i in range(len(s)-2):
    r = ''.join(s[i:i+3])[:-1]
    if maxi < len(r):
        maxi = len(r)
        print(maxi, r.count('X') + r.count('Y'), r)
print(maxi)
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



