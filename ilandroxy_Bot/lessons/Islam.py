# region Домашка:  ******************************************************************************

# endregion Домашка: ******************************************************************************


# region Урок:  ******************************************************************************
'''
1 бит - минимальная единица измерения
1 байт = 8 бит = 2**3 бит
1 Кбайт = 1024 байт = 2**10 байт = 2**13 бит
1 Мбайт = 1024 Кбайт = 2**10 Кбайт = 2**20 байт = 2**23 бит
1 Гбайт = 1024 Мбайт = 2**10 Мбайт = 2**30 байт = 2**33 бит
'''

# Тип 7 № 15849
# Автоматическая камера производит растровые изображения размером 600 на 1000 пикселей.
# Для кодирования цвета каждого пикселя используется одинаковое количество бит,
# коды пикселей записываются в файл один за другим без промежутков.
# Объём файла с изображением не может превышать 250 Кбайт без учёта размера заголовка файла.
# Какое максимальное количество цветов можно использовать в палитре?

# I = pixels * i  (бит на 1 пиксель)
# Colors = 2 ** i
'''
pixels = 600 * 1000
I = 250 * 2**13  # бит
print(I / pixels)  # 3.4133333333333336
i = 3
Colors = 2 ** i
print(Colors)  # 8
'''
# Ответ: 8


# Тип 7 № 45241
# Для хранения сжатого произвольного растрового изображения размером 192 на 960 пикселей
# отведено 90 Кбайт памяти без учёта размера заголовка файла.
# При сжатии объём файла уменьшается на 35%.
# Для кодирования цвета каждого пикселя используется одинаковое количество бит,
# коды пикселей записываются в файл один за другим без промежутков.
# Какое максимальное количество цветов можно использовать в изображении?
'''
I = ((90*2**13) / 65) * 100
i = I / (192 * 960)
print(i) # 6.153846153846153
i = 6
print(2**6)
'''


# Тип 7 №  18078
# Какой минимальный объём памяти (в Кбайт) нужно зарезервировать, чтобы можно было
# сохранить любое растровое изображение размером 640 на 320 пикселей при условии,
# что в изображении могут использоваться 64 различных цвета?
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
pixels = 640 * 320
Colors = 64
i = 6  # бит на 1 пиксель 
# I = pixels * i
I = pixels * i
print(I / (2 ** 13))
'''
# Ответ: 150


# Тип 7 № 57414
# Голосовое сообщение продолжительностью 90с было записано в формате стерео и
# оцифровано с глубиной кодирования 16 бит и частотой дискретизации 48000 измерений в секунду.
# Сжатие данных не использовалось. Файл с оцифрованным голосовым сообщением был
# передан по каналу связи, пропускная способность которого 3200 бит/с. Сколько секунд длилась передача файла?
# В ответе запишите целое число, единицу измерения указывать не нужно.
'''
# I (бит)  = a (каналов) * b (бит)  * c (Гц) * t (сек)
a = 2  # стерео
b = 16
c = 48000  # Гц
t = 90
I = a * b * c * t  # бит
print(I / 3200)  # сек
'''
# Ответ: 43200


# Тип 7 № 48455
# Музыкальный фрагмент был записан в формате квадро (четырёхканальная запись),
# оцифрован с частотой дискретизации 44 кГц и разрешением 16 бит
# и сохранён без использования сжатия данных. Получился файл размером 160 Мбайт.
# Затем тот же фрагмент был записан в формате моно с разрешением 8 бит и тоже сохранён
# без сжатия, при этом получился файл размером 10 Мбайт.
# С какой частотой дискретизации проводилась вторая запись?
# В ответе укажите целое число — частоту в кГц, единицу измерения писать не нужно.
'''
# I = a * b * c * t

a1 = 4
b1 = 16
c1 = 44000
I1 = 160 * 2**23
t = I1 / (a1 * b1 * c1)

I2 = 10 * 2 ** 23
b2 = 8
a2 = 1
c2 = I2 / (a2 * b2 * t)

print(c2 / 1000)
'''
# Ответ: 22


# Тип 11 № 7758
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль,
# состоящий из 21 символов и содержащий только символы A, D, F, H, X, Y, Z
# (таким образом, используется 7 различных символов).
# Каждый такой пароль в компьютерной программе записывается минимально возможным и
# одинаковым целым количеством байт (при этом используют посимвольное кодирование и
# все символы кодируются одинаковым и минимально возможным количеством бит).
# Определите объём памяти в байтах, отводимый этой программой для записи 40 паролей.
'''
symbols = 21   # pixels
alphabet = 7   # Colors = 2 ** i
i = 3  # 2**3 = 8
bit = symbols * i  # I
print(bit / 8)   # 7.875
byte = 8  # уходит для записи 1 пароля 
print(40 * byte)
'''
# Ответ: 320


# Тип 11 №  18561
# Каждый сотрудник предприятия получает электронный пропуск, на котором
# записаны личный код сотрудника, код подразделения и некоторая дополнительная информация.
# Личный код состоит из 13 символов, каждый из которых может быть одной из 12
# допустимых заглавных букв или одной из 10 цифр.
# Для записи личного кода используют посимвольное кодирование, все символы кодируют
# одинаковым минимально возможным количеством бит.
# Код подразделения состоит из двух натуральных чисел, не превышающих 1000,
# каждое из которых кодируется как двоичное число и занимает минимально возможное целое число бит.
# Личный код и код подразделения записываются подряд и вместе занимают
# минимально возможное целое число байт. Всего на пропуске хранится 32 байт данных.
# Сколько байт выделено для хранения дополнительных сведений об одном сотруднике?
# В ответе запишите только целое число — количество байт.
'''
symbols1 = 13
alphabet1 = 22
i2 = 5
bit1 = symbols1 * i2
print(bit1 / 8)  # 8.125
byte1 = 9

symbols2 = 2
alphabet2 = 1000
i2 = 10
bit2 = symbols2 * i2
print(bit2 / 8)
byte2 = 3

# I = byte1 + byte2 + дополнительная информация
I = 32
print(I - byte2 - byte1)
'''
# Ответ: 20


# и может включать латинские буквы из 26-символьного латинского алфавита (заглавные и строчные буквы различаются),
# десятичные цифры и специальные знаки из набора @#$%^&*().
'''
alphabet = 26 * 2 + 10 + 9
print(alphabet)  # 71
'''


# Тип 23 № 37158
# Исполнитель преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
#
# 1. Прибавить 1
# 2. Прибавить 2
# 3. Умножить на 3

# Сколько существует таких программ, которые исходное число 2 преобразуют в число 19
# и при этом траектория вычислений программы проходит через 9 и не проходит через 12?
'''
def F(a, b):
    if a > b or a == 12:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(2, 9) * F(9, 19))


def F(a, b):
    if a >= b or a == 12:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(2, 9) * F(9, 19))
'''
# Ответ: 650


# Тип 24 № 45258
# Текстовый файл состоит из символов A, B и C.
#
# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
#
# Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB,
# или только из пар AB и CB в произвольном порядке следования этих пар.
'''
s = open('24.txt').readline()
s = s.replace('AB', '*').replace('CB', '*')
for x in 'ABC':
    s = s.replace(x, ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 65

# endregion Урок:  *************************************************************************

import useful
print(useful.Who_Is_Name())

# todo: Ислам = [2, 3, 5, 6, 8, 9, 12, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# на прошлом уроке: Повторяли номера: 7, 11 всех типов и 23, 24
# на следующем уроке:
