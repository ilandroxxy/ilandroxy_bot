# region Домашка: ******************************************************************

# КЕГЭ № 376 (Уровень: Базовый)
#
# НАЧАЛО
#    ПОКА нашлось (11)
#       заменить (112, 4)
#       заменить (113, 2)
#       заменить (42, 3)
#       заменить (43, 1)
#    КОНЕЦ ПОКА
# КОНЕЦ

# Какая строка получится в результате применения приведённой программы
# к строке вида 1…13…32…2 (170 единиц, 100 троек и 7 двоек)?
'''
s = '1' * 170 + '3' * 100 + '2' * 7
while '11' in s:
    s = s.replace('112', '4', 1)
    s = s.replace('113', '2', 1)
    s = s.replace('42', '3', 1)
    s = s.replace('43', '1', 1)
print(s)
'''
# Ответ: 22


# КЕГЭ № 1751 Danov2102 (Уровень: Сложный) (А. Богданов)
# Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
#
# ПОКА нашлось(10) ИЛИ нашлось(20)
#    ЕСЛИ нашлось(20)
#       ТО заменить(20,00)
#       ИНАЧЕ заменить(10,200)
#    КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА

# Определите максимально возможное количество цифр 0,
# которое может получиться в результате применения представленного ниже алгоритма к строке,
# состоящей из 19 цифр 0, 13 цифр 1 и 17 цифр 2, идущих в произвольном порядке.
'''
s = '2' * 17 + '1' * 13 + '0' * 19

while '10' in s or '20' in s:
    if '20' in s:
        s = s.replace('20', '00', 1)
    else:
        s = s.replace('10', '200', 1)

print(s.count('0'))
'''
# Ответ: 62

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# todo Разобрать номера: 1-7, 10-14 (Письменные задачи: 1, 4, 7, 11, 13; Excel: 3, 10; Python: 2, 5, 12, 14)


# Единицы измерения информации
# Компьютеры бинарные - то есть используют для работы только 0 и 1

# минимальная единица измерения: 1 бит
# 1 байт = 8 бит = 2**3 бит
# 1 Кбайт = 1024 байт = 2**10 байт = 2**13 бит
# 1 Мбайт = 1024 Кбайт = 2**10 Кбайт = 2**20 байт = 2**23 бит
# 1 Гбайт = 1024 Мбайт = 2**10 Мбайт = 2**30 байт = 2**33 бит

# 23 Мбайта перевести в биты = 23 * 2**23 бит
# 47 Кбайт в байт = 47 * 2 ** 10 байт
# 5 Гбайт в бит = 5 * 2 ** 33 бит


# Тип 7 № 27404
# Для хранения произвольного растрового изображения размером 128×320 пикселей
# отведено 20 Кбайт памяти без учёта размера заголовка файла.
# Для кодирования цвета каждого пикселя используется одинаковое количество бит,
# коды пикселей записываются в файл один за другим без промежутков.
# Какое максимальное количество цветов можно использовать в изображении?
'''
# I (вес картинки) = pixels (кол-во всех пикселей) * i (бит на 1 пиксель)
# Colors = 2 ** i (бит на 1 пиксель)

# 20 Кбайт = (128 * 320) * i
i = (20 * 2 ** 13) / (128 * 320)
print(i)  # 4 бит на 1 пиксель
Colors = 2 ** i
print(Colors)
'''
# Ответ: 16


# Тип 7 №9759
# Какой минимальный объём памяти (в Кбайт) нужно зарезервировать,
# чтобы можно было сохранить любое растровое изображение размером 128×128 пикселей
# при условии, что в изображении могут использоваться 256 различных цветов?
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
# (Colors) 256 = 2 ** i
i = 8  # бит на 1 пиксель

I = (128 * 128) * i
print(I / (2 ** 13))  # 16

# бит = 1
# байт = 2**3 бит
# Кбайт = 2 ** 13 бит
# Мбайт = 2 ** 23 бит
# Гбайт = 2 ** 33 бит
'''
# Ответ: 16


# Тип 7 №48455
# Музыкальный фрагмент был записан в формате квадро (четырёхканальная запись),
# оцифрован с частотой дискретизации 44кГц и разрешением 16бит и сохранён без использования
# сжатия данных. Получился файл размером 160 Мбайт.
# Затем тот же фрагмент был записан в формате моно с разрешением 8бит и
# тоже сохранён без сжатия, при этом получился файл размером 10 Мбайт.
# С какой частотой дискретизации проводилась вторая запись?
# В ответе укажите целое число — частоту в кГц, единицу измерения писать не нужно.

# I (бит) = a (шт) * b (Гц) * c (бит) * t (сек)
I = 160 * 2 ** 23
a = 4
b = 44 * 1000
c = 16
t = I / (a * b * c)

I2 = 10 * 2 ** 23
a2 = 1
c2 = 8
b2 = I2 / (a2 * c2 * t)
print(b2 / 1000)



# endregion Урок: ******************************************************************


# todo: Анастасия = [1.1, 2.1, 12.1, 14.1]
# todo:  КЕГЭ  = []
# на прошлом уроке: Успели разобрать два 4 номера на условие Фано и базовую теорию для основных типов 7-го номера.
# на следующем уроке: На след. уроке продолжаем 7-й и 11-ый.
