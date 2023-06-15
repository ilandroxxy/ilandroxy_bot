# region Домашка:  ******************************************************************************

# endregion Домашка: ******************************************************************************


# region Урок:  ******************************************************************************
#
# № 8481 (Уровень: Базовый)
# (В. Рыбальченко) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# - символ «?» означает ровно одну произвольную цифру;
# - символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Найдите все натуральные числа меньшие 10**8, которые кратны 237,
# соответствуют маске «81?2*80», но не соответствуют маске «*9*».
# В ответ в первом столбике перечислите все найденные числа в порядке возрастания,
# а во втором столбце – соответствующие им результаты деления этих чисел на 237.
'''
from fnmatch import *
for x in range(237, 10**8, 237):
    if fnmatch(str(x), '81?2*80'):  # соответствуют маске «81?2*80»
        if not fnmatch(str(x), '*9*'):   #  не соответствуют маске «*9*»
            print(x, x//237)


'''
# Показать ответ
# 815280 3440
# 8162280 34440
# 81324180 343140
# 81727080 344840
# 81821880 345240



# № 8469 (Уровень: Базовый)
# (В. Рыбальченко) При регистрации в компьютерной системе каждому пользователю
# выдаётся идентификатор, состоящий из 33 символов и содержащий только символы
# из 18-буквенного набора. В базе данных для хранения сведений о каждом пользователе
# отведено одинаковое целое число байт, при этом для хранения сведений о 768 пользователях
# используется 21 Кбайт. Для каждого пользователя хранятся идентификатор и дополнительные
# сведения. Каждый символ в идентификаторе кодируется одинаковым и минимально возможным к
# оличеством бит. На хранение идентификатора отведено минимальное возможное целое
# количество байт. Сколько байт отведено для хранения дополнительных сведений о пользователе?

symbols = 33
alphabet = 18
i = 5
bit = i * symbols
print(bit / 8)
byte = 21


I = (21 * 2 ** 10) / 768  # бит на 1 пользователя
print(I)

print(I - byte)
# Разбор: 7


# endregion Урок:  *************************************************************************

import useful
print(useful.Who_Is_Name())

# todo: Ислам = [2, 3, 5, 6, 8, 9, 12, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# на прошлом уроке:  Прорешивали 15 номер по запросу Булата, 25 номера по запросу Ислама. Занимались 1.5 часа за прошлые разы.
# на следующем уроке:
