# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************

'''
from itertools import product, permutations

for var in permutations('ABC'):
    r = ''.join(var)
    print(var, r)
    # ('A', 'B', 'C') ABC
    # ('A', 'C', 'B') ACB
    # ('B', 'A', 'C') BAC
    # ('B', 'C', 'A') BCA
    # ('C', 'A', 'B') CAB
    # ('C', 'B', 'A') CBA


for var in product('ABC', repeat=2):
    r = ''.join(var)
    print(var, r)
    # ('A', 'A') AA
    # ('A', 'B') AB
    # ('A', 'C') AC
    # ('B', 'A') BA
    # ('B', 'B') BB
    # ('B', 'C') BC
    # ('C', 'A') CA
    # ('C', 'B') CB
    # ('C', 'C') CC
'''

# Тип 8 №3570
# Все 4-буквенные слова, составленные из букв С, Л, О, Н записаны в алфавитном порядке и пронумерованы.
#
# Вот начало списка:
# 1. ЛЛЛЛ
# 2. ЛЛЛН
# 3. ЛЛЛО
# 4. ЛЛЛС
# 5. ЛЛНЛ
#
# Запишите слово, которое стоит под номером 250.

# Вариант 1
'''
s = sorted('СЛОН')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if num == 250:
                    print(num, slovo)
                num += 1
'''

# Вариант 2
'''
from itertools import product
num = 1
for var in product(sorted('СЛОН'), repeat=4):
    slovo = ''.join(var)
    if num == 250:
        print(num, slovo)
    num += 1
'''
# Ответ: ССОН


# Тип 8 №7328
# Герасим составляет 7-буквенные коды из букв Г, Е, Р, А, С, И, М.
# Каждую букву нужно использовать ровно 1 раз,
# при этом нельзя ставить подряд две гласные или две согласные.
# Сколько различных кодов может составить Герасим?
'''
from itertools import permutations
cnt = 0
for var in permutations('ГЕРАСИМ', 7):
    slovo = ''.join(var)
    slovo = slovo.replace('Е', 'А').replace('И', 'А')
    slovo = slovo.replace('Р', 'Г').replace('С', 'Г').replace('М', 'Г')
    if 'ГГ' not in slovo and 'АА' not in slovo:
        cnt += 1
print(cnt)
'''
# Ответ: 144


# Тип 8 №7986
# Сколько слов длины 5, начинающихся с согласной буквы и заканчивающихся гласной буквой,
# можно составить из букв З, И, М, А? Каждая буква может входить в слово несколько раз.
# Слова не обязательно должны быть осмысленными словами русского языка.
'''
from itertools import product
cnt = 0
for var in product('ЗИМА', repeat=5):
    slovo = ''.join(var)
    if slovo[0] in 'ЗМ' and slovo[-1] in 'ИА':
        cnt += 1
print(cnt)
'''
# Ответ: 256


# Тип 8 №40983
# Георгий составляет коды из букв своего имени.
# Код должен состоять из 7 букв,
# и каждая буква в нём должна встречаться столько же раз, сколько в имени Георгий.
# Кроме того, одинаковые буквы в коде не должны стоять рядом.
# Сколько кодов может составить Георгий?
'''
from itertools import permutations
cnt = []
for var in permutations('ГЕОРГИЙ'):
    slovo = ''.join(var)
    if 'ГГ' not in slovo:
        cnt.append(slovo)
print(len(set(cnt)))
'''
# Ответ: 1800


# Тип 8 №55595
# Митрофан составляет коды из букв, входящих в слово МИТРОФАН.
# Код должен состоять из 6 букв, буквы в коде не должны повторяться,
# согласных в коде должно быть больше, чем гласных, две гласные буквы нельзя ставить рядом.
# Сколько кодов может составить Митрофан?
'''
print('ИО ОИ ИА АИ ОА АО'.split())
for pair in 'ИО ОИ ИА АИ ОА АО'.split():
    print(pair)
'''

'''
from itertools import permutations
cnt = 0
for var in permutations('МИТРОФАН', 6):
    slovo = ''.join(var)
    sogl = [x for x in slovo if x in 'МТРФН']
    glas = [x for x in slovo if x in 'ИОА']
    if len(sogl) > len(glas):
        if all(pair not in slovo for pair in 'ИО ОИ ИА АИ ОА АО'.split()):
            cnt += 1
print(cnt)
'''
# Ответ: 9360


# Тип 8 №58237
# Сколько существует различных четырёхзначных чисел, записанных в семеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?
'''
from itertools import product
cnt = 0
for var in product('0123456', repeat=4):
    num = ''.join(var)
    if num[0] > num[1] > num[2] > num[3]:
        cnt += 1
print(cnt)


from itertools import permutations
cnt = 0
for var in permutations('0123456', 4):
    if list(var) == sorted(var, reverse=True):
        cnt += 1
print(cnt)
'''
# Ответ: 35


# Тип 8 №59742
# Определите количество четырехзначных чисел, записанных в десятичной системе счисления,
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
from itertools import permutations
cnt = 0
for var in permutations('0123456789', 4):
    num = ''.join(var)
    if num[0] != '0':
        num = num.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        num = num.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        if '22' not in num and '11' not in num:
            cnt += 1
print(cnt)
      '''
# Ответ: 720.





# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Олеся = [1.1, 2.1, 4.1, 5.1, 6.1, 7.1, 9.1, 10.1, 11.1, 12.1, 14.1, 16.1, 17.1, 18.1, 19-21 (кодом), 25.1]
# КЕГЭ = []
# на следующем уроке: # порешать 8 номер через itertools
