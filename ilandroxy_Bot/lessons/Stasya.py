
# region Домашка


# Тип 14 № 48385
# Операнды арифметического выражения записаны в системах счисления с основаниями 13 и 18:
#
# 8x78y_13 + 79xy7_18
#
# Определите наименьшие значения x и y, при которых значение данного арифметического выражения кратно 9.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 9 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
for x in '0123456789abc':
    for y in '0123456789abc':
        a = int(f'8{x}78{y}', 13)
        b = int(f'79{x}{y}7', 18)

        if (a + b) % 9 == 0:
            print((a + b) // 9)
            break
# Ответ: 113024
'''

# Тип 14 № 48377
# Операнды арифметического выражения записаны в системе счисления с основанием 13:
#
# 26x98_13 + 4x296_13
#
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 34.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 34 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
for x in '0123456789abc':
    a = int(f'26{x}98', 13)
    b = int(f'4{x}296', 13)

    if (a + b) % 34 == 0:
        print((a + b) // 34)
        break
# Ответ: 6141
'''



# Тип 8 № 33753
# Андрей составляет 6-буквенные коды из букв А, Н, Д, Р, Е, Й. Буква А должна входить в код не менее одного раза, а буква Й — не более одного раза.
# Сколько различных кодов может составить Андрей?
'''
count = 0
s =  'АНДРЕЙ'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        if temp.count('А') >= 1 and temp.count('Й') <= 1:
                                print(temp)
                                count += 1
print(count)
# Ответ: 24135
'''


# Тип 8 № 36021
'''
# Вася составляет 6-буквенные слова, в которых могут быть использованы только буквы В, И, Ш, Н, Я, причём буква В используется не более одного раза.
# Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
# Слово не должно начинаться с буквы Ш и оканчиваться гласными буквами.
# Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
# Сколько существует таких слов, которые может написать Вася?

count = 0
s = 'ВИШНЯ'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        if temp.count('В') <= 1 and a != 'Ш' and f not in 'ИЯ':
                        #if temp.count('В') <= 1 and temp[0] != 'Ш' and temp[-1] not in 'ИЯ':
                            print(temp)
                            count += 1
print(count)
'''
# Ответ 4352





# Тип 8 № 19059
# Все 4-буквенные слова, в составе которых могут быть буквы Н, О, Т, К, И, записаны в алфавитном порядке и пронумерованы, начиная с 1.
# Ниже приведено начало списка.
# 1.ИИИИ
# 2.ИИИК
# 3.ИИИН
# 4.ИИИО
# 5.ИИИТ
# 6.ИИКИ
# Под каким номером в списке идёт первое слово, которое начинается с буквы О?
'''
s = 'ИКНОТ'
count = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                if a == 'О':
                    print(count, temp)
                    exit()
                count += 1
# Ответ: 376
'''
# endregion Домашка


# region Урок

# Тип 8 № 45242
'''
# Все пятибуквенные слова, в составе которых могут быть только буквы Б, А, Т, Ы, Р, записаны в алфавитном порядке и пронумерованы начиная с 1.
#
# Ниже приведено начало списка.
# 1.ААААА
# 2.ААААБ
# 3.ААААР
# 4.ААААТ
# 5.ААААЫ
# 6.АААБА

# Под каким номером в списке идёт первое слово, которое не содержит ни одной буквы Ы и не содержит букв А, стоящих рядом?



s = 'АБРТЫ'
count = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('Ы') == 0 and 'АА' not in temp:
                        print(count, temp)
                        exit()
                    count += 1
'''
# Ответ: 131.


# (№ 5708) (Л. Малинов) Ваня составляет 6-буквенные слова из букв В, И, Д, Е, О.
# Его интересуют коды, в которых есть хотя бы одна буква И и хотя бы одна буква Е.
# Кроме того, все гласные в слове должны стоять в алфавитном порядке.
# Сколько различных подходящих кодов может составить Ваня?
'''
s = 'ВДЕИО'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        if temp.count('И') >= 1 and temp.count('Е') >= 1:
                            if 'О' in temp:
                                if temp.rindex('Е') < temp.index('И') and temp.rindex('И') < temp.index('О'):
                                    print(temp)
                                    count += 1
                            else:
                                if temp.rindex('Е') < temp.index('И'):
                                    print(temp)
                                    count += 1

print(count)
'''
# Ответ: 1215


# (№ 5010) Вася составляет слова из букв слова ПРЕПАРАТ.
# Код должен состоять из 8 букв, и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде должны стоять рядом две гласные или две согласные буквы.
# Сколько различных слов может составить Вася?
'''
Symbol = ["АА", "АЕ", "ЕА", "ПП", "РР", "ПР", "РП", "ТР", "РТ", "ТП", "ПТ"]
s = 'ПРЕПАРАТ'
RES = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                temp = a + b + c + d + e + f + g + h
                                if temp.count('П') == 2 and temp.count('Р') == 2 and  temp.count('А') == 2 and  temp.count('Т') == 1 and  temp.count('Е') == 1:
                                    flag = True
                                    for x in Symbol:
                                        if x in temp:
                                            RES.append(temp)
                                            flag = False
                                            break
A = set(RES)
print(len(A))
'''
# Ответ: 5040


# Тип 12 № 14700
# Какая строка получится в результате применения приведённой ниже программы к строке вида 1…12…2 (7 единиц, затем 7 двоек)?
# В ответе запишите полученную строку.
#
# НАЧАЛО
# ПОКА нашлось (111) ИЛИ нашлось (222)
#     ЕСЛИ нашлось (111)
#         ТО заменить (111, 2)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (222)
#         ТО заменить (222, 1)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ

'''
s = '1' * 7 + '2' * 7
while '111' in s or '222' in s:  # ПОКА нашлось (111) ИЛИ нашлось (222)
    if '111' in s:  # ЕСЛИ нашлось (111)
        s = s.replace('111', '2', 1)
    if '222' in s:
        s = s.replace('222', '1')

print(s)
'''
# Ответ: 12




# Тип 12 № 25844
'''
# На вход приведённой ниже программе поступает строка, начинающаяся с символа «>», а затем содержащая 11 цифр 1, 12 цифр 2 и 30 цифр 3,
# расположенных в произвольном порядке.
# Определите сумму числовых значений цифр строки, получившейся в результате выполнения программы.
# Так, например, если результат работы программы представлял бы собой строку, состоящую из 50 цифр 4, то верным ответом было бы число 200.
#
# НАЧАЛО
# ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
#     ЕСЛИ нашлось (>1)
#         ТО заменить (>1, 22>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>2)
#         ТО заменить (>2, 2>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>3)
#         ТО заменить (>3, 1>)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ

s = '>' + '1' * 11 + '2' * 12 + '3' * 30
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)

print(s)

summ = s.count('1') + s.count('2') * 2 + s.count('3') * 3
print(summ)

M = [int(i) for i in s[:-1]]
print(sum(M))

summ2 = 0
for x in s[:-1]:
    summ2 += int(x)
print(summ2)

A = []
for i in range(0, len(s)-1):
    A.append(int(s[i]))
print(sum(A))
'''

# Тип 12 № 46970
'''
# НАЧАЛО
#     ПОКА НЕ нашлось (00)
#         заменить (01, 210)
#         заменить (02, 3101)
#         заменить (03, 2012)
#     КОНЕЦ ПОКА
# КОНЕЦ
#
# 
# Известно, что исходная строка начиналась с нуля и заканчивалась нулём, а между ними содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка, содержащая 70 единиц, 56 двоек и 23 тройки. Сколько цифр было в исходной строке?

for x in range(1, 50):
    for y in range(1, 50):
        for z in range(1, 50):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'
            temp = s


            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)

            if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
                print(len(temp))
'''
# Ответ: 40.


# endregion Урок


# todo: Стася = [2, 5, 6, 8, 12, 14+], на следующем уроке:  Разбираем функции и 16 номер