# region Домашка:  **************************************************



# endregion Домашка: **************************************************


# region Урок:  **************************************************

# Тип 8 № 14225
# Олег составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё
# кодовое слово. В качестве кодовых слов Олег использует 4-буквенные слова, в которых есть только буквы A, B, C, D,
# E, X, Z, причём буквы X и Z встречаются только на двух первых позициях, а буквы A, B, C, D, E — только на двух
# последних. Сколько различных кодовых слов может использовать Олег?
'''
# Вариант 1
count = 0
for a in 'XZ':
    for b in 'XZ':
        for c in 'ABCDE':
            for d in 'ABCDE':
                slovo = a + b + c + d
                count += 1
print(count)

# Вариант 2
count = 0
s = 'ABCDEXZ'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if slovo[0] in 'XZ' and slovo[1] in 'XZ' and slovo[2] in 'ABCDE' and slovo[3] in 'ABCDE':
                    count += 1
print(count)


# Вариант 3
import itertools
count = 0
for s in itertools.product('ABCDEXZ', repeat=4):
    slovo = ''.join(s)
    if slovo[0] in 'XZ' and slovo[1] in 'XZ' and slovo[2] in 'ABCDE' and slovo[3] in 'ABCDE':
        count += 1
print(count)
'''
# Ответ: 100



# Тип 8 № 3811
# Все 5-буквенные слова, составленные из букв Е, Ж, И, записаны в алфавитном порядке и пронумерованы.
#
# Вот начало списка:
# 1. ЕЕЕЕЕ
# 2. ЕЕЕЕЖ
# 3. ЕЕЕЕИ
# 4. ЕЕЕЖЕ
#
# Запишите слово, которое стоит под номером 238.
'''
s = sorted('ЕЖИ')
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if k == 238:
                        print(k, slovo)
                    k += 1
'''
# Ответ: ИИИЖЕ

# endregion Урок:  **************************************************

import useful
print(useful.Who_Is_Name())

# todo: Кирилл = [1, 2, 3, 4, 5, 8, 9, 12, 13, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25], на следующем уроке:
# на прошлом уроке:
# на следующем уроке: Поразбирать 8 номера с any all
