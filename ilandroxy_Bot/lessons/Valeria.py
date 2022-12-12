
# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************


# Тип 25 № 28122
'''
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [489421;489440], числа,
# имеющие ровно четыре различных натуральных делителя. Для каждого найденного числа запишите эти четыре делителя в
# четыре соседних столбца на экране с новой строки. Делители в строке должны следовать в порядке возрастания.

def D(n):
    dl = set()
    for j in range(1, round(n ** 0.5) + 1):
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
            if len(dl) > 4:
                return sorted(dl)
    return sorted(dl)

for n in range(489421, 489440 + 1):
    dl = D(n)
    if len(dl) == 4:
        print(*dl)
'''
# Ответ:
# 1 19 25759 489421
# 1 2 244711 489422
# 1 13 37649 489437



# Тип 25 № 41000
'''
# Пусть M(N) — сумма двух наибольших различных натуральных делителей натурального числа N, не считая самого числа и единицы.
# Если у числа N меньше двух таких делителей, то M(N) считается равным 0.
#
# Найдите 5 наименьших натуральных чисел, превышающих 11_000_000, для которых 0 < M(N) < 10 000.
# В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.

def D(n):
    dl = set()
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
            if dl == 4:
                return sorted(dl)
    return sorted(dl)

k = 0
for n in range(11_000_000, 111_000_000):
    dl = D(n)
    if 2 <= len(dl) <= 4:
        M = dl[-2] + dl[-1]
        if 0 < M < 10000:
            print(n, M)
            k += 1
            if k == 5:
                break
'''
# Ответ:
# 8672
# 8388
# 8532
# 7042
# 7364



# Тип 25 № 37160
'''
# Найдите 5 чисел больших 500000, таких, что среди их делителей есть число,
# оканчивающееся на 8, при этом этот делитель не равен 8 и самому числу.
# В качестве ответа приведите 5 наименьших чисел, соответствующих условию.
# Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала выводится само число, затем минимальный делитель,
# оканчивающийся на 8, не равный 8 и самому числу.

def D(n):
    dl = set()
    for j in range(2, int(n**0.5)+1):
        if n % j == 0 and j != 8:
            if j % 10 == 8:  #if j % 8 == 0:
                dl.add(j)
            if (n // j) % 10 == 8:
                dl.add(n // j)
    return sorted(dl)

k = 0
for n in range(500_000, 100_000_000):
    dl = D(n)
    if len(dl) != 0:
        print(n, dl[0])
        k += 1
        if k == 5:
            break
'''
# Ответ:
# 500002 178
# 500004 18
# 500016 48
# 500018 58
# 500020 4348


# Тип 25 № 33495
'''
# Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде произведения двух натуральных
# чисел и найдём для каждого такого произведения разность сомножителей.
# Например, для числа 16 получим: 16=16*1=8*2=4*4, множество разностей содержит числа 15, 6 и 0.
# Найдите все натуральные числа, принадлежащие отрезку [2_000_000; 3_000_000],
# у которых составленное описанным способом множество разностей будет содержать не меньше трёх элементов, не превышающих 115.
# В ответе перечислите найденные числа в порядке возрастания.

def D(n):
    dl = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            if (n // j) - j <= 115:
                dl.add((n // j) - j)
                if len(dl) > 3:
                    return sorted(dl)
    return sorted(dl)

for n in range(2_000_000, 3_000_000+1):
    dl = D(n)
    if len(dl) >= 3:
        print(n, dl)
'''
# Ответ:
# 2053440
# 2098080
# 2328480
# 2638944


# Тип 25 № 45259
'''
# Среди натуральных чисел, не превышающих 10**9, найдите все числа, соответствующие маске 12345?7?8, делящиеся на число 23 без остатка.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце — соответствующие им результаты деления этих чисел на 23.
#
# Количество строк в таблице для ответа избыточно.

for x in '0123456789':
    for y in '0123456789':
        s = int(f'12345{x}7{y}8')
        if s % 23 == 0:
            print(s, s // 23)
 '''
# Ответ:
# 123450798 5367426
# 123451718 5367466
# 123453788 5367556
# 123454708 5367596
# 123456778 5367686
# 123459768 5367816


# Тип 25 № 47229
'''
# Среди натуральных чисел, не превышающих 10**10, найдите все числа, соответствующие маске 1?2139*4, делящиеся на 2023 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце — соответствующие им результаты деления этих чисел на 2023.

# Вариант 1
print(10**10)
d = {}
for x in '0123456789':
    for z in range(0, 1000):
        s = int(f'1{x}2139{z}4')
        if s % 2023 == 0:
            d[s] = s//2023

for key in sorted(d):
    print(key, d[key])

# Вариант 2
for i in range(2023, 10**10, 2023):
    if (i % 10 == 4) and (str(i)[2:6] == '2139') and (str(i)[0] == '1'):
        print(i, i//2023)
'''
# Ответ
# 162139404 80148
# 1321399324 653188
# 1421396214 702618
# 1521393104 752048


# endregion Урок: ******************************************************************




# todo: Валерия = [2, 5, 6, 8, 12, 14+, 15, 16, 23, 25], на следующем уроке:  Разбираем 15 номер на множества и отрезки
