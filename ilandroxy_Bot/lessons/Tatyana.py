# region Домашка:  **************************************************

'''
# Цифра 1
s = str(input())
M = [int(i) for i in s]
print(sum(M))
'''

'''
# В столбик 2
s = str(input())
x = s[::-1]
for i in x:
    print(i)
'''

# тип 5 №7454
'''
for i in range(1000, 10000):
    M = [int(i) for i in str(i)]
    a = M[0] + M[1]
    b = M[2] + M[3]
    r = str(max(a, b)) + str(min(a, b))
    if r == '1311':
        print(i)
        break
'''

'''
# №14767
for i in range(1000, 10000):
    s = str(i)
    M = [int(i) for i in s]
    a = M[0] + M[1]
    b = M[1] + M[2]
    c = M[2] + M[3]
    x = str(a + b + c - max(a, b, c) - min(a, b, c))
    y = str(max(a, b, c))
    r = x + y
    if r == '613':
        print(i)
        break
'''


'''
# №13617
for i in range(100, 1000):
    s = str(i)
    M = [int(i) for i in s]
    a = M[0] * M[1]
    b = M[1] * M[2]
    r = str(max(a, b)) + str(min(a, b))
    if r == '123':
        print(i)
        break
'''

# endregion Домашка: **************************************************


# region Урок:  **************************************************

# Тип 8 № 3693
'''
# Все 5-буквенные слова, составленные из 5 букв А, К, Л, О, Ш, записаны в алфавитном порядке.
# Вот начало списка:
# 1. ААААА
# 2. ААААК
# 3. ААААЛ
# 4. ААААО
# 5. ААААШ
# 6. АААКА

# На каком месте от начала списка стоит слово ШКОЛА

s = 'АКЛОШ'
i = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp == 'ШКОЛА':
                        print(i, temp)
                    i += 1
'''
# Ответ: 2711


# Тип 8 № 3698
'''
# Все 6-буквенные слова, составленные из букв Б, К, Ф, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ББББББ
# 2. БББББК
# 3. БББББФ
# 4. ББББКБ

# Запишите слово, которое стоит на 345-м месте от начала списка.

s = 'БКФ'
i = 1
M = ['0']
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        M.append(temp)
                        if i == 345:
                            print(i, temp)
                        i += 1

print(M[345])
'''
# Ответ: ККБФБФ


# Тип 8 № 5055
'''
# Все 5-буквенные слова, составленные из букв В, Е, К, Н, О, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ВВВВВ
# 2. ВВВВЕ
# 3. ВВВВК
# 4. ВВВВН
# 5. ВВВВО
# 6. ВВВЕВ
#
# Под каким номером стоит первое из слов, которое начинается с буквы О?

s = 'ВЕКНО'
i = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if a == 'О':
                        print(i, temp)
                        exit()
                    i += 1
'''
# Ответ: 2501


# Тип 8 № 11306
'''
# Вася составляет 4-буквенные слова, в которых есть только буквы Б, Р, О, Н, Х, И, причём буква Х используется в каждом слове, и только 1 раз.
# Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
# Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
# Сколько существует таких слов, которые может написать Вася?

s = 'БРОНХИ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                if temp.count('Х') == 1:
                    count += 1
print(count)
'''
# Ответ 500


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
                    A = set([i for i in temp])  # в множестве set() не может лежать двух одинаковых элементов
                    if len(A) == len(temp):
                        print(temp)
                        count += 1

for a in '246':
    for b in s1:
        for c in s2:
            for d in s1:
                for e in s2:
                    temp = a + b + c + d + e
                    A = set([i for i in temp])  # в множестве set() не может лежать двух одинаковых элементов
                    if len(A) == len(temp):
                        print(temp)
                        count += 1

print(count)
'''
# Ответ: 504



# Тип 8 № 16037
'''
# Вася составляет 5-буквенные слова, в которых есть только буквы З, И, М, А,
# причём в каждом слове есть ровно одна гласная буква и она встречается ровно 1 раз.
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
                    if (temp.count('А') == 1 and temp.count('И') == 0) or (temp.count('И') == 1 and temp.count('А') == 0):
                        print(temp)
                        count += 1
print(count)
'''




# endregion Урок:  **************************************************


# todo: Татьяна = [2, 5, 14+], на следующем уроке: Разбираем 8, 12 номера