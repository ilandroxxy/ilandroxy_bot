# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ************************************************************

# Тип 11 №59749
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 121 символа.
# В качестве символов используют 4090 специальных символов и десятичные цифры. В базе данных для хранения
# сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт.
#
# При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально
# возможным количеством бит. В компьютерной системе зарегистрировано 65 536 пользователей.
# Укажите количество Кбайт, выделенное на хранение всех паролей. В ответе запишите только целое число.
'''
symbols = 121
alphabet = 4090 + 10
# alphabet = 2 ** i  (i - бит на один символ)
print(alphabet, 2**13)
i = 13
bit = symbols * i  # 1573 - бит
print(bit / 8)  # 196.625 -> 197
byte = 197  # 197 - байт
I = (byte * 65536) / (2**10)
print(I)  # 12608
'''
# Ответ: 12608


# Тип 11 №35985
# Каждый объект, зарегистрированный в информационной системе, получает уникальный код из 11 символов,
# каждый из которых может быть одной из 26 заглавных или строчных латинских букв.
# Для представления кода используют посимвольное кодирование, все символы кодируют одинаковым
# минимально возможным количеством битов, а для кода в целом выделяется минимально возможное целое количество байтов.
# Кроме того, для каждого объекта в системе выделен одинаковый объём памяти для хранения
# содержательной информации.Для хранения данных (код и содержательная информация) о 40 объектах потребовалось 2400 байт.
#
# Сколько байтов выделено для хранения содержательной информации об одном объекте?
# В ответе запишите только целое число — количество байтов.
'''
symbols = 11
alphabet = 26 * 2
print(alphabet, 2**6)
i = 6
bit = symbols * i
print(bit / 8)  # 8.25 -> 9
byte = 9
I = 2400 / 40
print(I - byte)
'''
# Ответ: 51

# моно - 1, стерео - 2, квадра - 4

# Тип 7 №57414
# Голосовое сообщение продолжительностью 90с было записано в формате стерео и оцифровано с глубиной кодирования 16 бит
# и частотой дискретизации 48000 измерений в секунду. Сжатие данных не использовалось.
# Файл с оцифрованным голосовым сообщением был передан по каналу связи, пропускная способность которого 3200 бит/с.
# Сколько секунд длилась передача файла? В ответе запишите целое число, единицу измерения указывать не нужно.

# I (бит) = a (шт) * b (Гц) * c (бит) * t (сек)
# Вес файла = Кол-во каналов * Частота * Глубин кодирования * Время
'''
t = 90  # сек
a = 2  # шт
c = 16  # бит
b = 48000  # Гц
I = a * b * c * t   # бит
U = 3200  # бит/с
print(I / U)
'''
# Ответ: 43200


# Тип 7 №13620
# Производится звукозапись музыкального фрагмента в формате стерео (двухканальная запись)
# с частотой дискретизации 32 кГц и 32-битным разрешением. Результаты записываются в файл,
# сжатие данных не производится; размер полученного файла – 64 Мбайт.
# Затем производится повторная запись этого же фрагмента в формате моно (одноканальная запись)
# с частотой дискретизации 16 кГц и 16-битным разрешением. Сжатие данных не производилось.
# Укажите размер файла в Мбайт, полученного при повторной записи.
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
a1 = 2
b1 = 32000
c1 = 32
I1 = 64 * 2**23
t = I1 / (a1 * b1 * c1)

a2 = 1
b2 = 16000
c2 = 16
I2 = a2 * b2 * c2 * t
print(I2 / (2**23))
'''

# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Евгений = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23]
# КЕГЭ = []
# на следующем уроке:
