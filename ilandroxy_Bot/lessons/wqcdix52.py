# region Домашка: ******************************************************************

'''
from itertools import permutations, product
for var in permutations('123'):
    print(var)
    # ('1', '2', '3')
    # ('1', '3', '2')
    # ('2', '1', '3')
    # ('2', '3', '1')
    # ('3', '1', '2')
    # ('3', '2', '1')

for var in permutations('123', 2):
    print(var)
    # ('1', '2')
    # ('1', '3')
    # ('2', '1')
    # ('2', '3')
    # ('3', '1')
    # ('3', '2')

for var in product('123', repeat=3):
    print(var)
    # ('1', '1', '1')
    # ('1', '1', '2')
    # ('1', '1', '3')
    # ('1', '2', '1')
    # ('1', '2', '2')
    # ('1', '2', '3')
    # ('1', '3', '1')
    # ('1', '3', '2')
    # ('1', '3', '3')
    # ('2', '1', '1')
    # ('2', '1', '2')
    # ('2', '1', '3')
    # ('2', '2', '1')
    # ('2', '2', '2')
    # ('2', '2', '3')
    # ('2', '3', '1')
    # ('2', '3', '2')
    # ('2', '3', '3')
    # ('3', '1', '1')
    # ('3', '1', '2')
    # ('3', '1', '3')
    # ('3', '2', '1')
    # ('3', '2', '2')
    # ('3', '2', '3')
    # ('3', '3', '1')
    # ('3', '3', '2')
    # ('3', '3', '3')
'''
'''
from itertools import permutations
R = []
for var in permutations(['3' * 40, '1' * 20, '2' * 15]):
    s = '>' + ''.join(var) + '<'
    while '><' not in s:
        s = s.replace('>1', '3>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>3', '1>', 1)
        s = s.replace('3<', '<1', 1)
        s = s.replace('2<', '<3', 1)
        s = s.replace('1<', '<2', 1)
    R.append(s.count('1') * 1 + s.count('2') * 2 + s.count('3') * 3)
print(max(R))
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 8 №3698
# Все 6-буквенные слова, составленные из букв Б, К, Ф, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ББББББ
# 2. БББББК
# 3. БББББФ
# 4. ББББКБ
#
# Запишите слово, которое стоит на 345-м месте от начала списка.
'''
s = sorted('БКФ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if num == 354:
                            print(num, slovo)
                        num += 1

# Вариант 2
from itertools import product
num = 1
for s in product(sorted('БКФ'), repeat=6):
    slovo = ''.join(s)
    if num == 354:
        print(num, slovo)
    num += 1
'''
# Ответ: КККББФ


# Тип 8 №3206
# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке.
# Вот начало списка:

# 1. ААААА
# 2. ААААК
# 3. ААААР
# 4. ААААУ
# 5. АААКА
#
# Укажите номер первого слова, которое начинается с буквы К.
'''
from itertools import product
num = 1
for s in product(sorted('АКРУ'), repeat=5):
    slovo = ''.join(s)
    if slovo[0] == 'К':
        print(num, slovo)
        exit()
    num += 1
'''
# Ответ: 257


# Тип 8 №18491
# Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А.
# Каждую букву нужно использовать ровно 1 раз, при этом Ь нельзя ставить первым и нельзя ставить после гласной.
# Сколько различных кодов может составить Ольга?
'''
s = 'ОЛЬГА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):  # Каждую букву нужно использовать ровно 1 раз
                        if a != 'Ь':
                            if 'АЬ' not in slovo and 'ОЬ' not in slovo:
                                count += 1
print(count)

# Вариант 2
from itertools import permutations
count = 0
for s in permutations('ОЛЬГА', 5):
    slovo = ''.join(s)
    print(slovo)
    if slovo[0] != 'Ь':
        if 'АЬ' not in slovo and 'ОЬ' not in slovo:
            count += 1
print(count)
'''
# Ответ: 48


# Тип 8 №40983
# Георгий составляет коды из букв своего имени.
# Код должен состоять из 7 букв, и каждая буква в нём должна встречаться столько же раз, сколько в имени Георгий.
# Кроме того, одинаковые буквы в коде не должны стоять рядом. Сколько кодов может составить Георгий?
'''
from itertools import permutations
count = set()
for s in permutations('георгий'):
    slovo = ''.join(s)
    if 'гг' not in slovo:
        count.add(slovo)
print(len(count))
'''
# Ответ: 1800


# Тип 8 №59743
# Алиса составляет 6-буквенные слова из букв М,А,Н,Г,У,С,Т.
# Каждая из букв может встречаться сколько угодно раз,
# причём первой буквой не может быть А, буква У должна встречаться не менее 1 раза.
# Также в записи должны быть ровно две буквы М.
# Сколько различных слов может составить Алиса?
'''
from itertools import product
cnt = 0
for s in product('МАНГУСТ', repeat=6):
    slovo = ''.join(s)
    if slovo[0] != 'А':
        if slovo.count('У') >= 1:
            if slovo.count('М') == 2:
                cnt += 1
print(cnt)
'''
# Ответ: 9155


# Тип 8 №59746
# Сколько существует десятичных чисел, которые делятся на 5, при условии что все цифры числа различные?

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

'''
from itertools import permutations
cnt = 1  # почему-то считают 0 
for l in range(1, 10+1):
    for s in permutations('0123456789', l):
        slovo = ''.join(s)
        if slovo[0] != '0':
            if slovo[-1] in '05':
                print(slovo)
                cnt += 1
print(cnt)
'''
# Ответ: 1863219


# Тип 8 №59741
# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр, причем в записи нет цифры 1.
# Также все цифры записи различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
print('20 40 60 42 24 62 26 46 64 13 15 17 31 51 71 35 53 37 73 57 75'.split())
# ['20', '40', '60', '42', '24', '62', '26', '46', '64', '13', '15', '17', '31', '51', '71', '35', '53', '37', '73', '57', '75']

from itertools import permutations
cnt = 0
for s in permutations('01234567', 5):
    num = ''.join(s)
    if num[0] != '0':
        if '1' not in num:
            for x in '0246':
                num = num.replace(x, '+')
            for x in '1357':
                num = num.replace(x, '*')
            if all(pair not in num for pair in '++ **'.split()):
                cnt += 1
print(cnt)

from itertools import permutations
cnt = 0
for s in permutations('01234567', 5):
    num = ''.join(s)
    if num[0] != '0' and '1' not in num:
        for x in '0246': num = num.replace(x, '+')
        for x in '1357': num = num.replace(x, '*')
        if '++' not in num and '**' not in num:
            cnt += 1
print(cnt)
'''
# Ответ: 180


# endregion Урок: ******************************************************************


# Артур = [2.1. 6.1, 8.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
