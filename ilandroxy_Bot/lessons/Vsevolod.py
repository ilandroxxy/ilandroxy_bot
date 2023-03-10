
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 25 № 28120 i
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [201455; 201470],
# числа, имеющие ровно 4 различных натуральных делителя.
# Выведите эти четыре делителя для каждого найденного числа в порядке возрастания.

# Вариант 2 - шаблонная конструкция
'''
def F(n):
    dl = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

for n in range(201455, 201470+1):
    dl = F(n)
    if len(dl) == 4:
        print(*dl)
'''

# Вариант 1 (плохой и долгий)
'''
for n in range(201455, 201470+1):
    dl = []
    for j in range(1, n+1):
        if n % j == 0:
            dl.append(j)
    if len(dl) == 4:
        print(*dl)
'''
# Ответ:
# 1 3 67153 201459
# 1 13 15497 201461
# 1 29 6947 201463
# 1 2 100733 201466


# Тип 25 № 33770
# Найдите все натуральные числа, принадлежащие отрезку [106000000; 107000000],
# у которых ровно три различных чётных делителя.
# В ответе перечислите найденные числа в порядке возрастания.
'''
def F(n):
    dl = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            if j % 2 == 0:
                dl.add(j)
            if (n // j) % 2 == 0:
                dl.add(n // j)
            if len(dl) > 3:  # позволяет отсеить все числа, у которых 4 и выше четных делителя
                return sorted(dl)
    return sorted(dl)  # будет возвращать список делителей длинной: 0, 1, 2, 3

for n in range(106000000, 107000000+1):
    dl = F(n)
    if len(dl) == 3:
        print(n)
'''
# ОТвет:
# 106084178
# 106492418
# 106784498
# 106842962


# Тип 25 № 27422
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457; 174505], числа,
# имеющие ровно два различных натуральных делителя, не считая единицы и самого числа.
# Для каждого найденного числа запишите эти два делителя в два соседних столбца на экране
# с новой строки в порядке возрастания произведения этих двух делителей.
# Делители в строке также должны следовать в порядке возрастания.
'''
def F(n):
    dl = set()
    for j in range(2, int(n**0.5)+1):  # не считая единицы и самого числа.
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

for n in range(174457, 174505+1):
    dl = F(n)
    if len(dl) == 2:
        print(*dl)
'''
# Ответ:
# 3 58153
# 7 24923
# 59 2957
# 13 13421
# 149 1171
# 5 34897
# 211 827
# 2 87251


# Тип 25 № 27850 i
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245690; 245756] простые числа.
# Выведите на экран все найденные простые числа в порядке возрастания,
# слева от каждого числа выведите его порядковый номер в последовательности.
# Каждая пара чисел должна быть выведена в отдельной строке.
'''
def F(n):
    dl = set()
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

for n in range(245690, 245756+1):
    dl = F(n)
    if len(dl) == 0:
        print(n)
'''
# Ответ:
# 245711
# 245719
# 245723
# 245741
# 245747
# 245753


# Тип 25 № 33197
# Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде
# произведения двух натуральных чисел и найдём для каждого такого произведения разность сомножителей.
# Найдите все натуральные числа, принадлежащие отрезку [1000000; 2000000], у которых составленное описанным способом
# множество разностей будет содержать не меньше трёх элементов, не превышающих 100. В ответе перечислите найденные
# числа в порядке возрастания.
'''
def F(n):
    dl = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0 and ((n // j) - j) <= 100:
            dl.add((n // j) - j)
            if len(dl) >= 3:
                return sorted(dl)
    return sorted(dl)

for n in range(1000000, 2000000+1):
    dl = F(n)
    if len(dl) >= 3:
        print(n)
'''
# Ответ:
# 1113840
# 1179360
# 1208844
# 1499400


# Тип 25 № 29673
# Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
# Найдите все натуральные числа, принадлежащие отрезку
# [123456789; 223456789] и имеющие ровно три нетривиальных делителя.
# Для каждого найденного числа запишите в ответе его наибольший нетривиальный делитель.
# Ответы расположите в порядке возрастания.
'''
def F(n):
    dl = set()
    if round(n ** 0.5) == (n ** 0.5):  # если у числа есть квадратный корень
        for j in range(2, int(n**0.5)+1):  # не равный единице и самому числу
            if n % j == 0:
                dl.add(j)
                dl.add(n // j)
    return sorted(dl)

for n in range(123456789, 223456789+1):
    dl = F(n)
    if len(dl) == 3:
        print(n, max(dl))
'''
# Ответ:
# 131079601 1225043
# 141158161 1295029
# 163047361 1442897



# Тип 25 № 38603
# Пусть M — сумма минимального и максимального натуральных делителей целого числа, не считая единицы и самого числа.
# Если таких делителей у числа нет, то значение M считается равным нулю.
#
# Напишите программу, которая перебирает целые числа, бо́льшие 700000,
# в порядке возрастания и ищет среди них такие, для которых значение M оканчивается на 8.
# Выведите первые пять найденных чисел и соответствующие им значения M.
#
# Формат вывода: для каждого из пяти таких найденных чисел в отдельной
# строке сначала выводится само число, затем — значение М.
#
# Строки выводятся в порядке возрастания найденных чисел.
'''
def F(n):
    dl = set()
    for j in range(2, int(n**0.5)+1):  # не считая единицы и самого числа
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

count = 0
for n in range(700000+1, 7000000000):
    dl = F(n)
    if len(dl) > 2:
        M = dl[-1] + dl[0]  # max(dl) + min(dl)
        if M % 10 == 8:
            print(n, M)
            count += 1
            if count == 5:
                break
'''
# Ответ:
# 700005 233338
# 700007 100008
# 700012 350008
# 700015 140008
# 700031 24168


# Тип 25 № 38959
# Пусть M(N) — произведение 5 наименьших различных натуральных делителей натурального числа N, не считая единицы.
# Если у числа N меньше 5 таких делителей, то M(N) считается равным нулю.
#
# Найдите 5 наименьших натуральных чисел, превышающих 200_000_000, для которых 0<M(N)<N.
# В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.
'''
def F(n):
    dl = set()
    for j in range(2, int(n**0.5)+1):  # не считая единицы и самого числа
        if n % j == 0:
            dl.add(j)
            dl.add(n // j)
    return sorted(dl)

count = 0
for n in range(200_000_000+1, 100_000_000_000):
    dl = F(n)
    if len(dl) > 5:
        M = dl[0] * dl[1] * dl[2] * dl[3] * dl[4]
        if 0 < M < n:
            print(M)
            count += 1
            if count == 5:
                break
'''
# 1728
# 21632
# 1260
# 1152
# 4127787




# endregion Урок: ******************************************************************


# todo: Всеволод = [2, 5.1, 8, 12, 14, 15, 16, 23, 25.1]
# на прошлом уроке: Разобрали 16, 23 номера. В том числе на аналитическое решение.
# на следующем уроке:
