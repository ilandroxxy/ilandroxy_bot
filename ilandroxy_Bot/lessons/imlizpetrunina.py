# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 8 №3237
# Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке.
# Вот начало списка:
# 1. ААААА
# 2. ААААО
# 3. ААААУ
# 4. АААОА
#
# Запишите слово, которое стоит на 170-м месте от начала списка.
'''
# Вариант 1
s = sorted('АОУ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if num == 170:
                        print(slovo)
                    num += 1

# Ответ: УААУО


# Вариант 2
from itertools import product
num = 1
for x in product(sorted('АОУ'), repeat=5):
    slovo = ''.join(x)
    if num == 170:
        print(slovo)
    num += 1
'''


# Тип 8 №19059
# Все 4-буквенные слова, в составе которых могут быть буквы Н, О, Т, К, И,
# записаны в алфавитном порядке и пронумерованы, начиная с 1.
#
# Ниже приведено начало списка.
# 1. ИИИИ
# 2. ИИИК
# 3. ИИИН
# 4. ИИИО
# 5. ИИИТ
# 6. ИИКИ
#
# Под каким номером в списке идёт первое слово, которое начинается с буквы О?
'''
s = sorted('НОТКИ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if a == 'О':
                    print(num)
                    exit()
                num += 1
'''
# Ответ: 376


# Тип 8 №33510
# Тимофей составляет 5-буквенные коды из букв Т, И, М, О, Ф, Е, Й.
# Буква Т должна входить в код не менее одного раза, а буква Й — не более одного раза.
# Сколько различных кодов может составить Тимофей?
'''
s = 'ТИМОФЕЙ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if slovo.count('Т') >= 1:  # Буква Т должна входить в код не менее одного раза
                        if slovo.count('Й') <= 1:  # а буква Й — не более одного раза
                            count += 1
print(count)
'''
# Ответ: 8006


# Тип 8 №9760
# Алексей составляет таблицу кодовых слов для передачи сообщений, каждому сообщению
# соответствует своё кодовое слово. В качестве кодовых слов Алексей использует 5-буквенные слова,
# в которых есть только буквы A, B, C, X, причём буква X может
# появиться на первом месте или не появиться вовсе.
# Сколько различных кодовых слов может использовать Алексей?
'''
s = 'ABCX'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if ('X' not in slovo) or (a == 'X' and slovo.count('X') == 1):
                        count += 1
print(count)
'''
# Ответ: 324


# Тип 8 №28685
# Петя составляет 6-буквенные коды из букв П, Е, Т, Я.
# Каждую букву можно использовать любое количество раз или совсем не использовать,
# при этом нельзя ставить подряд две гласные или две согласные.
# Сколько различных кодов может составить Петя?
'''
s = 'ПЕТЯ'
s1 = 'ПТ'
s2 = 'ЕЯ'
count = 0
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    for f in s2:
                        slovo = a + b + c + d + e + f
                        count += 1
print(count * 2)


# Вариант 3
print('ПП ПТ ТП ТТ ЕЯ ЯЕ ЕЕ ЯЯ'.split())

s = 'ПЕТЯ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if all(pair not in slovo for pair in 'ПП ПТ ТП ТТ ЕЯ ЯЕ ЕЕ ЯЯ'.split()):
                            count += 1
print(count)

# Вариант 3

from itertools import product
count = 0
for x in product('ПЕТЯ', repeat=6):
    slovo = ''.join(x)
    if all(pair not in slovo for pair in 'ПП ПТ ТП ТТ ЕЯ ЯЕ ЕЕ ЯЯ'.split()):
        count += 1
print(count)

# Вариант 4

from itertools import product
PAIRS = []
for x in product('ПЕТЯ', repeat=2):
    if (x[0] in 'ПТ' and s[1] in 'ПТ') or (x[0] in 'ЕЯ' and s[1] in 'ЕЯ'):
        PAIRS.append(''.join(x))

count = 0
for x in product('ПЕТЯ', repeat=6):
    slovo = ''.join(x)
    if all(pair not in slovo for pair in PAIRS):
        count += 1
print(count)
'''
# Ответ: 128


# Тип 8 №51977
# Вероника составляет коды из букв слова ВЕРОНИКА.
# Код должен состоять из 6 букв, любую букву можно использовать произвольное
# число раз или не использовать вовсе. Вероника хочет, чтобы гласных
# в каждом коде было больше, чем согласных.
# Сколько кодов, удовлетворяющих этому условию, она сможет составить?
'''
s = 'ВЕРОНИКА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        gl = [x for x in slovo if x in 'ЕОИА']
                        sog = [x for x in slovo if x in 'ВРНК']
                        if len(gl) > len(sog):
                            count += 1
print(count)

# Вариант 2
from itertools import product
count = 0
for x in product('ВЕРОНИКА', repeat=6):
    slovo = ''.join(x)
    gl = [x for x in slovo if x in 'ЕОИА']
    sog = [x for x in slovo if x in 'ВРНК']
    if len(gl) > len(sog):
        count += 1
print(count)
'''
# Ответ: 90112


# Тип 8 №59744
# Евгений составляет 6-буквенные слова из букв М, У, Ж, Ч, И, Н, А.
# Каждая из букв может встречаться в слове ровно один раз, причём первой буквой не может быть Ч,
# буква Ж должна встречаться не менее 1 раза и номер слова должен быть нечётный.
# Сколько различных слов может составить Евгений?
'''
s = 'МУЖЧИНА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if len(slovo) == len(set(slovo)):  # Каждая из букв может встречаться в слове ровно один раз
                            if a != 'Ч':
                                if slovo.count('Ж') >= 1:
                                    count += 1
print(count / 2)
'''
# Ответ: 1860


# endregion Урок: ******************************************************************


# Лиза = [2.1, 6.1, 8.1, 12.1]
# КЕГЭ  = []
# на следующем уроке:
