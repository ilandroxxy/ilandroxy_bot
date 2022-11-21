# region Домашка:  ******************************************************************************



# endregion Домашка:  ******************************************************************************


# region Урок:  ******************************************************************************

# Однострочный комментарий

'''
1
Многострочный комментарий
2
'''

'''
for i in range(0, 20):  # [0, 20)
    if i % 2 == 0:  # если число поделилось на 2 без остатка, то оно четное
        continue  # способ прервать итерацию цикла (шаг цикла)
    if i == 15:
        break  # способ прервать цикл
    print(i)
'''

# Тип 15 № 16447
'''
# Для какого наибольшего целого неотрицательного числа A выражение
#
# (2x + 3y < 30) ∨ (x + y ≥ A)
#
# тождественно истинно при любых целых неотрицательных x и y?

for A in range(1000, 0, -1):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if (((2*x + 3*y) < 30) or (x + y >= A)) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
'''

# Правила алгебры логики на языке Python
#   ¬y   <--->  (not(y))   инверсия (отрицание)
# x ∧ y  <--->  x and y    конъюнкция (логическое умножение)
# x ∨ w  <--->  x or y     дизъюнкция (логическое сложение)
# w → z  <--->  w <= z     импликация
# x ≡ z  <--->  x == z     тождество (равны ли элементы)


# Тип 2 № 19051
'''
# Миша заполнял таблицу истинности функции (x ∧ ¬y) ∨ (x ≡ z) ∨ ¬w,
# но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав,
# какому столбцу таблицы соответствует каждая из переменных w, x, y, z.

print('x y z w F')
for x in range(2):   # [0,1]
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x and (not(y))) or (x == z) or (not(w)))
                if F == False:
                    print(x, y, z, w, F)
'''


# Тип 2 № 29650
'''
# Логическая функция F задаётся выражением (w ∨ ¬x) ∧ (w ≡ ¬y) ∧ (w → z).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):   # [0,1]
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w or (not(x))) and (w == (not(y))) and (w <= z))
                if F == True:
                    print(x, y, z, w, F)
'''

# Тип 2 № 33174
'''
# Логическая функция F задаётся выражением ((x → y) ≡ (w → x)) ∧ (z → w).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):   # [0,1]
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((x <= y) == (w <= x)) and (z <= w))
                if F == True:
                    print(x, y, z, w, F)
'''


# Тип 2 № 17366
'''
# Логическая функция F задаётся выражением ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x)).
#
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
#
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((x and w) or (w and z)) == ((z <= y) and (y <= x)) )
                if F == True:
                    print(x, y, z, w, F)
'''

# endregion Урок:  ******************************************************************************


# todo: Богдан = [], на следующем уроке: Обсуждаем дз, отвечаем на вопросы. Разбираем тему списков и строк (частично)
