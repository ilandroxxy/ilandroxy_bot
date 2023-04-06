
# region Домашка: ******************************************************************

'''Тип 17 № 37373
M = [int(i) for i in open('17.txt')]
c = 0
maxraz = -999
for i in range(len(M) - 1):
    for y in range(i + 1, len(M)):
        if (max(M[i], M[y]) - min(M[i], M[y])) % 36 == 0 and (M[i] % 13 == 0 or M[y] % 13 == 0):
                c += 1
                if max(M[i], M[y]) - min(M[i], M[y]) > maxraz:
                    maxraz = max(M[i], M[y]) - min(M[i], M[y])
print(c, maxraz)
'''

'''Тип 17 № 37337
M = [int(i) for i in open('17.txt')]
maxim = -9999
c = 0
for i in range(len(M) - 1):
    for j in range(i + 1, len(M)):
        if M[i] % 160 != M[j] % 160 and (M[i] % 7 == 0 or M[j] % 7 == 0):
            c += 1
            if maxim < M[i] + M[j]:
                maxim = M[i] + M[j]
print(c, maxim)
'''

'''Тип 17 № 37371
M = [int(i) for i in open('17.txt')]
c = 0
maxim = -9999
for i in range(len(M) - 1):
    for j in range(i + 1, len(M)):
        if (max(M[i], M[j]) - min(M[i], M[j])) % 60 == 0:
            c += 1
            maxim = max(maxim, max(M[i], M[j]) - min(M[i], M[j]))
print(c, maxim)
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

M = [1, 2, 3, 4, 5]
'''
print(M[3])
print(M[3:])  # все что справа
print(M[:3])  # все что слева
print(M[::-1])

# for i in range(len(M)-1):
#     print(f'{M[i]}{M[i+1]}', end=' ')

for i in range(len(M)-1):
    print(M[i:i+2], end=' ')
'''

# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
'''   
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(f'{M[i]}{M[j]}', end=' ')
    print()

for i in range(0, len(M)):
    for j in range(0, len(M)):
        if i < j:
            print(f'{M[i]}{M[j]}', end=' ')
    print()

for x in M:
    for y in M:
        if x < y:
            print(f'{x}{y}', end=' ')
    print()
'''


# Тип 9 № 33088
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх
# месяцев. Определите, сколько раз за время наблюдений суточные колебания температуры (разность между максимальной и
# минимальной температурой в течение суток) были меньше 14 градусов.
'''
count = 0
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    if max(M) - min(M) < 14:
        count += 1
print(count)
'''
# Ответ: 6

'''
M = [1, 4, 5,23,43 ,423]
M.sort()
print(M)

A = [1, 5, 6,34,4 ,5,45, 4]
print(sorted(A))
print(A)
'''


# КЕГЭ № 6897 OpenFIPI (Уровень: Средний)
# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# – наибольшее из четырёх чисел меньше суммы трёх других;
#
# – четыре числа нельзя разбить на две пары чисел с равными суммами.
#
# В ответе запишите только число.

import itertools
count = 0
for s in open('9.txt'):
    # M = sorted([int(i) for i in s.split()])
    # if M[3] < M[0] + M[1] + M[2]:
    M = [int(i) for i in s.split()]
    if max(M) < sum(M) - max(M):
        # if all(A[0] + A[1] != A[2] + A[3] for A in itertools.permutations(M, 4)):
        # if all(sum(A[:2]) != sum(A[2:]) for A in itertools.permutations(M, 4)):
        if any(sum(A[:2]) == sum(A[2:]) for A in itertools.permutations(M, 4)) == False:
            count += 1
print(count)

# Ответ: 2396


# M = [int(i) for i in open('9.txt').read().split()]
# print(M)




# endregion Урок: ******************************************************************


# todo: Сергей = [2, 5, 8, 9, 12, 14, 15, 16, 17, 23, 25]
# на прошлом уроке: Разбирали 9-ые номера работа с txt файлами
# на следующем уроке:
