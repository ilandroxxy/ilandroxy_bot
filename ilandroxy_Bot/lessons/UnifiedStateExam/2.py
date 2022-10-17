
# Теория: Операции Математической логики
# отрицание (инверсия): ¬y  <---->  (not(y))
# логическое умножение (конъюнкция):  x ∧ y   <---->  x and y
# логическое сложение (дизъюнкция): x ∨ y  <---->  x or y
# импликация: x → y  <---->  x <= y
# тождество: x ≡ y  <---->  x == y

# region Тип 2 № 16878
'''
# Логическая функция F задаётся выражением (x≡¬y)→(z≡(y∨w))
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not(y))) <= (z == (y or w))
                if F == False:
                    print(x, y, z, w, F)
'''
#  Ответ: zwyx
# endregion Тип 2 № 16878

# region Тип 2 № 27287
'''
# Логическая функция F задаётся выражением ((¬z ∨ w) ∧ (¬x ≡ y))→(x∧z).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((not(z)) or w) and ((not(x)) == y)) <= (x and z)
                if not(F):
                    print(x, y, z, w, F)
'''
# Ответ: wzyx
# endregion Тип 2 № 27287

# region Тип 2 № 19051
# Миша заполнял таблицу истинности функции (x ∧ ¬y) ∨ (x ≡ z) ∨ ¬w, но успел
# заполнить лишь фрагмент из трёх различных её строк, даже не указав,
# какому столбцу таблицы соответствует каждая из переменных w, x, y, z.
"""
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not(y))) or (x == z) or (not(w))
                if F == False:
                    print(x, y, z, w, F)
"""
# Ответ: xwzy
# endregion Тип 2 № 19051

# region Тип 2 № 15124
# Логическая функция F задаётся выражением (x ≡ y ) ∨ ((y ∨ z) → x).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z.
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x == y) or ((y or z) <= x)
            if F == False:
                print(x, y, z, F)
# Ответ: xzy
# endregion Тип 2 № 15124

# region Тип 2 № 29650
'''
#Логическая функция F задаётся выражением (w ∨ ¬x) ∧ (w ≡ ¬y) ∧ (w → z)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w or (not(x))) and (w == (not(y))) and (w <= z)
                if F == True:
                    print(x, y, z, w, F)
'''
# endregion Тип № 29650

# region Тип 2 № 15097
'''
#Логическая функция F задаётся выражением (x ≡ z ) ∨ (x → (y ∧ z))
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x == z) or (x <= (y and z))
            if F == False:
                print(x, y, z, F)
'''
# endregion Тип № 15097

# region Тип 2 № 40718
'''
#Логическая функция F задаётся выражением ((x → y) ∧ (z ∨ w)) → ((x ≡ w) ∨ (y ∧ ¬z))
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) and (z or w)) <= ((x == w) or (y and (not(z))))
                if F == False:
                    print(x, y, z, w, F)
'''
# endregion Тип № 40718