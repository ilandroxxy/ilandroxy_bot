
# region Домашка: ************************************************************

# № 8602
'''
s = sorted("АЕКНС")
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if slovo == 'СЕНЕКА':
                            print(k)
                        k += 1
'''

# № 6985
# Под каким последним номером идёт слово, в котором буквы К
# не стоят рядом с буквой С и одна буква повторяется трижды, а остальные не повторяются?
'''
s = sorted("МАРКСЛ")
R = []
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if 'КС' not in slovo and 'СК' not in slovo:
                            if len(set(slovo)) == 4 and any(slovo.count(x) == 3 for x in slovo):  # СЛРРРА
                                R.append(k)
                        k += 1
print(max(R))
'''

# Ответ: 46605



# endregion Домашка: ************************************************************


# region Урок: ************************************************************

# endregion Урок: ************************************************************


# todo: Евгений = [2.1, 8.1]
# на прошлом уроке:
# на следующем уроке: На следующем уроке добиваем 8-ой номер и прорешиваем 12-ый номер.
