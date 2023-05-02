# region Домашка:  **************************************************



# endregion Домашка: **************************************************


# region Урок:  **************************************************

# Тип 7 № 16036
# Автоматическая камера производит растровые изображения размером 200×256 пикселей. Для кодирования
# цвета каждого пикселя используется одинаковое количество бит, коды пикселей записываются в файл один за другим без
# промежутков. Объём файла с изображением не может превышать 65 Кбайт без учёта размера заголовка файла. Какое
# максимальное количество цветов можно использовать в палитре?
'''
# I (бит) = pixels (шт) * i (бит на 1 пиксель)
# Colors (шт) = 2 ** i (бит на 1 пиксель)
I = 65 * 2**13
pixels = 200 * 256

print(I / pixels)
i = 10

Colors = 2 ** i
print(Colors)
'''
# Ответ: 1024


# Тип 7 № 48455
# Музыкальный фрагмент был записан в формате квадро (четырёхканальная запись), оцифрован с частотой
# дискретизации 44 кГц и разрешением 16 бит и сохранён без использования сжатия данных. Получился файл размером
# 160 Мбайт. Затем тот же фрагмент был записан в формате моно с разрешением 8 бит и тоже сохранён без сжатия,
# при этом получился файл размером 10 Мбайт. С какой частотой дискретизации проводилась вторая запись? В ответе
# укажите целое число — частоту в кГц, единицу измерения писать не нужно.
'''
# I (бит) = a (шт каналов) * b (Гц) * c (бит) * t (сек)
I = 160 * 2**23
a = 4
b = 44000
c = 16
# t - ?
t = I / (a * b * c)

I2 = 10 * 2**23
a2 = 1
# b2 - ?
c2 = 8
# t - ?

b2 = I2 / (a2 * c2 * t)
print(b2 / 1000)
'''
# Ответ: 22


# Тип 11 № 25843
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 25
# символов и содержащий только символы из 7-символьного набора: С, Д, А, М, Е, Г, Э. В базе данных для хранения
# сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт. При этом используют
# посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным количеством бит. Кроме
# собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения, для чего выделено целое
# число байт; это число одно и то же для всех пользователей. Для хранения сведений о 100 пользователях потребовалось
# 2400 байт.

# Сколько байт выделено для хранения дополнительных сведений об одном пользователе?
# В ответе запишите только целое число – количество байт.
'''
symbols = 25
alphabet = 7
# alphabet = 2 ** i

i = 3  # 2**2 < alphabet < 2**3

bit = symbols * i
print(bit / 8)
byte = 10

I = 2400 / 100
print(I - byte)
'''
# Ответ: 14

# endregion Урок:  **************************************************

import useful
print(useful.who_is_name())

# todo: Кирилл = [1, 2, 3, 4, 5, 8, 9, 12, 13, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25], на следующем уроке:
# на прошлом уроке: Прорешиваи 7 и 11 номера
# на следующем уроке: Поразбирать 8 номера с any all
