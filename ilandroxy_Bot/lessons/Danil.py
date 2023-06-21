# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# 2, 5, 8, 9, 17
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or y) and (not(y == z)) and (not w)
                if F == True:
                    print(x, y, z, w)
'''
'''
s = sorted('ПЯТНИЦА')
k = 1
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if a != 'Ц' and slovo.count('И') == 2:
                            if k % 2 != 0:
                                count += 1

                        k += 1
print(count)
'''


'''
def troich(x):
    s = ""
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

for n in range(1, 1000):
    s = troich(n)

    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + troich(5 * (n % 3))

    r = int(s, 3)

    if r >= 146:
        print(n)
        break
'''

'''
def F(a, b):
    if a > b or a == 15:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+3, b) + F(a*3, b)

print(F(7, 14) * F(14, 20))


def F(a, b):
    if a >= b or a == 15:
        return a == b
    return F(a+1, b) + F(a+3, b) + F(a*3, b)

print(F(7, 14) * F(14, 20))
'''
'''
s = 'HHHHHHHHHHHHHHAAABBBHHHHHHCCACACAHHHHHHHACHHHHHHHHHHHHCBB'  # example
s = s.replace('A', 'C').replace('B', 'C')

# CCHHHHHHHC
s = s.replace('CC', 'C C')
print(s)
M = [len(i) for i in s.split()]
print(max(M))
'''
'''
from fnmatch import *
m = [2**i for i in range(1, 100)]
print(m)
for x in range(2031, 10**9, 2031):
    if fnmatch(str(x), '*31*65?'):
        if x % 31 == 0:
            d = set()
            for j in range(1, int(x**0.5)+1):
                if x % j == 0:
                    d.add(j)
                    d.add(x // j)
            if len(d) in m:
                print(x, x // 2031)
'''

# endregion Урок: ******************************************************************************


# todo:    Данил   = [1, 2, 3, 4, 5, 6, 7.1, 8, 9.1, 10, 11, 12, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25.2]
# todo: Данил КЕГЭ = [14, 15]
# на прошлом уроке: Посмотрели на решение 25 через fnmatch
# на следующем уроке:
