
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

'''
from functools import *

@lru_cache(None)
def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * f(n-2) - f(n-1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * f(n-1) + f(n-2) - 2

print(f(170))
'''


# каждую строчку файла 9.txt разбиваем на списки
'''
for s in open('9.txt'):
    M = [int(x) for x in s.split()]

# каждую строчку файла 17.txt сразу читаем в общий список
M = [int(x) for x in open('17.txt')]
'''

# Работа с разными типами задач номер 17
'''
M = [1, 2, 3, 4, 5]
# 1. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    print(f'{x}{y}', end=' ')
print()
# IndexError: list index out of range


# 2. Назовём тройкой три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    print(f'{x}{y}{z}', end=' ')
print()

# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        print(f'{x}{y}', end=' ')
    print()
'''

'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if str(x)[-2:] == '21' and len(str(abs(x))) == 5]
R = []  # Складывать суммы пар и таким образом найдем кол-во пар
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A and y not in A) or (y in A and x not in A):
        if (x**2 + y ** 2) >= max(A) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''


# № 14653 Открытый курс "Слово пацана" (Уровень: Сложный)
'''
M = [int(x) for x in open('17.txt')]
A = sorted([x for x in M if abs(x) % 17 == 0 and x > 0])
B = [x for x in M if str(x)[-2:] == '69']
R = []
mini = 10**9
for i in range(len(M)-3):
    x, y, z, w = M[i:i+4]  # M[i], M[i+1], M[i+2], M[i+3]
    if len([a for a in (x, y, z, w) if len(str(abs(a))) == 3]) == 2:
        if len([a for a in (x, y, z, w) if abs(a) % 18 == 0]) == 1:
            if (x + y + z + w) % sum(A[:2]) == 0:

                if (x * y * z * w) <= max(B) ** 2:
                    R.append((x + y + z + w) ** 2)
print(len(R), min(R))
'''

'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)
'''
# 351261495 183235
# 3212614035 1675855
# 3412614645 1780185
# 3712414275 1936575
# 3912414885 2040905
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '112?57*4'):
        # summa = sum([int(a) for a in str(x)])
        summa = sum(map(int, str(x)))
        if summa % 2 != 0:
            print(x, x//2024)
'''
# 11275704 5571
# 1124576904 555621
# 1126570544 556606
# 1127572424 557101
# 1128574304 557596

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Геля = [1, 2, 3, 4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 13, 14, 17, 18, 19-21, 22, 23]
# на следующем уроке: 24, 25
