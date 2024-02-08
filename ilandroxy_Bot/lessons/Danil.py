# region Домашка: ******************************************************************

# Дано натуральное число n. Напишите программу, которая определяет его максимальную и минимальную цифры.
'''
n = int(input())  # 534253465
maxi = -9999999
mini = 9999999
while n > 0:
    x = n % 10
    if maxi < x:
        maxi = x
    mini = min(mini, x)
    n //= 10
print(maxi)
print(mini)
'''

# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
'''
n = int(input())  # 324352
summa = 0
kol = 0
pr = 1
first = 0

last = n % 10
while n > 0:
    x = n % 10
    summa += x
    kol += 1
    pr *= x
    first = x
    n //= 10
print(summa)
print(kol)
print(pr)
print(summa / kol)
print(first)
print(first + last)
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # F = (z and y) or ((x <= z) == (y <= w))  # Тип 2 №15939 (z ∧ y) ∨ ((x → z ) ≡ (y → w))
                F = ((z <= w) or (y == w)) and ((x or z) == y)  # Тип 2 #29109 ((z → w) ∨ (y ≡ w))∧((x∨z) ≡ y)
                if F == True:
                    print(x, y, z, w)


'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (w <= (y == z)) and (y == (z <= x))  # Тип 2 №48450 (w → (y ≡ z)) ∧ (y ≡ (z → x))
                print(x, y, z, w, int(F))
'''
# endregion Урок: ******************************************************************

# Данил = []
# КЕГЭ  = []
# на следующем уроке:
