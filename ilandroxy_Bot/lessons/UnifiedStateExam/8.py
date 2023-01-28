

# region Тип 8 № 8658
'''
# Все 5-буквенные слова, составленные из букв А, Н, П, записаны в алфавитном порядке.
# Вот начало списка:
# 1.ААААА
# 2.ААААН
# 3.ААААП
# 4.АААНА
# 5.АААНН
# Запишите слово, которое стоит на 201-м месте от начала списка.
s = "АНП"
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    count += 1
                    if count == 201:
                        print(temp)
'''
# Ответ: ПННАП
# endregion Тип 8 № 8658

# region Тип 8 № 16037
'''
#Вася составляет 5-буквенные слова, в которых есть только буквы З, И, М, А, причём в каждом слове есть ровно одна гласная буква и она встречается ровно 1 раз.
# Каждая из допустимых согласных букв может встречаться в слове любое количество раз или не встречаться совсем.
# Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
# Сколько существует таких слов, которые может написать Вася?

s = 'ЗИМА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('А')== 1 and temp.count('И')== 0 or temp.count('А')== 0 and temp.count('И')== 1:
                        count += 1
print(count)
'''
# Ответ 160
# endregion Тип 8 № 16037

# region Тип 8 № 3515
'''
#Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке.
#Вот начало списка:
#1.ААААА
#2.ААААО
#3.ААААУ
#4.АААОА
#Сколько букв А встречается в слове, стоящем на 101-м месте от начала списка.
s = 'АОУ'
M = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M.append(temp)
print(M[101+1].count('А'))
'''
# Ответ: 2
# endregion Тип 8 № 3515

# region Тип 8 № 9361
'''
#Игорь составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
#В качестве кодовых слов Игорь использует 5-буквенные слова, в которых есть только буквы П, И, Р, причём буква П появляется ровно 1 раз. 
Каждая из других допустимых букв может встречаться в кодовом слове любое количество раз или не встречаться совсем.
#Сколько различных кодовых слов может использовать Игорь?

s = 'ПИР'
M =[]
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('П') == 1:
                        M.append(temp)
print(len(M))
'''
# Ответ: 80
# endregion Тип 8 № 9361

# region Тип 8 № 16439
'''
#Михаил составляет 6-буквенные коды.
#В кодах разрешается использовать только буквы А, Б, В, Г, при этом код не может начинаться с гласной и не может содержать двух одинаковых букв подряд.
#Сколько различных кодов может составить Михаил?

s = 'АБВГ'
s1 = 'А'
s2 = 'БВГ'
count = 0
for a in s2:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        if 'АА' not in temp and 'ББ' not in temp and 'ВВ' not in temp and 'ГГ' not in temp:
                            count += 1
                        print(count)
'''
# Ответ: 729
# endregion Тип 8 № 16439

# region Тип 8 № 27379
"""
# Виктор составляет 4-буквенные коды из букв В, И, К, Т, О, Р.
# Каждую букву можно использовать не более одного раза, при этом нельзя ставить рядом две гласные и две согласные.
# Сколько различных кодов может составить Виктор?
s = 'ВИКТОР'
gl = 'ИО'
sgl = 'ВКТР'
count = 0
for a in gl:  # sgl
    for b in sgl:  # gl
        for c in gl:  # sgl
            for d in sgl:  # gl
                temp = a + b + c + d
                if temp.count(a) == 1 and temp.count(b) == 1 and temp.count(c) == 1 and temp.count(d) == 1:
                    count += 1
                '''
                M = [a, b, c, d]
                Setter = set(M)
                print(M, Setter)
                if len(Setter) == 4:
                    count += 1
                '''
print(count * 2)
"""
# Ответ: 48
# endregion Тип 8 № 27379

# region Тип 8 № 47005
'''
# Светлана составляет коды из букв слова ПАРАБОЛА. Код должен состоять из 8 букв, и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы. Сколько кодов может составить Светлана?

s = "ПАРАБОЛА"
s1 = 'АААО'
s2 = 'ПРБЛ'
M = []
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    for f in s2:
                        for g in s1:
                            for h in s2:
                                temp = a + b + c + d + e + f + g + h
                                if temp.count('П') == 1 and temp.count('Р') == 1 and temp.count(
                                        'Б') == 1 and temp.count('О') == 1 and temp.count('Л') == 1 and temp.count('А') == 3:
                                    if temp not in M:
                                        M.append(temp)
print(len(M) * 2)
'''
# Ответ 192
# endregion Тип 8 № 47005

