# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 16374 ЕГКР 27.04.24 (Уровень: Базовый)
# Сколько существует семизначных семеричных чисел,
# которые содержат в своей записи ровно две чётные цифры?
'''
from itertools import *
cnt = 0
for s in product('0123456', repeat=7):
    num = ''.join(s)
    if num[0] != '0':
        chet = [x for x in num if x in '0246']
        if len(chet) == 2:
            cnt += 1
print(cnt)
'''
# 75816


# № 6894 OpenFIPI (Уровень: Базовый)
'''
from itertools import *
num = 0
for s in product(sorted('ЦАПЛЯ'), repeat=5):
    slovo = ''.join(s)
    num += 1
    if slovo.count('А') <= 1:
        if slovo.count('Ц') == 2:
            if 'Л' not in slovo:
                print(num, slovo)
                break
'''


# № 16383 ЕГКР 27.04.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('17.txt')]
D = [x for x in M if str(x)[-2:] == '21' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-1):
    x, y = M[i:i+2]
    if (x in D) != (y in D):
        if (x**2 + y**2) >= max(D) ** 2:
            R.append(x+y)
print(len(R), max(R))
'''


# № 14653 Открытый курс "Слово пацана" (Уровень: Сложный)
'''
M = [int(x) for x in open('17.txt')]
D = sorted([x for x in M if x > 0 and x % 17 == 0])
B = [x for x in M if str(x)[-2:] == '69']
R = []
for i in range(len(M)-3):
    x, y, z, w = M[i:i+4]
    if len([j for j in (x, y, z, w) if len(str(abs(j))) == 3]) == 2:  # в которых только два элемента являются трехзначными числами
        if len([j for j in (x, y, z, w) if j % 18 == 0]) == 1:  # ровно один элемент делится на 18
            if (x + y + z + w) % (D[0] + D[1]) == 0:  # а сумма элементов делится на сумму двух минимальных положительных элементов последовательности, кратных 17
                if (x * y * z * w) <= max(B) ** 2:  # и произведение элементов не превосходит квадрат максимального элемента последовательности, оканчивающегося на 69
                    R.append((x + y + z + w)**2)
print(len(R), min(R))
'''

# № 7718 (Уровень: Средний)
'''
M = [int(x) for x in open('17.txt')]
R = []
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) != ((x * y) % 18 == 0):
            R.append(x + y)
print(len(R), max(R))
'''
# 120400 19971


# № 16375 ЕГКР 27.04.24 (Уровень: Базовый)
'''
import math
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    not_copied = sorted([x for x in M if M.count(x) == 1])
    if len(copied) == 2 and len(not_copied) == 5:
        if math.prod(not_copied[:3]) > math.prod(copied):
            cnt += 1
print(cnt)
'''


# № 16320 Открытый вариант 2024 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M[-1] < (M[0] + M[1] + M[2]):
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Вика = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ  = [2, 3, 6, 8, 9, 14, 17]
# на следующем уроке:
