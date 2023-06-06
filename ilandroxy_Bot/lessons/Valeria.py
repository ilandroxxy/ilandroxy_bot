
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 7 № 9795
# Какой минимальный объём памяти (в Кбайт) нужно зарезервировать, чтобы можно было сохранить любое растровое
# изображение размером 128×128 пикселей при условии, что в изображении могут использоваться 128 различных цветов?
# В ответе запишите только целое число, единицу измерения писать не нужно.

# I = pixels * i
# Colors = 2 ** i
'''
pixels = 128 * 128
Colors = 128
i = 7  # 2 ** 7 = 128
I = pixels * i   # бит
print(I / (2**13))
'''
# Ответ: 14.0


# Тип 7 № 48428
# Музыкальный фрагмент был записан в формате стерео (двухканальная запись),
# оцифрован с частотой дискретизации 44 кГц и разрешением 16 бит и сохранён без использования сжатия данных.
# Получился файл размером 120 Мбайт. Затем тот же фрагмент был записан в формате квадро (четырёхканальная запись)
# с частотой дискретизации 88 кГц и тоже сохранён без сжатия, при этом получился файл размером 720Мбайт.
# С каким разрешением проводилась вторая запись? В ответе укажите целое
# число — разрешение в битах, единицу измерения писать не нужно.

# I (бит) = a (каналов) * b (бит) * c (Гц) * t (сек)
'''
# 120 * 2**23 = 2 * 16 * 44000 * t
t = (120 * 2 ** 23) / (2 * 16 * 44000)
print(t)
# 720 * 2 ** 23 = 4 * b * 88000 * t
b = (720 * 2 ** 23) / (4 * 88000 * t)
print(b)
'''
# Ответ: 24


# № 8495 Апробация 17.05 (Уровень: Базовый)
# Голосовое сообщение продолжительностью 120 с было записано в формате стерео и оцифровано с глубиной кодирования 16 бит
# и частотой дискретизации 56 000 измерений в секунду. Сжатие данных не использовалось.
# Файл с оцифрованным голосовым сообщением был передан по каналу связи, пропускная способность которого 32 000 бит/с.
# Сколько секунд длилась передача файла? В ответе запишите целое число, единицу измерения указывать не нужно.
'''
t = 120
a = 2
b = 16
c = 56000  # 56 000 измерений в секунду - 56 кГц
I = a * b * c * t  # бит

print(I / 32000)
'''
# Показать ответ: 6720



# Тип 7 № 47211
# Музыкальный фрагмент был записан в формате моно, оцифрован и сохранён в виде файла без использования сжатия данных.
# Размер полученного файла — 28 Мбайт. Затем тот же музыкальный фрагмент был записан повторно
# в формате стерео (двухканальная запись) и оцифрован с разрешением в 3,5 раза выше и частотой дискретизации
# в 2 раза меньше, чем в первый раз. Сжатие данных не производилось.
# Укажите размер полученного при повторной записи файла в Мбайт.
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
# 28 Мбайт = 1 * b * c * t
# x  Мбайт = 2 * 3.5*b * c/2 * t

# 28 = 1
# x = 3.5

