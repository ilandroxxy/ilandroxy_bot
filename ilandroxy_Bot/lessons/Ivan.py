# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Задание 14 (N°234) (м.в. Кузнецова)
# Значение арифметического выражения: 2*27**7 + 3**10 - 9 записали в системе счисления с основанием з.
# Сколько цифр «О» содержится в этой записи?
'''
x = 2*27**7 + 3**10 - 9
n = 3
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M.count(0))
'''
# Ответ: 13


# Какой-то 12 номер
'''
s = '1' * 103
while '111' in s or '2222' in s:
    s = s.replace('111', '22', 1)
    s = s.replace('2222', '1', 1)
print(s)
'''


# Задание 14 (N°466).
# Значение арифметического выражения:
# 5**1*7**3+2*5**2*7**2+3*5**3*7**1
# сначала записали в системе счисления с основанием 7, затем в системе счисления с основанием 5.
# В какой системе счисления сумма разрядов числа будет больше?

# В качестве ответа приведите одно число - сумму основания системы счисления,
# в которой сумма разрядов больше, и разность найденных сумм.
# Так, например, если в 7сс сумма получилась 20, а в 5сс - 15, необходимо записать сумму 7 (основание) + 5 (разность 20 и 15) = 12.
'''
def F(x, n):
    M = []
    while x > 0:
        M.append(x % n)
        x //= n
    M.reverse()
    return M

a = sum(F(5**1*7**3+2*5**2*7**2+3*5**3*7**1, 7))
b = sum(F(5**1*7**3+2*5**2*7**2+3*5**3*7**1, 5))

print('основания системы счисления,в которой сумма разрядов больше', 'разность найденных сумм')
print(7+6)
'''
# Ответ: 13


# Задание 15 (N°1859).
# Найдите максимальное значение параметра А, при котором выражение
# (2x + y # 70) v (x <y) V (A < x)
# истинно (т.е. принимает значение 1) при любых неотрицательных значениях х и у.

'''
for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((2*x + y != 70) or (x < y) or (A < x)) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
'''

'''
def F(x, y, A):
    return (2*x + y != 70) or (x < y) or (A < x)

for A in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
'''

'''
def F(x, y):
    return (2*x + y != 70) or (x < y) or (A < x)

for A in range(1, 1000):
    if all(F(x, y) for x in range(1, 100) for y in range(1, 100)):
        print(A)
'''

'''
def F(x, y):
    return (2*x + y != 70) or (x < y) or (A < x)

for A in range(1000, 0, -1):
    if all(F(x, y) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''
# Ответ: 23

'''
from turtle import*
k = 10

for i in range(20):
    color('black')
    for j in range(4):
        forward(15*k)
        right(90)
    color('red')
    back(20*k)
    right(90)
up()
for x in range(11):
    for y in range(11):
        goto(x*k, y*k)
        dot(5)
done()
'''

'''
from turtle import *
k = 40
speed(100)
x, y = 0, 0
dot(5, 'red')

for i in range(13):
    x += 4
    y += 3
    goto(x*k, y*k)

    x += -5
    y += 10
    goto(x * k, y * k)

    x += 6
    y += -6
    goto(x * k, y * k)

    x += -5
    y += -8
    goto(x * k, y * k)
done()
'''


# endregion Урок: ******************************************************************************


# todo: Иван = [2, 6, 8, 10, 12, 13, 14+, 15+, 16, 17, 23]
# на прошлом уроке: Разобрал задачи из школы, номера: 2, 4, 6, 14, 15
# на следующем уроке: