# region Домашка: ******************************************************************

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet)
result = 3 * 625**173 + 4 * 125**180 + 3 * 25**157 + 2 * 5**155 + 156

base = 25
digits = ''
while result > 0:
    digits += alphabet[result % base]
    result //= base

count_zeros = digits.count("0")
print(count_zeros)

# Вариант 2
result = 3 * 625**173 + 4 * 125**180 + 3 * 25**157 + 2 * 5**155 + 156
digits = []
while result > 0:
    digits.append(result % base)
    result //= base
print(digits.count(0))
'''


# КЕГЭ № 5632 (Уровень: Средний) (М. Ишимов)
# Операнды арифметического выражения записаны в системе счисления с основанием 21.
#
# 32yxA_21 + 16y18_21
#
# В записи чисел переменными х и у обозначены две неизвестные цифры
# из алфавита 21-ричной системы счисления. Определите наименьшее значение х,
# при котором значение данного арифметического выражения кратно 12 при любом нечётном значении у.
# Для найденного значения х вычислите частное от деления значения
# арифметического выражения на 12 при у = 7 и укажите его в ответе
# в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:21]:
    if all((int(f'32{y}{x}A', 21) + int(f'16{y}18', 21)) % 12 == 0 for y in alphabet[1:21:2]):
        print((int(f'32{7}{x}A', 21) + int(f'16{7}18', 21)) // 12)
        break
'''
# Ответ: 71524


# КЕГЭ № 6844 (Уровень: Средний)
# В системе счисления с основанием p выполняется равенство
# 5x83 + x9x9 = y20y
# Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p.
# Определите значение числа xyyx_p и запишите это значение в десятичной системе счисления.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'5{x}83', p) + int(f'{x}9{x}9', p) == int(f'{y}20{y}', p):
                print(int(f'{x}{y}{y}{x}', p))
'''
# Ответ: 18990

# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# № 12240 ЕГКР 16.12.23 (Уровень: Базовый)
# Сколько существует девятеричных пятизначных чисел, содержащих в своей записи ровно одну цифру 5,
# в которых никакие две одинаковые цифры не стоят рядом?
'''
s = '012345678'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0' and num.count('5') == 1:
                        # if all(num[i] != num[i+1] for i in range(len(num)-1)):
                        if all(pair not in num for pair in '00 11 22 33 44 66 77 88'.split()):
                            count += 1
print(count)

# Вариант 2
from itertools import product, permutations
count = 0
for var in product('012345678', repeat=5):
    num = ''.join(var)
    if num[0] != '0' and num.count('5') == 1:
        # if all(num[i] != num[i+1] for i in range(len(num)-1)):
        if all(pair not in num for pair in '00 11 22 33 44 66 77 88'.split()):
            count += 1
print(count)
'''
# Ответ: 13377


# Тип 8 №3517
# Все 4-буквенные слова, составленные из букв В, И, Р, Т, записаны в алфавитном порядке.
# Вот начало списка:
# 1. ВВВВ
# 2. ВВВИ
# 3. ВВВР
# 4. ВВВТ
# 5. ВВИВ
#
# Запишите слово, которое стоит на 249-м месте от начала списка.
'''
s = sorted('ВРИТ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if num == 249:
                    print(num, slovo)
                num += 1
'''
# Ответ: ТТРВ


# Тип 8 №15947
# Все четырёхбуквенные слова, составленные из букв А, Л, Г, О, Р, И, Т, М,
# записаны в алфавитном порядке и пронумерованы, начиная с 1. Начало списка выглядит так:
# 1. АААА
# 2. АААГ
# 3. АААИ
# 4. АААЛ
# 5. АААМ
# 6. АААО
# 7. АААР
# 8. АААТ
# 9. ААГА
#
# Под каким номером в списке идёт первое слово, которое начинается с букв ИГ?
'''
s = sorted('АЛГОРИТМ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if a == 'И' and b == 'Г':
                    print(num)
                    exit()
                num += 1
'''
# Ответ: 1089


# Тип 8 №55625
# Ярослав составляет коды из букв, входящих в слово ЯРОСЛАВ.
# Код должен состоять из 5 букв, буквы в коде не должны повторяться,
# согласных в коде должно быть больше, чем гласных, две гласные буквы нельзя ставить рядом.
# Сколько кодов может составить Ярослав?
'''
# Вариант 1
s = 'ЯРОСЛАВ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):  # буквы в коде не должны повторяться
                        sogl = [x for x in slovo if x in 'РСЛВ']
                        glas = [x for x in slovo if x in 'ЯОА']
                        if len(sogl) > len(glas):
                            if all(pair not in slovo for pair in 'ЯА АЯ ЯО ОЯ АО ОА'.split()):
                                count += 1
print(count)

# Вариант 2
from itertools import permutations
count = 0
for var in permutations('ЯРОСЛАВ', 5):
    slovo = ''.join(var)
    sogl = [x for x in slovo if x in 'РСЛВ']
    glas = [x for x in slovo if x in 'ЯОА']
    if len(sogl) > len(glas):
        if all(pair not in slovo for pair in 'ЯА АЯ ЯО ОЯ АО ОА'.split()):
            count += 1
print(count)


# Вариант 3
from itertools import permutations
count = 0
for var in permutations('ЯРОСЛАВ', 5):
    slovo = ''.join(var)
    sogl = [x for x in slovo if x in 'РСЛВ']
    glas = [x for x in slovo if x in 'ЯОА']
    if len(sogl) > len(glas):
        slovo = slovo.replace('Я', 'А').replace('О', 'А')
        if 'АА' not in slovo:
            count += 1
print(count)
'''
# Ответ: 1224


# Тип 8 №26982
# Сколько существует шестизначных чисел, делящихся на 5, в которых каждая цифра может встречаться только один раз,
# при этом никакие две чётные и две нечётные цифры не стоят рядом.
'''
from itertools import permutations
count = 0
for var in permutations('0123456789', 6):
    num = ''.join(var)
    if num[0] != '0' and num[-1] in '05':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        if '22' not in num and '11' not in num:
            count += 1
print(count)
'''

# endregion Урок: ******************************************************************


# Славик = [2.1, 6.1, 8.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
