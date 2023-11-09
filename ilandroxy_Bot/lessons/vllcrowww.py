
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
d1 = True
d2 = False
print(type(d1))  # <class 'bool'>
'''


# Тип 2 №27228
# Логическая функция F задаётся выражением (¬x ∨ y ∨ z) ≡ (¬y ∧ z ∧ w).
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x) or y or z) == ((not y) and z and w)
                if F == True:
                    print(x, y, z, w, int(F))
'''


# Тип 2 №25832
# Миша заполнял таблицу истинности функции (x ∧ ¬y) ∨ (x ≡ z) ∨ ¬w
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not y)) or (x == z) or (not w)
                if F == False:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №18483
# Логическая функция F задаётся выражением ((y → w) ≡ (x → ¬z)) ∧ (x ∨ w).
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= w) == (x <= (not z))) and (x or w)
                print(x, y, z, w, int(F))
'''



# Тип 15 №38949
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
#
# Так, например, 14 & 5 = 11102 & 01012 = 01002 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
#
# x & 85 = 0 → (x & 54 ≠ 0 → x & А ≠ 0)
#
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном
# целом значении переменной x)?
'''
# Вариант 2
def F(x, A):
    return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))


for A in range(0, 10000):
    flag = True
    for x in range(0, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break


# Вариант 2
def F(x, A):
    return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))

for A in range(0, 10000):
    if all(F(x, A) for x in range(0, 10000)):
        print(A)
        break

# Вариант 3
for A in range(0, 10000):
    if all(((x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))) for x in range(0, 10000)):
        print(A)
        break

# Вариант 4
R = []
for A in range(0, 1000):
    if all(((x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))) for x in range(0, 10000)):
        R.append(A)
print(min(R))

# Вариант 5
print(min([A for A in range(0, 1000) if all(((x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))) for x in range(0, 10000))]))

# Вариант 6
def F(x, A):
    return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))

print(min([A for A in range(0, 1000) if all(F(x, A) for x in range(0, 10000))]))
'''
# Ответ: 34

# endregion Урок: ******************************************************************


# Марго = []
# КЕГЭ  = []
# на следующем уроке:
