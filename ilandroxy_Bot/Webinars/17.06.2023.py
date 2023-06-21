
#
'''
print('x y z w F')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    F = (z <= w) and y and (not x)
                    print(x, y, z, w, F)
'''


# № 4317 Пробный 06.2022 /dev/inf advanced (Уровень: Сложный)
'''
for n in range(1, 1000):
    x = n
    M = []
    while x > 0:
        M.append(x % 5)
        x //= 5
    M.reverse()
    if M[-1] % 2 == 0:
        M.append(2)
    else:
        M = [2] + M + [3]

    R = [str(i) for i in M]
    r = int(''.join(R), 5)

    if r < 1000:
        print(n)
'''


# № 5870 Danov 2301 (Уровень: Средний)
'''
R = []
for n in range(64, 1000):
    s = bin(n)[2:]
    # summ = sum([int(i) for i in s])
    if s.count('1') % 2 == 0:
        s = s[:-4] + s[-4:].replace('1', '*').replace('0', '1').replace('*', '0')
    else:
        s = s[:-5] + s[-5:-1].replace('1', '*').replace('0', '1').replace('*', '0') + s[-1]

    r = int(s, 2)
    R.append([r, n])
print(min(R))
'''

'''
for x in range(100, 1000):
    for y in range(100, 1000):
        X = [int(i) for i in str(x)]
        Y = [int(i) for i in str(y)]
        a = X[0] + Y[0]
        b = X[1] + Y[1]
        c = X[2] + Y[2]
        s = str(c) + str(a) + str(b)
        result = s[-4:-1]
        if int(result) == 2:
            print(x, y)
'''
# Ответ: 190


# № 7671 (Уровень: Базовый)
'''
import turtle as t
t.left(90)
t.speed(100)
l = 5

t.up()
x, y = 0, 0

x += 5
y += 5
t.goto(x * l, y * l)

t.down()
for _ in range(20):
    x += -5
    y += -5
    t.goto(x * l, y * l)

    x += 0
    y += 5
    t.goto(x * l, y * l)

x += 0
y += -5
t.goto(x * l, y * l)

for _ in range(20):
    x += 5
    y += 0
    t.goto(x * l, y * l)


t.done()
'''
# Ответ: 237


# № 8416 (Уровень: Средний)
# Книгу объёмом 1 Мбайт записали как аудиокнигу.
# Запись велась в формате стерео (2 канала) с частотой 48 кГц и разрешением 24 бит.
# За одну минуту записывалось в среднем 1,5 Кбайт текста.
# Сжатие данных позволило сократить размер полученного звукового файла на 84 %.
# Для удобства использования запись разделили на фрагменты со средним
# размером 15 Мбайт. Определите количество полученных фрагментов.
'''
a = 2
b = 24
c = 48000

book = 1 * 2 ** 23  # бит
audio = 1.5 * 2 ** 13  # бит
t = book / audio

I = a * b * c * t * 60  # бит
I = (I * 0.16)  # бит после сжатия
I = I / (2**23)
print(I / 15)
'''
# Ответ: 120

# № 5625 (Уровень: Базовый)
'''
# I = pixels * i
# Colors = 2 ** i

pixels = 512 * 240
I = 270 * 2 ** 13  # бит
i_spoiler = 5
# I = pixels * (i_colors + i_spoiler)
i = I / pixels
print(i)
# i = i_colors + i_spoiler
i_colors = i - i_spoiler
print(2 ** i_colors)
'''
# 8192



# № 5218 (Уровень: Базовый)
'''
s = sorted('АРБУЗ')
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if slovo.count('А') == 3:
                            if 'АА' in slovo and 'ААА' not in slovo:
                                count += 1
print(count)


from itertools import *
count = 0
for s in product(sorted('АРБУЗ'), repeat=6):
    slovo = ''.join(s)
    if slovo.count('А') == 3:
        if 'АА' in slovo and 'ААА' not in slovo:
            count += 1
print(count)
'''
# Ответ: 768



# № 6782 (Уровень: Средний)
'''
from itertools import *
count = 0
for s in product('01234567', repeat=6):
    temp = ''.join(s)
    if temp[0] != '0':
        if temp.count('6') == 2:
            if all(x not in temp for x in '16 61 36 63 56 65 76 67'.split()):
                count += 1
print(count)


s = '01234567'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        if temp[0] != '0':
                            if temp.count('6') == 2:
                                if all(x not in temp for x in '16 61 36 63 56 65 76 67'.split()):
                                    count += 1
print(count)
'''
# Ответ: 5229


# 5626
'''
s = '01234567'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp[0] != '0' or a != '0':
                        if a not in '1357':
                            if e not in '26':
                                if temp.count('7') <= 2:
                                    count += 1
print(count)
'''
# Ответ: 9135


# № 7030 Danov2303 (Уровень: Сложный)
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if len(set(M)) == 3 and all(M.count(x) <= 2 for x in M):
        a, b, c = sorted(set(M))
        if c ** 2 == a ** 2 + b ** 2:
            count += 1
print(count)
'''
# Ответ: 148


# № 6081 /dev/inf 02.2023 (Уровень: Сложный)
'''
from itertools import *
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if len(set(M)) == len(M) - 1:
        if any(sum(A[:3]) == sum(A[3:]) for A in permutations(M, 6)):
            count += 1
print(count)
'''
# Ответ: 127


# № 6925 (Уровень: Сложный)
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    flag1, flag2 = False, False
    if len(set(M)) == len(M) - 1:
        flag1 = True

    chet = [i for i in M if i % 2 == 0]
    nechet = [i for i in M if i % 2 != 0]

    try:
        sred_chet = sum(chet) / len(chet)
        sred_nechet = sum(nechet) / len(nechet)
        if abs(sred_chet - sred_nechet) > 50:
            flag2 = True

    except ZeroDivisionError:
        if (sum(M) / len(M)) > 50:
            flag2 = True

    if flag1 + flag2 == 1:
        count += 1
print(count)
'''
# Ответ: 862


# № 6592 Пробник ИМЦ СПб (Уровень: Базовый)
'''
alphabet = 10 + 1024 * 2
i = 12
byte = (6 * 2 ** 10) / 256   # сколько уходит на один!
bit = byte * 8
print(bit)
symbols = bit / i
print(symbols)
'''
# Ответ: 16


# № 6604 Пробник ИМЦ СПб (Уровень: Средний)
'''
def Divisors(x):
    divisors = set()
    if round(x**0.5) == x**0.5:
        for j in range(2, int(x**0.5)+1):
            if x % j == 0:
                divisors.add(j)
                divisors.add(x//j)
    return sorted(divisors)


for m in range(1, 1000):
    s = '>' + '1' * 15 + '2' * 35 + '3' * m

    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '3>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>', 1)

    summ = sum([int(i) for i in s if i.isdigit()])

    if len(Divisors(summ)) == 3:
        print(m)
        break
'''
# Ответ: 245



# № 5895 (Уровень: Сложный)
'''
ALPHBAET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
my_set = set()
for y in range(9, 16):
    for x in ALPHBAET[:y]:
        A = int(f'5{x}{ALPHBAET[y]}C', 16) + int(f'8{x}{x}7', y)
        my_set.add(A)
print(len(my_set))
'''
# Ответ: 84


# № 4937 (Уровень: Средний)
'''
for x in range(0, 80):
    A = [3, x, 7, 5]
    a = 0
    A.reverse()
    for i in range(0, len(A)):
        a += A[i] * 80**i

    B = [1, 4, x, 0]
    b = 0
    B.reverse()
    for j in range(0, len(B)):
        b += B[j] * 80**j

    if (a + b) % 17 == 0:
        print(x, (a + b) // 17)
'''
# Ответ: 146405




# № 6087 /dev/inf 02.2023 (Уровень: Сложный)
'''
def F(x, E):
    D = 15 <= x <= 40
    C = 21 <= x <= 63
    A = 7 <= x <= E
    return D <= (((not C) and (not A)) <= (not D))


M = [i/10 for i in range(7*10, 70*10)]
#M = [i/4 for i in range(7*4, 70*4)]
# M = [i for i in range(7, 70)]
for E in M:
    if all(F(x, E) for x in M):
        print(E)
        break
'''
# Ответ: 21



# F(n) = 1, при n < 3
# F(n) = F(n-1) + n, если n > 2 и при этом n нечетное
# F(n) = F(n-3) + 2*n, если n > 2 и при этом n четное

# F(2048) = F(2045) + 2*2048
# F(2045) = F(2044) + 2045
# F(2044) = F(2041) + 2*2044   - F(2041)
'''
print(2*2048 + 2045 + 2*2044)
'''
'''
import sys
sys.setrecursionlimit(1000000)

def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n-1) + n
    if n > 2 and n % 2 == 0:
        return F(n-3) + 2*n
print(F(2048) - F(2041))
'''
# RecursionError: maximum recursion depth exceeded
# Ответ: 10229


