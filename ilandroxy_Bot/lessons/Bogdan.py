# region Домашка:  ******************************************************************************

# Тип 12 № 26986
'''
# Дана программа для Редактора:

# ПОКА нашлось (49) ИЛИ нашлось (97) ИЛИ нашлось (47)
#     ЕСЛИ нашлось (47)
#     ТО заменить (47, 74)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (97)
#     ТО заменить (97, 79)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (49)
#     ТО заменить (49, 94)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА

# На вход приведённой ниже программе поступает строка, содержащая 40 цифр 7, 40 цифр 9 и 50 цифр 4, расположенных в произвольном порядке.
# Запишите без разделителей символы, которые имеют порядковые номера 25, 71 и 105 в получившейся строке.

s = '4' * 50 + '7' * 40 + '9' * 40

while '49' in s or '97' in s or '47' in s:
    if '47' in s:
        s = s.replace('47', '74', 1)
    if '97' in s:
        s = s.replace('97', '79', 1)
    if '49' in s:
        s = s.replace('49', '94', 1)

print(s[25-1], s[71-1], s[105-1])
print(s)
'''
# Ответ: 794

# endregion Домашка:  ******************************************************************************


# region Урок:  ******************************************************************************

# Тип 8 № 3193
'''
# Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:
#
# 1. ААААА
# 2. ААААО
# 3. ААААУ
# 4. АААОА
#
# Запишите слово, которое стоит на 210-м месте от начала списка.

s = 'АОУ'
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if k == 210:
                        print(k, temp)
                    k += 1
'''
# Ответ: УОУАУ


# Тип 8 № 3200
'''
# Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:
#
# 1. ААААА
# 2. ААААО
# 3. ААААУ
# 4. АААОА
#
# Укажите номер первого слова, которое начинается с буквы У.

s = 'АОУ'
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if a == 'У':
                        print(k, temp)
                        exit()
                    k += 1
 '''
# Ответ: 163


# Тип 8 № 15978
'''
# Все шестибуквенные слова, составленные из букв К, Л, Н, Т, Э, записаны в алфавитном порядке и пронумерованы, начиная с 1.
# Начало списка выглядит так:
# 1. КККККК
# 2. КККККЛ
# 3. КККККН
# 4. КККККТ
# 5. КККККЭ
#
# Под каким номером в списке идёт слово ККЛКЛК?

s = 'КЛНТЭ'
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        if temp == 'ККЛКЛК':
                            print(k, temp)
                        k += 1
'''
# Ответ: 131


# Тип 8 № 27009
'''
# Николай составляет 4-буквенные коды из букв Н, И, К, О, Л, А, Й.
# Каждую букву можно использовать любое количество раз, при этом код не может начинаться с буквы Й и должен содержать хотя бы одну гласную.
# Сколько различных кодов может составить Николай?

s = 'НИКОЛАЙ'
glas = 'ИОА'
count = 0
for a in 'НИКОЛА':
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                if 'А' in temp or 'О' in temp or 'И' in temp:
                    count += 1
print(count)
'''
# Ответ: 1866


# Тип 8 № 18622
'''
# Демьян составляет 6-буквенные коды из букв Д, Е, М, Ь, Я, Н.
# Каждую букву нужно использовать ровно 1 раз, при этом Ь нельзя ставить первым и нельзя ставить после гласной.
# Сколько различных кодов может составить Демьян?

s = 'ДЕМЬЯН'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        M = [i for i in temp]
                        if len(set(M)) == len(M):
                            if a != 'Ь' and 'ЕЬ' not in temp and 'ЯЬ' not in temp:
                                print(temp, M, set(M))
                                count += 1
print(count)
'''
# Ответ: 360


# Тип 8 № 10473
'''
# Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 4.
# Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно два раза,
# а каждая из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

s = '1234'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('1') == 2:
                        count += 1
print(count)
'''
# Ответ: 270


# Тип 8 № 26953
'''
# Найдите количество пятизначных восьмеричных чисел, в которых все цифры различны и никакие две четные или нечетные не стоят рядом.

s = '01234567'
s1 = '1357'
s2 = '0246'
count = 0
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    temp = a + b + c + d + e
                    M = [i for i in temp]
                    if len(set(M)) == len(M):
                        print(temp)
                        count += 1

for a in '246':
    for b in s1:
        for c in s2:
            for d in s1:
                for e in s2:
                    temp = a + b + c + d + e
                    M = [i for i in temp]
                    if len(set(M)) == len(M):
                        print(temp)
                        count += 1
print(count)
'''

# Тип 8 № 3570
'''
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

s = sorted([i for i in 'СЛОН'])
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                if k == 250:
                    print(k, temp)
                k += 1
'''
# Ответ: ССОН


# Тип 8 № 35466
'''
# Вероника составляет 3-буквенные коды из букв В, Е, Р, О, Н, И, К, А, причём буква В должна входить в код ровно один раз.
# Все полученные коды Вероника записала в алфавитном порядке и пронумеровала. Начало списка выглядит так:
# 1. ААВ
# 2. АВА
# 3. АВЕ
#
# На каком месте будет записан первый код, не содержащий ни одной буквы А?

s = sorted([i for i in 'ВЕРОНИКА'])
k = 1
for a in s:
    for b in s:
        for c in s:
            temp = a + b + c
            if temp.count('В') == 1:
                if 'А' not in temp:
                    print(k, temp)
                    exit()
                k += 1
'''
# Ответ: 23


# endregion Урок:  ******************************************************************************


# todo: Богдан = [2, 5, 8, 12, 14+]
# на прошлом уроке: Повторили 5 и 12 номера разобрали 8 номер.
# на следующем уроке: Начать пораньше на 10 минут, повторить 8 номер и Разбираем теорию функций (16, 23)