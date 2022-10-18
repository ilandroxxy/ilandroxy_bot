# Домашка:
'''
#Тип 14 № 27301.Сколько единиц содержится в двоичной записи значения выражения 16**4 + 8**4 + 4**6 - 64?
x = 16**4 + 8**4 + 4**6 - 64
M = []
while x > 0:
    M.append(x%2)
    x//= 2
M.reverse()
print(M.count(1))
'''

'''
#Тип 14 № 46972. Значение выражения 5*343**8 + 4*49**12 + 7**14 - 98 записали в системе счисления с основанием 7 без незначащих нулей. 
Какая цифра чаще всего встречается в этой записи?
x = 5*343**8 + 4*49**12 + 7**14 - 98
M = []
while x > 0:
    M.append(x%7)
    x//= 7
M.reverse()
print(M)
A = {}
for x in M:
    A[x] = M.count(x)
print(A)
'''

'''
# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1.Строится троичная запись числа N.
# 2.В конец записи (справа) дописывается остаток от деления числа N на 3.
# 3.Результат переводится из троичной системы в десятичную и выводится на экран.
#
# Пример. Дано число N=11. Алгоритм работает следующим образом:
# 1.Троичная запись числа N: 102.
# 2.Остаток от деления 11 на 3 равен 2, новая запись 1022.
# 3.На экран выводится число 35.
#
# Какое наименьшее трёхзначное число может появиться на экране в результате работы автомата?

A = []
for n in range(1, 10000):
    x = n

    M = []
    while n > 0:
        M.append(n % 3)  
        n //= 3
    M.reverse()

    M.append(x % 3)   

    res = 0
    M.reverse()
    for i in range(0, len(M)):  
        res += M[i] * 3 ** i

    if 100 <= res < 1000: 
        A.append(res)
print(min(A))
'''






# Тип 5 № 33475
"""
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. В конец записи (справа) дописывается вторая справа цифра двоичной записи.
# 3. В конец записи (справа) дописывается вторая слева цифра двоичной записи.
# 4. Результат переводится в десятичную систему.
#
# При каком наименьшем числе N в результате работы алгоритма получится R > 180?
# В ответе запишите это число в десятичной системе счисления.

for n in range(2, 1000):
    x = n

    N = []
    while n > 0:
        N.append(n % 2)  # 1. Строится двоичная запись числа N.
        n //= 2
    N.reverse()

    print(N)
    N.reverse()
    temp = N[1]
    N.reverse()
    N.append(temp)  # 2. В конец записи (справа) дописывается вторая справа цифра двоичной записи.

    N.append(N[1])  # 3. В конец записи (справа) дописывается вторая слева цифра двоичной записи.

    N.reverse()
    r = 0
    for i in range(0, len(N)):  # 4. Результат переводится в десятичную систему.
        r += N[i] * 2 ** i

    if r > 180:
        print(x)
        break
"""
# Ответ: 46


# Тип 5 № 15622
'''
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему правилу: складываются все цифры двоичной записи, если
# а) сумма нечетная к числу дописывается 11,
# б) сумма четная, дописывается 00.
#
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
# Укажите такое наименьшее число R, которое превышает 114 и может являться результатом работы алгоритма.
# В ответе это число запишите в десятичной системе счисления.

for n in range(0, 10000):

    N = []
    while n > 0:
        N.append(n % 2)  # 1. Строится двоичная запись числа N.
        n //= 2
    N.reverse()

    summ = sum(N)
    if summ % 2 == 0:
        N.append(0)
        N.append(0)
    else:
        N.append(1)
        N.append(1)

    N.reverse()
    r = 0
    for i in range(0, len(N)):
        r += N[i] * 2 ** i

    if r > 114:
        print(r)
        break
'''
# Ответ: 115



# Тип 5 № 35463
"""
# Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. Подсчитывается количество нулей и единиц в полученной записи.
# Если их количество одинаково, в конец записи добавляется её последняя цифра.
# В противном случае в конец записи добавляется та цифра, которая встречается реже.
# 3. Шаг 2 повторяется ещё два раза
# 4. Результат переводится в десятичную систему.
#
# Пример. Дано число N = 19. Алгоритм работает следующим образом:
#
# 1. Двоичная запись числа N: 10011.
# 2. В полученной записи нулей меньше, чем единиц, в конец записи добавляется 0. Новая запись: 100110.
# 3. В текущей записи нулей и единиц поровну, в конец записывается последняя цифра, это 0.
# Получается 1001100. В этой записи единиц меньше, в конец добавляется 1: 10011001.
# 4. Результат работы алгоритма R = 153.
#
# При каком наименьшем числе N > 99 в результате работы алгоритма получится число, кратное 4?


for n in range(100, 1000):
    x = n

    N = []
    while n > 0:
        N.append(n % 2)  # 1. Строится двоичная запись числа N.
        n //= 2
    N.reverse()

    for _ in range(3):  # 3. Шаг 2 повторяется ещё два раза
        if N.count(0) == N.count(1):
            N.append(N[-1])  # Если их количество одинаково, в конец записи добавляется её последняя цифра.
        else:
            if N.count(0) < N.count(1):  # В противном случае в конец записи добавляется та цифра, которая встречается реже.
                N.append(0)
            else:
                N.append(1)

    N.reverse()
    r = 0
    for i in range(0, len(N)):
        r += N[i] * 2 ** i

    if r % 4 == 0:
        print(x)
        break
"""
# Ответ: 103



# Задания 14 № 4938
"""
# Решите уравнение 100_7 + x = 200_5.
# Ответ запишите в шестнадцатеричной системе (основание системы счисления в ответе писать не нужно).

M = [1, 0, 0]
M.reverse()
m = 0
for i in range(0, len(M)):
    m += M[i] * 7 ** i


N = [2, 0, 0]
N.reverse()
n = 0
for i in range(0, len(N)):
    n += N[i] * 5 ** i

x = n - m

A = []
while x > 0:
    A.append(x % 16)
    x //= 16
A.reverse()
print(A)
"""


# Тип 14 № 47218
"""
# Операнды арифметического выражения записаны в системе счисления с основанием 15:
#
# 123x515 + 1x23315
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 14.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 14 и укажите
# его в ответе в десятичной системе счисления. 
# Основание системы счисления в ответе указывать не нужно.

for num in range(15):
    A = list(reversed([1, 2, 3, num, 5]))
    B = list(reversed([1, num, 2, 3, 3]))

    sum1, sum2 = 0, 0
    for i in range(5):
        sum1 += A[i] * 15 ** i
        sum2 += B[i] * 15 ** i
    print(A, B)
    if (sum1 + sum2) % 14 == 0:
        print((sum1 + sum2)// 14)
        break
"""


import turtle as t


for _ in range(4):
    t.forward(100)  # а движение в пикселях
    t.left(90)  # повороты указываются в градусах

t.color('red')
for _ in range(2):
    t.forward(200)  # а движение в пикселях
    t.left(90)  # повороты указываются в градусах
    t.forward(150)
    t.left(90)

t.done()  # зафиксировать окно вывода





# todo: на следующем уроке разбираем 6 номер turtle