# region Тип 8 № 10473
'''
# Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 4.
# Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно два раза, а каждая из других
# допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

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
# Ответ 270
# endregion Тип 8 № 10473

# region Тип 8 № 40724
'''
# Светлана составляет коды из букв своего имени.
# Код должен состоять из 8 букв, и каждая буква в нём должна встречаться столько же раз, сколько в имени Светлана.
# Кроме того, одинаковые буквы в коде не должны стоять рядом. Сколько кодов может составить Светлана?

s = 'СВЕТЛАНА'

M = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                temp = a + b + c + d + e + f + g + h
                                if 'АА' not in temp and temp.count('С') == 1 and temp.count('В') == 1 and temp.count('Е') == 1 and temp.count('Т') == 1 and temp.count('Л') == 1 and temp.count('Н') == 1 and temp.count('А') == 2:
                                    if temp not in M:
                                        M.append(temp)
print(len(M))
'''
# Ответ: 15120
# endregion Тип 8 № 40724

# region Тип 8 № 3195
# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке.

# Вот начало списка:
# 1. ААААА
# 2. ААААК
# 3. ААААР
# 4. ААААУ
# 5. АААКА

# Запишите слово, которое стоит на 350-м месте от начала списка.

# вариант 1
'''
s = 'АКРУ'
count = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    #print(count, temp)
                    if count == 350:
                        print(temp)
                    count += 1
'''

# вариант 2
'''
s = 'АКРУ'
M = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M.append(temp)

print(M[350-1])
'''
# Ответ: КККУК
# endregion Тип 8 № 3195

# region Тип 8 № 3207
'''
# Все 5-буквенные слова, составленные из букв К, О, Р, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ККККК
# 2. ККККО
# 3. ККККР
# 4. КККОК
#
# Запишите слово, которое стоит под номером 238.

s = 'КОР'
count = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    # print(count, temp)
                    if count == 238:
                        print(temp)
                    count += 1
'''
# Ответ: Р Р Р О К
# endregion Тип 8 № 3207

# region Тип 8 № 26953
'''
# Найдите количество пятизначных восьмеричных чисел, в которых все цифры различны и никакие две четные или нечетные не стоят рядом.

s = '01234567'
s1 = '0246'
s2 = '1357'
count = 0
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    temp = a + b + c + d + e
                    if a != '0':
                        M = [i for i in temp]
                        A = set(M)
                        if len(A) == 5:
                            count += 1

for a in s2:
    for b in s1:
        for c in s2:
            for d in s1:
                for e in s2:
                    temp = a + b + c + d + e
                    if a != '0':
                        M = [i for i in temp]
                        A = set(M)
                        if len(A) == 5:
                            count += 1

print(count)
'''
# Ответ: 504
# endregion Тип 8 № 26953

# region Тип 8 № 9302
'''
# Сколько слов длины 4, начинающихся с согласной буквы и заканчивающихся гласной буквой, можно составить из букв М, Е, Т, Р, О?
# Каждая буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными словами русского языка.

s = 'МЕТРО'
s1 = 'МТР'
s2 = 'ЕО'
count = 0
for a in s1:
    for b in s:
        for c in s:
            for d in s2:
                temp = a + b + c + d
                count += 1
print(count) 
'''
# Ответ: 150
# endregion Тип 8 № 9302

# region Тип 8 № 23908
'''
# Вася составляет 5-буквенные слова, в которых есть только буквы В, О, Л, К, причём буква В используется в каждом слове ровно 1 раз.
# Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
# Словом считается любая допустимая последовательность букв, не обязательно осмысленная. Сколько существует таких слов, которые может написать Вася?

s = 'ВОЛК'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('В') == 1:
                        count += 1
print(count)
'''
# Ответ: 405
# endregion Тип 8 № 23908

# region Тип 8 № 39237
'''
# Все четырёхбуквенные слова, в составе которых могут быть только буквы А, В, Т, О, Р, записаны в алфавитном порядке и пронумерованы, начиная с 1. 
# Ниже приведено начало списка:
# 1.АААА
# 2.АААВ
# 3.АААО
# 4.АААР
# 5.АААТ
# 6.ААВА
#
# Под каким номером в списке идёт слово ТАРА?

s = 'АВОРТ'
M = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                M.append(temp)

for i in range(0, len(M)):
    if M[i] == 'ТАРА':
        print(i+1)
        break
'''
# Ответ: 516
# endregion Тип 8 № 39237

# region Тип 8 № 3194
# Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке.
# Вот начало списка
# 1.ААААА
# 2.ААААО
# 3.ААААУ
# 4.АААОА
#
# Запишите слово, которое стоит на 101-м месте от начала списка.

# Вариант 1
"""
s = 'АОУ'
count = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if count == 101:
                        print(count, temp)
                    count += 1
"""


# Вариант 2
"""
s = 'АОУ'
M = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M.append(temp)

print(M[101-1])
"""
# Ответ: О А У А О
# endregion Тип 8 № 3194

# region Тип 8 № 14771
# Все трёхбуквенные слова, составленные из букв П, А, Р, У, С, записаны в алфавитном порядке и пронумерованы, начиная с 1.
# Начало списка выглядит так:
#
# 1.ААА
# 2.ААП
# 3.ААР
# 4.ААС
# 5.ААУ
# 6.АПА
#
# Под каким номером в списке идёт первое слово, которое начинается с буквы Р?

# Вариант 1
'''
s = 'АПРСУ'
i = 1
for a in s:
    for b in s:
        for c in s:
            temp = a + b + c
            if a == 'Р':
                print(i, temp)
                exit()
            i += 1
'''

# Вариант 2
'''
s = 'АПРСУ'
i = 0
for a in s:
    for b in s:
        for c in s:
            i += 1
            temp = a + b + c
            if a == 'Р':
                print(i, temp)
                exit()
'''


# Вариант 3
'''
s = 'АПРСУ'
M = ['0']
for a in s:
    for b in s:
        for c in s:
            temp = a + b + c
            M.append(temp)

for i in range(0, len(M)):
    if M[i] == 'РАА':
        print(i)
'''

# Ответ: 51 РАА

# endregion Тип 8 № 14771

# region Тип 8 № 18491
'''
# Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А.
# Каждую букву нужно использовать ровно 1 раз, при этом Ь нельзя ставить первым и нельзя ставить после гласной.
# Сколько различных кодов может составить Ольга?

s = 'ОЛЬГА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if a != 'Ь' and 'ОЬ' not in temp and 'АЬ' not in temp:
                        M = [i for i in temp]
                        A = set(M)  # переводим список М в множество, чтобы убрать повторяющиеся элементы
                        if len(A) == 5:
                            count += 1
                            print(temp, A)
print(count)
'''
# Ответ: 48

# endregion Тип 8 № 18491


# КЕГЭ задачи из сборника Полякова

# region (№ 5708) (Л. Малинов)
# Ваня составляет 6-буквенные слова из букв В, И, Д, Е, О.
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
# endregion (№ 5708) (Л. Малинов)

# region (№ 5010)
# Вася составляет слова из букв слова ПРЕПАРАТ.
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

# endregion (№ 5010)


# region Тип 8 Статград

# Определите количество пятизначных чисел, записанных в восьмеричной системе счисления,
# в записи которых только одна цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6
'''
counter = 0
nums = '01234567'
X = list(map(str, "16 61 36 63 56 65 76 67".split()))
for a in '1234567':
    for b in nums:
        for c in nums:
            for d in nums:
                for e in nums:
                    l = a + b + c + d + e
                    flag = True
                    if l.count('6') == 1:
                        for x in X:
                            if x in l:
                                flag = False
                        if flag == True:
                            print(l)
                            counter += 1
print(counter)

# Ответ: 2961
'''
# endregion Тип 8 Статград

# region Тип 8 № 9302

# Сколько слов длины 4, начинающихся с согласной буквы и заканчивающихся гласной буквой, можно составить из букв М, Е, Т, Р, О?
# Каждая буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными словами русского языка.

# Вариант 1
'''
import itertools
sogl = 'МТР'
glas = 'ЕО'
count = 0
s = itertools.product('МЕТРО', repeat=4)
for temp in s:
    if temp[0] in sogl and temp[3] in glas:
        count += 1
print(count)
'''

# Вариант 2
'''
import itertools
count = 0
s = itertools.product('МЕТРО', repeat=4)
for temp in s:
    if temp[0] in 'МТР' and temp[3] in 'ЕО':
        count += 1
print(count)
'''

# Вариант 3
'''
s = 'МЕТРО'
sogl = 'МТР'
glas = 'ЕО'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                if a in sogl and d in glas:
                    count += 1
print(count)
'''

# Вариант 4
'''
s = 'МЕТРО'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                if a in 'МТР' and d in 'ЕО':
                    count += 1
print(count)
'''
# Ответ: 150

# endregion Тип 8 № 9302

# region Тип 8 № 27295

# Света составляет 5-буквенные коды из букв С, В, Е, Т, А.
# Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные.
# Сколько различных кодов может составить Света?

# Вариант 1
'''
import itertools
s = itertools.permutations('СВЕТА', r=5)
count = 0
for temp in s:
    temp = ''.join(temp)
    if 'ЕА' not in temp and 'АЕ' not in temp:
        count += 1
print(count)
'''

# Вариант 1
'''
s = 'СВЕТА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M = [a, b, c, d, e]
                    if len(set(M)) == len(M):
                        if 'ЕА' not in temp and 'АЕ' not in temp:
                            count += 1
print(count)
'''
# Ответ: 72

# endregion Тип 8 № 27295