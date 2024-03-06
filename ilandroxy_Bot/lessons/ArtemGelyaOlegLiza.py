
# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Задание 5
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(number, system):
    result = ''
    while number > 0:
        result = alphabet[number % system] + result
        number //= system
    return result


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s += s[-2:]
    else:
        x = (n % 3) * 5
        s += convert(x, 3)

    r = int(s, 3)
    if r < 242:
        R.append(r)

print(max(R))
'''
# Ответ: 230


# Задание 6
'''
import turtle as t  # переименовали библиотеку в t
t.tracer(0)
t.left(90)
m = 30  # масштаб отрисовки

# Ваш псевдокод по условию
for _ in range(2):
    t.forward(19 * m)
    t.right(90)
    t.forward(10 * m)
    t.right(90)

t.up()

t.backward(3 * m)
t.right(90)
t.forward(8 * m)
t.left(90)

t.down()
t.color('green')
for _ in range(2):
    t.forward(32 * m)
    t.right(90)
    t.forward(12 * m)
    t.right(90)


t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * m, y * m)
        t.dot(2, 'red')

t.update()
t.done()
'''
# Ответ: 18


# Задание 7
'''
# I = pixels * i
pixels = 2688 * 344
i = 12 * 2**3  # бит на один символ

I = pixels * i  # бит
U = 49152  # бит / с
print(I / U)
'''
# Ответ: 1806

# Задание 8
'''
cnt = 0
num = 1
s = sorted('ПРОГУЛКА')
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if num % 2 == 0 and a != 'Г' and slovo.count('Л') <= 2:
                        cnt += 1
                    num += 1
print(cnt)

# Вариант 2
from itertools import product
cnt = 0
num = 1
for v in product(sorted('ПРОГУЛКА'), repeat=5):
    slovo = ''.join(v)
    if num % 2 == 0 and slovo[0] != 'Г' and slovo.count('Л') <= 2:
        cnt += 1
    num += 1
print(cnt)
'''
# Ответ: 13951


# Задание 9
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len([x for x in M if M.count(x) == 2]) == 4:
        if M.count(max(M)) == 2:
            print(M)
            cnt += 1
print(cnt)
'''
# Ответ: 88

# Задание 11
'''
symbols = 491
alphabet = 10 + 9575
# print(alphabet, 2**14)
i = 14  # бит на один символ
bit = symbols * i
print(bit / 8)  # 859.25
byte = 860
I = (byte * 23552) / (2 ** 10)
print(I)
'''
# Ответ: 19780

'''
def F(a1, a2, x):
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    A = a1 <= x <= a2
    return C <= (((not A) and B) <= (not C))


R = []
M = [x / 4 for x in range(20 * 4, 120 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(a1, a2, x) for x in M):
            R.append(a2-a1)
print(min(R))
'''
# Ответ: 43

'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n <= 11:
        return 7
    if n > 11:
        return n-3 + F(n-1)

print(F(2022) - F(2020))

# F(2022) = 2019 + F(2021)
# F(2021) = 2018 + F(2020) - F(2020)
print(2018 + 2019)
'''
# Ответ: 4037


# Задание 17
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 10 == 3 and len(str(abs(x))) == 4]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i], M[i+1], M[i+2]
    if len([p for p in [x, y, z] if abs(p) % 10 == 3]) != 3:
        if (x + y + z) >= min(A):
            R.append(x + y + z)
print(len(R), max(R))
'''
# Ответ: 4335 186619

# Задание 24
'''
s = open('24.txt').readline().split('Y')
maxi = 0
for i in range(len(s)-150):
    r = 'Y'.join(s[i:i+151])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 1605


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo Тип 24 №55641
'''
f = open('24.txt').readlines()
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

# todo Задание 13
'''
from ipaddress import *

net = ip_network(f'222.63.131.128/255.255.255.192', 0)
print(net)
'''

# endregion Разобрать: *************************************************************


# GOAL = [1.1, 2.1, 4.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке:
