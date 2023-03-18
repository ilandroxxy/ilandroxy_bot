# region Домашка: ******************************************************************************

# 1. № 4693 Демоверсия 2023 (Уровень: Базовый)
#  На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 0, а затем два левых разряда заменяются на 10;
# б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 1, а затем два левых разряда заменяются на 11.
# Полученная таким образом запись является двоичной записью искомого числа R.
# Например, для исходного числа 610 = 1102 результатом является число 10002 = 810, а для исходного числа 410 = 1002 результатом является число 11012 = 1310.
# Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число R, большее 40. В ответе запишите это  число в десятичной системе счисления.

'''
for N in range(0, 10000):
    s = bin(N)[2:]
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    R = int(s, 2)
    if R > 40:
        print(N)
# Ответ: 16
'''


# № 3073 (Уровень: Сложный)
# Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
# 1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные двузначные числа (числа не могут начинаться с нуля).
# 2. На экран выводится разность полученных двузначных чисел.
# Пример:
# Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53, наименьшее – 13. На экран выводится разность 53 – 13 = 40.
# Чему равно наименьшее возможное трёхзначное число N, в результате обработки которого на экране автомата появится число 5?

'''
for N in range(100, 1000):
    s = str(N)
    M = [s[0] + s[1], s[0] + s[2], s[1] + s[0], s[1] + s [2], s[2] + s[0], s[2] + s[1]]
    M = [int(i) for i in M if i[0] != '0']
    R = max(M) - min(M)
    if R == 5:
        print(N)
# Ответ: 505
'''

# № 2208 Halloween 2021 (Уровень: Средний)
# (А. Калинин) Ведьма обрабатывает десятичное натуральное число N по следующему алгоритму.
# 1. Все цифры числа перемножаются.
# 2. Получившееся число переводится в двоичное представление.
# 3. К двоичной записи этого числа справа дописывается два нуля.
# 4. Полученное в результате этих операций число переводится в десятичную систему счисления.
# Пример.
# Дано число 13.
# 13_10 -> 3_10 -> 11_2 -> 1100_2 -> 12_10
# Укажите число N, после обработки которого получится число 864, если известно, что все цифры числа N одинаковые.
'''
import itertools
def F(x):
    r = 1
    while x > 0:
        r *= x % 10
        x //= 10
    return r

alphabet = '123456789'
M = []
for lenght in range(1, 6):
    for s in itertools.product(alphabet, repeat=lenght):
        if s.count(s[0]) == lenght:
            s = int(''.join(s))
            M.append(s)

for n in M:
    x = F(n)
    s = bin(x)[2:]
    s = s + '00'
    r = int(s, 2)
    if r == 864:
        print(n)
'''
'''
def F(x):
    r = 1
    while x > 0:
        r *= x % 10
        x //= 10
    return r

for n in range(1, 10000):
    B = [i for i in str(n)]
    if B.count(B[0]) == len(B):  # что если список заполнен одинаковыми цифрами
        x = F(n)
        s = bin(x)[2:]
        s = s + '00'
        r = int(s, 2)
        if r == 864:
            print(n)
'''
# Решение которое предложило мне ChatGPT:
'''
def witch_transform(n):
    digits = [int(d) for d in str(n)]
    product = 1
    for digit in digits:
        product *= digit
    binary = bin(product)[2:]
    binary += '00'
    return int(binary, 2)

for n in range(1, 10000):
    if len(set(str(n))) == 1: 
        # проверяем, все ли цифры одинаковые
        result = witch_transform(n)
        if result == 864:
            print(n)
'''
# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# В начальный момент Черепаха находится в начале координат и направлена вверх
# (вдоль положительного направления оси ординат).

# Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 10 Направо 270]
# Поднять хвост
# Вперёд 3 Направо 270 Вперёд 5 Направо 90
# Опустить хвост
# Повтори 2 [Вперёд 10 Направо 270 Вперёд 12 Направо 270]
#

# Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур, ограниченных
# заданными алгоритмом линиями, включая точки на линиях.

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
# Показать ответ: 216


# endregion Урок: ******************************************************************************


# todo: Степан = [2, 3, 4, 5, 7, 8, 9, 13, 14+, 15+, 16, 17, 18, 19-21, 22, 23, 24, 25.2]
# на прошлом уроке: Степан сам прорешивал 5, 8 номера с КЕГЭ
# на следующем уроке: