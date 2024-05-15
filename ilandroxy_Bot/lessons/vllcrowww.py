# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************
'''
def convert(num, base):
    r = ''
    while num > 0:
        r += str(num % base)
        num //= base
    return r[::-1]


for n in range(1, 1000):
    s = convert(n, 2)  # s = f'{n:b}'  # s = bin(n)[2:]
    if n % 2 == 0:
        s += '01'
    else:
        s = '1' + s + '1'
    r = int(s, 2)
    if r > 156:
        print(n)
        break  # exit()
'''


'''
def convert(num, base):
    r = ''
    while num > 0:
        r += str(num % base)
        num //= base
    return r[::-1]


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 7 == 0:
        s += s[-2:]
    else:
        x = (n % 7) * 3
        s += convert(x, 3)
    r = int(s, 3)
    if r > 369:
        R.append(r)
print(min(R))
'''
# Ответ: 384

'''
R = []
for n in range(1, 100000):
    s = bin(n)[2:]
    s += s[-1]
    s += str(s.count('1') % 2)
    r = int(s, 2)
    if r < 13500:
        R.append(r)
print(max(R))
'''


# 12721  (Уровень: Базовый)
# (C. Горбачёв)
'''
R = []
for n in range(81, 10000):
    s = oct(n)[2:]  # f'{n:o}'
    chet = [x for x in s if x in '02468']
    if len(chet) % 2 != 0:
        s = s[-3:] + '46'
    else:
        x = (n % 8) * 5
        s = oct(x)[2:] + s
    r = int(s, 8)
    R.append(r)
print(min(R))

# Ответ: 38
'''


# № 11818 (Уровень: Средний)
# (Л. Шастин) На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
# 1. Строится запись числа N в системе счисления с основанием 12.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    r = ''
    while num > 0:
        r += alphabet[num % base]
        num //= base
    return r[::-1]


R = []
for n in range(1, 10000):
    s = convert(n, 12)
    if n % 4 == 0:
        s = '2' + s + '64'
    else:
        s += max([x for x in s])
    r = int(s, 12)
    if r > 1799:
        R.append(r)
print(min(R))
'''
# Ответ: 1806
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    r = ''
    while num > 0:
        r += alphabet[num % base]
        num //= base
    return r[::-1]

R = []
for n in range(1, 10000):
    s = convert(n, 7)
    if s.count('2') % 2 == 0:
        s += '555'
    else:
        s = '1' + s
    r = int(s, 7)
    if r < 3799:
        R.append(n)
print(max(R))
'''


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    r = ''
    while num > 0:
        r += alphabet[num % base]
        num //= base
    return r[::-1]

R = []
for n in range(1, 10000):
    s = convert(n, 3)
    if sum([int(x) for x in s]) % 4 == 0:
        s = '1' + s
        s = s[:-2]
    else:
        x = sum([int(x) for x in s]) * 3
        s += convert(x, 3)
    r = int(s, 3)
    if n > 353:
        R.append(n)
print(min(R))




# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Марго = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 12, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
