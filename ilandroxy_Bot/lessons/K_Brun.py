# region Домашка: ******************************************************************

# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
#     а) если число N делится на 3, то все нули заменяются на 11;
#     б) если число N на 3 не делится, то все единицы заменяются на 10.
# Полученная таким образом запись является двоичной записью искомого числа R.
# 3. Результат переводится в десятичную систему и выводится на экран.
#
# Укажите максимальное число R, не превышающее 161, которое может быть получено
# с помощью описанного алгоритма. В ответе запишите это число в десятичной системе счисления.
'''
D = []
for n in range(0, 10000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s.replace('0', '11')
    else:
        s = s.replace('1', '10')
    r = int(s, 2)
    if r <= 161:
        D.append(r)
print(max(D))
'''

# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

# Тип 7 №15946
# Автоматическая фотокамера производит растровые изображения размером 1600 на 900 пикселей.
# При этом объём файла с изображением не может превышать 900 Кбайт, упаковка данных не производится.
# Какое максимальное количество цветов можно использовать в палитре?

# I = pixels * i (бит на один пиксель)
# colors = 2 ** i
'''
pixels = 1600 * 900
I = 900 * 2 ** 13
i = I / pixels
print(i)  # 5.12 -> 5
print(2 ** 5)  
'''
# Ответ: 32


# Тип 7 №18078
# Какой минимальный объём памяти (в Кбайт) нужно зарезервировать, чтобы можно
# было сохранить любое растровое изображение размером 640 на 320 пикселей при условии,
# что в изображении могут использоваться 64 различных цвета?
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
pixels = 640 * 320
colors = 64
i = 6  # бит на один пиксель
I = (pixels * i) / (2**13)
print(I)
'''
# Ответ: 150


# Тип 7 №63023
# Камера наблюдения каждые n секунд (n — целое число) делает фотографию с разрешением
# 1024 × 768 пикселей и палитрой 4096 цветов.
# Фотографии передаются по каналу с пропускной способностью 200 Кбайт/сек, при этом используются методы сжатия,
# позволяющие уменьшить размер изображения в среднем на 20%.
# Определите минимально возможное значение n, при котором возможна передача в режиме реального времени.
'''
colors = 4096
i = 12
pixels = 1024 * 768
I = ((pixels * i) / (2**13)) * (1-0.2)
print(I / 200)
'''
# Ответ: 4.6080 -> 5


# Тип 7 №18621
# Автоматическая фотокамера делает фотографии высокого разрешения с палитрой,
# содержащей 2**16 = 65536 цветов.
# Средний размер фотографии составляет 12 Мбайт.
# Для хранения в базе данных фотографии преобразуют в чёрно-белый формат с палитрой, содержащей 256 цветов.
# Другие преобразования и дополнительные методы сжатия не используются.
# Сколько Мбайт составляет средний размер преобразованной фотографии?
'''
i1 = 16
I1 = 12 * 2 ** 23  # бит
pixels = I1 / i1

colors2 = 256
i2 = 8
I2 = pixels * i2
print(I2 / (2 ** 23))
'''
# Ответ: 6


# Тип 7 №35981
# В информационной системе хранятся изображения размером 2048×1536пк.
# При кодировании используется алгоритм сжатия изображений, позволяющий уменьшить размер памяти
# для хранения одного изображения в среднем в 8 раз по сравнению с независимым кодированием каждого пикселя.
# Каждое изображение дополняется служебной информацией, которая занимает 128 Кбайт.
# Для хранения 32 изображений потребовалось 16 Мбайт. Сколько цветов использовано в палитре каждого изображения?
'''
I = (16 * 2 ** 23) / 32
I = I - (128 * 2 ** 13)
I = I * 8
pixels = 2048 * 1536
i = I / pixels  # 8
print(2**i)
'''
# Ответ: 256


# Тип 11 №5081
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 6 символов и содержащий
# только символы из 7 буквенного набора Н, О, Р, С, Т, У, X. В базе данных для хранения сведений о
# каждом пользователе отведено одинаковое и минимально возможное целое число байт.
#
# При этом используют посимвольное кодирование паролей, все символы кодируются одинаковым и минимально
# возможным количеством бит. Кроме собственно пароля для каждого пользователя
# в системе хранятся дополнительные сведения, для чего отведено 10 байт.

# Определите объём памяти, необходимый для хранения сведений о 100 пользователях. (Ответ дайте в байтах.)
'''
symbols = 6
alphabet = 7  # alphabet = 2 ** i
i = 3  # i - (бит на один символ)
bit = symbols * i
print(bit / 8)  # 2.25 -> 3
byte = 3

I = 10 + byte  # вес одного пользователя = дополнительные сведения + пароль
print(100 * I)
'''
# Ответ: 1300


# Тип 11 №18589
# Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код сотрудника,
# код подразделения и некоторая дополнительная информация. Личный код состоит из 13 символов, каждый
# из которых может быть одной из 16 допустимых заглавных букв или одной из 10 цифр.
# Для записи личного кода используют посимвольное кодирование, все символы кодируют одинаковым минимально
# возможным количеством бит. Код подразделения состоит из двух натуральных чисел, не превышающих 100,
# каждое из которых кодируется как двоичное число и занимает минимально возможное целое число бит.
# Личный код и код подразделения записываются подряд и вместе занимают минимально возможное целое число байт.
# Всего на пропуске хранится 32 байт данных.
# Сколько байт выделено для хранения дополнительных сведений об одном сотруднике?
# В ответе запишите только целое число — количество байт
'''
symbols1 = 13
alphabet1 = 26
i1 = 5
bit1 = symbols1 * i1

symbols2 = 2
alphabet2 = 100
i2 = 7
bit2 = symbols2 * i2

bit = bit1 + bit2  # 9.875 -> 10
print(bit / 8)

byte = 10
print(32 - byte)
'''
# Ответ: 22


# Тип 7 №27538
# Для проведения эксперимента записывается звуковой фрагмент в формате квадро (четырёхканальная запись)
# с частотой дискретизации 32 кГц и 32-битным разрешением. Результаты записываются в файл,
# сжатие данных не производится; дополнительно в файл записывается служебная информация, необходимая
# для эксперимента, размер полученного файла 97 Мбайт. Затем производится повторная запись этого же фрагмента
# в формате моно (одноканальная запись) с частотой дискретизации 16 кГц и 16-битным разрешением.
# Результаты тоже записываются в файл без сжатия и со служебной информацией, размер полученного файла 7 Мбайт.
# Объём служебной информации в обоих случаях одинаков. Укажите этот объём в мегабайтах.
# В ответе укажите только число (количество Мбайт), единицу измерения указывать не надо

# I (бит) = a (шт) * b (Гц) * c (бит) * t (сек)

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# todo Разобрать Тип 7 №27538

# endregion Разобрать: *************************************************************


# Екатерина = [1, 2, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
