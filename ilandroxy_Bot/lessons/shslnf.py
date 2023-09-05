
# Тип 1 №19052
'''
from itertools import *

table = '14 17 24 26 36 41 42 45 46 47 54 56 57 62 63 64 65 71 74 75'
graph = 'АБ БА БВ ВБ БГ ГБ БД ДБ ВД ДВ ГД ДГ ДЕ ЕД ЕК КЕ КД ДК ГК КГ'

for p in permutations('АБВГДЕК'):
    new_graph = table
    for x in range(1, 7+1):
        new_graph = new_graph.replace(str(x), p[x-1])
    if set(new_graph.split()) == set(graph.split()):
        print(*p)
'''


# Тип 14 №9651
# Сколько единиц содержится в двоичной записи значения выражения:
# 4**2018 + 2**2017 - 5?
'''
print(bin(4**2018 + 2**2017 - 5)[2:].count('1'))
'''
# Ответ: 2017


M = []
M.append(1)
print(help(M.append))


import aiogram

import itertools
import os
import fnmatch
import math
import turtle
