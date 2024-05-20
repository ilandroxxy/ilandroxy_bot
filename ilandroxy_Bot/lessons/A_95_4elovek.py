# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************
'''
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '01'
    else:
        s = '1' + s + '1'
    r = int(s, 2)
    if r > 156:
        print(n)
        break
'''

'''
import turtle as t
t.left(90)
t.tracer(0)
l = 20

for i in range(2):
    t.forward(13 * l)
    t.right(90)
    t.forward(18 * l)
    t.right(90)
t.up()
t.forward(5 * l)
t.right(90)
t.forward(9 * l)
t.left(90)
t.down()
for i in range(2):
    t.forward(11 * l)
    t.right(90)
    t.forward(7 * l)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''
'''
s = sorted('ПАРУС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if slovo.count('У') <= 1 and 'АА' not in slovo:
                        print(num, slovo)
                        exit()
'''

'''
from itertools import *
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if max(M) < sum(M[:3]):
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''

'''
x = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 -4*3**2024 - 2029
M = []
while x > 0:
    M.append(x % 27)
    x //= 27
print(len([x for x in M if x > 9]))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:27]:
    A = int(f'123{x}24', 27)
    B = int(f'135{x}78', 27)
    if (A + B) % 26 == 0:
        print((A + B) // 26)
'''

# endregion Урок: ***************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Сева = [1, 2, 3, 4, 6, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 9, 12, 15, 16, 23, 17, 24, 25