# № 6024 ФИПИ 03.02.23 (Уровень: Базовый)
'''
M = [int(i) for i in open('17.txt')]
A = [i for i in M if abs(i) % 100 == 12]
count = 0
maxi = -999999
for i in range(0, len(M)-1):
    if (abs(M[i]) % 100 == 12 and abs(M[i+1]) % 100 != 12) or (abs(M[i]) % 100 != 12 and abs(M[i + 1]) % 100 == 12):
        if (M[i] + M[i+1]) ** 2 < max(A) ** 2:
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 114 89033



# № 8475 (Уровень: Средний)
'''
M = [int(i) for i in open('17.txt')]
A = [i for i in M if len(str(abs(i))) == 3 and str(i)[-1] == '8']

count = 0
maxi = 0
for i in range(0, len(M)-2):
    if any(len(str(abs(x))) == 3 for x in [M[i], M[i+1], M[i+2]]):
        flag1, flag2, flag3 = False, False, False
        if M[i] ** 2 > min(A) ** 2:
            flag1 = True
        if M[i+1] ** 2 > min(A) ** 2:
            flag2 = True
        if M[i+2] ** 2 > min(A) ** 2:
            flag3 = True
        if flag1 + flag2 + flag3 == 2:
            count += 1
            maxi = max(maxi, M[i] + M[i + 1] + M[i + 2])
print(count, maxi)
'''
# Ответ: 5312 20235

# № 5640 (Уровень: Средний)
'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-4, b) + F(a - sum([int(i) for i in str(a)]), b)

print(F(36, 14) * F(14, 2))



def F(a, b):
    if a <= b:
        return a == b
    return F(a-4, b) + F(a - sum([int(i) for i in str(a)]), b)

print(F(36, 14) * F(14, 2))
'''
# Ответ: 7


# № 7852 Danov2304 (Уровень: Базовый)
'''
def is_prime(x):
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

def F(a, b):
    if a >= b or is_prime(a):
        return a == b
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(8, 16) * F(16, 32))
'''
# Ответ: 40


# № 6635 Пробник ИМЦ СПб (Уровень: Средний)
'''
my_set = set()
def F(a, h):
    if h == 13:
        if a < 0:
            my_set.add(a)
        return 0
    else:
        return F(a-3, h+1) + F(a*(-3), h+1)

F(333, 0)
print(len(my_set))
'''
# Ответ: 2224


# № 7891 (Уровень: Средний)
'''
ALPHBAET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = open('24.txt').readline()
maxi = 0
for a in ALPHBAET:
    M = [len(i) for i in s.split(a)]
    maxi = max(maxi, max(M))
print(maxi)
'''
# Ответ: 9747


# № 8481 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(237, 10**8, 237):
    if fnmatch(str(x), '81?2*80'):
        if not fnmatch(str(x), '*9*'):
            print(x, x//237)
'''
# 815280 3440
# 8162280 34440
# 81324180 343140
# 81727080 344840
# 81821880 345240


# № 6095 /dev/inf 02.2023 (Уровень: Базовый)
'''
from fnmatch import *
M = []

for x in range(111, 10**8, 111):
    if fnmatch(str(x), '*15*7424'):
        M.append([x, x//111])

for x in range(113, 10**8, 113):
    if fnmatch(str(x), '*15*7424'):
        M.append([x, x//113])

for x in range(127, 10**8, 127):
    if fnmatch(str(x), '*15*7424'):
        M.append([x, x//127])

for x in sorted(M):
    print(*x)
'''
# 1587424 14048
# 15147424 134048
# 15227424 137184
# 15457424 121712
# 28157424 221712
# 85157424 767184



# № 5227 (Уровень: Сложный)
'''
from fnmatch import *
for x in range(0, 10**7):
    if fnmatch(str(x), '3*52?'):
        divisor = set()
        for j in range(2, int(x**0.5)+1):  # не считая самого числа.
            if x % j == 0:
                divisor.add(j)
                divisor.add(x//j)
        if len(divisor) % 2 != 0:
            print(x, max(divisor))
'''
# Ответ:
# 3143529 1047843
# 3175524 1587762
# 3200521 1789
# 3845521 103933
# 3908529 1302843