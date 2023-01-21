
# region Домашка: **********************************************************

# Тип 24 № 36879
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
import string
S = open('24.txt').readlines()

M = []
for x in S:
    if x.count('G') < 25:
        M.append(x)

alphabet = string.ascii_uppercase
maxi = 0
for x in M:
    for a in alphabet:
        maxi = max(maxi,  x.rindex(a) - x.index(a))
print(maxi)
'''
# Ответ: 1001

# Тип 24 № 38602
# Текстовый файл состоит из символов P, Q, R и S.
# Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых нет идущих подряд символов P.
'''
with open('24.txt', 'r') as f:
    s = f.readline()

    count = 1
    maxi = 0
    for i in range(0,len(s)-1):
        if s[i] == 'P' and s[i+1] == 'P':
            count = 1
        else:
            count += 1
            maxi = max(maxi, count)
    print(maxi)
'''
# Ответ: 188

# Тип 24 № 45258
# Текстовый файл состоит из символов A, B и C.
# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
# Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB, или только из пар AB и CB в произвольном порядке следования этих пар.
'''
s = open('24.txt').readline().replace('AB', '*').replace('CB', '*')
s = s.replace('A', ' ').replace('B', ' ').replace('C',' ')
print(max([len(i) for i in s.split()]))
'''
# Ответ: 65

# Тип 9 № 35983
'''
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Определите, сколько раз за время измерений максимальная суточная температура оказывалась выше среднесуточной на 7 и более градусов.

count = 0
for x in open('9.txt'):
    M = [float(i) for i in x.replace(',', '.').split()]
    if max(M) - (sum(M) / len(M)) >= 7:
        count += 1
print(count)
'''
# Ответ: 66

# Тип 9 № 28117
'''
# Откройте файл электронной таблицы, содержащей вещественные числа — результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Найдите количество суток, в которых среднее значение температуры не превышало 20°С.

count = 0
for x in open('9.txt'):
    M = [float(i) for i in x.replace(',', '.').split()]
    if (sum(M) / len(M)) <= 20:
        count += 1
print(count)
'''
# Ответ: 30


# Тип 9 № 33088
'''
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Определите, сколько раз за время наблюдений суточные колебания температуры
# (разность между максимальной и минимальной температурой в течение суток) были меньше 14 градусов.

count = 0
for x in open('9.txt'):
    M = [float(i) for i in x.replace(',', '.').split()]
    if (max(M) - min(M)) < 14:
        count += 1
print(count)
'''
# Ответ: 6.



# endregion Домашка: **********************************************************


# region Урок: **********************************************************

# Тип 9 № 33511
'''
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Определите величину самого большого повышения температуры между двумя соседними измерениями.
# Ответ округлите до целого числа. Например, с 3:00 до 4:00 1 апреля температура повысилась на 1,4 градуса.
# Если это повышение окажется максимальным, в ответе надо записать 1.

A = []
for x in open('9.txt'):
    M = [float(i) for i in x.replace(',', '.').split()]
    A += M

maxi = 0
for i in range(0, len(A)-1):
    maxi = max(maxi, A[i+1] - A[i])
print(maxi)
'''
# Ответ: 9



# Тип 9 № 47213
'''
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.

# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — в строке только одно число повторяется ровно два раза, остальные числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.
# В ответе запишите только число.

count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == 5:  # — в строке только одно число повторяется ровно два раза, остальные числа различны;
        repeat = sum(M) - sum(set(M))
        sred = (sum(M) - 2*repeat) / 4  # среднее арифметическое неповторяющихся чисел
        if sred <= 2*repeat:
            count += 1
print(count)
'''
# Ответ: 2241


# Тип 9 № 33181
'''
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Определите, сколько раз за время наблюдений температура в 8:00 была выше среднесуточной температуры того же дня.

count = 0
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    if M[8] > (sum(M) / len(M)):
        count += 1
print(count)
'''
# Ответ: 30



# Тип 9 № 36022
'''
# Откройте файл электронной таблицы, содержащей вещественные числа — результаты ежечасного измерения температуры воздуха в течение трёх месяцев.
# Найдите разность между максимальной температурой воздуха с 1 апреля по 31 мая с 9:00 до 12:00 включительно и средним значением
# температуры воздуха в эти часы в апреле и мае, используя данные, представленные в таблице.

count = 0
maxi = 0
A = []
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    maxi = max(maxi, max(M[9:12+1]))
    A += M[9:12+1]
sred = sum(A) / len(A)
print(maxi - sred)
'''
# Ответ: 5

# Вариант 2 если бы заранее подготовили файл
'''
A = []
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    A += M
print(max(A) - (sum(A) / len(A)))
'''
# Ответ: 5

# endregion Урок: **********************************************************


# todo: Стася = [2, 5, 6, 8, 9.1, 12, 14+, 15, 16, 17, 23, 24, 25.2]
# на прошлом уроке: Разобрали 9 номер на Пайтон, и глянули 4-ый номер пару задач.
# на следующем уроке:  30 минут дополнительного времени. Начинаем Эксель часть, номера: 3, 9, 10, 18, 19-21, 22

