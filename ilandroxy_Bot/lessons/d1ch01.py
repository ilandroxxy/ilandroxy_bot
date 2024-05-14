# region Домашка: ******************************************************************


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

'''
def my_prod(M: list):
    result = 1
    for x in M:
        result *= x
    return result

import math
num = 0
summa = 0
for s in open("9.txt"):
    M = [int(x) for x in s.split()]
    num += 1
    # if all((M[i] % 2) != (M[i+1] % 2) for i in range(len(M)-1)):
    if all((M[i] + M[i+1]) % 2 != 0 for i in range(len(M)-1)):
        copied = [x for x in M if M.count(x) > 1]
        not_copied = [x for x in M if M.count(x) == 1]
        # if (3 * sum(not_copied)) >= math.prod(copied):
        if (3 * sum(not_copied)) >= my_prod(copied):
            summa += num

print(summa)
'''
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for i in range(len(alphabet)):
    print(i, alphabet[i])

# U - 30
for p in range(31, 37):
    pass
'''

'''
# 00000000, 1000000, 11000000, 11100000, 11110000, 11111000, 11111100, 11111110, 11111111
s = '00000000 10000000 11000000 11100000 11110000 11111000 11111100 11111110 11111111'
for x in s.split():
    print(int(x, 2), end=' ')  # 0 128 192 224 240 248 252 254 255
'''
# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Дмитрий = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
