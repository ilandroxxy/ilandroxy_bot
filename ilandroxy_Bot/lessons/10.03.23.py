

# 1
'''
print('x y z w F')
for x in range(2):  # [0, 2-1]
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # F = (x <= (not (y <= z))) or w
                if ((x <= (not (y <= z))) or w) == False:   # F == False   # not F  # F == 0
                    print(x, y, z, w)
'''

# 2
'''
M = []
for n in range(1, 8+1):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'

    r = int(s, 2)
    M.append(r)

print(max(M))
'''

'''
maxi = -99999
for n in range(1, 8+1):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'

    r = int(s, 2)
    maxi = max(maxi, r)
print(maxi)
'''

# 6
# import turtle
# turtle.forward(100)
# turtle.done()

# from turtle import *
# forward(100)
# done()
'''
import turtle as t

t.left(90)
t.speed(10)
l = 30

for i in range(4):
    t.forward(10 * l)
    t.right(270)
t.up()
t.forward(3 * l)
t.right(270)
t.forward(5 * l)
t.right(90)
t.down()
t.color('blue')
for i in range(2):
    t.forward(10 * l)
    t.right(270)
    t.forward(12 * l)
    t.right(270)

t.up()
for x in range(0, -20, -1):
    for y in range(0, 15):
        t.goto(x * l, y * l)
        t.dot(3, 'red')

t.done()
'''


# 8
'''
s = 'АЙКОС'
s = sorted([i for i in 'СОЙКА'])
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if slovo.count('О') <= 1 and 'СС' not in slovo:
                        print(k)
                    k += 1
'''
'''
k = 1
from itertools import product
for s in product('АЙКОС', repeat=5):
    slovo = ''.join(s)
    if slovo.count('О') <= 1 and 'СС' not in slovo:
        print(k)
    k += 1

'''


#9
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    maxi = max(M) + min(M)
    if maxi < (sum(M) - maxi):
        count += 1
print(count)
'''

'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if M[0] + M[3] < M[1] + M[2]:
        count += 1
print(count)
'''
# Ответ: 1503


