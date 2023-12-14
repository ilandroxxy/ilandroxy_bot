
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# Тип 8 №9645
# Все 4-буквенные слова, составленные из букв В, Л, Т, У, записаны в алфавитном порядке и пронумерованы.
#
# Вот начало списка:
# 1. ВВВВ
# 2. ВВВЛ
# 3. ВВВТ
# 4. ВВВУ
# Запишите слово, которое стоит под номером 98.
'''
s = sorted('ВЛТУ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if num == 98:
                    print(num, slovo)
                num += 1

# Вариант 2
s = sorted('ВЛТУ')
words = [0]
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                words.append(slovo)
print(words[98])


# Вариант 3
from itertools import product
words = [0]
for s in product(sorted('ВЛТУ'), repeat=4):
    slovo = ''.join(s)
    words.append(slovo)
print(words[98])
'''
# Ответ: ЛТВЛ



# Тип 8 №3206
# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке.
# Вот начало списка:
# 1. ААААА
# 2. ААААК
# 3. ААААР
# 4. ААААУ
# 5. АААКА

# Укажите номер первого слова, которое начинается с буквы К.
'''
from itertools import product
num = 1
for s in product(sorted('АКРУ'), repeat=5):
    slovo = ''.join(s)
    if slovo[0] == 'К':
        print(num)
        break
    num += 1
'''
# Ответ: 257


# Тип 8 №59744
# Евгений составляет 6-буквенные слова из букв М, У, Ж, Ч, И, Н, А.
# Каждая из букв может встречаться в слове ровно один раз, причём первой буквой не может быть Ч,
# буква Ж должна встречаться не менее 1 раза и номер слова должен быть нечётный.
#
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
                            if a != 'Ч' and slovo.count('Ж') >= 1:
                                count += 1
print(count / 2)
'''
'''
from itertools import permutations
count = 0
for s in permutations('МУЖЧИНА', 6):
    slovo = ''.join(s)
    if slovo[0] != 'Ч' and slovo.count('Ж') >= 1:
        count += 1
print(count / 2)
'''
# Ответ: 1860

# from itertools import permutations
# for s in permutations('123'):
#     print(s)


# Тип 8 №27009
# Николай составляет 4-буквенные коды из букв Н, И, К, О, Л, А, Й.
# Каждую букву можно использовать любое количество раз, при этом код не может начинаться с буквы Й
# и должен содержать хотя бы одну гласную.
# Сколько различных кодов может составить Николай?
'''
from itertools import product
count = 0
for s in product('НИКОЛАЙ', repeat=4):
    slovo = ''.join(s)
    if slovo[0] != 'Й' and any(a in slovo for a in 'ИОА'):
        count += 1
print(count)
'''
# Ответ: 1866

# Тип 8 №7986
# Сколько слов длины 5, начинающихся с согласной буквы и
# заканчивающихся гласной буквой, можно составить из букв З, И, М, А?
# Каждая буква может входить в слово несколько раз.
# Слова не обязательно должны быть осмысленными словами русского языка.
'''
from itertools import product
count = 0
for s in product('ЗИМА', repeat=5):
    slovo = ''.join(s)
    if slovo[0] in 'ЗМ':
        if slovo[-1] in 'ИА':
            count += 1
print(count)
'''
# Ответ: 256


# Тип 8 №46966
# Светлана составляет коды из букв слова РОСОМАХА. Код должен состоять из 8 букв,
# и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
# Сколько кодов может составить Светлана?
'''
s = 'РОСОМАХА'
s1 = 'ОА'
s2 = 'РСМХ'
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
                                if len(set(slovo)) == 6 and slovo.count('О') == 2 and s.count('А') == 2:
                                    count.add(slovo)
                                   
print(len(count) * 2)
'''
# Ответ: 288



'''
from itertools import permutations
count = 0
for s in permutations('РОСОМАХА'):
    slovo = ''.join(s)
'''
# endregion Урок: ******************************************************************


# Варя = [2.1, 5.1, 6.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
