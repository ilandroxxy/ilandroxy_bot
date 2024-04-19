# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# бит - минимальная единица измерения информации
# 1 бай = 1024 байт = 2**10 байт = 2**13 бит
# # 1 Мбайт = 1024 Кбайт = 2**20 байт = 2**23 бит


# Тип 7 №13620
# Производится звукозапись музыкального фрагмента в формате стерео (двухканальная запись)
# с частотой дискретизации 32 кГц и 32-битным разрешением. Результаты записываются в файл,
# сжатие данных не производится; размер полученного файла – 64 Мбайт.
# Затем производится повторная запись этого же фрагмента в формате моно (одноканальная запись)
# с частотой дискретизации 16 кГц и 16-битным разрешением. Сжатие данных не производилось.
# Укажите размер файла в Мбайт, полученного при повторной записи.
# В ответе запишите только целое число, единицу измерения писать не нужно.

# I (бит) = a (шт) * b (Гц) * c (бит) * t (сек)
# Вес музыкального файла = кол-во каналов * частота дискретизации * разрешение * время
'''
I = 64 * 2 ** 23
a = 2
b = 32000
c = 32
t = I / (a * b * c)
print(t)  # 262.144

a2 = 1
b2 = 16000
c2 = 16
I2 = a2 * b2 * c2 * t
print(I2 / (2 ** 23))
'''
# Ответ: 8


# Тип 7 №55803
# Голосовое сообщение, записанное в стерео формате, передается со скоростью 64000бит/с.
# Файл был записан с такими параметрами: глубина кодирования — 24 бит на отсчет,
# частота дискретизации — 16000 отсчетов в секунду, время записи — 90с.
# Сколько секунд будет передаваться голосовое сообщение?
'''
a = 2
b = 16000
c = 24  # бит
t = 90
I = a * b * c * t  # бит

U = 64000  # бит / сек
T = I / U
# T - ?
print(T)
'''
# Ответ: 1080


# Тип 7 №61387
# Аудиопоток кодируется в режиме стерео (2 канала) с частотой дискретизации 32кГц
# и передаётся по каналу с пропускной способностью 40 Кбайт/сек.
# При этом используются методы сжатия, которые позволяют сократить объём передаваемой информации на 68%.
# С какой максимальной глубиной кодирования можно вести запись?
#
# В ответе укажите только целое число — максимально возможную глубину кодирования в битах.
'''
a = 2
b = 32000
I = 40 * 2 ** 13  # 100 - 68 %
t = 1

# a * b * t * c = I - (68%)
c = (I / (1 - 0.68)) / (a * b * t)
print(c)
'''
# Ответ: 16

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Артур = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
