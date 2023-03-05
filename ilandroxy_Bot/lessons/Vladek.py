
# region Домашка: ******************************************************************




# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************

# № 2407 (Уровень: Гроб)
# (PRO100 ЕГЭ) Найдите все натуральные числа, принадлежащие отрезку [1 000 000 000 ; 2 000 000 000],
# у которых больше 100 различных нечётных делителей, количество чётных делителей может быть любым.
# И при этом число должно делиться на каждое из чисел: 7, 13, 17, 23, 29, но не делиться ни на 3, ни на 5.
# В ответе запишите количество подходящих чисел.
'''
def F(x):
    dl = set()  # тип данных множество (1. работает быстрее списков 2. не может содержать двух копий значений)
    for j in range(1, int(x**0.5)+1):  # x**0.5 - квадратного корня
        if x % j == 0:
            if j % 2 != 0:
                dl.add(j)
            if (x // j) % 2 != 0:
                dl.add(x // j)
    return sorted(dl)


count = 0
for x in range(1_000_000_000, 2_000_000_000):
    if x % 7 == 0 and x % 13 == 0 and x % 17 == 0 and x % 23 == 0 and x % 29 == 0 and x % 3 != 0 and x % 5 != 0:
        dl = F(x)
        if len(dl) > 100:
            print(x)
            count += 1
print(count)
'''
# Ответ: 73
'''
M = [1, 2, 3, 4, 5]

# 1. Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(0, len(M)-1):
    print(f'{M[i]}{M[i+1]}', end=' ')
print('\n')

# 2. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(f'{M[i]}{M[j]}', end=' ')
    print()
  '''

# Шаблон первого типа:
M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    pass
print(count, maxi)


# Шаблон второго типа:
M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        pass
print(count, maxi)



# Тип 17 № 39246
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём парой
# два идущих подряд элемента последовательности. Определите количество пар, в которых хотя бы один из двух элементов
# делится на 5, а их сумма делится на 7. В ответе запишите два числа: сначала количество найденных пар, а затем —
# максимальную сумму элементов таких пар.
'''
M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    if M[i] % 5 == 0 or M[i+1] % 5 == 0:
        if (M[i] + M[i+1]) % 7 == 0:
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 308 18893


# Тип 17 № 47221
# В файле содержится последовательность целых чисел. Элементы последовательности могут принимать
# целые значения от −10000 до 10000 включительно. Определите количество пар последовательности, в которых только
# одно число оканчивается на 3, а сумма квадратов элементов пары не меньше квадрата максимального элемента
# последовательности, оканчивающегося на 3. В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную из сумм квадратов элементов таких пар. В данной задаче под парой подразумевается два идущих
# подряд элемента последовательности.
'''
# квадрата максимального элемента последовательности, оканчивающегося на 3
A = [int(i) for i in open('17.txt') if abs(int(i)) % 10 == 3]
square_max = max(A) ** 2

M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (abs(M[i]) % 10 == 3 and abs(M[i+1]) % 10 != 3) or (abs(M[i]) % 10 != 3 and abs(M[i+1]) % 10 == 3):
        if (M[i] ** 2 + M[i+1] ** 2) >= square_max:
            count += 1
            maxi = max(maxi, M[i] ** 2 + M[i+1] ** 2)
print(count, maxi)
'''
# Ответ: 180 190360573


#
# № 6354 (Уровень: Средний)
# (П. Волгин) В файле содержится последовательность целых чисел. Элементы последовательности могут принимать значения
# от -10 000 до 10 000 включительно. Определите количество пар элементов последовательности, в которой хотя бы одно
# число отрицательное, и хотя бы одно число четное, а куб суммы элементов пары больше максимального элемента,
# кратного 4, но не оканчивающегося на 2, 4, 6. В ответе запишите сначала количество найденных пар, а затем куб
# минимальной суммы элементов таких пар.
#
# Файлы к заданию:17.txt
'''
A = [int(i) for i in open('17.txt') if abs(int(i)) % 4 == 0 and abs(int(i)) % 10 != 2 and abs(int(i)) % 10 != 4 and abs(int(i)) % 10 != 6]
square_max = max(A)

M = [int(i) for i in open('17.txt')]
count = 0
mini = 99999  # так получается, что найденные нами суммы - больше 0. 
# Поэтому нельзя брать mini = 0, mini всегда должно быть очень большим число, а maxi - всегда очень маленьким
for i in range(0, len(M) - 1):
    if (M[i] < 0 or M[i+1] < 0) and (M[i] % 2 == 0 or M[i+1] % 2 == 0):
        print(M[i], M[i+1])
        if (M[i] + M[i+1]) ** 3 > square_max:
            count += 1
            mini = min(mini, M[i] + M[i+1])
print(count, mini**3)
'''
# 80 970299


# № 6353 (Уровень: Средний)
# (П. Волгин) В файле содержится последовательность целых чисел. Элементы последовательности могут принимать значения от -10 000 до 10 000 включительно.
# Определите количество троек элементов последовательности, в которой хотя бы одно число делится 118 и хотя бы одно число оканчивается 118,
# а сумма элементов тройки больше максимального элемента, кратного 118, но не оканчивающего на 8.
# В ответе запишите сначала количество найденных троек, а затем квадрат максимальной суммы элементов таких троек.
'''
A = [int(i) for i in open('17.txt') if abs(int(i)) % 10 != 8 and abs(int(i)) % 118 == 0]
maxa = max(A)

M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M) - 2):
    if (M[i] % 118 == 0 or M[i + 1] % 118 == 0 or M[i + 2] % 118 == 0) and (
            M[i] % 1000 == 118 or M[i + 1] % 1000 == 118 or M[i + 2] % 1000 == 118):
        if M[i] + M[i + 1] + M[i + 2] > maxa:
            count += 1
            maxi = max(maxi, M[i] + M[i + 1] + M[i + 2])

print(count, maxi ** 2)
'''
# 22 396209025

# endregion Урок: ******************************************************************


# todo: Владек = [2, 3, 5, 8, 12, 14+, 15, 16, 17, 19-21, 22, 23, 25.2]
# на прошлом уроке: Разобрали 17 номера от базовой теории (повторение), до задачи уровня сложности "Гроб".
# на следующем уроке: