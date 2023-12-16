# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# КЕГЭ № 5553 (Уровень: Базовый)
# Сколько можно составить различных кодов, в составе которых встречаются
# две подряд идущие гласные, путём перестановки букв слова СОТОЧКА?
'''
s = 'СОТОЧКА'
count = set()
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            slovo = a + b + c + d + e + f + g
                            if len(set(slovo)) == 6 and slovo.count('О') == 2:
                                if 'ОО' in slovo or 'ОА' in slovo or 'АО' in slovo:
                                    count.add(slovo)
print(len(count))
'''


# КЕГЭ № 6901 (Уровень: Средний) (Д. Статный)
# Все пятибуквенные слова, в составе которых могут быть только буквы слова БАРАШ,
# записаны в алфавитном порядке и пронумерованы начиная с 1.
#
# Ниже приведено начало списка.
# 1. ААААА
# 2. ААААБ
# 3. ААААР
# 4. ААААШ
# 5. АААБА
#
# Под каким последним номером идёт слово, в котором не более 3-х согласных
# и только одна буква повторяется дважды, а остальные не повторяются?
'''
R = []
s = sorted('БАРШ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(set(slovo)) == 4 and any(slovo.count(x) == 2 for x in slovo):
                        sogl = [x for x in slovo if x in 'БРШ']
                        if len(sogl) <= 3:
                            R.append(num)
                    num += 1
print(max(R))


from itertools import product
R = []
num = 1
for var in product(sorted('БАРШ'), repeat=5):
    slovo = ''.join(var)
    if len(set(slovo)) == 4 and any(slovo.count(x) == 2 for x in slovo):
        sogl = [x for x in slovo if x in 'БРШ']
        if len(sogl) <= 3:
            R.append(num)
    num += 1
print(max(R))
'''

'''
from itertools import permutations
k = set()
for w in permutations('АМФИБРАХИЙ'):
    slovo = ''.join(w)
    if 'ИИФАА' in slovo or 'ААФИИ' in slovo:
        k.add(slovo)
print(len(k))
'''

# Тип 8 №48429
# Определите количество семизначных чисел, записанных в девятеричной системе счисления,
# в записи которых ровно одна цифра 6 и ровно две нечётные цифры.

from itertools import product
count = 0
for var in product('012345678', repeat=7):
    num = ''.join(var)
    if len([x for x in num if x in '1357']) == 2:
        if num.count('6') == 1:
            if num[0] != '0':
                count += 1
print(count)

# Ответ: 368640




# endregion Урок: ******************************************************************


# Лера = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
