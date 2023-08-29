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

# Тип 5 №7917
# Автомат получает на вход трёхзначное число.
# По этому числу строится новое число по следующим правилам.
#
# 1. Складываются первая и вторая, а также вторая и третья цифры исходного числа.
# 2. Полученные два числа записываются друг за другом в порядке возрастания (без разделителей).
#
# Пример. Исходное число: 348. Суммы: 3+4 = 7; 4+8 = 12. Результат: 712.
#
# Укажите наименьшее число, в результате обработки которого автомат выдаст число 1115.
'''
for num in range(100, 999+1):
    s = str(num)  # '326'
    a = int(s[0]) + int(s[1])
    b = int(s[1]) + int(s[2])
    r = str(min(a, b)) + str(max(a, b))
    if r == '1115':
        print(num)
        break

        
# Вариант 2
for num in range(100, 999+1):
    s = [int(i) for i in str(num)]  # [3, 2, 6]
    a = s[0] + s[1]
    b = s[1] + s[2]
    r = str(min(a, b)) + str(max(a, b))
    if r == '1115':
        print(num)
        break
'''
# Ответ: 296


# Тип 5 № 15101
# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля).
# По этому числу строится новое число по следующим правилам.
#
# 1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# 2. Наименьшая из полученных трёх сумм удаляется.
# 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
#
# Пример. Исходное число: 1982. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 2 = 10.
# Удаляется 10. Результат: 1017.
#
# Укажите наименьшее число, при обработке которого автомат выдаёт результат 1215.
'''
for num in range(1000, 9999+1):
    s = [int(i) for i in str(num)]
    a = s[0] + s[1]
    b = s[1] + s[2]
    c = s[2] + s[3]
    M = sorted([a, b, c])  # сортируем набор цифр по возрастанию
    del M[0]
    r = str(min(M)) + str(max(M))
    if r == '1215':
        print(num)
        break
'''
# Ответ: 1396


# Тип 5 № 18075
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
#
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) находится остаток от деления на 2 суммы двоичных разрядов N,
# полученный результат дописывается в конец двоичной последовательности N.
# б) пункт а повторяется для вновь полученной последовательности.
#
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
# является двоичной записью искомого числа R. Укажите минимальное число R,
# которое превышает 123 и может являться результатом работы алгоритма.
# В ответе это число запишите в десятичной системе.
'''
R = []
for n in range(1, 1000):
    s = bin(n)[2:]  # 1) Строится двоичная запись числа N.
    for _ in range(2):  # б) пункт а повторяется для вновь полученной последовательности.
        s += str(s.count('1') % 2)  # а) находится остаток от деления на 2 суммы двоичных разрядов N,

    r = int(s, 2)
    if r > 123:
        R.append(r)

print(min(R))
'''
# Ответ: 126


# Тип 5 №18582
# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1. Строится двоичная запись числа N без ведущих нулей.
# 2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица.
# Если нулей больше или нулей и единиц поровну, справа приписывается ноль.
# 3. Полученное число переводится в десятичную запись и выводится на экран.
#
# Пример. Дано число N = 13. Алгоритм работает следующим образом.
# 1. Двоичная запись числа N: 1101.
# 2. В записи больше единиц, справа приписывается единица: 11011.
# 3. На экран выводится десятичное значение полученного числа 27.
#
# Какое наименьшее число, превышающее 100, может получиться в результате работы автомата?
'''
R = []
for num in range(1, 10000):
    s = bin(num)[2:]
    if s.count('1') > s.count('0'):
        s += '1'
    else:
        s += '0'
    r = int(s, 2)
    if r > 100:
        R.append(r)
print(min(R))
'''
# Ответ: 103


# Тип 5 №27375
# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1. Строится троичная запись числа N.
# 2. В конец записи (справа) дописывается остаток от деления числа N на 3.
# 3. Результат переводится из троичной системы в десятичную и выводится на экран.
#
# Пример. Дано число N=11. Алгоритм работает следующим образом:
# 1. Троичная запись числа N: 102.
# 2. Остаток от деления 11 на 3 равен 2, новая запись 1022.
# 3. На экран выводится число 35.
#
# Какое наименьшее трёхзначное число может появиться на экране в результате работы автомата?
'''
for n in range(1, 1000):
    num = n
    s = ''
    while num > 0:
        s += str(num % 3)  # s = bin(num)[2:]
        num //= 3
    s = s[::-1]

    s += str(n % 3)

    r = int(s, 3)

    if 100 <= r <= 999:
        print(r)
'''
# Ответ: 103


# Тип 5 №28681
# Автомат обрабатывает натуральное число N (128 ≤ N ≤ 255) по следующему алгоритму:
# 1. Строится восьмибитная двоичная запись числа N.
# 2. Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
# 3. Полученное число переводится в десятичную запись.
# 4. Из исходного числа вычитается полученное, разность выводится на экран.
#
# Пример. Дано число N = 131. Алгоритм работает следующим образом:
# 1. Восьмибитная двоичная запись числа N: 10000011.
# 2. Все цифры заменяются на противоположные, новая запись: 01111100.
# 3. Десятичное значение полученного числа: 124
# 4. На экран выводится число: 131 – 124 = 7.
#
# Какое число нужно ввести в автомат, чтобы в результате получилось 105?
'''
for n in range(128, 255+1):
    s = bin(n)[2:]  # они уже восьмибитные из-за диапазона # 10000001  ->  01111110
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
    r = int(s, 2)
    res = n - r
    if res == 105:
        print(n)
'''
# Ответ: 180





# endregion Урок: ******************************************************************


# todo: Анастасия = [1.1, 2.1, 12.1, 14.1]
# todo:  КЕГЭ  = []
# на прошлом уроке: Повторили 2 номера и разобрали полностью 14 номера, плюс повторили теорию множеств.
# на следующем уроке:
