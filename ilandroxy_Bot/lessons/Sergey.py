
# region Домашка: ******************************************************************

'''
Тип 17 № 37336
file = [int(i) for i in open('17.txt')]
c = 0
maxsum = -9999999
for x in range(len(file) - 1):
    if file[x] % 3 == 0 or file[x + 1] % 3 == 0:
        c += 1
        maxsum = max(maxsum, file[x] + file[x + 1])
print(c, maxsum)
'''

'''
Тип 17 № 37337
file = [int(i) for i in open('17.txt')]
c = 0
maxsum = -99999
for x in range(len(file) - 1):
    for y in range(x+1, len(file)):
        if ((file[x] % 160) != (file[y] % 160)) and (file[x] % 7 == 0 or file[y] % 7 == 0):
            c += 1
            maxsum = max(maxsum, file[x] + file[y])
print(c, maxsum)
'''

'''
Тип 17 № 37340
file = [int(i) for i in open('17.txt')]
c = 0
maxsum = -99999
for x in range(len(file) - 1):
    for y in range(x+1, len(file)):
        if (((file[x] - file[y]) % 2 == 0)) and (file[x] % 31 == 0 or file[y] % 31 == 0):
            c += 1
            maxsum = max(maxsum, file[x] + file[y])
print(c, maxsum)
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 24 № 27697 i
# Текстовый файл состоит не более чем из 10**6 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов D.
# Хотя бы один символ D находится в последовательности.
'''
# Вариант 1
s = open('24.txt').readline()
count = 1  # длина промежуточной последовательности
maxi_count = 0  # длина наибольшей последовательности
for i in range(0, len(s)-1):
    if s[i] == 'D' and s[i+1] == 'D':
        count += 1
        maxi_count = max(maxi_count, count)
    else:
        count = 1
print(maxi_count)

# Вариант 2.1
s = open('24.txt').readline()
s = s.replace('L', ' ').replace('R', ' ')
M = [len(i) for i in s.split()]
print(max(M))

# print(len(max(M, key=len)))
# print(len(max(M, key=lambda x: len(x))))

# Вариант 2.2
print(max([len(i) for i in open('24.txt').readline().replace('L', ' ').replace('R', ' ').split()]))

# Вариант 3
s = open('24.txt').readline()
print(s)
print(len('DDDDDDDDDDD'))
'''
# Ответ: 11


# Тип 24 № 27689
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
'''
s = open('24.txt').readline()
print(s)
print(len('XYZXYZXYZXYZX'))
'''
# Ответ: 13


# Тип 24 № 40740
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
# Определите максимальное количество идущих подряд символов,
# среди которых нет ни одной буквы A и при этом не менее трёх букв E.
'''
s = open('24.txt').readline()
s = s.replace('A', ' ')
M = [len(i) for i in s.split() if i.count('E') >= 3]
print(max(M))
'''
# Ответ: 282


# Тип 24 № 36037 i
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
'''
s = open('24.txt').readline()
s = s.replace('XZZY', ' ')
M = [len(i) for i in s.split()]
print(3 + max(M) + 3)
'''
# Ответ: 1713


# Тип 24 № 27421 i
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
s = open('24.txt').readline()
count = 1
maxi = 0
for i in range(0, len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''
# Ответ: 35


# Тип 24 № 47228
# Текстовый файл состоит из символов A, C, D, F и O.
#
# Определите максимальное количество идущих подряд пар символов вида
# согласная + гласная.
'''
s = open('24.txt').readline()
M = 'CA DA FA CO DO FO'.split()
print(M)
for x in M:
    s = s.replace(x, '*')
for x in 'ACDFO':
    s = s.replace(x, ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 95


# Тип 24 № 48445
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите максимальное количество идущих подряд групп символов вида
# согласная + согласная + гласная.
'''
import itertools
M = []
for s in itertools.product('ACDFO', repeat=3):
    if s[0] in 'CDF' and s[1] in 'CDF' and s[2] in 'AO':
        s = ''.join(s)
        M.append(s)

s = open('24.txt').readline()
for x in M:
    s = s.replace(x, '*')
for x in 'ACDFO':
    s = s.replace(x, ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 5


# Тип 24 № 33769 i
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле после двух одинаковых символов.
'''
s = open('24.txt').readline()
M = []
for i in range(0, len(s)-2):
    if s[i] == s[i+1]:
        M.append(s[i+2])

ALPHABET = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
print(ALPHABET)

# import string
# ALPHABET = string.ascii_uppercase
# print(ALPHABET)

R = []
for a in ALPHABET:
    R.append([M.count(a), a])
print(max(R))
'''
# Ответ: K


# Тип 24 № 29672
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква E встречается чаще, чем буква A.
'''
# Вариант 1
count = 0
for s in open('24.txt'):
    if s.count('E') > s.count('A'):
        count += 1
print(count)

# Вариант 2
print(len([s for s in open('24.txt') if s.count('E') > s.count('A')]))
'''
# Ответ: 467


# Тип 24 № 35482 i
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# - Необходимо найти строку, содержащую наименьшее количество букв G
# (если таких строк несколько, надо взять ту, которая находится в файле раньше);

# - И определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
mini = 9999
r = ''
for s in open('24.txt'):
    if mini > s.count('G'):  # надо взять ту, которая находится в файле раньше
        mini = s.count('G')
        r = s

ALPHABET = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
maxi = -9999
for a in ALPHABET:
    if maxi <= r.count(a):  # надо взять ту, которая позже стоит в алфавите
        maxi = r.count(a)
        print(maxi, a)
'''
# Ответ: Т


# Тип 24 № 36879
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# - В строках, содержащих менее 25 букв G, нужно определить;
# - B вывести максимальное расстояние между одинаковыми буквами в одной строке.

# Вариант 1
'''
M = []
for s in open('24.txt'):
    if s.count('G') < 25:
        M.append(s)

ALPHABET = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')

maxi = 0
for x in M:
    for a in ALPHABET:
        maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)
'''
# Вариант 2
'''
ALPHABET = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')

maxi = 0
for s in open('24.txt'):
    if s.count('G') < 25:
        for a in ALPHABET:
            maxi = max(maxi, s.rindex(a) - s.index(a))
print(maxi)
'''
# Ответ: 1001






# endregion Урок: ******************************************************************


# todo: Сергей = [2, 5, 8, 9, 12, 14, 15, 16, 17, 23, 24, 25]
# на прошлом уроке: Разбирали 9-ые номера работа с txt файлами
# на следующем уроке: Теория игр
