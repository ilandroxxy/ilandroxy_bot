# region Домашка: ******************************************************************


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

'''
from itertools import *
D = []
for x in product('012345678', repeat=5):
    x = ''.join(x)
    if x.count('5') == 1 and x[0] != '0' and all(x[i] != x[i+1] for i in range(len(x) - 1)):
        D.append(x)
print(len(D))
'''

'''
from fnmatch import *
for x in range(98591, 10**12, 98591):
    if fnmatch(str(x), '12?3*456??9'):
        print(x, x // 98591)
'''

'''
M = [int(x) for x in open('17.txt')]
D = [x for x in M if str(x)[-1] == '3' and len(str(abs(x))) == 5]
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]  # M[i], M[i+1], M[i+2]
    if str(x)[-1] == '3' or str(y)[-1] == '3' or str(z)[-1] == '3':
        if (x + y + z) <= max(D):
            R.append(x + y + z)
print(len(R), max(R))
'''
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    if len(copied) == 6:
        if (min(copied) + max(copied)) / 2 < sum(M) - sum(copied):
            cnt += 1
print(cnt)
'''
'''
def my_int(num, base):
    return sum(x*base**i for i, x in enumerate(num[::-1]))

R = []
for x in range(6, 63):
    for y in range(6, 63):
        if my_int([5, x, 3, x, y, 3, y, 5], 63) % 62 == 0:
            R.append(my_int([x, y, x], 63))
print(max(R))
'''
# Ответ: 249542

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Екатерина = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 12, 13, 14]
# на следующем уроке:
