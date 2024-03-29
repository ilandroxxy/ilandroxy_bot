# region Домашка: ******************************************************************

# КЕГЭ № 1549 (Уровень: Базовый)
#
# Какой минимальный объем памяти (в Кбайт) нужно зарезервировать, чтобы можно было сохранить любое растровое
# изображение размером 160х160 пикселей при условии, что в изображении могут использоваться 256 различных цветов?
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
pixels = 160 * 160
i = 8
I = pixels * i
print(I / (2 ** 13))
'''


# КЕГЭ № 2669 Пробный 02.2022 /dev/inf Base level (Уровень: Средний)
# Растровые изображения размером 1920 × 1080 пикселей сохраняются на компьютере.
# Для кодирования цвета каждого пикселя используется одинаковое количество бит,
# коды пикселей записываются в файл один за другим без промежутков.
# В изображениях используется 2**15 различных цветов. Для хранения изображений отведено 40 Мб.
# Какое максимальное количество изображений может поместиться в данном объеме? В ответе запишите целое число.
'''
pixels = 1920 * 1080
i = 15
I = (pixels * i) / (2**23)
print(I)  # 3.7  # Мбайт
print(40 / I)  # Порядка 10 изображений поместится в 40 Мбайт
'''


# КЕГЭ № 5247 (Уровень: Базовый) (Д. Статный)
# В памяти компьютера сохраняется изображение размером 4044×1028 пикселей.
# При кодировании каждого пикселя используется палитра из 2**16 цветов, кроме того
# сохраняется значение уровня прозрачности. Под это изображение зарезервировано 16 Мбайт
# памяти без учёта размера заголовка файла. Коды пикселей записываются в файл один за другим без промежутков.
# Какое максимальное число уровней прозрачности может быть использовано при кодировании данного изображения?
'''
pixels = 4044 * 1028
I = 16 * 2 ** 23
print(I / pixels)  # 32
# 32 - 16 = 16
print(2**16)
'''
# 65536


# Тип 7 №13593
# Производится звукозапись музыкального фрагмента в формате стерео
# (двухканальная запись) с частотой дискретизации 32 кГц и 32-битным разрешением.
# Результаты записываются в файл, сжатие данных не производится; размер полученного файла 40 Мбайт.
# Затем производится повторная запись этого же фрагмента в формате моно (одноканальная запись)
# с частотой дискретизации 16 кГц и 16-битным разрешением. Сжатие данных не производилось.
#
# Укажите размер файла в Мбайт, полученного при повторной записи.
# В ответе запишите только целое число, единицу измерения писать не нужно.

# I (бит) = a (шт) * b (Гц) * c (бит) * t (сек)
# Вес музыкального фрагмента = кол-во каналов * частоту дискретизации * битное разрешение * секунды
'''
I1 = 40 * 2 ** 23  # бит
a1 = 2
b1 = 32000
c1 = 32
t = I1 / (a1 * b1 * c1)

a2 = 1
b2 = 16000
c2 = 16
I2 = a2 * b2 * c2 * t  # бит
print(I2 / (2 ** 23))
'''
# Ответ: 5


# Тип 7 №61353
# Аудиопоток кодируется в режиме стерео (2 канала)
# с частотой дискретизации 48 кГц и передаётся по каналу с пропускной способностью 45Кбайт/сек.
# При этом используются методы сжатия, которые позволяют сократить объём передаваемой
# информации на 84%. С какой максимальной глубиной кодирования можно вести запись?
#
# В ответе укажите только целое число — максимально возможную глубину кодирования в битах.
'''
a = 2
b = 48000
I = (45 * 2 ** 13) / (1 - 0.84)
t = 1

c = I / (a * b * t)
# c - ?
print(c)
'''
# Ответ: 24


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo Разобрать задачку Лев
# КЕГЭ № 6094 /dev/inf 02.2023 (Уровень: Средний) (А. Рогов)
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд пар символов
# вида согласная + гласная среди которых нет подстроки XYZY.
# Примечание. Букву Y считайте всегда гласной.
'''
s = open('24.txt').readline()
s = s.replace('XY', '*').replace('ZY', '+')
for a in 'XYZ':
    s = s.replace(a, ' ')
print(max([len(x) for x in s.split() if '*+' not in x]))
'''

# endregion Разобрать: *************************************************************


# Лев = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке: Посмотреть 7 номера на музыку
