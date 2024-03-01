# region Домашка: ******************************************************************

# Дано натуральное число n. Напишите программу, которая определяет его максимальную и минимальную цифры.
'''
n = int(input())
maxi = 0
mini = 9999999
while n > 0:
    x = n % 10
    maxi = max(maxi, x)
    mini = min(mini, x)
    n //= 10
print(maxi, mini)
'''

# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
'''
n = int(input())
first = 0
summa = 0
cnt = 0
prod = 1
last = 0
while n > 0:
    x = n % 10

    first = x
    summa += x
    cnt += 1
    prod *= x
    if last == 0:
        last = x

    n //= 10
print(summa)
print(cnt)
print(prod)
print(summa / cnt)
print(first)
print(first + last)
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 2 №18808 Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z) ∨ w.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not y)) or (y == z) or w
                if not F:
                    print(x, y, z, w)
'''


# КЕГЭ  № 11606 (Уровень: Базовый)
# (С. Чайкин) Логическая функция F задаётся выражением (x→y) ∧ (¬y→z) ∧ w
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x <= y) and ((not y) <= z) and w
                if F:
                    print(x, y, z, w)
'''

# Тип 2 №36857
# Логическая функция F задаётся выражением ((¬x ∨ z) ≡ (y ∧ ¬w)) → (z ∧ y)
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((not x) or z) == (y and (not w))) <= (z and y)
                if not F:
                    print(x, y, z, w)
'''

# Решу ЕГЭ № 18483
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
# КЕГЭ № 9149 Джобс 06.06.2023 (Уровень: Базовый)
# Миша заполнял таблицу истинности логической функции F = ((x → y) ∨ (z ≡ x)) ∧ (w → z)

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) or (z == x)) and (w <= z)
                print(x, y, z, w, int(F))

# endregion Урок: **********************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Михаил = []
# КЕГЭ  = []
# на следующем уроке:
