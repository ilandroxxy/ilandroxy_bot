# region Домашка:  **************************************************

# 16
'''
import sys
sys.setrecursionlimit(1000000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 2 + F(n-1)

print(F(2023) - F(2021))


# F(2023) = 2023 - 2 + F(2022)
# F(2022) = 2022 - 2 + F(2021)
print(2023 - 2 + 2022 - 2)
'''


# 15
'''
def F(x, y, A):
    return (y + 3*x > A) or (x < 20) or (y < 50)

for A in range(0, 1000):
    if all(F(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        print(A)
'''

# 8
'''
s = sorted('ПЯТНИЦА')
k = 1
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if a != 'Ц' and slovo.count('И') == 2:
                            if k % 2 != 0:
                                count += 1
                                print(k, slovo)
                        k += 1
print(count)
'''

# 24
'''
s = open('files/24.txt').readline()
# s = 'HHHHHHHHHHHHHHAAABBBHHHHHHCCACACAHHHHHHHACHHHHHHHHHHHHCBB'
s = s.replace('A', 'C').replace('B', 'C')

while 'CC' in s:
    s = s.replace('CC', 'C C')
print(s)
M = [len(i) for i in s.split()]
print(max(M))
'''


'''
s = open('24.txt').readline()
# s = 'HHHHHHHHHHHHHHAAABBBHHHHHHCCACACAHHHHHHHACHHHHHHHHHHHHCBB'
count = 1
maxi = 1
a = ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) not in a:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

# 9
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == 5 and all(M.count(x) <= 2 for x in M):
        copied = (sum(M) - sum(set(M))) * 2
        sred_copied = copied / 4
        sred = (sum(M) - copied) / 3
        if sred_copied > sred:
            count += 1
print(count)
'''

'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    another = [x for x in M if M.count(x) == 1]
    if len(copied) == 0 or len(another) == 0:
        continue
    flag1 = len(set(copied)) == 2 and len(another) == 3
    flag2 = sum(copied)/len(copied) > sum(another)/len(another)
    if flag1 + flag2 == 2:
        count += 1
print(count)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:15]:
    r = int(f'98{x}79641', 22) + int(f'25{x}43', 22) + int(f'63{x}5', 22)
    if r % 21 == 0:
        print(r // 21)
'''



'''
def troich(x):
    M = []
    while x > 0:
        M.append(x % 3)
        x //= 3
    M.reverse()
    return M


for n in range(1, 1000):
    M = troich(n)

    if n % 3 == 0:
        M = M + M[-2:]
    else:
        M = M + troich(5 * (n % 3))

    s = ''.join([str(x) for x in M])
    r = int(s, 3)

    if r >= 146:
        print(n)
        break
'''


'''
def troich(x):
    s = ""
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

for n in range(1, 1000):
    s = troich(n)

    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + troich(5 * (n % 3))

    r = int(s, 3)

    if r >= 146:
        print(n)
        break
'''

# (Х * у < А) or(x<y)or (10<x)
'''
def F(x, y, A):
    return (x * y < A) or (x < y) or (10 < x)

for A in range(0, 1000):
    if all(F(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break
'''


'''
from fnmatch import fnmatch

def Divisors(x):
    dl = set()
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            dl.add(j)
            dl.add(x//j)
    return sorted(dl)
'''
'''
for i in range(2031, 10**9, 2031):
    if fnmatch(str(i), '*31*65?') and i % 31 == 0:
        dll = Divisors(i)
        for n in range(0, 100):
            if len(dll) == 2**n:
                print(i, i//2031)
'''

'''  
from fnmatch import *
m = [2**i for i in range(1,100)]
print(m)
for x in range(2031, 10**9, 2031):
    if fnmatch(str(x), '*31*65?'):
        if x % 31 == 0:
            d = set()
            for j in range(1, int(x**0.5)+1):
                if x % j == 0:
                    d.add(j)
                    d.add(x // j)
            if len(d) in m:
                print(x, x // 2031)
'''


'''
f = open('26.txt')
k = int(f.readline())
hub = [0] * k
n = int(f.readline())
count = 0

pairs = []
for _ in range(n):
    pairs.append(list(map(int, f.readline().split())))
pairs = sorted(pairs)

for pair in pairs:
    start, end = pair
    for j in range(k):
        if start > hub[j]:
            hub[j] = end
            count += 1
            print(count, j+1)
            break
'''

'''
f = open('27-A.txt')
n = int(f.readline())
k = int(f.readline())
M = [int(i) for i in f]
maxi = 0
for i in range(0, n):
    for j in range(i+k, n):
        for y in range(j+k, n):
            maxi = max(maxi, M[i] * M[j] * M[y])

print(maxi)
'''
from itertools import *
k = 1
count = 0
for s in product(sorted('ПЯТНИЦА'), repeat=6):
    slovo = ''.join(s)
    if slovo[0] != 'Ц' and slovo.count('И') == 2:
        if k % 2 != 0:
            count += 1
    k += 1
print(count)

# И сколько слов с нечетными номерами, которые не начинаются с Ч и имеют не менее 1 Ж

from itertools import *
k = 1
count = 0
for s in product(sorted('МУЖЧИНА'), repeat=6):
    slovo = ''.join(s)
    print(k, slovo)
    if k == 100:
        break
    if slovo[0] != 'Ч' and slovo.count('Ж') >= 1:
        if k % 2 != 0:
            count += 1
    k += 1
print(count)

'''
1аааааА
2аааааЖ
3аааааИ
4аааааМ
5аааааН
6аааааУ
7аааааЧ
'''



# endregion Урок:  **************************************************


# Татьяна решить номер 5672
# todo: Татьяна РЕШУ = [1, 2, 3, 4, 5, 6, 7, 8, 9.1, 10, 11, 12, 13, 14+, 15+, 16, 17, 18, 19-21, 22, 23, 24, 25]
# todo: Татьяна КЕГЭ = [5, 8, 24, 25]
# на прошлом уроке:
# на следующем уроке: #todo: разобрать 26 номер 5 варианта Шастина
