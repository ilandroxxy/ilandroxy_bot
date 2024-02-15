# region Домашка: ******************************************************************
'''
R = []
for n in range(9, 1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '00'
    else:
        b = b + bin(b.count('1'))[2:]
    r = int(b, 2)
    if r > 88 and r > 88:
        R.append([r, n])
print(min(R)[1])
'''


# КЕГЭ № 4868 (Уровень: Сложный)
# Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
# 1. Вычисляется сумма чётных цифр в десятичной записи числа N.
# Если чётных цифр в записи нет, сумма считается равной нулю.
# 2. Вычисляется сумма цифр, стоящих на чётных местах в десятичной
# записи числа N без ведущих нулей. Места отсчитываются слева направо
# (от старших разрядов к младшим, начиная с единицы).
# Если число однозначное (цифр на чётных местах нет), сумма считается равной нулю.
# 3. Результатом работы алгоритма становится модуль разности полученных двух сумм.
#
# При каком наименьшем N в результате работы алгоритма получится R = 13?
'''
for n in range(2, 1000):
    s = str(n)
    summa1 = sum([int(x) for x in s if int(x) % 2 == 0 or 'x' in '02468'])
    summa2 = sum([int(s[i]) for i in range(len(s)) if (i+1) % 2 == 0])
    r = abs(summa1 - summa2)  # abs - модуль числа

    if r == 13:
        print(n)
        break
'''
# Ответ: 618


# КЕГЭ № 4317 Пробный 06.2022 /dev/inf advanced (Уровень: Сложный)
# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1. Строится пятеричная запись числа N.
# 2. К полученной записи дописываются разряды.
# Если последняя цифра в пятеричной записи четная,
# справа дописывается 2, если нечетная – слева дописывается 2 и справа 3.
# 3. Результат переводится в десятичную систему и выводится на экран.
#
# В результате работы автомата на экране появилось число, меньшее 1000.
# Для какого наибольшего значения N данная ситуация возможна?

'''
def my_bin(number, system):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    s = ''
    while number > 0:
        s += alphabet[number % system]
        number //= system
    return s[::-1]
'''

'''
def my_bin(number, system):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    s = ''
    while number > 0:
        s = alphabet[number % system] + s
        number //= system
    return s


R = []
for n in range(1, 1000):
    s = my_bin(n, 5)
    if s[-1] in '024':
        s += '2'
    else:
        s = '2' + s + '3'
    r = int(s, 5)
    if r < 1000:
        R.append(n)

print(max(R))
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Тип 8 №3700
# Все 5-буквенные слова, составленные из букв Б, К, Ф, Ц, записаны в алфавитном порядке
# и пронумерованы. Вот начало списка:
# 1. БББББ
# 2. ББББК
# 3. ББББФ
# 4. ББББЦ
# 5. БББКБ
# Запишите слово, которое стоит на 486-м месте от начала списка.
'''
# Вариант 1
s = sorted('БКФЦ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if num == 486:
                        print(num, slovo)
                    num += 1

# Вариант 2
from itertools import product
num = 1
for x in product(sorted('БКФЦ'), repeat=5):
    slovo = ''.join(x)
    if num == 486:
        print(num, slovo)
    num += 1
'''
# Ответ: КЦФКК


# Тип 8 №18079
# Вася составляет 6-буквенные слова из букв К, О, Т.
# Причем буква К используется в каждом слове ровно 1 раз.
# Остальные буквы могут быть использованы любое количество раз,
# в том числе совсем отсутствовать. Сколько слов может составить Вася?
# Словом называется любая буквенная комбинация, не обязательно
# осмысленное слово русского языка.
'''
count = 0
s = 'КОТ'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if slovo.count('К') == 1:
                            count += 1
print(count)

from itertools import product
count = 0
for x in product('КОТ', repeat=6):
    slovo = ''.join(x)
    if slovo.count('К') == 1:
        count += 1
print(count)
'''
# Ответ: 192


# Тип 8 №59832
# Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления.
# Сколько различных чисел может составить Игорь, в которых ровно две цифры 3
# и нечётные цифры не стоят рядом с цифрой 2?
'''
s = '012345678'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    number = a + b + c + d + e
                    if a != '0':
                        if number.count('3') == 2:
                            if all(p not in number for p in '12 21 32 23 52 25 72 27'.split()):
                                count += 1
print(count)
'''

'''
from itertools import product
count = 0
for x in product('012345678', repeat=5):
    number = ''.join(x)
    if number[0] != '0':
        if number.count('3') == 2:
            if all(p not in number for p in '12 21 32 23 52 25 72 27'.split()):
                count += 1
print(count)
'''
# Ответ: 3352

# Тип 8 №27295
# Света составляет 5-буквенные коды из букв С, В, Е, Т, А.
# Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные.
# Сколько различных кодов может составить Света?
'''
count = 0
s = 'СВЕТА'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):
                        # if 'ЕА' not in slovo and 'АЕ' not in slovo:
                        if all(p not in slovo for p in 'ЕА АЕ'.split()):
                            count += 1
print(count)


from itertools import permutations
count = 0
for x in permutations('СВЕТА'):
    slovo = ''.join(x)
    if 'ЕА' not in slovo and 'АЕ' not in slovo:
        count += 1
print(count)
'''
# Ответ: 72


# endregion Урок: ******************************************************************

# Лев = [2.1, 5.1, 6.1, 8.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
