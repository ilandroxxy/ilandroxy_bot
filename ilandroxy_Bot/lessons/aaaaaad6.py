# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
def F(x, A):
    return ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)

R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        R.append(A)
print(max(R))
'''


'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res = alphabet[num % base] + res
        num //= base
    return res

R = []
for n in range(1, 1000):
    s = convert(n, 2)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = 3 * (n % 3)
        s = s + convert(x, 2)
    r = int(s, 2)
    if r >= 195:
        R.append(r)
print(min(R))
'''

'''
R = []
for n in range(1, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + f'{3 * (n % 3):b}'
    r = int(s, 2)
    if r >= 195:
        R.append(r)
print(min(R))
'''


# № 13874 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res = alphabet[num % base] + res
        num //= base
    return res


R = []
for n in range(1, 1000, 2):
    s = convert(n, 4)
    if n % 3 == 0:
        s = s[-1] + s[1:-1] + s[0] + '1'
    else:
        s += str(n % 3)
    r = int(s, 4)
    if r <= 340:
        R.append(r)
print(max(R))
'''
# Ответ 334

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res = alphabet[num % base] + res
        num //= base
    return res


x = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 -4*5**2023 - 2024
R = convert(x, 25)
print(len([a for a in R if a in alphabet[9:]]))


# Вариант 2
x = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 -4*5**2023 - 2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
print(len([a for a in M if a > 10]))
'''


# № 16261 Джобс 03.05.24 (Уровень: Базовый)
'''
R = []
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:21]:
    for y in alphabet[:21]:
        A = int(f'943697{x}21', 21)
        B = int(f'2{y}9253', 21)
        if (A - B) % 20 == 0:
            R.append([int(x, 21) - int(y, 21), (A - B) // 20])
print(max(R)[1])
'''
# 17394273143

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for i in range(len(alphabet)):
    print(i, alphabet[i])
'''


# № 13910 (Уровень: Базовый)
'''
for p in range(31, 36+1):  # U - 30
    if int('TH', p) + int('NQ', p) + int('U', p) == int('1L7', p):
        print(p)
'''
# Ответ: 33


# 14 № 7085 OpenFIPI (Уровень: Базовый)
'''
x = 3 * 625**173 + 4*125**180 + 3*25**157 + 2*5**155 + 156
M = []
while x > 0:
    M.append(x % 25)
    x //= 25

# Сколько значащих нулей содержится в этой записи?
print(M.count(0))

# Сколько значащих чисел, кроме нуля содержится в этой записи?
print(len(M) - M.count(0))
'''

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Лера = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 14, 15, 16, 23]
# на следующем уроке: повторять все номера кодом, 7, 11 и теорию игр
