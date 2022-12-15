
# region Домашка: ******************************************************************************

# Тип 5 № 7690
'''
# Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
# 1. Складываются первая и вторая, а также вторая и третья цифры исходного числа.
# 2. Полученные два числа записываются друг за другом в порядке убывания (без разделителей).
# Укажите наименьшее число, в результате обработки которого автомат выдаст число 157.

for n in range(100,1000):
    m = [int(i) for i in str(n)]
    a = m[0] + m[1]
    b = m[1] + m[2]
    if str(max(a, b)) + str(min(a, b)) == '157':
        print(n)
        break
# 169
'''

# Тип 5 № 18618
'''
# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1.Строится двоичная запись числа N.
# 2.Запись «переворачивается», то есть читается справа налево. Если при этом появляются ведущие нули, они отбрасываются.
# 3.Полученное число переводится в десятичную запись и выводится на экран.
# Какое наибольшее число, не превышающее 100, после обработки автоматом даёт результат 11?

for n in range(101):
    a = bin(n)[2:]
    a = a[::-1]
    if int(a, 2) == 11:
        print(n)
# 52
'''

# Тип 8 № 18558
'''
#Иван составляет 5-буквенные коды из букв И, В, А, Н. Буквы в коде могут повторяться, использовать все буквы не обязательно, 
# но букву И нужно использовать хотя бы один раз. 
# Сколько различных кодов может составить Иван?

s = 'ИВАН'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    if 'И' in (a + b + c + d + e):
                        count += 1
print(count)
# 781
'''

# Тип 8 № 3568
'''
# Все 5-буквенные слова, составленные из букв Б, О, Р, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1.БББББ
# 2.ББББО
# 3.ББББР
# 4.БББОБ

#Запишите слово, которое стоит под номером 240.

s = 'БОР'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    count += 1
                    temp = a + b + c + d + e
                    if count == 240:
                        print(count, temp)
                        break
# РРРОР
'''

# Тип 8 № 3195
'''
# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Вот начало списка:
# 1.ААААА
# 2.ААААК
# 3.ААААР
# 4.ААААУ
# 5.АААКА

# Запишите слово, которое стоит на 350-м месте от начала списка.

s = 'АКРУ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    count += 1
                    temp = a + b + c + d + e
                    if count == 350:
                        print(count, temp)
                        break
# КККУК
'''

# Тип 8 № 10500
'''
# Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 5. 
# Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно три раза, 
# а каждая из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

s = '12345'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('1') == 3:
                        count += 1
                        print(count)
# 160
'''

# endregion Домашка: ******************************************************************************




# region Урок: ******************************************************************************


# Тип 12 № 10504
'''
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 1000 идущих подряд цифр 9?
# В ответе запишите полученную строку.

# ПОКА нашлось (999) ИЛИ нашлось (888)
#   ЕСЛИ нашлось (888)
#     ТО заменить (888, 9)
#   ИНАЧЕ заменить (999, 8)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА

s = '9' * 1000

while '999' in s or '888' in s:
    if '888' in s:
        s = s.replace('888', '9', 1)
    else:
        s = s.replace('999', '8', 1)

print(s)
'''
# Ответ: 8899


# Тип 12 № 25844
'''
# На вход приведённой ниже программе поступает строка, начинающаяся с символа «>», а затем содержащая 11 цифр 1, 12 цифр 2 и 30 цифр 3, расположенных в произвольном порядке.
#
# Определите сумму числовых значений цифр строки, получившейся в результате выполнения программы.

# ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
#     ЕСЛИ нашлось (>1)
#         ТО заменить (>1, 22>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>2)
#         ТО заменить (>2, 2>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>3)
#         ТО заменить (>3, 1>)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА

s = '>' + '3' * 30 + '2' * 12 + '1' * 11

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)

print(s)

# Вариант 1
print(s.count('1') + s.count('2') * 2 + s.count('3') * 3)

# Вариант 2
summ = 0
for x in s[:-1]:
    summ += int(x)
print(summ)

# Вариант 3
print(sum([int(i) for i in s[:-1]]))
'''



# Тип 12 № 46970
''''
# Дана программа для редактора:
#     ПОКА НЕ нашлось (00)
#         заменить (01, 210)
#         заменить (02, 3101)
#         заменить (03, 2012)
#     КОНЕЦ ПОКА
#
# Известно, что исходная строка начиналась с нуля и заканчивалась нулём, а между ними содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка, содержащая 70 единиц, 56 двоек и 23 тройки. Сколько цифр было в исходной строке?

for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z + '0'

            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)

            if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
                print(1 + x + y + z + 1, x, y, z)
'''
# Ответ: 40


# Тип 12 № 40987
'''
# Дана программа для редактора:
#
#     ПОКА нашлось (1111)
#         заменить (1111, 22)
#         заменить (222, 1)
#     КОНЕЦ ПОКА
#
# Известно, что исходная строка содержала больше 200 единиц и не содержала других цифр.
# При какой наименьшей длине исходной строки результат работы данной программы будет содержать наименьшее возможное число единиц?

mini = 1000000
for n in range(200+1, 400):
    s = '1' * n

    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)

    if mini > s.count('1'):
        mini = s.count('1')
        print(n, s, mini)
'''
# Ответ: 204




# Тип 12 № 47216
'''
# Дана программа для Редактора:
#
# ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>0)
#     ЕСЛИ нашлось (>1)
#         ТО заменить (>1, 22>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>2)
#         ТО заменить (>2, 2>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>0)
#         ТО заменить (>0, 1>)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
#
# На вход приведённой выше программе поступает строка, начинающаяся с символа «>», а затем содержащая 39 цифр «0», n цифр «1» и 39 цифр «2», расположенных в произвольном порядке.
#
# Определите наименьшее значение n, при котором сумма числовых значений цифр строки, получившейся в результате выполнения программы, является простым числом.

def Simpler(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

for n in range(0, 1000):
    s = '>' + '0' * 39 + '1' * n + '2' * 39

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    summ = s.count('1') + s.count('2') * 2
    if Simpler(summ) == True:
        print(n)
        break
'''
# Ответ: 5


# P < N < Z < Q < I < R < C  # множество простых чисел
# Простое число - это число имеющее только лишь два делителя: 1 и самом себя

# N = [1, 2, 3, ..., + бесконечности) - множество натуральных
# Z = (- бесконечности, ..., -3, -2, -1, 0, 1, 2, 3, ...,  + бесконечности) - множество целых чисел
# N in Z, N < Z
# Q = (- бесконечности, ..., -3.5, -2, -1/2, 0, 1/2, 2, 4.7, ...,  + бесконечности) - множество рациональных чисел
# N in Z in Q, N < Z < Q
# I = (- бесконечности, ..., -3.555(5), -1/2, pi, sqrt(3), ...,  + бесконечности) - множество иррациональных чисел
# N in Z in Q in I, N < Z < Q < I
# R = (- бесконечности, ..., все предыдущие, ...,  + бесконечности) - множество вещественных (или действительных) чисел
# (N in Z in Q in I) in R, N < Z < Q < I < R

# C > R - множество комплексных чисел


# endregion Урок: ******************************************************************************


#todo: Дмитрий = [2, 5, 8, 12, 14+], на следующем уроке: Переходим к функциям и решать 23, 16, 15, 25