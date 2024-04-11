# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Задание 2
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not z)) or (y == z) or (not w)
                if F == False:
                    print(x, y, z, w)
'''


# Задание 6
'''
import turtle as t
t.left(90)
t.tracer(0)  # отключает анимацию
m = 30

# Тут пишем псевдокод
for i in range(2):
    t.fd(13 * m)
    t.rt(90)
    t.fd(18 * m)
    t.rt(90)
t.up()
t.fd(5 * m)
t.rt(90)
t.fd(9 * m)
t.lt(90)
t.down()
t.color('green')
for i in range(2):
    t.fd(11 * m)
    t.rt(90)
    t.fd(7 * m)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * m, y * m)
        t.dot(2, 'red')

t.done()
'''

# Задание 5
'''
for n in range(1, 1000):
    s = bin(n)[2:]  # перевод в двоичную запись
    if n % 2 == 0:
        s = s + '01'
    else:
        s = '1' + s + '1'
    r = int(s, 2)  # перевод из 2-ой в 10-ную систему
    if r > 156:
        print(n)
        break
'''
# Ответ: 33


# Задание 7
'''
pixels = 2764 * 1793
colors = 7026  # colors = 2 ** i
# print(2 ** 13)  # 8192
i = 13
I = pixels * i  # все нашей картинки (бит)
I = I * 148
U = 18349566  # бит / сек
t = I / U
print(t)  # 519.6340473665
'''
# Ответ: 519


# Задание 8
'''
s = sorted('ПАРУС')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if 'АА' not in slovo:
                        if slovo.count('У') <= 1:
                            print(num, slovo)
                            exit()
                    num += 1
'''
# Ответ: 131


# Задание 15
'''
def F(x, A):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''
# Ответ: 196


# Задание 16
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + F(n-1)

print(F(2024) - F(2020))
'''
# Ответ: 8098

# Задание 23
'''
def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a*2, b)

print(F(4, 8) * F(8, 10) * F(10, 15))
'''
# Ответ: 23

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Лиза = [1, 2, 4, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
