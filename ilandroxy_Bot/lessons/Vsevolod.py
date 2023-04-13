
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

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


# Тип 24 № 27689 i
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
'''
s = open('24.txt').readline()
print(s)
print(len('XYZXYZXYZXYZX'))
'''
# Ответ: 13


# Тип 24 № 36037 i
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
'''
# s = 'XZZYOOOOXZZY'
# s = ' ZZYOOOOXZZ '
# s = ' OOOO '

s = open('24.txt').readline()
s = s.replace('XZZY', ' ')
M = [len(i) for i in s.split()]
print(3 + max(M) + 3)
'''
# Ответ: 1713


# Тип 24 № 47228 i
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида
# согласная + гласная.
'''
s = open('24.txt').readline()
M = 'CA CO DA DO FA FO'.split()
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


# Тип 24 № 33494 i
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы E.
'''
s = open('24.txt').readline()
M = []
for i in range(0, len(s)-1):
    if s[i] == 'E':
        M.append(s[i+1])

ALPHABET = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])

# import string
# ALPHABET = string.ascii_uppercase

R = []
for a in ALPHABET:
    R.append([M.count(a), a])
print(max(R))
'''
# Ответ: Y


# Тип 24 № 33526 i
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
'''
s = open('24.txt').readline()
M = []
for i in range(0, len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])

ALPHABET = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])

# import string
# ALPHABET = string.ascii_uppercase

R = []
for a in ALPHABET:
    R.append([M.count(a), a])
print(max(R))
'''
# Ответ: D


# Тип 24 № 29672 i
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква E встречается чаще, чем буква A.
'''
# Вариант 1
s = open('24.txt').readlines()
count = 0
for x in s:
    if x.count('E') > x.count('A'):
        count += 1
print(count)

# Вариант 2
print(len([x for x in open('24.txt').readlines() if x.count('E') > x.count('A')]))
'''
# Ответ: 467


# Тип 24 № 35913
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# - Необходимо найти строку, содержащую наименьшее количество букв N
# (если таких строк несколько, надо взять ту, которая находится в файле раньше);

# - И определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
s = open('24.txt').readlines()
r = ''
mini = 99999
for x in s:
    if mini > x.count('N'):  # надо взять ту, которая находится в файле раньше
        mini = x.count('N')
        r = x

ALPHABET = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
maxi = -99999
for a in ALPHABET:
    if maxi <= r.count(a):  # надо взять ту, которая позже стоит в алфавите
        maxi = r.count(a)
        print(maxi, a)
'''
# Ответ: Y


# Тип 24 № 35998
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# - В строках, содержащих менее 25 букв A, нужно определить;
#
# - B вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
s = open('24.txt').readlines()
R = []
for x in s:
    if x.count('A') < 25:
        R.append(x)

ALPHABET = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
maxi = -99999
for x in R:
    for a in ALPHABET:
        maxi = max(maxi, x.rindex(a)-x.index(a))
print(maxi)
'''
# Ответ: 1004



# endregion Урок: ******************************************************************


# todo: Всеволод = [2, 5.1, 8, 9, 12, 14, 15, 16, 17, 23, 25]
# на прошлом уроке: Прорешали все 9 номера  и затронули 24 номер первого типа.
# на следующем уроке:
