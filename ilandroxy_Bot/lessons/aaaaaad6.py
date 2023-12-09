# region Домашка: ******************************************************************
'''
from itertools import permutations
R = []
for elem in permutations(['1' * 20, '2' * 15, '3' * 40]):
    s = '>' + ''.join(elem) + '<'

    while '><' not in s:
        if '>1' in s:
            s = s.replace('>1', '3>')
        if '>2' in s:
            s = s.replace('>2', '2>')
        if '>3' in s:
            s = s.replace('>3', '1>')
        if '3<' in s:
            s = s.replace('3<', '<1')
        if '2<' in s:
            s = s.replace('2<', '<3')
        if '1<' in s:
            s = s.replace('1<', '<2')
    summ = s.count('1') + s.count('2') * 2 + s.count('3') * 3
    R.append(summ)
print(max(R))
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 8 №9361
# Игорь составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов Игорь использует 5-буквенные слова, в которых есть только буквы П, И, Р,
# причём буква П появляется ровно 1 раз. Каждая из других допустимых букв может встречаться
# в кодовом слове любое количество раз или не встречаться совсем.
# Сколько различных кодовых слов может использовать Игорь?
'''
s = 'ПИР'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if slovo.count('П') == 1:
                        count += 1
print(count)

# Вариант 2
from itertools import product, permutations
count = 0
for elem in product('ПИР', repeat=5):
    slovo = ''.join(elem)
    if slovo.count('П') == 1:
        count += 1
print(count)
'''
# Ответ: 80


# Тип 8 №59801
# Игорь составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов Игорь использует пятибуквенные слова, в которых могут быть только буквы КОНФЕТА,
# причём буква Е появляется ровно 2 раза. Каждая из других допустимых букв может встречаться в кодовом
# слове любое количество раз или не встречаться совсем.
# На втором месте НЕ может стоять буква Ф. Сколько различных кодовых слов может использовать Игорь?
'''
s = 'КОНФЕТА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if slovo.count('Е') == 2:
                        if b != 'Ф':
                            count += 1
print(count)


from itertools import product, permutations
count = 0
for elem in product('КОНФЕТА', repeat=5):
    slovo = ''.join(elem)
    if slovo.count('Е') == 2:
        if slovo[1] != 'Ф':
            count += 1
print(count)
'''

# Тип 8 №18622
# Демьян составляет 6-буквенные коды из букв Д, Е, М, Ь, Я, Н.
# Каждую букву нужно использовать ровно 1 раз, при этом Ь
# нельзя ставить первым и нельзя ставить после гласной.
# Сколько различных кодов может составить Демьян?
'''
s = 'ДЕМЬЯН'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if len(slovo) == len(set(slovo)):  # set() - множество, то есть удаляет копии элементов списка/строки
                            if a != 'Ь':  # slovo[0] != 'Ь'
                                if 'ЯЬ' not in slovo and 'ЕЬ' not in slovo:
                                    count += 1
print(count)

from itertools import permutations
count = 0
for elem in permutations('ДЕМЬЯН', 6):
    slovo = ''.join(elem)
    if slovo[0] != 'Ь': 
        if 'ЯЬ' not in slovo and 'ЕЬ' not in slovo:
            count += 1
print(count)
'''
# Ответ: 360


# Тип 8 №60250
# Сколько существует восьмеричных пятизначных чисел, не содержащих в своей записи цифру 1,
# в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?
'''
s = '01234567'
s1 = '1357'
s2 = '0246'
count = 0
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    num = a + b + c + d + e
                    if '1' not in num:  # num.count('1') == 0
                        if len(num) == len(set(num)):  # в которых все цифры различны
                            count += 1

for a in s2:
    for b in s1:
        for c in s2:
            for d in s1:
                for e in s2:
                    num = a + b + c + d + e
                    if '1' not in num:  # num.count('1') == 0
                        if len(num) == len(set(num)):  # в которых все цифры различны
                            if num[0] != '0':
                                count += 1
print(count)
'''


# Тип 8 №40724
# Светлана составляет коды из букв своего имени. Код должен состоять из 8 букв,
# и каждая буква в нём должна встречаться столько же раз, сколько в имени Светлана.
# Кроме того, одинаковые буквы в коде не должны стоять рядом. Сколько кодов может составить Светлана?
'''
from itertools import permutations
count = set()
for elem in permutations('светлана'):
    slovo = ''.join(elem)
    if 'аа' not in slovo:
        count.add(slovo)
print(len(count))
'''
# Ответ: 15120


# КЕГЭ № 8417 (Уровень: Базовый)
# Ярослав составляет коды из букв, входящих в слово ЯРОСЛАВ.
# Код должен состоять из 5 букв, буквы в коде не должны повторяться, согласных в коде должно быть больше,
# чем гласных, две гласные буквы нельзя ставить рядом.
# Сколько кодов может составить Ярослав?
'''
s = 'ЯРОСЛАВ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):
                        sogl = [x for x in slovo if x in 'РСЛВ']
                        glas = [x for x in slovo if x in 'ЯОА']
                        if len(sogl) > len(glas):
                            if all(pair not in slovo for pair in 'ЯО ОЯ ОА АО ЯА АЯ'.split()):
                                count += 1
print(count)
'''


# КЕГЭ № 6985 (Уровень: Средний) (Д. Статный)
# Все шестибуквенные слова, в составе которых могут быть только русские буквы М, А, Р, К, С, Л
# записаны в алфавитном порядке и пронумерованы начиная с 1.
#
# Ниже приведено начало списка.
# 1. АААААА
# 2. АААААК
# 3. АААААЛ
# 4. АААААМ
# 5. АААААР
# 6. АААААС
#
# Под каким последним номером идёт слово, в котором буквы К не стоят рядом с буквой С
# и одна буква повторяется трижды, а остальные не повторяются?
'''
R = []
s = sorted('МАРКСЛ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if 'КС' not in slovo and 'СК' not in slovo:
                            if len(set(slovo)) == 4 and any(slovo.count(x) == 3 for x in slovo):
                                R.append(num)
                        num += 1
print(max(R))
'''
# Ответ: 46605

# endregion Урок: ******************************************************************


# Лера = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
