# region Домашка: ******************************************************************************



# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Правила математической логики на Python
#   ¬w    --->  (not w)   инверсия (отрицание)
#  y ∧ z  --->  y and z   конъюнкция (логическое умножение)
#  y ∨ x  --->  y or x    дизъюнкция (логическое сложение)
#  w → z  --->  w <= z   импликация  или можно записать (not w) or z
#  x ≡ y  --->  x == y   тождество (сравнение)


# Тип 2 № 36015
# Логическая функция F задаётся выражением (x → y) ∨ ¬(w → z).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.
'''
print('x y z w F')
for x in [0, 1]:  # [0, 2) ->
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x <= y) or (not(w <= z))
                if F == False:
                    print(x, y, z, w, F)
'''


# Тип 2 № 18614
# Логическая функция F задаётся выражением ((w → ¬x) ≡ (z → y)) ∧ (y ∨ w).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.
'''
print('x y z w F')
for x in [0, 1]:  # [0, 2) ->
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= (not x)) == (z <= y)) and (y or w)
                print(x, y, z, w, F)
'''

# Тип 14 № 9766
# Значение арифметического выражения: 9**8 + 3**8 – 2 – записали в системе счисления с основанием 3.
# Сколько цифр «2» содержится в этой записи?
'''
x = 9**8 + 3**8 - 2
M = []
while x > 0:
    M.append(x % 3)  # метод списка list() для добавления элемента в конец списка
    x //= 3
M.reverse()  # метод для разворота списка (переворачиваем список)
print(M.count(2))  # метод поиска вхождений элемента в список
'''
# Ответ: 7

A = []
print(f'Документация метода .append: {A.append.__doc__}')
print(f'Документация метода .reverse: {A.reverse.__doc__}')
print(f'Документация метода .count: {A.count.__doc__}')
print(f'Документация функции len: {len.__doc__}')

"""
def F(x, n):
    '''
Моя функция для перевода из 10-ной в n-ную систему счисления.
Перевод осуществляется через списки list()
    '''
    M = []
    while x > 0:
        M.append(x % n)  # метод списка list() для добавления элемента в конец списка
        x //= n
    M.reverse()  # метод для разворота списка (переворачиваем список)
    return M

x = 9 ** 8 + 3 ** 8 - 2
print(F(x, 3).count(2))

print(F.__doc__)
"""


# Тип 14 № 48394
# Операнды арифметического выражения записаны в системе счисления с основаниями 15 и 13:
#
# 4Cx4_15 + x62A_13
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита десятичной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 121.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 121
# и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
for x in '0123456789':
    A = int(f'4C{x}4', 15)  # перевод из 15-ричной в 10-ную
    B = int(f'{x}62A', 13)  # перевод из 13-ричной в 10-ную

    if (A + B) % 121 == 0:
        print((A + B) // 121)
'''
# Ответ: 234

# Тип 14 № 48389
# Операнды арифметического выражения записаны в системах счисления с основаниями 7 и 9:
#
# yx320_7 + 1x3y3_9
#
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 181.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 181
# и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.

'''
for x in '0123456':
    for y in '0123456':
        A = int(f'{y}{x}320', 7)  # перевод из 7-ричной в 10-ную
        B = int(f'1{x}3{y}3', 9)  # перевод из 9-ричной в 10-ную

        if (A + B) % 181 == 0:
            print((A + B) // 181)
'''
# Ответ: 148


# Тип 14 № 48382
# Операнды арифметического выражения записаны в системе счисления с основанием 16:
#
# 8x84x_16 + 78x34_16
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита шестнадцатеричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 23.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 23
# и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
for x in '0123456789abcdef':
    A = int(f'8{x}84{x}', 16)  # перевод из 15-ричной в 10-ную
    B = int(f'78{x}34', 16)  # перевод из 13-ричной в 10-ную

    if (A + B) % 23 == 0:
        print((A + B) // 23)
'''

'''
for x in '0123456789abcdef':
    R = int(f'8{x}84{x}', 16) + int(f'78{x}34', 16)
    if R % 23 == 0:
        print(R // 23)
'''

'''
for x in '0123456789ABCDEF':
    t = int('8' + x + '84' + x, 16) + int('78' + x + '34', 16)
    if t % 23 == 0:
        print(t // 23)
'''
# Ответ: 45963



# Тип 14 № 48380
# Числа M и N записаны в системе счисления с основанием 12 соответственно.
#
# M = 49x26_12, N = 49x70_12
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита двенадцатеричной системы счисления.
# Определите наименьшее значение натурального числа A, при котором существует такой x, что M + A кратно N.
'''
for A in range(1, 1000):
    for x in '0123456789ab':
        M = int(f'49{x}26', 12)
        N = int(f'49{x}70', 12)

        if (M + A) % N == 0:
            print(A)
            exit()
'''

'''
for A in range(1, 1000):
    for x in '0123456789ab':
        if (int(f'49{x}26', 12) + A) % int(f'49{x}70', 12) == 0:
            print(A)
            exit()
'''
# Ответ: 54

# endregion Урок: ******************************************************************************


# todo: Артем = [2, 14]
# на прошлом уроке: Разобрали 2, 14 номера и сопутствующую им теорию
# на следующем уроке: Разбираем 5, 8, 12
