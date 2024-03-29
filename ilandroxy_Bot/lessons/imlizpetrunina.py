# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Единицы измерения информации:
# 1 бит - минимальная единица измерения
# 1 байт = 8 бит = 2**3 бит
# 1 Кбайт = 1024 байт = 2**10 байт = 2**13 бит
# 1 Мбайт = 1024 Кбайт = 2**10 Кбайт = 2**23 бит


# Тип 7 №55803
# Голосовое сообщение, записанное в стерео формате, передается со скоростью 64 000 бит/с.
# Файл был записан с такими параметрами: глубина кодирования — 24 бит на отсчет,
# частота дискретизации — 16000 отсчетов в секунду, время записи — 90с.
# Сколько секунд будет передаваться голосовое сообщение?
'''
a = 2
b = 16000
c = 24
t = 90
I = a * b * c * t  # бит

U = 64000  # бит / с

print(I / U)
'''
# Ответ: 1080


# Тип 7 №13593
# Производится звукозапись музыкального фрагмента в формате стерео (двухканальная запись)
# с частотой дискретизации 32 кГц и 32-битным разрешением. Результаты записываются в файл,
# сжатие данных не производится; размер полученного файла 40 Мбайт. Затем производится
# повторная запись этого же фрагмента в формате моно (одноканальная запись) с частотой
# дискретизации 16 кГц и 16-битным разрешением. Сжатие данных не производилось.
#
# Укажите размер файла в Мбайт, полученного при повторной записи.
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
I1 = 40 * 2 ** 23  # бит
a1 = 2
b1 = 32000
c1 = 32
t = I1 / (a1 * b1 * c1)
print(t)

a2 = 1
b2 = 16000
c2 = 16
I2 = a2 * b2 * c2 * t

print(I2 / (2**23))
'''
# Ответ: 5


# Тип 7 №61387
# Аудиопоток кодируется в режиме стерео (2 канала) с частотой дискретизации 32 кГц
# и передаётся по каналу с пропускной способностью 40Кбайт/сек.
# При этом используются методы сжатия, которые позволяют сократить объём передаваемой информации на 68%.
# С какой максимальной глубиной кодирования можно вести запись?
#
# В ответе укажите только целое число — максимально возможную глубину кодирования в битах.
'''
a = 2
b = 32000
U = 40 * 2 ** 13  # бит / сек
I = 40 * 2 ** 13
t = 1

c = (I / (1 - 0.68)) / (a * b * t)
# c - ?
print(c)
'''
# Ответ: 16


# Тип 25 №55612
# Маска числа — это последовательность цифр,
# в которой могут встречаться специальные символы «?» и «*».
# Символ «?» означает ровно одну произвольную цифру,
# символ «*» означает произвольную (в том числе пустую) последовательность цифр.
#
# Пример. Маске 123*4?5 соответствуют числа 123405 и 1230000415.
#
# Найдите все натуральные числа, не превышающие 10**10,
# которые соответствуют маске 1?3948*5 и при этом без остатка делятся на 3013.
'''
from fnmatch import *
for x in range(3013, 10**10, 3013):
    if fnmatch(str(x), '1?3948*5'):
        print(x)
'''
# 1039485
# 1739480225
# 1839481695
# 1939483165


# Тип 25 №28120
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [201455; 201470],
# числа, имеющие ровно 4 различных натуральных делителя.
# Выведите эти четыре делителя для каждого найденного числа в порядке возрастания.
'''
def divisors(x):  # x = 24
    div = []
    for j in range(1, x+1):
        if x % j == 0:
            div.append(j)
    return div


# print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
# print(divisors(16))  # [1, 2, 4, 8, 16]


for x in range(201455, 201470+1):
    div = divisors(x)
    if len(div) == 4:
        print(*div)
'''
# 1 3 67153 201459
# 1 13 15497 201461
# 1 29 6947 201463
# 1 2 100733 201466

'''
import time
start = time.time()

# def divisors(x):
#     div = []
#     for j in range(1, x+1):
#         if x % j == 0:
#             div.append(j)
#     return div


def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


print(divisors(100_000_000))   # old: 3.006 / new: 0.0006

print(time.time() - start)
'''


# Тип 25 №28123
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [125256; 125330], числа, имеющие ровно шесть различных чётных натуральных делителей.
# Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(125256, 125330+1):
    div = divisors(x)
    chet = [x for x in div if x % 2 == 0]
    if len(chet) == 6:
        print(*chet)
'''
# 2 6 18 13918 41754 125262
# 2 4 8 31322 62644 125288
# 2 6 18 13922 41766 125298


# Тип 25 №40741
# Пусть M(N) — сумма двух наибольших различных натуральных делителей натурального числа N,
# не считая самого числа. Если у числа N меньше двух таких делителей, то M(N) считается равным 0.
#
# Найдите 5 наименьших натуральных чисел, превышающих 10000000, для которых 0 < M(N) < 10000.
# В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # 2 - не считая самого числа
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


k = 0
for x in range(10000000+1, 10**10):
    div = divisors(x)
    if len(div) >= 2:
        M = div[-1] + div[-2]
        if 0 < M < 10000:
            print(M)
            k += 1
            if k == 5:
                break
'''
# Ответ:
# 6876
# 6374
# 6924
# 8024
# 8358

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo Добавить разбор на канал Тип 7 №55594
# Книгу объёмом 1 Мбайт записали как аудиокнигу.
# Запись велась в формате стерео (2 канала) с частотой 32кГц и разрешением 16бит.
# За одну минуту записывалось в среднем 1,5 Кбайт текста.
# Сжатие данных позволило сократить размер полученного звукового файла на 80%.
# Для удобства использования запись разделили на фрагменты со средним размером 20 Мбайт.
# Определите количество полученных фрагментов.
'''
I_book = 1 * 2 ** 23  # бит вес одной книги
U = 1.5 * 2 ** 13  # бит / мин
t = (I_book / U) * 60  # 40960 секунд длилась аудиозапись аудиокниги
print(t)

a = 2
b = 32000
c = 16
I_music = a * b * c * t
I = (I_music * (1-0.8) / (2**23))
print(I / 20)  # 49.99
'''
# Ответ: 50

# endregion Разобрать: *************************************************************


# Лиза = [1, 2, 4, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: На следующем уроке повторить 25 и выдать домашку
