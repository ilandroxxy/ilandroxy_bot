
# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 2 №38534
# Миша заполнял таблицу истинности логической функции F
# ¬(y→(x≡w))∧(z→x)
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(y <= (x == w))) and (z <= x)
                if F:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №35460  ¬((x ∨ y) → (z ∧ w)) ∧ (x → w).
# Тип 2 №27371  ((x ∧ ¬y) → (¬z ∨ ¬w))∧((w→x) ∨ y)
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # F = (not((x or y) <= (z and w))) and (x <= w)  # 35460
                F = ((x and (not y)) <= ((not z) or (not w)) and (w <= x) or y)  # 27371
                if not F:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №18483
# Логическая функция F задаётся выражением ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w).

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= w) == (x <= (not z))) and (x or w)
                print(x, y, z, w, int(F))
# endregion Урок: ******************************************************************


# todo: Лера = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
