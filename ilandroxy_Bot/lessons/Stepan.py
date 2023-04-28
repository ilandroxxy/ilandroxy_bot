# region Домашка: ******************************************************************************

# 7
'''
I = 16000 * 24 * 90 * 2 #бит
a = 16000
t1 = 90
v = 64000
print(I)
t2 = I / 64000
print(t2)
'''

# 11
'''
alphabet = 2035
symbols = 113
i = 11
bit = symbols * i
print(bit)
byte = int(bit / 8) + 1
print(byte)
kbyte = (byte * 32768) / 1024
print(kbyte)
'''

# 2
'''
print(f'x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x * (not(y))) + (y == z) + (not(w))
                if F == 0:
                    print(x, y, z, w, F)
# Ответ: xwzy
'''

# 3
#Ответ: 455

# 8
'''
count = 0
import itertools as it
for s in it.product('АВЛОР', repeat = 4):
    s = ''.join(s)
    count += 1
    if s[0] == 'Л':
        print(count, s)
'''

# 16
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + F(n + 3)
print(F(23) - F(21))
'''

# 14
'''
for x in '0123456789ABCDE':
 a = int(f'97968{x}13', 15)
 b = int(f'7{x}213', 15)
 s = a + b
 if s % 14 == 0:
  print(s // 14)
  '''

# 6
'''
import turtle as t
t.left(90)
t.speed(30)
l = 15
t.right(315)
for _ in range(7):
    t.forward(16 * l)
    t.right(45)
    t.forward(8 * l)
    t.right(135)

t.up()
for x in range(-12, 0):
    for y in range(0, 20):
        t.goto(x * l, y * l)
        t.dot(2, 'red')
t.done()
'''

# 12
'''
for n in range(4, 100):
    s = '3' + n * '5'
    while ('25' in s) or ('355' in s) or ('555' in s):
        if '25' in s:
            s = s.replace('25', '3', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)
    if sum([int(i) for i in s]) == 27:
        print(n)
        break
'''

# 17

'''s = [int(i) for i in open('17_7596.txt')]'''

# 5
'''
for N in range(0, 10000):
    s = bin(N)[2:]
    if N % 3 == 0:
       s += s[-3:]
    else:
       s += bin(N % 3 * 3)[2:]
    R = int(s, 2)
    if R < 100:
        print(N)
'''

# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************


# endregion Урок: ******************************************************************************

import useful
print(useful.who_is_name())

# todo: Степан = [1, 2, 3, 4, 5, 7, 8, 9, 13, 14+, 15+, 16, 17, 18, 19-21, 22, 23, 24, 25.2]
# на прошлом уроке: Разбирали домашку и прорешивали 9, 17, 24 номера
# на следующем уроке:
