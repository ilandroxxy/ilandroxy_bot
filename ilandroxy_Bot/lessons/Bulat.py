# region Домашка:  ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок:  ******************************************************************************

# 3. КЕГЭ № 7094 OpenFIPI (Уровень: Базовый)
# Текстовый файл состоит из символов A, C, D, F и U.
# Определите максимальное количество идущих подряд пар символов вида
#
# согласная + гласная в прилагаемом файле.
#
# Для выполнения этого задания следует написать программу.

# согласная + гласная: 'CA DA FA CU DU FU'
'''
s = open('24.txt').readline()
M = 'CA DA FA CU  DU FU'.split()  # ['CA', 'DA', 'FA', 'CU', 'DU', 'FU']
for x in M:
    s = s.replace(x, '*')
for x in 'ACDFU':
    s = s.replace(x, ' ')
R = [len(i) for i in s.split()]
print(max(R))
'''
# Ответ: 173


# 4. КЕГЭ № 5677 Вариант 09.01.23 (Уровень: Средний)
# (А. Игнатюк) В текстовом файле дана последовательность латинских букв.
# Необходимо найти в этой последовательности самую длинную подстроку,
# состоящую из комбинации DAD, при этом первый и последний элементы могут быть неполными.
#
# В ответе укажите количество символов, составляющих наибольшую длину подходящей подстроки.
'''
s = open('24.txt').readline()
print(s)
print(len('DADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))
print(len('DDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))
'''
# Ответ: 99

# № 6828 (Уровень: Сложный)
# (Д. Статный) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится
# без остатка на натуральное число m». На числовой прямой даны три отрезка:
# P = [257, 356], Q = [5, 600] и R = [59, 228].
# Какова наименьшая длина отрезка A, при котором формула
# ((x ∈ R) → (x ∈ A)) v ((ДЕЛ(x, 3) → (x ∈ P)) → ((x ∈ Q) → (x ∈ A)))


'''
def F(x, a1, a2):
    return ((59 <= x <= 228) <= (a1 <= x <= a2)) or (((x % 3 == 0) <= (257 <= x <= 356)) <= ((5 <= x <= 600) <= (a1 <= x <= a2)))

import useful
print(useful.valid_parentheses('((59 <= x <= 228) <= (a1 <= x <= a2)) or (((x % 3 == 0) <= (257 <= x <= 356)) <= ((5 <= x <= 600) <= (a1 <= x <= a2)))'))
'''

# endregion Урок:  *************************************************************************

import useful
print(useful.who_is_name())

# todo: Булат = [2, 3, 8, 9, 10, 12, 14+, 15, 16, 17, 18, 19-21, 22, 24, 25]
# на прошлом уроке: Разбирали 3, 22, 18 номера (18 не все задачи)
# на следующем уроке:
