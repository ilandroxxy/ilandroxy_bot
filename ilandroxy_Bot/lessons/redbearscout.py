# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 2 №29187
# Логическая функция F задаётся выражением (w → y) ∧ (¬y ≡ x) ∧ (x ∨ z).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w <= y) and ((not y) == x) and (x or z)
                if F:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №55798
# Логическая функция F задаётся выражением:
# (x∧¬y)∨(y≡z)∨¬w.
# На рисунке приведён фрагмент таблицы истинности функции F,
# содержащий неповторяющиеся наборы аргументов.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not y)) or (y == z) or (not w)
                if not F:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №16805
# Логическая функция F задаётся выражением (¬x ≡ z) → (y ≡ (w ∨ x))
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x) == z) <= (y == (w or x))
                if not F:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №18430
# Миша заполнял таблицу истинности функции (x ∧ y) ∨ (y ≡ z) ∨ w
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and y) or (y == z) or w
                if not F:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №33472
# Логическая функция F задаётся выражением (w → x) ∧ ((y → z) ≡ (x → y))
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w <= x) and ((y <= z) == (x <= y))
                if F:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №59707
# Миша заполнял таблицу истинности логической функции F:
# (x ∨¬ y) ∧ ¬(y ≡ z) ∧ ¬w
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or (not y)) and (not(y == z)) and (not w)
                if F:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №33174
# Логическая функция F задаётся выражением ((x → y) ≡ (w → x)) ∧ (z → w)
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) == (w <= x)) and (z <= w)
                if F:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №15912
# Логическая функция F задаётся выражением ((x → y ) ≡ (z → w)) ∨ (x ∧ w)

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y ) == (z <= w)) or (x and w)
                if not F:
                    print(x, y, z, w, int(F))

# endregion Урок: ******************************************************************


# Тимур = []
# КЕГЭ  = []
# на следующем уроке:
