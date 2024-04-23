
# region Домашка: *********************************************************************

# endregion Домашка: ******************************************************************

# region Урок: *********************************************************************
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not y)) or (z == x) or w
                if not F:
                    print(x, y, z, w)
'''


# номер 7
'''
pixels = 2912 * 480
colors = 8558
print(2 ** 14)
i = 14
I = pixels * i  # бит
print((32758 * I) / (2**23))
'''
# Ответ: 76416


# Номер 9: № 15321
# (М. Ишимов) Откройте файл электронной таблицы, содержащей в
# каждой строке четыре натуральных числа. Определите количество строк
# таблицы, содержащих числа, для которых выполнены оба условия:
# – максимальное число строки меньше суммы трёх оставшихся чисел;
# – четыре числа строки можно разбить на две пары чисел с равными суммами.
# В ответе запишите только число.
'''
from itertools import permutations
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M[3] < (M[0] + M[1] + M[2]):
        if any(R[0] + R[1] == R[2] + R[3] for R in permutations(M)):
            cnt += 1
print(cnt)
'''
# Ответ: 128


# Номер 24 № 15339
# (М. Ишимов) Текстовый файл состоит из символов латинского алфавита A, B, C,
# и цифр 6, 7, 8, 9.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых никакая буква не стоит рядом с буквой, а цифра – с цифрой.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A')
s = s.replace('6', '8').replace('7', '8').replace('9', '8')
while '88' in s or 'AA' in s:
    s = s.replace('88', '8 8').replace('AA', 'A A')
print(max([len(x) for x in s.split()]))
'''


# № 14645 Открытый курс "Слово пацана" (Уровень: Средний)
# (М. Попков) Во входном файле в строчку записаны заглавные буквы английского алфавита.
# Требуется найти самую длинную последовательность, в которой гласные и
# согласные буквы чередуются. В ответ запишите длину найденной последовательности.
# Примечание: Y – гласная буква.
'''
import string

alphbaet = string.ascii_uppercase

s = open('24.txt').readline()
for a in 'AEIOUY':
    s = s.replace(a, 'A')
for a in alphbaet:
    if a not in 'AEIOUY':
        s = s.replace(a, 'B')
while 'AA' in s or 'BB' in s:
    s = s.replace('AA', 'A A').replace('BB', 'B B')
print(s)
print(max([len(x) for x in s.split()]))
'''


# Задача № 7174
# (А. Носкин) Маша составляет семибуквенные слова перестановкой букв слова ГЛУБИНА.
# Сколько существует слов, в которых буква «Г» расположена после букв «А» и «И»?
'''
from itertools import permutations
cnt = 0
for p in permutations('ГЛУБИНА'):
    word = ''.join(p)
    if word.index('А') < word.index('Г') and word.index('И') < word.index('Г'):
        cnt += 1
print(cnt)
'''

'''
from ipaddress import *
net = ip_network('124.8.0.0/255.248.0.0', 0)
maxi = 0
for ip in net:
    s = f'{ip:b}'
    maxi = max(maxi, s.count('0'))
print(maxi)
'''


# (№ 4199) Ксения составляет слова из букв К, С, Е, Н, И, Я.
# Каждая гласная буква встречается в слове не более двух раз.
# Каждая согласная может стоять в слове на первой позиции, либо не встречаться вовсе.
# Сколько различных слов длиною более двух символов может составить Ксения?
'''
from itertools import *
cnt = 0
for n in range(3, 7+1):
    for p in product('КСЕНИЯ', repeat=n):
        word = ''.join(p)
        if all(word.count(x) <= 2 for x in 'ЕИЯ'):
            word = word.replace('Н', 'С').replace('К', 'С')
            if (word[0] == 'С' and word.count('С') == 1) or ('С' not in word):
                cnt += 1
print(cnt)
'''
# Ответ: 1059


