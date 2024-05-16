# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Единицы измерения информации
# 1. бит - минимальная единица измерения информации
# 2. 1 байт = 8 бит = 2**3 бит
# 3. 1 Кбайт = 1024 байт = 2**10 байт = 2**13 бит
# 4. 1 Мбайт = 1024 Кбайт = 2**20 байт = 2**23 бит
# 4. 1 Гбайт = 1024 Мбайт = 2**30 байт = 2**33 бит

# Формулы для 7 номера

# Прототип 1:
# I (вес картинки в бит) = pixels (кол-во пикселей) * i (бит на один пиксель)
# colors (допустимая цветовая палитра) = 2 ** i (бит на один пиксель)

# Прототип 2:
# I (вес аудио файла) = a (кол-во каналов) * b (частота дискретизации) * c (глубина кодирования) * t (время в секундах)

# Формулы для 11 номера

# alphabet (допустимый алфавит для построения пароля) = 2 ** i (бит на один символ)


# Тип 7№ 16384
# Автоматическая фотокамера производит растровые изображения размером 512 на 300 пикселей.
# При этом объём файла с изображением не может превышать 150 Кбайт,
# упаковка данных не производится. Какое максимальное количество цветов можно использовать в палитре?
'''
pixels = 512 * 300
I = 150 * 2**13  # бит
# I (вес картинки в бит) = pixels (кол-во пикселей) * i (бит на один пиксель)
# colors (допустимая цветовая палитра) = 2 ** i (бит на один пиксель)
i = I / pixels  # 8.0
print(2 ** i)
'''

# Тип 7 №29116
# В информационной системе хранятся изображения размером 224 x 128 пикселей, содержащие
# не более 64 различных цветов. Коды пикселей записываются подряд, никакая дополнительная
# информация об изображении не сохраняется, данные не сжимаются.
# Сколько Кбайт нужно выделить для хранения одного изображения?
# В ответе укажите только целое число — количество Кбайт,
# единицу измерения указывать не надо.
'''
pixels = 224 * 128
colors = 64   # 2 ** i == 64,  i = 6  бит на один пиксель
i = 6
I = pixels * i  # бит
print(I / (2**13))  # Кбайт
'''


# Тип 7 №36862
# В информационной системе хранятся изображения размером 2048×1536пк.
# При кодировании используется алгоритм сжатия изображений, позволяющий уменьшить
# размер памяти для хранения одного изображения в среднем в 4 раза по сравнению
# с независимым кодированием каждого пикселя. Каждое изображение дополняется
# служебной информацией, которая занимает 128 Кбайт.
# Для хранения 32 изображений потребовалось 16 Мбайт.
# Сколько цветов использовано в палитре каждого изображения?
'''
pixels = 2048 * 1536
I = (16 * 2 ** 23) / 32  # бит
I = I - (128 * 2 ** 13)  # вес одного изображения без доп информации
I = I * 4
i = I / pixels
print(i)  # i = 4
print(2 ** 4)
'''

# Тип 7 №60249
# Прибор автоматической фиксации нарушений правил дорожного поведения делает
# цветные фотографии размером 1024×768 пикселей, используя палитру из 4096 цветов.
# Для передачи снимки группируются в пакеты по 256 штук.
# Определите размер одного пакета фотографий в Мбайт.
# В ответе запишите только число.
'''
pixels = 1024 * 768
colors = 4096   # colors = 2 ** i, i = 12
i = 12
I = pixels * i  # бит
I = I * 256
print(I / (2 ** 23))
'''


# Тип 11 №11269
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 15 символов
# и содержащий только символы из 12-символьного набора: А, В, C, D, Е, F, G, H, K, L, M, N.

# В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально
# возможное целое число байт. При этом используют посимвольное кодирование паролей, все символы
# кодируют одинаковым и минимально возможным количеством бит.
#
# Кроме собственно пароля, для каждого
# пользователя в системе хранятся дополнительные сведения, для чего выделено целое число байт;
# это число одно и то же для всех пользователей.
#
# Для хранения сведений о 20 пользователях потребовалось 400 байт.
# Сколько байт выделено для хранения дополнительных сведений об одном пользователе?
# В ответе запишите только целое число — количество байт.

symbols = 15
alphabet = 12   # alphabet = 2 ** i
i = 4  # бит на один символ

bit = symbols * i
print(bit / 8)  # 7.5
byte = 8

I = 400 / 20  # вес одного пользователя (пароль + допы)
print(I - byte)




# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Данил = [1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
