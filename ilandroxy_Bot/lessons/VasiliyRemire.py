
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# КЕГЭ № 6575 (Уровень: Базовый)
# Сколько раз в этой записи встречается цифра С?
'''
x = 766**66 + 15**13 - 22
base = 13
M = []
while x > 0:
    M.append(x % base)
    x //= base
M.reverse()
print(M.count(12))
'''


# КЕГЭ № 7816 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:15]:
    A = int(f'97531{x}19', 15)
    B = int(f'3{x}519', 15)
    if (A + B) % 11 == 0:
        print((A + B) // 11)
        break
'''


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Василий = [1, 2, 3, 4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [3, 14]
# на следующем уроке: 15, 8, 9, 17, 10, 22
