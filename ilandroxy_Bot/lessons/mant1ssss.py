# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 12918 PRO100 ЕГЭ 26.01.24 (Уровень: Средний)
'''
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    povtor = [x for x in M if M.count(x) == 2]
    if len(set(povtor)) == 2:
        if M.count(max(M)) == 1:
            if max(M)*min(M) > sum(M[1:-1]):
                print(sum(M))
                exit()
'''


# № 12463 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый)
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    povtor = [M.count(x) for x in M]
    copied = [x for x in M if M.count(x) > 1]
    nepovtor = [x for x in M if M.count(x) == 1]
    if povtor.count(4) == 4 and povtor.count(1) == 3:
        if sum(nepovtor)/len(nepovtor)>= max(copied):
            count += 1
print(count)
'''


# № 12098 Новогодний вариант (Уровень: Базовый)
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    povtor = [x for x in M if M.count(x) == 3]
    nepovtor = [x for x in M if M.count(x) == 1]
    if len(set(povtor)) == 1:
        if povtor[0] % 2 != 0:
            if nepovtor[0] % 2 == 0:
                count += 1
print(count)
'''

# № 9062 Danov2306 (Уровень: Средний)
'''
count = 0
for s in open('9.txt'):
    M = [int(x)for x in s.split()]
    if M[0] != min(M) and M[-1] != min(M) and M[0] != max(M) and M[-1] != max(M):
        m = sorted([int(x) for x in s.split()])
        if m[1] != m[2]:
            if ((max(m)-min(m)) % abs(m[1]-m[2])) == 0:
                count += 1
print(count)
'''


# № 6898 OpenFIPI (Уровень: Базовый)
'''
from itertools import permutations
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if max(M) < (sum(M) - max(M)):
        if any((p[0] + p[1]) == (p[2] + p[3]) for p in permutations(M)):
            count += 1
print(count)
'''

# endregion Урок: *******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Марк = [1.1, 2.1, 3.1, 6.1, 4.1, 5.1, 7.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 22.1, 23.1, 24.1, 25.1]
# КЕГЭ  = [5.1, 8.1, 9.1, 14.1]
# на следующем уроке:
