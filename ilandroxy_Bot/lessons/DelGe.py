# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ************************************************************

# КЕГЭ № 7262 OpenFIPI (Уровень: Базовый)
'''
s = '4' * 60 + '6' * 60 + '8' * 60
while '46' in s or '84' in s or '86' in s:
    if '46' in s:
        s = s.replace('46', '64', 1)
    if '84' in s:
        s = s.replace('84', '48', 1)
    if '86' in s:
        s = s.replace('86', '68', 1)
print(s[24] + s[74] + s[149])
'''


# КЕГЭ № 9835 Основная волна 27.06.23 (Уровень: Базовый)
'''
for n in range(4, 10000):
    s = "1" + "8" * n
    while "18" in s or "388" in s or "888" in s:
        if "18" in s:
            s = s.replace("18", "8", 1)
        if "388" in s:
            s = s.replace("388", "81", 1)
        if "888" in s:
            s = s.replace("888", "3", 1)
    if s.count("1") == 3:
        print(n)
        break
'''


# КЕГЭ № 9367 (Уровень: Сложный)
'''
from itertools import *
for n in range(1, 100):
    for p in permutations(["1" * 40, "2" * 40, "3" * n]):
        s = ''.join(p)
        while "23" in s or "12" in s or "32" in s:
            if "12" in s:
                s = s.replace("12", "21", 1)
            if "32" in s:
                s = s.replace("32", "1", 1)
            if "23" in s:
                s = s.replace("23", "2", 1)
        summa = sum([int(x) for x in s])
        if summa == 100:
            print(n)
            break
'''

'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for m in range(0, 1000):
    s = '>' + '1' * 15 + '2' * 35 + '3' * m

    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '3>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>', 1)

    summa = sum([int(x) for x in s if x.isdigit()])
    if len(divisors(summa)) == 3:
        print(m)
'''

'''
from fnmatch import *
for x in range(98591, 10**10, 98591):
    if fnmatch(str(x), '5?2*3?3?'):
        print(x, x // 98591)
'''

'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)
'''

'''
from fnmatch import *
for x in range(2023, 10**9, 2023):
    if fnmatch(str(x), '20*23'):
        summa = sum([int(x) for x in str(x)])
        if summa % 7 == 0 and summa < 20:
            print(x)
'''
# Ответ:
# 2023
# 204323
# 2025023
# 20232023
# 202302023

# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Евгений = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12]
# на следующем уроке:
