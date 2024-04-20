# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
from itertools import permutations
graph = 'AB BA BC CB CD DC CA AC DA AD AE EA EF FE FA AF FG GF GA AG GH HG AH HA'
table = '12 17 21 27 28 34 35 37 43 47 53 57 67 68 71 72 73 74 75 76 78 82 86 87'

for per in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    # print(per, table, new_table, '--------------', sep='\n')
    # ('H', 'G', 'F', 'E', 'D', 'A', 'C', 'B')
    # 12 17 21 27 28 34 35 37 43 47 53 57 67 68 71 72 73 74 75 76 78 82 86 87
    # HG HC GH GC GB FE FD FC EF EC DF DC AC AB CH CG CF CE CD CA CB BG BA BC
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
'''


from itertools import permutations
graph = 'АБ БА АИ ИА ИБ БИ ВБ БВ БЖ ЖБ ИЖ ЖИ ЖВ ВЖ ВГ ГВ ЖЕ ЕЖ ЕД ДЕ ЕГ ГЕ ДГ ГД'
table = '12 15 21 23 25 32 36 37 38 46 47 51 52 58 63 64 67 68 73 74 76 83 85 86'

for per in permutations('АБВГДЕЖИ'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)

# 1 2 3 4 5 6 7 8
# Д Е Ж А Г Б И В

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Лера = [2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
