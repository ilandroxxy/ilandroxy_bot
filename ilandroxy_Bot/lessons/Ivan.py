
# region Домашка

# endregion Домашка


# region Урок

# Тип 8 № 18558
'''
# Иван составляет 5-буквенные коды из букв И, В, А, Н.
# Буквы в коде могут повторяться, использовать все буквы не обязательно, но букву И нужно использовать хотя бы один раз.
# Сколько различных кодов может составить Иван?

s = 'ИВАН'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if 'И' in temp:
                        count += 1
print(count)
'''
# Ответ: 781


# Тип 8 № 26982
'''
# Сколько существует шестизначных чисел, делящихся на 5, в которых каждая цифра может
# встречаться только один раз, при этом никакие две чётные и две нечётные цифры не стоят рядом.

s = '0123456789'
s1 = '02468'
s2 = '13579'
count = 0
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    for f in s2:
                        temp = a + b + c + d + e + f
                        if a != '0':
                            if int(temp) % 5 == 0:
                                A = [i for i in temp]
                                B = set(A)
                                if len(B) == 6:
                                    print(temp)
                                    count += 1
for a in s2:
    for b in s1:
        for c in s2:
            for d in s1:
                for e in s2:
                    for f in s1:
                        temp = a + b + c + d + e + f
                        if a != '0':
                            if int(temp) % 5 == 0:
                                A = [i for i in temp]
                                B = set(A)
                                if len(B) == 6:
                                    print(temp)
                                    count += 1
print(count)
'''

# endregion Урок


# todo: Иван = [2, 8, 13, 14, 5, 16], на следующем уроке: 12 номер











