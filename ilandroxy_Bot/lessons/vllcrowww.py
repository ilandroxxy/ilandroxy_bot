# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************


# Список необходимых функций библиотеки
'''
import turtle as t
t.tracer(0)

t.fd(10)  # t.bk(10)
t.rt(90)  # t.lt(90)

t.up()
t.down()

x, y = 0, 0
t.goto(x, y)
t.dot(2, 'red')

t.done()
'''


# Шаблон для решения 6 номера
'''
import turtle as t
t.lt(90)
t.tracer(0)
l = 20

# Тут пишется псевдокод:
for i in range(2):
    t.fd(8*l)
    t.rt(90)
    t.fd(18 * l)
    t.rt(90)
t.up()
t.fd(4 * l)
t.rt(90)
t.fd(10 * l)
t.rt(90)
t.down()
for i in range(2):
    t.fd(17 * l)
    t.rt(90)
    t.fd(7 * l)
    t.rt(90)


t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(2, 'red')
t.done()
'''


# КЕГЭ № 10090 Демоверсия 2024 (Уровень: Базовый)
# Сколько существует восьмеричных пятизначных чисел, не содержащих в своей записи цифру 1,
# в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?
'''
s = '0234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':  # if num[0] != '0':
                        if '1' not in num:
                            if len(num) == len(set(num)):  # # в которых все цифры различны
                                num = num.replace('0', '2').replace('4', '2').replace('6', '2')
                                num = num.replace('5', '3').replace('7', '3')
                                if '22' not in num and '33' not in num:
                                    cnt += 1
print(cnt)
'''

'''
# Вариант 1
x = 5**1600 + 625**600 - 5**400
cnt = 0
while x > 0:
    if x % 5 == 4:
        cnt += 1
    x //= 5
print(cnt)

# Вариант 2
x = 5**1600 + 625**600 - 5**400
M = []
while x > 0:
    M.append(x % 5)
    x //= 5
print(M.count(4))
'''
# Ответ: 1200

# КЕГЭ № 12462 (Уровень: Базовый)
# (PRO100 ЕГЭ) Сколько существует различных трёхзначных и пятизначных чисел,
# записанных в шестнадцатеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?
'''
import string
s = string.hexdigits
print(s)  # 0123456789ABCDEF

s = '0123456789ABCDEF'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            num = a + b + c
            if a != '0':
                if a > b > c:
                    cnt += 1

for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if a > b > c > d > e:
                            cnt += 1
print(cnt)
'''

# todo Почему if a != 'Л' and b != 'М': не работает
'''
s = sorted('ЛОГАРИФМ')
cnt = 0
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if num % 2 == 0:
                        if slovo[:2] != 'ЛМ':
                        # if a != 'Л' and b != 'М':
                            print(slovo)
                            if slovo.count('И') >= 2:
                                cnt += 1
print(cnt)


from itertools import *
k = n = 0
for s in product(sorted('ЛОГАРИФМ'), repeat = 5):
    s = ''.join(s)
    n += 1
    if n % 2 == 0 and s[:2] != 'ЛМ' and s.count('И') >= 2:
        k += 1
print(k)
'''

print('20 02 22 24 42'.split())
# ['20', '02', '22', '24', '42']
'''
from itertools import *
cnt = 0
for s in product('012345', repeat=7):
    s = ''.join(s)
    if s[0] != '0':
        if s.count('2') == 1:
            if all(x not in s for x in '20 02 22 24 42'.split()):
                cnt += 1
print(cnt)
'''
# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Марго = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 12, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