# № 8472 (Уровень: Средний)
# (В. Рыбальченко) Дано арифметическое выражение: 7Ax0123_100 −1BA64x_100 + x98012C_100
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 100-ричной
# системы счисления. Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 21.
# Найденное значения x укажите в ответе в шестеричной системе счисления.
'''
from string import digits, ascii_uppercase
alphabet = digits + ascii_uppercase


def my_int(num: list, base: int):
    return sum(x*base**i for i, x in enumerate(num[::-1]))


def convert(num: int, base: int):
    result = ''
    while num > 0:
        result = alphabet[num % base] + result
        num //= base
    return result


maxi = 0
for x in range(0, 100):
    r = my_int([7, 10, x, 0, 1, 2, 3], 100) - my_int([1, 11, 10, 6, 4, x], 100) + my_int([x, 9, 8, 0, 1, 2, 12], 100)
    if r % 21 == 0:
        maxi = max(maxi, int(convert(x, 6)))
print(maxi)
'''
# Ответ: 224

'''
def my_int(num: list, base: int):
    result = 0
    num.reverse()
    for i in range(len(num)):
        result += num[i] * base ** i
    return result
'''

"""
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
for i, x in enumerate(M):
    print(i, x)
    # 0 a
    # 1 b
    # 2 c
    # 3 d
    # 4 e
    
    
def my_int(num: list, base: int):
    return sum(x*base**i for i, x in enumerate(num[::-1]))


print(my_int([1, 0, 0, 0], 2))
"""


# № 9904 (Уровень: Сложный)
# (С. Чайкин) Дано арифметическое выражение:
# В записи чисел переменными x и y обозначены неизвестная цифра из допустимого алфавита для указанных систем счисления.
# Определите значения x и y, при которых значение данного арифметического выражения является максимальным.
# Для найденных значений вычислите частное от деления нацело значения арифметического выражения на сумму
# x и y и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответ указывать не нужно.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in range(10, 14):
    for y in range(9, x):
        r = int(f'7{alphabet[x]}37{alphabet[y]}', 14) + int(f'9{alphabet[y]}63', x) - int(f'15148', y)
        R.append([r, r // (x + y)])
print(max(R)[1])


def my_int(num: list, base: int):
    return sum(x*base**i for i, x in enumerate(num[::-1]))

R = []
for x in range(10, 14):
    for y in range(9, x):
        r = my_int([7, x, 3, 7, y], 14) + my_int([9, y, 6, 3], x) - my_int([1, 5, 1, 4, 8], y)
        R.append([r, r // (x + y)])
print(max(R)[1])
'''

# Вариант PRO100EGE номер 7 (https://kompege.ru/variant?kim=25048321)
# Номер 17
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if str(x)[-3:] == '121']
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if len([p for p in (x, y, z) if len(str(abs(p))) == 4 and abs(p) % 2 == 0]) <= 1:
        if (x + y + z) <= max(A):
            R.append(x + y + z)
print(len(R), max(R))
'''
# Ответ: 5211 20116


# КЕГЭ № 858 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 106 заглавных латинских букв (A..Z).
# Текст разбит на строки различной длины.
# Определите количество строк, в которых встречается комбинация F*O,
# где звёздочка обозначает любой символ.
'''
s = open('24.txt').readlines()
cnt = 0
for x in s:
    if any(f'F{a}O' in x for a in 'QWERTYUIOPASSDFGHJKLZXCVBNM'):
        cnt += 1
print(cnt)
'''
# Ответ: 757


# КЕГЭ № 6094 /dev/inf 02.2023 (Уровень: Средний) (А. Рогов)
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд пар символов
# вида согласная + гласная среди которых нет подстроки XYZY.
'''
s = open('24.txt').readline()
s = s.replace('XY', '*').replace('ZY', '+')
for a in 'XYZ':
    s = s.replace(a, ' ')
s = s.replace('*+', '* +')
print(max([len(x) for x in s.split()]))
'''


# На числовой прямой даны два отрезка: C=[152;223].
# Укажите наименьшую возможную длину такого отрезка A,
# для которого логическое выражение
# (¬(x∈A)∧(x∈B))→((x∈B)→¬(x∈C))
# истинно (т. е. принимает значение 1) при любом значении переменной x.
'''
def F(a1, a2, x):
    B = 74 <= x <= 194
    C = 152 <= x <= 223
    A = a1 <= x <= a2
    return ((not A) and B) <= (B <= (not C))

R = []
M = [x / 4 for x in range(70 * 4, 230 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(a1, a2, x) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


# Откройте файл электронной таблицы, содержащей в каждой строке
# четыре натуральных числа. Определите количество строк таблицы,
# содержащих числа, для которых выполнены все условия:
#
# четыре числа строки можно разбить на две пары чисел с равными суммами
# максимальное число строки меньше суммы трёх оставшихся чисел
# сумма чисел в строке чётна
'''
from itertools import *

cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
        if M[3] < M[0] + M[1] + M[2]:
            cnt += 1
print(cnt)
'''

# Занятие
'''
pixels = 1079 * 1919
print(2**13)
i = 13
I = (pixels * i) * 199
print(I / 19_999_999)
'''

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo Разобрать новые 22 номера № 12474 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый)

# todo Тип 24 №55641
'''
f = open('24.txt').readlines()пш
li = []
for j in f:
    st = ''
    for x, y in zip(j, j[1:]):
        if x == 'T':
            st += y
    maxi = max(st.count(i) for i in set(st))
    for s in set(st):
        if st.count(s) == maxi:
            li += [s]
print(max(li.count(l) for l in set(li)))
'''


# todo - Разобрать Тип 13 №64943
# Узлы с IP -адресами 202.3.20.24 и 202.3.27.11 находятся в одной сети.
# Укажите наименьшее возможное количество принадлежащих этой сети IP-адресов,
# в двоичной записи которых чётное число единиц.
'''
from ipaddress import *
mini = 10**9
for mask in range(32+1):
    cnt = 0
    net1 = ip_network(f'202.3.20.24/{mask}', 0)
    net2 = ip_network(f'202.3.27.11/{mask}', 0)
    if net1 == net2:
        for ip in net1:
            s = f'{ip:b}'
            if s.count('1') % 2 == 0:
                cnt += 1
    maxi = max(maxi, cnt)
    print(maxi)
'''
# Ответ: 2048


# todo Разобрать задачку https://stepik.org/lesson/1231755/step/9?unit=1245338
# (А.Богданов) В файле содержится последовательность натуральных чисел.
# Рассматриваются все пары элементов, в которых только один элемент чётный,
# и между элементами пары есть ровно один элемент и он кратен минимальному
# четному элементу из всех элементов последовательности.
# Найти количество таких пар и пару с минимальной суммой.
'''
M = [int(i) for i in open('17.txt')]
n = min([i for i in M if i % 2 == 0])  # минимальному четному элементу из всех элементов последовательности
B = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        z = M[M.index(x) + 1]
        if M.index(y) - M.index(x) == 2:
            if (x % 2 == 0) != (y % 2 == 0):
                if z % n == 0:
                    B.append(x + y)
print(len(B), min(B))
'''
#  0  1  2  3  4
# [4, 5, 6, 7, 8]

'''
M = [int(i) for i in open('17.txt')]
n = min([i for i in M if i % 2 == 0])  # минимальному четному элементу из всех элементов последовательности
count = 0
mini = 9999999
r = ''
for i in range(len(M) - 2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x % 2 == 0) != (z % 2 == 0):
        if y % n == 0:
            count += 1
            if mini > x + z:
                mini = x + z
                r = [x, y]
print(count, r)
'''


# endregion Разобрать: *************************************************************


# GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:

# if __name__ == "__main__":
#     print('Файл групповых занятий')


