# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 3:
        return 2**1024
    if n > 2:
        return 2 * n + 3 + F(n-2)
print(F(4048) - F(16))
'''

'''
x = 3213   # 9
summa = sum([int(a) for a in str(x) if a.isdigit()])
print(summa)

summa = sum(map(int, str(x)))
print(summa)
'''


'''
def Divisors(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(326496, 649632+1):
    d = Divisors(x)
    chet = [a for a in d if a % 2 == 0]
    nechet = [a for a in d if a % 2 != 0]
    if len(chet) == len(nechet):
        if len(chet) >= 70 and len(nechet) >= 70:
            print(x, min([a for a in d if a > 1000]))
'''
# Ответ:
# 450450 1001
# 589050 1050
# 630630 1001
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 2:
        return 7
    if n > 1:
        return 7 * F(n - 2)


print(F(12950) / 7**6473)
'''


def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

cnt = 0
for n in range(1, 1000+1):
    if F(n) == 3:
        cnt += 1
print(cnt)


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Тимур = [1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = [16, 23]
# на следующем уроке:
