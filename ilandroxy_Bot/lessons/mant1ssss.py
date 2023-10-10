
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Тип 8 №15795
# Все четырёхбуквенные слова, составленные из букв П, А, Р, У, С,
# записаны в алфавитном порядке и пронумерованы, начиная с 1. Начало списка выглядит так:
# 1.АААА
# 2.АААП
# 3.АААР
# 4.АААС
# 5.АААУ
# 6.ААПА
#
# Под каким номером в списке идёт первое слово, в котором нет буквы А?

# Вариант 1
'''
s = sorted('ПАРУС')
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                # if slovo.count('А') == 0:
                if 'А' not in slovo:
                    print(k)
                    exit()
                k += 1
'''


#  Вариант 2
'''
from itertools import permutations, product
k = 1
for s in product(sorted('ПАРУС'), repeat=4):
    slovo = ''.join(s)
    if 'А' not in slovo:
        print(k)
        exit()
    k += 1
'''
# Ответ: ПППП


# Тип 8 №40983
# Георгий составляет коды из букв своего имени.
# Код должен состоять из 7 букв, и каждая буква в нём должна встречаться столько же раз,
# сколько в имени Георгий. Кроме того, одинаковые буквы в коде не должны стоять рядом.
# Сколько кодов может составить Георгий?
'''
# Вариант 1
s = 'ГЕОРГИЙ'
count = 0
result = set()
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            slovo = a + b + c + d + e + f + g
                            # if len(set(slovo)) == len(s)-1 and slovo.count('Г') == 2:
                            if all(s.count(x) == slovo.count(x) for x in slovo):
                                if 'ГГ' not in slovo:
                                    result.add(slovo)
print(len(result))


# Вариант 2
from itertools import permutations
result = set()
for s in permutations('ГЕОРГИЙ', 7):
    slovo = ''.join(s)
    if 'ГГ' not in slovo:
        result.add(slovo)
print(len(result))
'''
# Ответ: 1800


'''
# Тип 8 № 59832
# Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления.
# Сколько различных чисел может составить Игорь,
# в которых ровно две цифры 3 и нечётные цифры не стоят рядом с цифрой 2?
s = '012345678'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp[0] != '0' or a != '0':
                        if temp.count('3') == 2:
                            if all(x not in temp for x in '12 21 23 32 52 25 72 27'.split()):
                                count += 1
print(count)

# Ответ: 3391.  3352

# todo найти разницу между двумя решениями 
from itertools import product
count = 0
for s in product('012345678', repeat=5):
    temp = ''.join(s)
    if temp[0] != '0':
        if temp.count('3') == 2:
            if all(x not in temp for x in '12 21 23 32 52 25 72 27'.split()):
                count += 1
                print(temp)
print(count)

from itertools import product

count = 0
for p in product("012345678", repeat=5):
    if p.count("3") == 2 and p[0] != "0":
        if p.count('2') > 0:
            i = p.index('2')
            if i != 0 and i != 4:
                if p[i - 1] not in '1357' and p[i + 1] not in '1357':
                    count += 1
            elif i == 0:
                if p[1] not in '1357':
                    count += 1
            elif i == 4:
                if p[3] not in '1357':
                    count += 1
        else:
            count += 1
print(count)
'''



# Тип 8 № 59745
# Все 5-буквенные слова, в составе которых могут быть буквы А, Л, Г, О, Р, И, Т, М,
# записаны в алфавитном порядке и пронумерованы начиная с 1.
#
# Ниже приведено начало списка.
# ААААА
# ААААГ
# ААААИ
# ААААЛ
# ААААМ
# ААААО
# ААААР
#
# Определите в этом списке количество слов с нечетными номерами,
# которые не начинаются с буквы Г и при этом содержат в своей записи не менее двух букв И
'''
s = sorted('АЛГОРИТМ')
k = 1
count = 0
from itertools import product
for s in product(s, repeat=5):
    slovo = ''.join(s)
    if k % 2 != 0:
        if slovo[0] != 'Г' and slovo.count('И') >= 2:
            print(k, slovo)
            count += 1
    k += 1
print(count)
'''
# Ответ: 2429



# endregion Урок: ******************************************************************


# todo: Марк = [2.1, 6.1, 8.1, 14.1]
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
