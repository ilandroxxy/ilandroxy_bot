# region Домашка: ******************************************************************

# КЕГЭ № 6636 Пробник ИМЦ СПб (Уровень: Базовый)
#
# Текстовый файл состоит из цифр 1, 2, 3, 4 и 5.
# Определите максимальное количество идущих подряд пар символов вида: четная цифра + нечетная цифра в прилагаемом файле.
'''
s = open('24.txt').readline()
for a in '135':
    s = s.replace(a, '*')
for a in '24':
    s = s.replace(a, '#')
s = s.replace('#*', '+')
s = s.replace('*', ' ').replace('#', ' ')
print(max([len(x) for x in s.split()]))


s = open('24.txt').readline()
for a in '135':
    s = s.replace(a, '*')
for a in '24':
    s = s.replace(a, '#')
print(s)

print(len('#*#*#*#*#*#*#*#*#*#*') // 2)  # решение через ctrl + F
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
from itertools import permutations

table = '12 15 21 23 25 32 36 37 38 46 47 51 52 58 63 64 67 68 73 74 76 83 85 86'
graph = 'АБ БА АИ ИА ИБ БИ ЖБ БЖ ИЖ ЖИ БВ ВБ ВЖ ЖВ ЖЕ ЕЖ ВГ ГВ ГЕ ЕГ ГД ДГ ЕД ДЕ'

for per in permutations('АБВГЖДЕИ'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
'''
# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Артур = [1, 2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: Решить 24 номера на строки и кол-во