x = 28 * 3.5
print(x)
'''
# Ответ: 98


# Тип 7 № 13355
# Музыкальный фрагмент был оцифрован и записан в виде файла без использования сжатия данных.
# Получившийся файл был передан в город А по каналу связи за 15 секунд.
# Затем тот же музыкальный фрагмент был оцифрован повторно с разрешением в 2 раза выше
# и частотой дискретизации в 1,5 раза меньше, чем в первый раз. Сжатие данных не производилось.
# Полученный файл был передан в город Б; пропускная способность канала связи с городом Б в 2 раза выше,
# чем канала связи с городом А. Сколько секунд длилась передача файла в город Б?
# В ответе запишите только целое число, единицу измерения писать не нужно.

# Ответ: 10 - решение пропорцией через картинку



# № 8416 (Уровень: Средний)
# Книгу объёмом 1 Мбайт записали как аудиокнигу.
# Запись велась в формате стерео (2 канала) с частотой 48 кГц и разрешением 24 бит.
# За одну минуту записывалось в среднем 1,5 Кбайт текста.
# Сжатие данных позволило сократить размер полученного звукового файла на 84 %.
# Для удобства использования запись разделили на фрагменты со средним размером 15 Мбайт.
# Определите количество полученных фрагментов.

# За одну минуту записывалось в среднем 1,5 Кбайт текста.
# 1 Мбайт книга / 1,5 Кбайт текста
'''
t = (1 * 2 ** 23) / (1.5 * 2 ** 13)  # мин
t = t * 60  # сек
I = 2 * 48000 * 24 * t
I_size = (I / 100) * 16  # бит
byte = I_size / 2**23  # Мбайт
print(byte / 15)  # получилось фрагментов 
'''
# Показать ответ: 120


# Тип 11 № 26956
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль,
# состоящий из 9 символов и содержащий только заглавные буквы латинского 26-символьного алфавита.
# В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт.
# При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально
# возможным количеством бит. Кроме собственно пароля, для каждого пользователя в системе хранятся
# дополнительные сведения, для чего выделено целое число байт; это число одно и то же для всех пользователей.
# Для хранения сведений о 15 пользователях потребовалось 300 байт.
#
# Сколько байт выделено для хранения дополнительных сведений об одном пользователе?
# В ответе запишите только целое число — количество байт.
'''
symbols = 9
alphabet = 26
# alphabet = 2 ** i
i = 5  # бит на 1 символ
bit = symbols * i
print(bit / 8)
byte = 6

I = 300 / 15  # на хранение информации ободном пользователи
print(I - byte)  # остается на дополнительную информацию о пользователи
'''
# Ответ: 14


# Тип 11 № 7364
# Для регистрации на сайте некоторой страны пользователю требуется придумать пароль. Длина пароля – ровно 7 символов.
# В качестве символов используются десятичные цифры и 26 различных букв местного алфавита,
# причём все буквы используются в двух начертаниях: как строчные, так и прописные (регистр буквы имеет значение!).
#
# Под хранение каждого такого пароля на компьютере отводится минимально возможное и одинаковое целое количество байтов,
# при этом используется посимвольное кодирование и все символы кодируются одинаковым и минимально возможным
# количеством битов. Определите объём памяти, который занимает хранение 65 паролей. (Ответ дайте в байтах.)
'''
symbols = 7
alphabet = 10 + 26*2  # 52
i = 6
bit = i * symbols
print(bit / 8)
byte = 6
print(byte * 65)
'''
# Ответ: 390


# Тип 11 № 27382
# Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код сотрудника и срок действия
# пропуска. Личный код состоит из 14 символов, каждый из которых может быть одной из 26 заглавных латинских букв
# или 10 цифр. Для записи кода на пропуске отведено минимально возможное целое число байтов, при этом используют
# посимвольное кодирование, все символы кодируют одинаковым минимально возможным количеством битов.
# Срок действия записывается как номер года (число от 0 до 99, означающее год от 2000 до 2099)
# и номер месяца (число от 1 до 12).
#
# Номер года и номер месяца записаны на пропуске как двоичные числа, каждое из них занимает
# минимально возможное число битов, а два числа вместе – минимально возможное число байтов.
# Сколько байтов занимает вся информация на пропуске?
# В ответе запишите только целое число – количество байтов.
'''
symbols1 = 14
alphabet1 = 36
i1 = 6
bit1 = symbols1 * i1
print(bit1 / 8)
byte1 = 11

symbols2 = 2
bit2 = 1 * 7 + 1 * 4
print(bit2 / 8)
byte2 = 2

print(byte2 + byte1)
'''
# Ответ: 13


# Тип 9 № 47213
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — в строке только одно число повторяется ровно два раза, остальные числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.
# В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    
    if len(set(M)) == len(M)-1:  # — в строке только одно число повторяется ровно два раза, остальные числа различны;
        repeat = sum(M) - sum(set(M))  # нашли число, которое имеет копию
        if (sum(M) - repeat * 2) / 4 <= repeat * 2:
            count += 1
print(count)
'''

# endregion Урок: ******************************************************************



# todo: Валерия = [1, 2, 3, 5+, 6, 7, 8+, 9+, 11, 12+, 13, 14+, 15+, 16, 17, 18, 19-21, 22, 23, 24, 25]
# на прошлом уроке: Повторяли 7, 11 номера всех типов.
# на следующем уроке:  #todo: Письменные, Эксель: 9, 19-21, 18, 22, 26
