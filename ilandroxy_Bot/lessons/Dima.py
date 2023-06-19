
# region Домашка: ******************************************************************************



# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************


# № 5909 (Уровень: Сложный)
# (Д. Тараскин) Программа перебирает числа больше 10**9 и выбирает из них числа-палиндромы,
# в которых никакие две четные и две нечетные цифры не стоят рядом и наибольший делитель
# (отличный от 1 и самого числа) кратен 7. Выведите первые 5 чисел, которые выберет программа,
# и для каждого числа выведите наибольший делитель.
'''
def d(x):
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            return x // j
    return 0

k = 0
for n in range(10**4+1, 10**5, 2):
    for a in '0123456789':
        x = int(str(n) + a + str(n)[::-1])
        if all((int(str(x)[j]) + int(str(x)[j + 1])) % 2 != 0 for j in range(len(str(x)) - 1)):
            dl = d(x)
            if dl != 0 and dl % 7 == 0:
                k += 1
                print(x, dl)
                if k == 5:
                    exit()
'''
# Показать ответ
# 10101010101 3367003367
# 10121212101 3373737367
# 10141414101 3380471367
# 10161616101 3387205367
# 10167076101 3389025367


# Тип 11 № 11349
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 9 символов.
# Из соображений информационной безопасности каждый пароль должен содержать хотя бы 1 десятичную цифру, как прописные,
# так и строчные латинские буквы (в латинском алфавите 26 букв), а также не менее 1 символа
# из 6-символьного набора: «&», «#», «$», «*», «!», «@». В базе данных для хранения сведений
# о каждом пользователе отведено одинаковое и минимально возможное целое число байт.
# При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным
# количеством бит. Кроме собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения,
# для чего выделено целое число байт; это число одно и то же для всех пользователей.
#
# Для хранения сведений о 20 пользователях потребовалось 500 байт.
# Сколько байт выделено для хранения дополнительных сведений об одном пользователе?
# В ответе запишите только целое число – количество байт.
#
# Примечание. В латинском алфавите 26 букв.
'''
from math import *
symbols = 9
alphabet = 6 + 10 + 26 * 2
i = 7
bit = i * symbols
byte = ceil(bit / 8)
I = 500 / 20
dop = I - byte
print(dop)
'''
# Ответ: 17

# Тип 11 № 27298
# Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код сотрудника
# и срок действия пропуска. Личный код состоит из 19 символов, каждый из которых может быть одной из
# 26 заглавных латинских букв. Для записи кода на пропуске отведено минимально возможное целое число байтов,
# при этом используют посимвольное кодирование, все символы кодируют одинаковым минимально возможным количеством битов.
# Срок действия записывается как номер года (число от 0 до 60, означающее год от 2000 до 2060)
# и номер дня в году (число от 1 до 366).

# Номер года и номер дня записаны на пропуске как двоичные числа, каждое из них занимает
# минимально возможное число битов, а два числа вместе — минимально возможное число байтов.
# Сколько байтов занимает вся информация на пропуске? В ответе запишите только целое число — количество байтов.
'''
from math import *
symbols_kod = 19
alphabet_kod = 26
i_kod = 5
bit_kod = i_kod * symbols_kod
byte_kod = ceil(bit_kod / 8)
print(byte_kod)

bit_srok = 1 * 6 + 1 * 9
byte_srok = ceil(bit_srok / 8)
print(byte_srok)
'''
# Ответ: 14



# № 6592 Пробник ИМЦ СПб(Уровень: Базовый)
# При регистрации в компьютерной системе каждому объекту присваивается идентификатор,
# содержащий только десятичные цифры и символы из 1024-символьного специального алфавита (прописные и строчные).
# В базе данных для хранения каждого идентификатора отведено одинаковое и минимально возможное целое число байт.
# При этом используется посимвольное кодирование идентификаторов, все символы кодируются одинаковым и минимально
# возможным количеством бит. Известно, что для хранения 256 идентификаторов выделено 6 Кбайт памяти.
# Укажите максимально допустимую длину идентификатора пользователя.
'''
alphabet = 1024 * 2 + 10
i = 12
byte = (6 * 2 ** 10) / 256
bit = byte * 8
symbols = bit / i
print(symbols)
'''
# Ответ: 16


# endregion Урок: ******************************************************************************


# todo:    Дмитрий   = [1, 2, 3, 4, 5+, 6, 7, 8+, 9.1, 10, 11, 12, 13, 14+, 15+, 16+, 17, 18, 19-21, 22, 23, 24, 25.2]
# todo: Дмитрий КЕГЭ = [5, 14, 16, 25]
# на прошлом уроке:
# на следующем уроке:  # todo: Тип 26 №  55822, Тип 26 № 48474 |
