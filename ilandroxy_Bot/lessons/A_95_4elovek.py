# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

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
                        print(num)
                    num += 1

# Вариант 2
from itertools import product
num = 1
for s in product(sorted('АОУ'), repeat=5):
    slovo = ''.join(s)  # Склеиваем кортеж строк в одну строку: ('У', 'У', 'У', 'О', 'У') УУУОУ
    if slovo == 'УАУАУ':
        print(num)
    num += 1
'''
# Ответ: 183


# Тип 8 №15920
# Все четырёхбуквенные слова, составленные из букв А, Л, Г, О, Р, И, Т, М,
# записаны в алфавитном порядке и пронумерованы, начиная с 1.
# Начало списка выглядит так:
# 1. АААА
# 2. АААГ
# 3. АААИ
# 4. АААЛ
# 5. АААМ
# 6. АААО
# 7. АААР
# 8. АААТ
# 9. ААГА

# Под каким номером в списке идёт первое слово, которое начинается с букв ГО?
'''
s = sorted('АЛГОРИТМ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if a == 'Г' and b == 'О':
                    print(num)
                    exit()
                num += 1
'''
# Ответ: 833


# Тип 8 №7921
# Сколько слов длины 6, начинающихся с согласной буквы, можно составить из букв Г, О, Д?
# Каждая буква может входить в слово несколько раз.
# Слова не обязательно должны быть осмысленными словами русского языка.
'''
s = 'ГОД'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if a in 'ГД':
                            count += 1
print(count)

# Вариант 2
from itertools import product
count = 0
for s in product('ГОД', repeat=6):
    slovo = ''.join(s)
    if slovo[0] in 'ГД':
        count += 1
print(count)
'''
# Ответ: 486


# Тип 8 №59713
# Составляют 5-буквенные слова из букв слова ПЯТНИЦА.
# Найти количество слов, которые не начинаются с Н
# и в которых есть только одна буква Я. Буквы в слове могут повторяться.
# i        01234
# slovo = 'АААЦИ'
'''
from itertools import product
count = 0
for s in product('ПЯТНИЦА', repeat=5):
    slovo = ''.join(s)  # АААЦИ
    a, b, c, d, e = slovo
    if a != 'Н':  # slovo[0] != 'Н'
        if slovo.count('Я') == 1:
            count += 1
print(count)
'''
# Ответ: 5616


# Тип 8 №27295
# Света составляет 5-буквенные коды из букв С, В, Е, Т, А.
# Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные.
# Сколько различных кодов может составить Света?
'''
from itertools import permutations
count = 0
for s in permutations('СВЕТА', 5):  # Каждую букву нужно использовать ровно один раз
    slovo = ''.join(s)
    if 'ЕА' not in slovo and 'АЕ' not in slovo:
        count += 1
print(count)

# Вариант 2
s = 'СВЕТА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):  # Каждую букву нужно использовать ровно один раз
                        if 'ЕА' not in slovo and 'АЕ' not in slovo:
                            count += 1
print(count)
'''
# Ответ: 72


# КЕГЭ № 1933 (Уровень: Базовый) (А. Куканова)
# Вероника составляет слова, меняя местами буквы в слове КЛАБХАУС так,
# что любые две соседние буквы различны между собой.
# Сколько слов, включая исходное, может составить Вероника?
'''
from itertools import permutations
count = set()
for s in permutations('КЛАБХАУС'):
    slovo = ''.join(s)
    if all(slovo[i] != slovo[i+1] for i in range(len(slovo)-1)):
        count.add(slovo)
print(len(count))
'''
# КЛАБХАУС  КЛАБХАУС


# Тип 8 №59831
# Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления.
# Сколько различных чисел может составить Игорь, в которых только одна цифра 5
# и рядом с ней НЕ стоят нечётные цифры?
'''
s = '012345678'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0':
                        if num.count('5') == 1:
                            if all(pair not in num for pair in '15 51 35 53 57 75'.split()):
                                count += 1
print(count)

from itertools import product
count = 0
for s in product('012345678', repeat=5):
    num = ''.join(s)
    if num[0] != '0':
        if num.count('5') == 1:
            if all(pair not in num for pair in '15 51 35 53 57 75'.split()):
                count += 1
print(count)
'''
# Ответ: 8880


# Тип 8 №26953
# Найдите количество пятизначных восьмеричных чисел,
# в которых все цифры различны и никакие две четные или нечетные не стоят рядом.
'''
s = '01234567'
s1 = '1357'
s2 = '0246'
count = 0
for a in s2:
    for b in s1:
        for c in s2:
            for d in s1:
                for e in s2:
                    num = a + b + c + d + e
                    if a != '0':
                        if len(num) == len(set(num)):
                            count += 1

for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    num = a + b + c + d + e
                    if a != '0':
                        if len(num) == len(set(num)):
                            count += 1
print(count)
'''
# Ответ: 504

# Тип 8 №48456
# Определите количество шестизначных чисел, записанных в девятеричной системе счисления,
# в записи которых ровно одна цифра 4 и ровно две нечётные цифры.
'''
from itertools import product
count = 0
for s in product('012345678', repeat=6):
    num = ''.join(s)
    if num[0] != '0':
        if num.count('4') == 1:
            nechet = [x for x in num if x in '1357']
            if len(nechet) == 2:
                count += 1
print(count)
'''
# Ответ: 53 760.


# ВАЖНО: в задачах с цифрами первая буква не должна ровняться 0




# endregion Урок: ***************************************************************


# Сева = [2.1, 6.1, 5.1, 8.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
