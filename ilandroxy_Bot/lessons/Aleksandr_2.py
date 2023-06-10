# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************
'''
import turtle as t
t.left(90)
t.speed(100)
l = 20

for i in range(2):
    t.forward(7 * l)
    t.right(90)
    t.forward(18 * l)
    t.right(90)
t.up()
t.backward(2 * l)
t.right(90)
t.forward(9 * l)
t.left(90)
t.down()
t.color('blue')
for i in range(3):
    t.forward(8 * l)
    t.right(120)

t.up()
for x in range(0, 20):
    for y in range(0, 8):
        t.goto(x *l, y * l)
        t.dot(2, 'red')
t.done()
'''


# 16
'''
print(4**3 + 6**3 + 8**3)
'''

'''
M = [int(i) for i in open('17.txt')]
summ = 0
for x in M:
    summ += sum([int(i) for i in str(x)])
count = 0
mini = 9999999
for i in range(0, len(M)-1):
    if (abs(M[i] % 100) == 10 and abs(M[i+1] % 100) != 10) or (abs(M[i] % 100) != 10 and abs(M[i+1] % 100) == 10):
        if (M[i] + M[i+1]) < summ:
            count += 1
            mini = min(mini, M[i] + M[i+1])
print(count, mini)
'''

# endregion Урок: ******************************************************************************

import useful
print(useful.Who_Is_Name())

# todo:    Александр2   = [1, 2, 3, 4, 5, 6, 7, 8, 9.1, 11, 12, 14+, 15+, 16, 17, 18, 19-21, 23, 24, 25.2]
# todo: Александр2 КЕГЭ = [9, 15, 17, 24]
# на прошлом уроке: Прорешали номера с домашки: 6, письменные 16 и 17
# на следующем уроке:
