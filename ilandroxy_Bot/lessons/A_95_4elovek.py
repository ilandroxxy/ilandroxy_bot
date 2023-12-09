# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Тип 5 №18618
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится двоичная запись числа N.
# 2. Запись «переворачивается», то есть читается справа налево.
# Если при этом появляются ведущие нули, они отбрасываются.
# 3. Полученное число переводится в десятичную запись и выводится на экран.
#
# Какое наибольшее число, не превышающее 100, после обработки автоматом даёт результат 11?
'''
for n in range(1, 100):
    s = bin(n)[2:]  # 1. Строится двоичная запись числа N.
    s = s[::-1]  # 2. Запись «переворачивается», то есть читается справа налево.
    r = int(s, 2)  # 3. Полученное число переводится в десятичную запись и выводится на экран.
    if r == 11:
        print(n)
'''
# Ответ: 52


# Тип 5 №18812
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) в конец числа (справа) дописывается 1, если число единиц в двоичной записи числа чётно, и 0,
# если число единиц в двоичной записи числа нечётно;
# б) к этой записи справа дописывается 1, если остаток от деления количества единиц на 2
# равен 0, и 0, если остаток от деления количества единиц на 2 равен 1.
# Полученная таким образом запись является двоичной записью искомого числа R.
#
# Укажите минимальное число R, которое превышает 54 и может являться результатом работы алгоритма.
# В ответе это число запишите в десятичной системе.
'''
for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = s + '1'
    else:
        s = s + '0'
    if s.count('1') % 2 == 0:
        s = s + '1'
    else:
        s = s + '0'
    r = int(s, 2)

    if r > 54:
        print(r)
        exit()
'''
# Ответ: 56


# Тип 5 №33750
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
# 1. Строится двоичная запись числа N.
# 2. Вместо последней (самой правой) двоичной цифры дважды записывается вторая слева цифра двоичной записи.
# 3. Результат переводится в десятичную систему.
#
# При каком наименьшем числе N в результате работы алгоритма получится R > 76?
# В ответе запишите это число в десятичной системе счисления.


# Тип 5 №26978
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются разряды по следующему правилу:
# а) если число четное, то к двоичной записи числа в конце дописываются 1 и 0;
# б) если число нечетное, то к двоичной записи числа в конце дописывается 01.
#
# Полученная таким образом запись является двоичной записью искомого числа R.
# Укажите наибольшее число R меньшее 109, которое может получиться после обработки этого алгоритма.
# В ответе это число запишите в десятичной системе.


# endregion Урок: ***************************************************************


# Сева = [2.1, 6.1, 5.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
