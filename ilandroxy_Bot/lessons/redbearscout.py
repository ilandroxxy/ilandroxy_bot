# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
R = []
for n in range(4, 100):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum(map(int, s))
    R.append(summa)
print(max(R))
'''


# № 16374 ЕГКР 27.04.24 (Уровень: Базовый)
# Сколько существует семизначных семеричных чисел,
# которые содержат в своей записи ровно две чётные цифры?
'''
s = '0123456'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if num[0] != '0':
                                chet = [x for x in num if x in '0246']
                                if len(chet) == 2:
                                    print(num, chet)
                                    cnt += 1
print(cnt)
'''


# 8 № 16255 Джобс 03.05.24 (Уровень: Средний)
# (Е.Джобс) Определите количество семизначных чисел, записанных
# в девятеричной системе счисления, которые не начинаются
# с нечетных цифр, оканчиваются на цифры, не делящиеся на 3 без остатка,
# а также содержат в своей записи хотя бы одну цифру 6.
'''
s = '012345678'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if num[0] != '0' and num[0] not in '1357':
                                if num[-1] not in '036':  # оканчиваются на цифры, не делящиеся на 3 без остатка
                                    if num.count('6') >= 1:
                                        cnt += 1
print(cnt)
'''

'''
s = sorted('ПАРУС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if slovo.count('У') <= 1:
                        if 'АА' not in slovo:
                            print(num, slovo)
                            exit()
'''


# todo № 12453 (Уровень: Базовый)
# (Л. Шастин) Леонид составляет коды перестановкой букв слова СОВЕСТЬ.
# При этом в кодах не должно быть двух стоящих рядом гласных
# и двух стоящих рядом согласных одновременно.
# Сколько различных кодов может составить Леонид?
'''
s = 'СОВЕСТЬ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            slovo = a + b + c + d + e + f + g
                            if len(s)-1 == len(set(slovo)) and slovo.count('О') == 2:
                                slovo = slovo.replace('В', 'С').replace('Т', 'С')
                                slovo = slovo.replace('Ь', 'Е').replace('О', 'Е')
                                if 'ЕЕ' not in slovo and 'СС' not in slovo:
                                    cnt += 1
print(cnt)


from itertools import *
cnt = 0
for s in permutations('СОВЕСТЬ'):
    s = ''.join(s)
    s = s.replace('В', 'С').replace('Т', 'С')
    s = s.replace('Ь', 'Е').replace('О', 'Е')
    if ('ЕЕ' not in s) and ('СС' not in s):
        cnt += 1
print(cnt)
'''

#
# № 5488 (Уровень: Базовый)
# Полина составляет коды из букв слова ПОЛИНА.
# Код должен состоять из 8 букв, любую букву можно использовать
# произвольное число раз или не использовать вовсе. Полина хочет,
# чтобы согласных в каждом коде было больше, чем гласных.
# Сколько кодов, удовлетворяющих этому условию, она сможет составить?
'''
s = 'ПОЛИНА'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                slovo = a + b + c + d + e + f + g + h
                                sogl = [x for x in slovo if x in 'ПЛН']
                                glas = [x for x in slovo if x in 'ОИА']
                                if len(sogl) > len(glas):
                                    cnt += 1
print(cnt)
'''
# Ответ: 610173

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Тимур = [1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = [8, 12, 13, 15, 16, 23, 25]
# на следующем уроке:
