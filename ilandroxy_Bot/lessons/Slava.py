'''
#Задание 29650
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

'''
#Задание 15097
#Логическая функция F задаётся выражением (x ≡ z ) ∨ (x → (y ∧ z))
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x == z) or (x <= (y and z))
            if F == False:
                print(x, y, z, F)
'''

'''
#Задание 40718
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


# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1.Строится троичная запись числа N.
# 2.В конец записи (справа) дописывается остаток от деления числа N на 3.
# 3.Результат переводится из троичной системы в десятичную и выводится на экран.

# Пример. Дано число N=11. Алгоритм работает следующим образом:
# 1.Троичная запись числа N: 102.
# 2.Остаток от деления 11на 3 равен 2, новая запись 1022.
# 3.На экран выводится число 35.

# Какое наименьшее трёхзначное число может появиться на экране в результате работы автомата?

A = []
for n in range(1, 10000):
    x = n

    M = []
    while n > 0:
        M.append(n % 3)  # 1. Строится троичная запись числа N.
        n //= 3
    M.reverse()

    M.append(x % 3)   # 2. В конец записи (справа) дописывается остаток от деления числа N на 3.

    res = 0
    M.reverse()
    for i in range(0, len(M)):  # 3. Результат переводится из троичной системы в десятичную и выводится на экран.
        res += M[i] * 3 ** i

    if 100 <= res < 1000: # Какое наименьшее трёхзначное число может появиться на экране в результате работы автомата?
        A.append(res)
print(min(A))


# todo: на следующем уроке разбираем 5 номер, тип 2 - с системами счисления





