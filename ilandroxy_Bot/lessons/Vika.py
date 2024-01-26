# region Домашка: ******************************************************************

# Напишите программу, которая принимает два целых числа a и b и выводит все целые числа от a до b включительно
# в порядке возрастания, если a < b, или в порядке убывания в противном случае.
'''
a = int(input())
b = int(input())
for i in range(a, b+1):
    print(i)
'''


# Напишите программу, которая принимает два натуральных числа a и b (a≤b)
# и выводит все целые числа от a до b включительно, удовлетворяющие хотя бы одному из условий:
#
# число кратно 20
# число кратно 7 и 14 одновременно
# число оканчивается на 9.

# 125 // 10 = 12
# 125 % 10 = 5
'''
a = int(input())
b = int(input())
for i in range(a, b+1):
    if i % 20 == 0 or (i % 7 == 0 and i % 14 == 0) or i % 10 == 9:
        print(i)
'''


# Напишите программу, которая принимает натуральное число m и вычисляет произведение всех его делителей.
'''
m = int(input())  # 24 {1, 2, 3, 4, 6, 8, 12, 24}
r = 1
for j in range(1, m+1):
    if m % j == 0:
        r = r * j
print(r)
'''


# Тип 2 №39231
# Логическая функция F задаётся выражением (¬z ≡ y) → ((w ∧ ¬x) ≡ (y ∧ x)).
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not z) == y) <= ((w and (not x)) == (y and x))
                if F == 0:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №16377
# Логическая функция F задаётся выражением ((x → y) ≡ (y → z)) ∧ (y ∨ w).
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) == (y <= z)) and (y or w)
                if F == 1:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №15970
# Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z ) ∨ w.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not y)) or (y == z ) or w
                if F == 0:
                    print(x, y, z, w, int(F))
'''

# Тип 2 №33081
# Логическая функция F задаётся выражением (x ∨ ¬z) ∧ (x ≡ ¬w) ∧ (x → y)
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or (not z)) and (x == (not w)) and (x <= y)
                if F == 1:
                    print(x, y, z, w, int(F))
'''
# Тип 2 №15939
# Логическая функция F задаётся выражением (z ∧ y) ∨ ((x → z ) ≡ (y → w))

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # F = (z and y) or ((x <= z) == (y <= w))
                F = ((not x) == z) <= (y == (w or x))
                # F == 1:
                if F == 0:
                    print(x, y, z, w, int(F))

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# endregion Урок: ******************************************************************

# Вика = []
# КЕГЭ  = []
# на следующем уроке:
