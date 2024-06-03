
# region Домашка: *********************************************************************

# endregion Домашка: ******************************************************************

# region Урок: *********************************************************************
'''
num = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    num += 1
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2 and len(not_copied) == 4:
        if copied[0] >= (sum(not_copied) / 4):
            print(num)
            exit()
'''


# № 9793 Основная волна 20.06.23 (Уровень: Средний)
'''
f = open('26.txt')
N = int(f.readline())
A = []
B = []
M = []

# f = ["30 50", "100 175", "150 170", "10 160", "120 55"]
for s in f:
    x, y = [int(x) for x in s.split()]
    A += [x]
    B += [y]
    M += [x, y]

M = sorted(M)

R1 = []
R2 = []
K = 0
for x in sorted(M):
    if x in A:
        if A.index(x)+1 not in R1 and A.index(x)+1 not in R2:
            R1 += [A.index(x)+1]
            K = A.index(x)+1
    elif x in B:
        if B.index(x)+1 not in R2 and B.index(x)+1 not in R1:
            R2 = [B.index(x)+1] + R2
            K = B.index(x)+1
print(K)
if K in R1:
    print(len(R1)-1)
else:
    print(len(R1))
'''
# [2, 1, 0, 3, 4]
# [4, 1, 2, 3, 5]
# 4  1  2  3| 5
# 10 30 50 55 100 120 150 155 160 170


# № 4712 Демоверсия 2023 (Уровень: Базовый)
'''
f = open('26.txt')
N = int(f.readline())
M = sorted([int(x) for x in f])[::-1]

R = [9998]
for x in M[1:]:
    if x <= R[-1] - 3:
        R.append(x)
print(len(R), min(R))



f = open('26.txt')
N = int(f.readline())
M = sorted([int(x) for x in f])[::-1]

R = [M.pop(0)]
for x in M:
    if x <= R[-1] - 3:
        R.append(x)
print(len(R), min(R))


M = [3, 4, 5, 6, 7, 8]
x = M.pop(0)
print(M)
print(x)
'''

# № 4629 Основная волна 2022 (Уровень: Базовый)
'''
f = open('26.txt')
N = int(f.readline())
M = sorted([int(x) for x in f])

summa1 = sum(M) - sum(M[7500:]) * 0.5
summa2 = sum(M) - sum(M[:2500]) * 0.5
print(summa1, summa2)
'''


# № 2612 (Уровень: Базовый)

f = open('26.txt')
N, M = [int(x) for x in f.readline().split()]
A = sorted([int(x) for x in f])[::-1]

for i in range(M, 0, -1):
    if A[i] > A[M]:
        print(A[i])
        break
R = []
for i in range(M, N):
    if A[i] < A[M]:
        R.append(A[i])
print(sum(R) // len(R))



# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:



