# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 16380 ЕГКР 27.04.24 (Уровень: Базовый)
'''
x = 4 * 3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
print(len([i for i in M if i > 10]))
'''


# № 12923 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
'''
x = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
print(len(M))  # 23 - кол-во всех чисел в списке M
print(M.count(0))  # Сколько значащих нулей содержится в этой записи?
print(len(M) - M.count(0))  # Сколько значащих чисел не равных нулю
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet[:10])  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(alphabet[:2])  # ['0', '1']
for x in alphabet[:27]:
    A = int(f'123{x}24', 27)
    B = int(f'135{x}78', 27)
    if (A + B) % 26 == 0:
        print((A + B) // 26)
'''
# Ответ: 1213206

# Тип 14 №48384
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:9]:
    for y in alphabet[:9]:
        A = int(f'88{x}4{y}', 9)
        B = int(f'7{x}44{y}', 11)
        if (A + B) % 61 == 0:
            print((A+B) // 61)
'''
# 2715


# № 13910 (Уровень: Базовый)
'''
# print(int('43897539', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0

# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# for i in range(len(alphabet)):
#     print(i, alphabet[i])

for p in range(31, 37):
    if int('TH', p) + int('NQ', p) + int('U', p) == int('1L7', p):
        print(p)
'''

# № 16371 ЕГКР 27.04.24 (Уровень: Базовый)
'''
R = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r >= 195:
        R.append(r)
print(min(R))
'''

# № 16316 Открытый вариант 2024 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res += alphabet[num % base]
        num //= base
    return res[::-1]  # развернули строку


R = []
for n in range(1, 1000):
    s = convert(n, 2)
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if r > 516:
        R.append(n)
print(min(R))


# x = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
# print(convert(x, 25).count('0'))
'''


# № 13874 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res += alphabet[num % base]
        num //= base
    return res[::-1]  # развернули строку


R = []
for n in range(1, 1000):
    s = convert(n, 4)
    if n % 3 == 0:
        s = s[-1] + s[1:-1] + s[0] + '1'
    else:
        s = s + str(n % 3)
    r = int(s, 4)
    if r <= 340:
        R.append(r)
print(max(R))
'''


# № 9828 Основная волна 27.06.23 (Уровень: Средний)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(num, base):
    res = ''
    while num > 0:
        res += alphabet[num % base]
        num //= base
    return res[::-1]  # развернули строку


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        R.append(n)
print(max(R))
'''


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Лиза = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [1, 4, 5, 7, 8, 12, 14, 15, 16, 23]
# на следующем уроке:
