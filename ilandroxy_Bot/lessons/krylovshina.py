# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************
'''
for s in open('17.txt'):
    print(s, type(s))
'''

# M = [int(x) for x in open('17.txt')]
# print(M)

# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(0, len(M)-1):
    print(f'{M[i]}{M[i+1]}', end=' ')
print()


# 2. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345
for i in range(0, len(M)-2):
    print(f'{M[i]}{M[i+1]}{M[i+2]}', end=' ')
print()


# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        print(f'{M[i]}{M[j]}', end=' ')
    print()


# Тип 17 №40733
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 3
# и хотя бы один из двух элементов меньше среднего арифметического всех чётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар,
# а затем — максимальную сумму элементов таких пар.
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if x % 2 == 0]
sred = sum(A) / len(A)
count = 0
maxi = 0
for i in range(0, len(M)-1):
    x, y = M[i], M[i+1]
    if x % 3 == 0 or y % 3 == 0:
        if x < sred or y < sred:
            count += 1
            maxi = max(maxi, x+y)

print(count, maxi)  
'''
# 2288 14875


# Тип 17 №59722
# Элементы ряда могут принимать целые значения в диапазоне [−10000; 10000].
# Определите количество троек элементов последовательности, в которой только одно число трехзначное,
# а сумма тройки меньше наибольшего числа, оканчивающегося на 17.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 100 == 17]
count = 0
for i in range(0, len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (len(str(abs(x))) == 3) ^ (len(str(abs(y))) == 3) ^ (len(str(abs(z))) == 3):
        if (x + y + z) < max(A):
            # print(x, y, z, (x + y + z) < max(A))
            count += 1
print(count)
'''

# todo Разобрать задачку, почему ответы не сходятся
'''
count = 0
f = open('17.txt')
l = [int(i) for i in f]
max_dvy = 0
for i in range(len(l)):
    if abs(l[i]) % 100 == 17:
        max_dvy = max(max_dvy, l[i])
print(max_dvy)
for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1],  l[i+2]]
    for x in s:
        if 99 < abs(x) < 1000:
            c += 1
    if c == 1 and sum(s) < max_dvy:
        count += 1
print(count)
'''


# Тип 17 №37355
# В файле содержится последовательность из 10 000 целых положительных чисел.
# Каждое число не превышает 10 000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 7, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
count = 0
maxi = 0
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if (x + y) % 7 == 0:
            count += 1
            maxi = max(maxi, x+y)
print(count, maxi)
'''
# 7142586 19992

'''
M = [int(x) for x in open('17.txt')]
count = 0
maxi = 0
for i in range(len(M)):  # 100000000
    for j in range(len(M)): 
        x, y = M[i], M[j]
        if (x * y) % 34 != 0:
            maxi = max(maxi, x + y)
            count += 1
print(count, maxi)
'''

'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '3?6906*4'):
        print(x)
'''
# 3969064
# 336906944
# 3069064064
# 3169069904
# 3269065624
# 3369061344
# 3469067184
# 3569062904
# 3669068744
# 3769064464
# 3869060184
# 3969066024


from fnmatch import *
for x in range(2919, 10**10, 2919):
    if fnmatch(str(x), '9*253?74'):
        print(x, x // 2919)


# 983253474 336846
# 9167253774 3140546
# 9531253074 3265246
# 9740253474 3336846
# 9949253874 3408446

# endregion Урок: ***************************************************************


# Анастасия = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 16.1, 17.1, 23.1]
# КЕГЭ  = []
# на следующем уроке:
