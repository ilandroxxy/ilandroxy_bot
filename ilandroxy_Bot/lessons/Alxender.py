# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

'''
from itertools import permutations

graph = 'АБ БА АВ ВА БВ ВБ ВД ДВ ЕД ДЕ ВЕ ЕВ ВГ ГВ ЕГ ГЕ ЕК КЕ КГ ГК'
table = '12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76'

for per in permutations('АБВДЕГК'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
'''


'''
from itertools import permutations

graph = 'АБ БА АГ ГА ГБ БГ БВ ВБ БД ДБ ВД ДВ ЕВ ВЕ ДЕ ЕД ГД ДГ ГЖ ЖГ ГИ ИГ ЖИ ИЖ ДИ ИД ИК КИ ЕК КЕ'
table = '12 13 16 17 19 21 24 25 26 29 31 36 37 42 49 52 56 61 62 63 65 71 73 78 87 89 91 92 94 98'

for per in permutations('АБВДЕГКИЖ'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8 9')
        print(*per)
'''

#
# № 4869 (Уровень: Сложный)
# Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
# 1 Строится двоичная запись числа N.
# 2 Вычисляется количество единиц, стоящих на чётных местах в двоичной записи числа N без ведущих нулей,
# и количество нулей, стоящих на нечётных местах. Места отсчитываются слева направо
# (от старших разрядов к младшим, начиная с единицы).
# 3 Результатом работы алгоритма становится модуль разности полученных двух чисел.

# При каком наименьшем N в результате работы алгоритма получится R = 5?
'''
for n in range(2, 10000):
    s = bin(n)[2:]
    cnt1 = len([x for x in s[1::2] if x == '1'])
    cnt0 = len([x for x in s[::2] if x == '0'])
    r = abs(cnt1 - cnt0)
    if r == 5:
        print(n)
        break
'''
# Ответ: 1023


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# № 9753 Основная волна 19.06.23 (Уровень: Сложный)
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ Y встречается не более 150 раз.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline()
s = s.split('Y')
maxi = 0
for i in range(len(s)-150):
    r = 'Y'.join(s[i:i+151])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 244


# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается не более 3 раз.
# Для выполнения этого задания следует написать программу.

# ['', 'xxxxx', 'xxxxxxx', 'xxxxxxx', 'xxxxx', 'xxxxxx', 'xxxxx', 'xxxxx', '']
# TxxxxxTxxxxxxxTxxxxxxx 22
# xxxxxTxxxxxxxTxxxxxxxTxxxxx 27
# xxxxxxxTxxxxxxxTxxxxxTxxxxxx 28
# xxxxxxxTxxxxxTxxxxxxTxxxxx 26
# xxxxxTxxxxxxTxxxxxTxxxxx 24
# xxxxxxTxxxxxTxxxxxT 19
'''
s = 'TxxxxxTxxxxxxxTxxxxxxxTxxxxxTxxxxxxTxxxxxTxxxxxT'
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    r = 'T'.join(s[i:i+4])
    # maxi = max(maxi, len(r))
    if maxi < len(r):
        maxi = len(r)
        print(r, maxi)
print(maxi)  # 28
'''


# Тип 24 №59794
# Текстовый файл состоит не более чем из 10**6 символов латинского алфавита.
# Определите минимальную длину подстроки, содержащую ровно 110 символов "U".
'''
s = open('24.txt').readline()
s = s.split('U')
mini = 9999999
for i in range(len(s)-108):
    r = 'U'.join(s[i:i+109])
    mini = min(mini, len(r))
print(mini + 2)
'''
# Ответ: 1765


# Определите в прилагаемом файле минимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается не более 3 раз.
# Для выполнения этого задания следует написать программу.

# ['', 'xxxxx', 'xxxxxxx', 'xxxxxxx', 'xxxxx', 'xxxxxx', 'xxxxx', 'xxxxx', '']
# Txxxxxxxxxxxxxxx 18
# xxxxxxxxxxxxxxxTxxxxxxx 25
# xxxxxxxTxxxxxxx 17
# xxxxxxxTxxxxx 15
# xxxxxTxxxxxx 14
# xxxxxxTxxxxx 14
# xxxxxTxxxxxxxxxxxxxxxxxx 26
# xxxxxxxxxxxxxxxxxxT 21
'''
s = 'TxxxxxxxxxxxxxxxTxxxxxxxTxxxxxxxTxxxxxTxxxxxxTxxxxxTxxxxxxxxxxxxxxxxxxT'
s = s.split('T')
mini = 9999999
for i in range(len(s)-1):
    r = 'T'.join(s[i:i+2])
    # mini = min(mini, len(r))
    if mini > len(r):
        mini = len(r)
        print(r, mini + 2)
print(mini + 2)  # 14
'''


# № 11954 (Уровень: Средний)
# (PRO100 ЕГЭ) Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих
# подряд символов (длину непрерывной подпоследовательности),
# среди которых символ X встречается не менее 500 раз, а символ Y не встречается совсем.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('X')
mini = 99999999
for i in range(len(s)-498):
    r = 'X'.join(s[i:i+499])
    if mini > len(r):
        if 'Y' not in r:
            mini = len(r)
print(mini+2)
'''


# № 4500 (Уровень: Сложный)
# 1. Прибавь 1
# 2. Прибавь 2
# 3. Умножь на 2

# Сколько существует программ, которые преобразуют исходное число 3 в число 79,
# и при этом траектория вычислений содержит число 11 и не содержит число 23.
# Также программа не должна содержать двух команд «Прибавь 1» подряд.
'''
from functools import *


@lru_cache(None)
def F(a, b, f1, f2):
    if a == 11:
        f2 = True
    if a >= b or a == 23:
        return a == b and f2 == True
    if f1 == 1:
        return F(a + 2, b, 0, f2) + F(a * 2, b, 0, f2)
    return F(a + 1, b, 1, f2) + F(a + 2, b, 0, f2) + F(a * 2, b, 0, f2)


print(F(3, 79, 0, 0))
'''

'''  # Не верно
from functools import *

@lru_cache(None)
def F(a, b, f):
    if a >= b or a == 23:
        return a == b
    if f == 1:
        return F(a + 2, b, 0) + F(a * 2, b, 0)
    return F(a+1, b, 1) + F(a+2, b, 0) + F(a*2, b, 0)

print(F(3, 11, 0) * F(11, 79, 0))
'''
# Ответ: 812266767

# endregion Разобрать: *************************************************************


# Александр = [1.1, 5.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 18.1, 19-21.1, 22.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке: Разобрать 13 номер и 5 сложыне номера
