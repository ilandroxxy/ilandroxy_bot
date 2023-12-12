# region Домашка: ******************************************************************

# С клавиатуры вводится одна строка, состоящая из символов X и Y.
# Найдите, какой символ чаще всего встречается в этой строке.
# Выведите количество повторений (совпадений). Сначала необходимо вывести символ,
# затем количество повторений.
'''
s = input()
if s.count('X') > s.count('Y'):
    print('X')
    print(s.count('X'))
else:
    print('Y')
    print(s.count('Y'))
'''


'''
print(input().replace('22', 'two', 3))
'''
# 222222222222222222222
# twotwotwo222222222222222


# КЕГЭ № 5268 (Уровень: Средний) (С. Якунин)
# Дмитрий составляет слова, переставляя буквы в слове АМФИБРАХИЙ.
# Сколько различных слов, содержащих ИИФАА или ААФИИ, может составить Дмитрий?
'''
from itertools import permutations
count = set()
for s in permutations('АМФИБРАХИЙ'):
    slovo = ''.join(s)
    if 'ИИФАА' in slovo or 'ААФИИ' in slovo:
        count.add(slovo)
print(len(count))
'''

# todo Доделать задание: https://stepik.org/lesson/1038667/step/9?unit=1062772

s = sorted('БАРАШ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(set(slovo)) == 4 and any(slovo.count(x) == 2 for x in slovo):
                        if slovo.count('Б') + slovo.count('Р') + slovo.count('Ш') <= 3:
                            print(num)
                    num +=1


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

# Тип 8 №3696
# Все 5-буквенные слова, составленные из букв В, И, Н, Т, записаны в алфавитном порядке.
# Вот начало списка:
# 1.  ВВВВВ
# 2.  ВВВВИ
# 3.  ВВВВН
# 4.  ВВВВТ
# 5.  ВВВИВ
#
# Запишите слово, которое стоит под номером 1020.
'''
s = sorted('ВИНТ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if num == 1020:
                        print(num, slovo)
                    num += 1

# Вариант 2
from itertools import product
num = 1
for s in product(sorted('ВИНТ'), repeat=5):
    slovo = ''.join(s)
    if num == 1020:
        print(slovo)
    num += 1
'''
# Ответ: ТТТНТ


# Тип 8 №33510
# Тимофей составляет 5-буквенные коды из букв Т, И, М, О, Ф, Е, Й.
# Буква Т должна входить в код не менее одного раза,
# а буква Й — не более одного раза. Сколько различных кодов может составить Тимофей?
'''
s = sorted('ТИМОФЕЙ')
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if slovo.count('Т') >= 1:
                        if slovo.count('Й') <= 1:
                            count += 1
print(count)

# Вариант 2
from itertools import product
count = 0
for s in product('ТИМОФЕЙ', repeat=5):
    slovo = ''.join(s)
    if slovo.count('Т') >= 1:
        if slovo.count('Й') <= 1:
            count += 1
print(count)
'''
# Ответ: 8006



# endregion Урок: ******************************************************************


# Екатерина = [2.1, 6.1, 12.1]
# КЕГЭ  = []
# на следующем уроке:
