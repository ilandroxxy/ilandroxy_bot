# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************

# Тип 8 №3228
# Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке.
# Вот начало списка:
# 1. ААААА
# 2. ААААО
# 3. ААААУ
# 4. АААОА
#
# Укажите номер слова УАУАУ.
'''
s = sorted('АОУ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if slovo == 'УАУАУ':
                        print(num, slovo)
                    num += 1


# Вариант 2
from itertools import product
num = 1
for var in product(sorted('АОУ'), repeat=5):
    slovo = ''.join(var)
    if slovo == 'УАУАУ':
        print(num, slovo)
    num += 1
'''
# Ответ: 183


# Тип 8 №11306
# Вася составляет 4-буквенные слова, в которых есть только буквы Б, Р, О, Н, Х, И,
# причём буква Х используется в каждом слове, и только 1 раз.
# Каждая из других допустимых букв может встречаться
# в слове любое количество раз или не встречаться совсем.
# Сколько существует таких слов, которые может написать Вася?
'''
s = 'БРОНХИ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if slovo.count('Х') == 1:
                    count += 1
print(count)

# Вариант 2
from itertools import product
count = 0
for var in product('БРОНХИ', repeat=4):
    slovo = ''.join(var)
    if slovo.count('Х') == 1:
        count += 1
print(count)

# Вариант 3
print(len([1 for var in product('БРОНХИ', repeat=4) if ''.join(var).count('Х') == 1]))
'''
# Ответ: 500


# Тип 8 №27236
# Андрей составляет 4-буквенные коды из букв А, Н, Д, Р, Е, Й.
# Каждую букву можно использовать любое количество раз, при
# этом код не может начинаться с буквы Й и должен содержать хотя бы одну гласную.
# Сколько различных кодов может составить Андрей?
'''
s = 'АНДРЕЙ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if a != 'Й' and any(x in slovo for x in 'АЕ'):
                    count += 1
print(count)

# Вариант 2
from itertools import product
count = 0
for var in product('АНДРЕЙ', repeat=4):
    slovo = ''.join(var)
    if slovo[0] != 'Й' and any(x in slovo for x in 'АЕ'):
        count += 1
print(count)

# Вариант 3
print(len([1 for var in product('АНДРЕЙ', repeat=4) if ''.join(var)[0] != 'Й' and any(x in ''.join(var) for x in 'АЕ')]))
'''
# Ответ: 888


# Тип 8 №47005
# Светлана составляет коды из букв слова ПАРАБОЛА. Код должен состоять из 8 букв,
# и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
# Сколько кодов может составить Светлана?
'''
s = 'ПАРАБОЛА'
s1 = 'ПРБЛ'
s2 = 'АО'
count = set()
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    for f in s2:
                        for g in s1:
                            for h in s2:
                                slovo = a + b + c + d + e + f + g + h
                                if len(set(slovo)) == 6 and slovo.count('А') == 3:
                                    count.add(slovo)
print(len(count) * 2)


from itertools import permutations
s1 = 'ПРБЛ'
s2 = 'АО'
count = set()
for var in permutations('ПАРАБОЛА', 8):
    slovo = ''.join(var)
    if all((slovo[i] in s1 and slovo[i+1] in s2) or (slovo[i+1] in s1 and slovo[i] in s2) for i in range(len(slovo)-1)):
        count.add(slovo)
print(len(count))
'''
# Ответ: 192

'''
M = [1, 1, 1, 2, 3, 2, 2, 2, 3, 3, 3, 3, 1]
print(set(M))  # {1, 2, 3}
'''


# Тип 8 №58235
# Сколько существует различных трёхзначных чисел, записанных в четверичной системе счисления,
# в записи которых сумма первой и последней цифры строго больше цифры стоящей по середине?
'''
s = '0123'
count = 0
for a in s:
    for b in s:
        for c in s:
            num = a + b + c
            if num[0] != '0':
                if int(a) + int(c) > int(b):
                    count += 1
print(count)
'''
# Ответ: 38

# todo Разбираем домашку по 8 номерам и начинаем 5 номер.
# endregion Урок: ************************************************************


# Никита = [8.1, 12.1, 14.1]
# КЕГЭ = []
# на следующем уроке:
