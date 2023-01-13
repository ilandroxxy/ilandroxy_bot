
# region Домашка:  ************************************************************

# №234
'''
def F(n):
    if n > 2:
        return F(n - 1) + F(n - 2) + F(n - 3)
    else:
        return n
print(F(6))
'''

# №237
'''
def F(n):
    print("*")
    if n > 0:
        G(n - 1)
def G(n):
    print("*")
    if n > 1:
        F(n - 2)
print(F(13))
'''

# №235
'''
def F(n):
    print('1', end='')
    if n > 0:
        print('1', end='')
        G(n - 1)
def G(n):
    print('1', end='')
    if n > 1:
        print('1', end='')
        F(n - 2)
F(12)
'''

# Тип 23 № 18450
'''
# Исполнитель преобразует число на экране.
#
# У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
#
# Сколько существует программ, для которых при исходном числе 2 результатом является число 29
# и при этом траектория вычислений содержит число 14?

def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b)

print(F(2, 14) * F(14, 29))
'''
# Ответ: 26


# Тип 23 № 14783
'''
# У исполнителя есть две команды, которым присвоены номера:
#
# 1. Прибавить 1
# 2. Умножить на 2

# Сколько существует программ, которые преобразуют исходное число 1 в число 40
# и при этом траектория вычислений содержит числа 12 и 25?

def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*2, b)

print(F(1, 12) * F(12, 25) * F(25, 40))
'''
# Ответ: 40

# endregion Домашка: ************************************************************


# region Урок:  ************************************************************

# Тип 25 № 28122 i
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [489_421; 489_440], числа, имеющие ровно четыре различных натуральных делителя.
# Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.

# Вариант 1
'''
for x in range(489_421, 489_440+1):
    M = []
    for j in range(1, x+1):
        if x % j == 0:
            M.append(j)
    if len(M) == 4:
        print(x, *M)
'''

# Вариант 2
'''
def D(x):
    M = set()
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            M.add(j)
            M.add(x//j)
    return sorted(M)

for x in range(489_421, 489_440+1):
    M = D(x)
    if len(M) == 4:
        print(*M)
'''

# Ответ:
# 1 19 25759 489421
# 1 2 244711 489422
# 1 13 37649 489437


# Тип 25 № 27854
'''
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [110203; 110245],
# числа, имеющие ровно четыре различных чётных натуральных делителя (при этом количество нечётных делителей может быть любым).
# Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.

def D(x):
    M = set()
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            if j % 2 == 0:
                M.add(j)
            if (x//j) % 2 == 0:
                M.add(x//j)
    return sorted(M)

for x in range(110203, 110245+1):
    M = D(x)
    if len(M) == 4:
        print(*M)
'''
# Ответ:
# 2 4 55102 110204
# 2 14 15746 110222
# 2 6 36742 110226
# 2 22 10022 110242



# Тип 25 № 37130
'''
# Напишите программу, которая перебирает целые числа, большие 600_000,
# в порядке возрастания и ищет среди них такие, среди делителей которых есть хотя бы одно число,
# оканчивающееся на 7, но не равное 7 и самому числу. Необходимо вывести первые 5 таких чисел, и наименьший делитель,
# оканчивающийся на 7, не равный 7 и самому числу.
#
# Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала выводится
# само число, затем — наименьший делитель, оканчивающийся на 7, не равный 7 и самому числу.
# Строки выводятся в порядке возрастания найденных чисел.

def D(x):
    M = set()
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0 and j != 7:
            if j % 10 == 7:
                M.add(j)
            if (x // j) % 10 == 7:
                M.add(x//j)
    return sorted(M)

k = 0
for x in range(600_000+1, 600_000_000):
    M = D(x)
    if len(M) >= 1:
        print(x, M[0])
        k += 1
        if k == 5:
            break
'''
# 600001 437
# 600002 47
# 600003 1227
# 600005 217
# 600012 16667


# Тип 25 № 27850
'''
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245_690; 245_756] простые числа.
# Выведите на экран все найденные простые числа в порядке возрастания, слева от каждого числа выведите его порядковый номер в последовательности.
# Каждая пара чисел должна быть выведена в отдельной строке.

def D(x):
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            return False
    return True

k = 1
for x in range(245_690, 245_756+1):
    if D(x) == True:
        print(k, x)
    k += 1
'''
# Ответ:
# 22 245711
# 30 245719
# 34 245723
# 52 245741
# 58 245747
# 64 245753




# endregion Урок: ************************************************************


# todo: Мария = [2, 5, 8, 12, 14+, 16+, 23]
# на прошлом уроке: Повторили 23 номер и начали разбирать простейшие 25 номера.
# на следующем уроке: Продолжаем 25.2