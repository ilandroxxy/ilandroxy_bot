# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ************************************************************
'''
alphabet = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
R = []
for x in alphabet[:27]:
    A = int(f"123{x}24",27)
    B = int(f"135{x}78",27)
    if (A + B) % 26 == 0:
        R.append((A + B) // 26)
print(max(R))
'''
# Ответ: 1213206

'''
def F(A, x):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))


for A in range(1, 1000):
    if all(F(A, x) for x in range(1, 1000)):
        print(A)
'''
# Ответ: 196

'''
def F(A1,A2,x):
    B = 24 <= x <= 90
    A = A1 <= x < A2
    C = 47 <= x <= 115
    return C <= (((not A) and B) <= (not C))


M = [x / 5 for x in range(20 * 5, 120 * 5)]
R = []
for A1 in M:
    for A2 in M:
        if all(F(A1, A2, x)for x in M):
            R.append(A2-A1)
print(round(min(R)))
'''
# Ответ: 43

'''
M = []
for n in range(1,10000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 2 == 0:
        s = s + "01"
    else:
        s = "1" + s + "1"
    r = int(s, 2)
    if r > 156:
        M.append(n)
print(min(M))
'''
# Ответ: 33

'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a * 2, b)

print(F(4,8) * F(8,10) * F(10,15))


def F(a, b):
    if a >= b:
        return a == b
    return F(a + 1, b) + F(a * 2, b)

print(F(4, 8) * F(8, 10) * F(10, 15))
'''
# Ответ: 2

'''
import turtle as t
t.left(90)
t.tracer(0)

l = 20

# Тут пишем алгоритм
for i in range(2):
    t.fd(13 * l)
    t.rt(90)
    t.fd(18 * l)
    t.rt(90)
t.up()
t.fd(5*l)
t.rt(90)
t.fd(9*l)
t.lt(90)
t.down()
for i in range(2):
    t.fd(11*l)
    t.rt(90)
    t.fd(7*l)
    t.rt(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''


s = '8' * 45
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '88', 1)
    else:
        s = s.replace('8888', '11', 1)
print(s)


# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Евгений = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23]
# КЕГЭ = []
# на следующем уроке: повторить 12 номера
