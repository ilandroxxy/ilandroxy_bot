

# Тип 5 № 18554
# Автомат обрабатывает натуральное число N по следующему алгоритму:
#
# 1. Строится двоичная запись числа N без ведущих нулей.
# 2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица.
# Если нулей больше или нулей и единиц поровну, справа приписывается ноль.
# 3. Полученное число переводится в десятичную запись и выводится на экран.

# Пример. Дано число N = 13. Алгоритм работает следующим образом.
# 1. Двоичная запись числа N: 1101.
# 2. В записи больше единиц, справа приписывается единица: 11011.
# 3. На экран выводится десятичное значение полученного числа 27.
#
# Какое наименьшее число, превышающее 80, может получиться в результате работы автомата?
'''
R = []
for x in range(1, 1000):
    s = bin(x)[2:]

    if s.count('1') > s.count('0'):
        s = s + '1'
    else:
        s = s + '0'
    r = int(s, 2)

    if r > 80:
        R.append(r)
print(min(R))
'''
'''
R = []
for x in range(1, 1000):
    M = []
    while x > 0:
        M.append(x % 2)  # Строится двоичная запись числа N без ведущих нулей.
        x = x // 2  # x //= 2
    M.reverse()
    if M.count(1) > M.count(0):
        M.append(1)
    else:
        M.append(0)
    r = 0
    M.reverse()
    for i in range(0, len(M)):
        r += M[i] * 2 ** i

    if r > 80:
        R.append(r)
print(min(R))
'''



# Тип 5 № 27402

# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#
# 1. Строится двоичная запись числа N.
# 2. К этой записи дописываются справа ещё два разряда по следующему правилу:
#
# а) складываются все цифры двоичной записи числа N, и остаток от деления суммы на 2
# дописывается в конец числа (справа). Например, запись 11100 преобразуется в запись 111001;
#
# б) над этой записью производятся те же действия — справа дописывается остаток от деления суммы её цифр на 2.
#
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной
# записью искомого числа R. Укажите такое наименьшее число N, для которого результат работы данного алгоритма больше числа 77.
# В ответе это число запишите в десятичной системе счисления.

#
# for n in range(1, 1000):
#     s = bin(n)[2:]
#     for i in range(2):
#         s = s + str((s.count('1') + s.count('0')) % 2)
#     r = int(s, 2)
#     if r > 77:
#         print(n)
#         break
'''
M = list(map(str.upper, 'beegeek'))
print(M)

my_dict = {'bee': 1, 'geek': 2}
print(my_dict['geek'])
'''
numbers = (1, 2, 3, 4)

next(numbers)
next(numbers)

print(next(numbers))



# на прошлом уроке:  Собрали проект для изучения aiogram. Реализовали команду /start и начали обсуждать/создавать классы для работы с текстовыми сообщениями.
# на следующем уроке: