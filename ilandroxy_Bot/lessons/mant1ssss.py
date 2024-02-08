# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# КЕГЭ 13094
'''
count = 0
s = '12345678'
from itertools import product
for s in product(s, repeat = 9):
    chislo = ''.join(s)
    if all([chislo.count(x) <= 3 for x in chislo]):
        """if all((int(chislo[i])% 2 == 0) != (int(chislo[i+1])% 2 == 0) for i in range(len(chislo) - 1)):"""
        chislo = chislo.replace('4', '2').replace('6', '2').replace('8', '2')
        chislo = chislo.replace('3', '1').replace('5', '1').replace('7', '1')
        if '22' not in chislo and '11' not in chislo:
            count += 1
print(count)
'''


# КЕГЭ 11827
'''
count = 0
s = '01234567'
from itertools import product
for s in product(s, repeat = 7):
    chislo = ''.join(s)
    if chislo[0] != '0':
        if len([x for x in chislo if int(x) % 2 == 0]) == 2:
            if all(p not in chislo for p in '17 71 37 73 57 75 77'.split()):
                count += 1
print(count)
'''


# КЕГЭ 11202
'''
from itertools import permutations
alphabet = sorted('АССЕМБЛЕР')
count = 0
slova = []
for s in permutations(alphabet):
    slovo = ''.join(s)
    if sum([i+1 for i in range(len(slovo)) if slovo[i] in 'АЕ']) == 9:
        slova.append(s)
print(len(set(slova)))

'''


# Номер КЕГЭ 9363
'''
from itertools import permutations
alphabet = 'ХОЧУНАБЮДЖЕТ'
count = 0
slova = []
for s in permutations(alphabet):
    slovo = ''.join(s)
    for x in 'ОУЮЕ':
        slovo = slovo.replace(x, "A")
    if 'ААААА' not in slovo:
        slova.append(slovo)
print(len(set(slova)))

'''

# endregion Урок: *******************************************************************


# Марк = [1.1, 2.1, 3.1, 6.1, 4.1, 5.1, 7.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 22.1, 23.1, 24.1, 25.1]
# КЕГЭ  = [5.1, 8.1, 14.1]
# на следующем уроке:
