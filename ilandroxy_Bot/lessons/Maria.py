
# region Домашка:  ************************************************************


# endregion Домашка: ************************************************************


# region Урок:  ************************************************************

# № 6904 (Уровень: Базовый)
# (Д. Статный) Логическая функция F задаётся выражением
# ¬(((x→y∧w)∧(z→x∨y))≡w).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
# содержащий неповторяющиеся строки. Определите, какой столбец в таблице каждой переменной в выражении.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not (((x <= (y and w)) and (z <= (x or y))) == w))
                if F == True:
                    print(x, y, z, w, F)
'''


#
# № 6903 (Уровень: Базовый)
# (Д. Статный) На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 00,
# а затем два левых разряда заменяются на 11;
# б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 11,
# а затем два левых разряда заменяются на 10.
# 3. Пункт 2 повторяется ещё раз к записи, полученной после второго пункта.
#
# Полученная таким образом запись является двоичной записью искомого числа R.
# Например, для исходного числа 6_10 = 110_2 результатом является число 96_10 = 11000002,
# а для исходного числа 410 = 1002 результатом является число 7910 = 10011112.

# Найдите максимальное число R, которое получается при обработке N, меньших 100.
# В ответе укажите R.

# s = '372.163dfg47,8216f4'
# # summ = s.count('1') + s.count('2') * 2 + s.count('3') * 3 + .... корчое долго
# # summ = sum([int(i) for i in s])  # ValueError: invalid literal for int() with base 10: '.'
# summ = sum([int(i) for i in s if i.isdigit()])  # универсальный способ взятия сумму цифр строки
# print(summ)
'''
R = []
for n in range(1, 100):
    s = bin(n)[2:]

    for i in range(2):
        summ = s.count('1')
        #  summ = sum([int(i) for i in s if i.isdigit()])

        if summ % 2 == 0:
            s = '11' + s[2:] + '00'
        else:
            s = '10' + s[2:] + '11'

    r = int(s, 2)  # перевели строку из двоичной с десятичную

    print(n, r)

    R.append(r)
print(max(R))
'''
# Показать ответ: 1584

#
# № 6901 (Уровень: Средний)
# (Д. Статный) Все пятибуквенные слова, в составе которых могут быть только буквы слова БАРАШ,
# записаны в алфавитном порядке и пронумерованы начиная с 1.

# Ниже приведено начало списка.
# 1. ААААА
# 2. ААААБ
# 3. ААААР
# 4. ААААШ
# 5. АААБА

# Под каким последним номером идёт слово,
# в котором не более 3-х согласных
# и только одна буква повторяется дважды,
# а остальные не повторяются?
'''
s = sorted('БАРШ')
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(set(slovo)) == 4:  # только одна буква повторяется дважды
                        if slovo.count('Б') + slovo.count('Р') + slovo.count('Ш') <= 3:  # в котором не более 3-х согласных 
                            print(k, slovo)
                    k += 1
'''
# Показать ответ: 913 ШРБАА


# endregion Урок: ************************************************************


# todo: Мария = [1, 2, 3, 4, 5, 6, 7.1, 8, 9.1, 10, 12, 13, 14+, 16+, 17, 18, 19-21, 22, 23, 24+, 25.1]
# на прошлом уроке:
# на следующем уроке:
