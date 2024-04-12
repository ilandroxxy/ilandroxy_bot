# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
M = [int(x) for x in open('17.txt')]
print(len(M))  # 6634
s = M.copy()


flag = True
mini = min(s)
while flag:
    mini = min(s)
    s.remove(mini)
    if (mini % 52) == 0:
        flag = False

print(len(M))  # 5841

cnt = 0
maxi = 0
mini = 52
for j in range(len(M)-2):
    ost_1 = M[j] % 113
    ost_2 = M[j+1] % 113
    ost_3 = M[j+2] % 113
    summa = ost_3 + ost_2 + ost_1
    if summa == mini:
        cnt += 1
        if (M[j] + M[j+1] + M[j+2]) > maxi:
            maxi = (M[j] + M[j+1] + M[j+2])
print(cnt, maxi)
'''

import sys
from functools import *

sys.setrecursionlimit(10000)
@lru_cache(None)
def F(st, fin, flag):
    if st > fin:
        return 0
    if st == fin:
        print(flag)
        return 1 and flag.count('A') <= 2
    return  F(st * 2, fin, flag+'B') + F(st * 3, fin, flag+'C')



print(F(6, 48, ''))

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Никита = [3, 5, 7, 8, 9, 12, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: Повторить 11 номера и разобрать 22
