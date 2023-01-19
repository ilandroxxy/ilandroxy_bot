# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Тип 14 № 23914
'''
# Значение арифметического выражения: 9**11*3**20 − 3**9 − 27 — записали в системе счисления с основанием 3.
# Сколько цифр 2 содержится в этой записи?

x = 9**11*3**20 - 3**9 - 27

M = []
while x > 0:
    M.append(x % 3)
    x //= 3
M.reverse()
print(M.count(2))
'''
# Ответ: 38


# Тип 14 № 48386
'''
# Операнды арифметического выражения записаны в системах счисления с основаниями 15 и 16:
# 90x4y_15 + 91xy2_16
#
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 56.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 56 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
M = []
for x in '0123456789abcd':
    for y in '0123456789abcd':
        A = int(f'90{x}4{y}', 15)
        B = int(f'91{x}{y}2', 16)
        if (A + B) % 56 == 0:
            M.append((A + B) // 56)
print(min(M))
'''
# Ответ: 18754

# endregion Урок: ******************************************************************************


# todo: Артем = []
# на прошлом уроке:
# на следующем уроке: Теория типов данных, арифметику проговорить, условные операторы, циклы.