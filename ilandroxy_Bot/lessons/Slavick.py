# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# Тип 8 №3207
# Все 5-буквенные слова, составленные из букв К, О, Р, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ККККК
# 2. ККККО
# 3. ККККР
# 4. КККОК
# Запишите слово, которое стоит под номером 238.
'''
# Вариант 1
s = sorted('КОР')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if num == 238:
                        print(slovo)  # РРРОК
                    num += 1

# Вариант 2
from itertools import product
num = 1
for s in product(sorted('КОР'), repeat=5):
    slovo = ''.join(s)
    if num == 238:
        print(slovo)  # РРРОК
    num += 1
'''
# Ответ: РРРОК


# Тип 8 №7986
# Сколько слов длины 5, начинающихся с согласной буквы и заканчивающихся гласной буквой,
# можно составить из букв З, И, М, А? Каждая буква может входить в слово несколько раз.
# Слова не обязательно должны быть осмысленными словами русского языка.
'''
# Вариант 1
s = 'ЗИМА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if a in 'ЗМ' and e in 'ИА':
                        count += 1
print(count)

# Вариант 2
from itertools import product
count = 0
for s in product('ЗИМА', repeat=5):
    slovo = ''.join(s)
    if slovo[0] in 'ЗМ' and slovo[-1] in 'ИА':
        count += 1
print(count)
'''
# Ответ: 256


# Тип 8 №59742
# Определите количество четырехзначных чисел, записанных в десятичной системе счисления,
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
# Вариант 1
s = '0123456789'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if slovo[0] != '0':
                    if len(slovo) == len(set(slovo)):  # в записи которых все цифры различны
                        slovo = slovo.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
                        slovo = slovo.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
                        if '11' not in slovo and '22' not in slovo:
                            count += 1
print(count)

# Вариант 2
from itertools import permutations
count = 0
for s in permutations('0123456789', 4):
    num = ''.join(s)
    if num[0] != '0':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        if '11' not in num and '22' not in num:
            count += 1
print(count)
'''
# Ответ: 720


# endregion Урок: *************************************************************


# Славик = [2.1, 5.1, 6.1, 8.1, 9.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
