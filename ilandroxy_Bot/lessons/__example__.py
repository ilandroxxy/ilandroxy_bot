
'''
MondayStudents = {1477701439: ["Valeria.py", '15:00', 1000, "Валерия", 1000],
                  768734764: ["Bogdan.py", '16:30', 3600//4, "Богдан", 4],
                  811476623: ["Georgie.py", "20:00", 3040//4, "Георгий", 4],
                  659796558: ['Ivan.py', '21:00', 1000, "Иван", 1000],
                  826004697: ['Nikita.py', '22:00', 3040//4, "Никита", 4]}
TuesdayStudents = {1949653479: ['Yanina.py', '10:00', 4080//8, "Янина", 8],
                   1649389148: ['Slava.py', "15:00", 6800//8, "Слава", 8],
                   789322200: ['Katya.py', "16:00", 3600//4, "Екатерина", 4],
                   1208542295: ['Sasha.py', '19:00', 4000//8, "Александра", 6],
                   879517768: ['Grisha.py', "20:00", 1000, 'Гриша', 1000],
                   804184353: ['Islam.py', '21:00', 3600//4, "Ислам", 4],
                   1537718492: ['Aleksandr.py', '22:00', 5760//8, "Александр", 8]}
ThursdayStudents = {1949653479: ['Yanina.py', '10:00', 4080//8, "Янина", 8],
                    5242003138: ['Dima.py', '16:00', 1000, "Дмитрий", 1000],
                    1187852992: ['Aleksandr_2.py', "17:00", 6800//8, "Александр2", 6],
                    1454117859: ['Diana', "19:00", 4320//8, "Диана", 8],
                    811476623:  ["Georgie.py", "20:00", 3040//4, "Георгий", 4],
                    799740089: ["Bulat.py", "21:00", 2280//4, "Булат", 4],
                    1537718492: ["Aleksandr.py", "22:00", 5760//8, "Александр", 8]}
FridayStudents = {644645774: ['Stasya.py', "16:00", 6800//8, "Стася", 8],
                  719571990: ['Stepan.py', "17:00", 6800//8, "Степан", 4],
                  986539147: ['Danil.py', '19:00', 6800 // 8, "Данил", 8],
                  659796558: ['Ivan.py', '20:00', 1000, "Иван", 1000],
                  1029532016: ['Maria.py', "21:00", 6800//8, "Мария", 8],
                  1649389148: ['Slava.py', "22:00", 6800//8,  "Слава", 8]}
SaturdayStudents = {438879394: ['ilya.py', '14:00', 0, "Илья", 4],
                    1347259493: ['Andrey.py', '15:00', 1500, 'Андрей', 1000],
                    1454117859: ['Diana', "17:00", 4320//8, "Диана", 8],
                    5148819382: ['Tatyana.py', "19:00", 6800//8, "Татьяна", 8],
                    1763801774: ['Kirill.py', "20:00", 6800//8, "Кирилл", 8],
                    1314375732: ['Vasiliy.py', "21:00", 6800//8, "Василий", 7],
                    871237277: ['Vladek.py', "22:00", 6800//8, "Владек", 8]}


Students = MondayStudents | TuesdayStudents | ThursdayStudents | FridayStudents | SaturdayStudents

sorted(Students.items())

for key in sorted(Students:
    print(Students[key][3], key)
'''

# region Пост: Способы получить сумму цифр строки
'''
# Способы получить сумму цифр строки
s = '11122233344'

# Вариант 1
M = [int(i) for i in s]  # разобьем строку на список целочисленных значений
summ1 = sum(M)  # через встроенную функцию sum() получим сумму строки
print(summ1)  # выводим полученную сумму цифр строки


# Вариант 1
summ2 = 0  # создаем счетчик для подсчета суммы
for i in s:  # пробегаем строку по переменной i
    summ2 += int(i)  # добавляем в счетчик переводя string цифру i в целочисленное int число
print(summ2)  # выводим полученную сумму цифр строки
# аналогичный трюк можно провернуть с индексным циклом for


# Вариант 3
summ3 = s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4
print(summ3)  # у каждой цифры есть свой вес - считаем кол-во цифр и умножаем на ее вес


# Вариант 4
summ4 = 0  # создаем счетчик для подсчета суммы
n = int(s)  # переводим строку в число используя функцию int()
while n > 0:  # пока n не станет нулем производим следующие действия:
    summ4 += n % 10  # к счетчику добавляем остаток от деления числа на 10
    n //= 10  # делим число на 10, чтобы избавиться от этого остатка
print(summ4)  # выводим полученную сумму цифр строки
'''
# endregion Пост: Способы получить сумму цифр строки


# region Пост: Сравнение решения 14 номера с РЕШУ ЕГЭ и через списки

# Два варианта решений 14 номера (старого типа) через строки и списки
'''
# Тип 14 № 29662
# Значение выражения 81**17 + 3**24 − 45 записали в системе счисления с основанием 9.
# Сколько цифр «8» содержится в этой записи?

x = 81 ** 17 + 3 ** 24 - 45  # посчитали значение выражения
s = ""  # создали пустую строку для сбора остаток от деления
while x != 0:  # пока x не занулится будем делать следующие действия:
    s += str(x % 9)  # в строку добавляем остаток от деления x на систему счисления 9 переводя его в строку
    x //= 9  # обязательно получаем частное от деления, чтобы не нарушать алгоритм
s = s[::-1]  # через срезы пробегаем всю строку в обратном порядке - переворачиваем остатки от делений
print(s.count("8"))  # через универсальный метод .count() выводим кол-вол 8-ок в строке s


x = 81 ** 17 + 3 ** 24 - 45  # посчитали значение выражения
M = []  # создали пустой список для сбора остаток от деления
while x > 0:  # пока x не занулится будем делать следующие действия:
    M.append(x % 9)   # через метод списков .append() добавляем остаток от деления
    x //= 9  # обязательно получаем частное от деления, чтобы не нарушать алгоритм
M.reverse()  # через метод списков .reverse() переворачиваем остатки от делений
print(M.count(8))  # через универсальный метод .count() выводим кол-вол 8-ок в списке M
'''
# endregion Пост: Сравнение решения 14 номера с РЕШУ ЕГЭ и через списки


# region Пост: Решение новых 14 номеров 2023 года

# Тип 14 № 48394
'''
# Операнды арифметического выражения записаны в системе счисления с основаниями 15 и 13:
#
# 4Cx4_15 + x62A_13
#
# В записи чисел переменной x обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 121.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 121.

for x in '0123456789abcde':  # алфавит выбираем по наименьшей системе счисления (числа из наибольшей не подходят)
    a = int(f'4c{x}4', 15)  # через f-строки перебираем всевозможные строки и переводим их в целочисленный int()
    b = int(f'{x}62a', 13)  # не забывайте указывать системы счисления для перевода в соответствии с условием
    if (a + b) % 121 == 0:  # если полученная сумма кратна 121 (остаток от деления равен нулю)
        print((a + b) // 121)  # то выводим частное от деления
        break  # так как по условию просят найти наименьшее, то можем выйти из цикла после первого вывода
'''
# Ответ: 234

# Тип 14 № 48386
'''
# Операнды арифметического выражения записаны в системах счисления с основаниями 15 и 16:

# 90x4y_15 + 91xy2_16

# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите наименьшие значения x и y, при которых значение данного арифметического выражения кратно 56.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 56.

for x in '0123456789abcde':  # алфавит выбираем по наименьшей системе счисления (числа из наибольшей не подходят)
    for y in '0123456789abcde':  # так как выражение состоит из двух неизвестных, то перебираем две переменные
        a = int(f'90{x}4{y}', 15)
        b = int(f'91{x}{y}2', 16)  # через f-строки перебираем всевозможные строки и переводим их в целочисленный int()
        if (a + b) % 56 == 0:
            print((a + b) // 56)   # выводим частное от деления, если выполняется условие
            exit()  # break не работает во вложенных циклах, поэтому после первого вывода прервем программу
# Ответ: 18754
'''

# endregion Пост: Решение новых 14 номеров 2023 года


# region Пост: Пример решения двух 5-х номеров двумя вариантами

# Условие:

# Тип 5 № 14767
# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля).
# По этому числу строится новое число по следующим правилам.
#
# 1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# 2. Наименьшая из полученных трёх сумм удаляется.
# 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
#
# Пример. Исходное число: 1984. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 4 = 12.
# Удаляется 10. Результат: 1217.
#
# Укажите наименьшее число, при обработке которого автомат выдаёт результат 613.

'''
# Вариант 1
for n in range(1000, 10000):  # пробегаем все четырёхзначные целые числа
    M = [int(i) for i in str(n)]  # используя списочное выражение разбиваем число на список чисел

    # через индексы списка складываются
    a = M[0] + M[1]  # первая и вторая
    b = M[1] + M[2]  # вторая и третья
    c = M[2] + M[3]  # третья и четвёртая цифры

    maxi = max(a, b, c)  # убирать минимальную необязательно, нам в любом случае нужны два наибольших числа
    sred = (a + b + c) - (max(a, b, c) + min(a, b, c))  # среднее число – это сумма минус (min и max)

    r = str(sred) + str(maxi)  # так как по условию числа записываются друг за другом, то переводим их в str
    if r == '613':  # результат конечно же сравниваем тоже со строкой str
        print(n)
        break  # по условию ищем наименьшее число, достаточно вывести первое, затем выходим из цикла
# Ответ: 1067
'''

''' 
# Вариант 2
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # создаем список целых чисел из десятичной системы счисления

for x1 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # для x1 убираем 0, так как первая цифра не может быть нулем
    for x2 in s:
        for x3 in s:  # это стандартный перебор всех возможных значений через вложенные циклы
            for x4 in s:  # так как по условию цифры четырехзначные, то циклов четыре штуки

                # здесь можно обойтись без индексов, поэтому складываются
                a = x1 + x2  # первая и вторая
                b = x2 + x3  # вторая и третья
                c = x3 + x4  # третья и четвёртая цифры

                maxi = max(a, b, c)  # остальное фрагмент кода без изменений, как в варианте 1
                sred = (a + b + c) - (max(a, b, c) + min(a, b, c))

                r = str(sred) + str(maxi)
                if r == '613':
                    print(x1, x2, x3, x4)  # последовательность переменных это и есть число
                    exit()
# Ответ: 1067
'''

# endregion Пост: Пример решения двух 5-х номеров двумя вариантами


# region Пост: Заменить все 0 на 1, 1 на 0 в двоичной системе счисления
'''
n = 14
# Вариант 1
s = bin(n)[2:]  # 1110 переводим число в двоичную систему счисления (получаем str)
s = s.replace('0', '*')  # через метод replace заменяем одни элементы на другие
s = s.replace('1', '0')  # через классический тройной swap меням '0' на '1' и наоборот
s = s.replace('*', '1')  # для тройного swap необходима промежуточная переменная ('*')
print(s)  # 0001

# Вариант 2
s = bin(n)[2:]  # 1110 переводим число в двоичную систему счисления (получаем str)
M = [i for i in s]  # разбиваем строку на список строк
for i in range(0, len(M)):  # пробегаем список строк через их индексы
    if M[i] == '0':  # если видим '0', то по индексу меняем на противоположное значение
        M[i] = '1'
    else:
        M[i] = '0'  # если видим '1', то по индексу меняем на противоположное значение
s = ''.join(M)  # список строк мы объединяем в общую строку s
print(s)  # 0001

# Вариант 3
s = bin(n)[2:]  # 1110
for i in range(0, len(s)):  # сразу бежим по строке через индексы
    if s[i] == '0':  # если видим '0', то по индексу меняем на противоположное значение
        s = s[:i] + '1' + s[i+1:]  # через срезы создаю новую строку за исключением i
    else:
        s = s[:i] + '0' + s[i + 1:]  # делаем аналогичное действие с '1'
print(s)  # 0001
'''
# endregion Пост: Заменить все 0 на 1, 1 на 0 в двоичной системе счисления


# Тип 5 № 17324
# Сколько разных значений будет показано на экране автомата при последовательном вводе всех натуральных чисел от 10 до 1000?



# Как убрать первую единицу
# s = '10001000'  # при переводе 136
#
# s = s[1:]
# print(int(s, 2))
#
# s = '10001000'
#
# s = s.replace('1', '', 1)  # избавились от первой единицы
# print(int(s, 2))
#
#
# x = int(input())
# print(x)



# Тип 24 № 27696
'''
# Текстовый файл состоит не более чем из 10**6 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов L.
# Хотя бы один символ L находится в последовательности.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
f = open('24.txt', 'r')
s = f.readline()
print(s)


# Вариант 1
print(max([len(i) for i in open('24.txt', 'r').readline().replace('D', ' ').replace('R', ' ').split()]))

# Вариант 2
f = open('24.txt', 'r')
s = f.readline()
s = s.replace('D', ' ')
s = s.replace('R', ' ')
M = s.split()
A = [len(i) for i in M]
print(max(A))


# Вариант 3
f = open('24.txt').readline()
k = 1
m = 1
for i in range(len(f)-1):
    if f[i] == 'L' and f[i+1] == 'L':
        k += 1
        m = max(m, k)
    else:
        k = 1
print(m)
'''
# Ответ: 7






# Тип 5 № 46963
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. Вычисляется количество единиц, стоящих на чётных местах в двоичной записи числа N без ведущих нулей,
# и количество нулей, стоящих на нечётных местах.
# Места отсчитываются слева направо (от старших разрядов к младшим, начиная с единицы).
# 3. Результатом работы алгоритма становится модуль разности полученных двух чисел.
#
# Пример. Дано число N = 39. Алгоритм работает следующим образом:
# 1. Строится двоичная запись: 39_10 = 100111_2.
# 2. Выделяем единицы на чётных и нули на нечётных местах: 100111. На чётных местах стоят две единицы, на нечётных — один ноль.
# 3. Модуль разности равен 1.
# Результат работы алгоритма R = 1.
#
# При каком наименьшем N в результате работы алгоритма получится R = 5?

# Вариант 1
'''
for n in range(2, 100000+1):
    s = bin(n)[2:]

    k1 = 0
    k0 = 0
    for i in range(0, len(s)):
        if i % 2 == 0 and s[i] == '1':
            k1 += 1
        if i % 2 != 0 and s[i] == '0':
            k0 += 1


    r = abs(k0 - k1)

    if r == 5:
        print(n)
        break
'''

# Вариант 2
'''
for n in range(2, 100000 + 1):
    s = bin(n)[2:]

    k1 = [s[i] for i in range(0, len(s)) if i % 2 == 0].count('1')
    k0 = [s[i] for i in range(0, len(s)) if i % 2 != 0].count('0')

    if abs(k0 - k1) == 5:
        print(n)
        break
'''
# Ответ: 511










# Тип 5 № 16882
# Автомат обрабатывает натуральное число N (0 ≤ N ≤ 255) по следующему алгоритму:
#
# 1. Строится восьмибитная двоичная запись числа N.
# 2. Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
# 3. Полученное число переводится в десятичную запись.
# 4. Из нового числа вычитается исходное, полученная разность выводится на экран.
#
# Пример. Дано число N = 13. Алгоритм работает следующим образом.
#
# 1. Восьмибитная двоичная запись числа N: 00001101.
# 2. Все цифры заменяются на противоположные, новая запись 11110010.
# 3. Десятичное значение полученного числа 242.
# 4. На экран выводится число 242 − 13 = 229.
#
# Какое число нужно ввести в автомат, чтобы в результате получилось 111?

# Вариант 1
'''
for n in range(0, 255+1):
    s = bin(n)[2:]

    while len(s) != 8:
        s = '0' + s

    z = ''
    for x in s:
        if x == '0':
            z += '1'
        else:
            z += '0'

    r = int(z, 2) - n

    if r == 111:
        print(n)
'''

# Вариант 2
'''
for n in range(0, 255+1):
    s = bin(n)[2:]

    while len(s) != 8:
        s = '0' + s

    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')

    r = int(s, 2) - n

    if r == 111:
        print(n)
'''

# Вариант 2
'''
for n in range(0, 255+1):
    x = n

    M = []
    while x > 0:
        M.append(x % 2)
        x //= 2
    M.reverse()

    while len(M) != 8:
        M.reverse()
        M.append(0)
        M.reverse()

    for i in range(0, len(M)):
        if M[i] == 0:
            M[i] = 1
        else:
            M[i] = 0

    sum = 0
    M.reverse()
    for i in range(0, len(M)):
        sum += M[i] * 2 ** i

    r = sum - n

    if r == 111:
        print(n)
'''
# Ответ: 72



# Тип 25 № 35999
# Найдите все натуральные числа N, принадлежащие отрезку [200_000_000;400_000_000],
# которые можно представить в виде N=2**m·3**n, где m — чётное число, n — нечётное число.
# В ответе запишите все найденные числа в порядке возрастания.

# print(2**28)
# print(3**17)
'''
for m in range(2, 28+1, 2):
    for n in range(1, 17+1, 2):
        N = 2**m * 3**n
        if 200_000_000 <= N <= 400_000_000:
            print(N)
'''
# Ответ:
# 229582512
# 322486272
# 254803968
# 201326592

'''
Alphabet = '0123456789bcdefghijklmpqrsuvwxyz'
R = []
n = int(input())
for i in range(n):
    s = input()
    for x in Alphabet:
        s = s.replace(x, ' ')
    r = ''.join(s.split())
    if 'anton' in r:
        R.append(i+1)
print(*R)
'''



# region Тип 25 № 29673  Большие числа
'''
# Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
# Например, у числа 6 есть два нетривиальных делителя: 2 и 3.
# Найдите все натуральные числа, принадлежащие отрезку [123456789;223456789] и имеющие ровно три нетривиальных делителя.
# Для каждого найденного числа запишите в ответе его наибольший нетривиальный делитель. Ответы расположите в порядке возрастания.

print(123456789 ** 0.25)  # 105
print(223456789 ** 0.25)  # 122


def Simpler(x):
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            return False
    return True

for x in range(105, 122+1):
    if Simpler(x) == True:
        print(x**4, x**3)
'''
# Ответ:
# 131079601 1225043
# 141158161 1295029
# 163047361 1442897
# endregion Тип 25 № 29673



# Тип 25 № 35914
# Найдите все натуральные числа, принадлежащие отрезку [45000000;50000000], у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.
'''
simple = set()
def Simpler(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for x in range(3, int(50000000**0.25) + 1):
    if Simpler(x):
        simple.add(x)

for i in range(45000000, 50000001):
    p = i
    while p % 2 == 0:
        p //= 2
    if int(p**0.25) in simple and (int(p**0.25))**4 == p:
        print(i)
        '''




# Пост:
M = [1, 2, 3, 4, 5]

# Тип 1: Назовём парой два идущих подряд элемента последовательности.
# Пары: 12 23 34 45

for i in range(0, len(M)-1):
    print(M[i], M[i+1], end=', ')

print()
# Тип 2: В данной задаче под парой подразумевается два различных элемента последовательности.
# Пары: 12 13 14 15
# Пары: 23 24 25
# Пары: 34 35
# Пары: 45

'''
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(M[i], M[j], end=', ')
'''

# Тип 17 № 38951

# Тип 17 № 37360




# Пост:
# Типы коллекций
'''
# Тип коллекции СПИСОК list()
A = []  # пустой список
A = list()  # пустой список
A = [1, 2, 3]

# Тип коллекции КОРТЕЖ tuple()
B = ()  # пустой кортеж
B = tuple()  # пустой кортеж
B = (1, 2, 3)

# Тип коллекции МНОЖЕСТВО set()
C = set()  # пустое множество
C = {1, 2, 3}

# Тип коллекции СЛОВАРЬ dict()
D = {}  # пустой словарь
D = dict()  # пустое словарь
D = {1, 2, 3}



'''
'''
x = '112412'
print(x.isdigit())


func = lambda x: True if x[0].lower() == 'a' and x[-1].lower() == 'a' else False

is_non_negative_num = lambda x: True if x.count('.') <= 1 and x.replace('.', '').isdigit() else False

print(is_non_negative_num('-2345.213'))

is_num = lambda x: True if x.count('-') <= 1 and '-' not in x[1:] and x.count('.') <= 1 and x.replace('.', '').replace('-', '').isdigit() else False
print(is_num('0'))






numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

filter_result = list(filter(lambda num: num if num % 2 == 0 or (num % 2 != 0 and num <= 47) else None, numbers))

map_result = list(map(lambda num: num // 2 if num % 2 == 0 else num, filter_result))

print(* map_result)




data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']



result = sorted(data, key=lambda point: (len(point), point))

print(*result)

# for x in result:
#     print(f'{x[1]}: {x[0]}')


mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]

A = sorted(filter(lambda x: x if type(x) == int else None, mixed_list))

B = sorted(filter(lambda x: x if type(x) == str else None, mixed_list))

R = A + B
print(*R)
'''

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for pair in zip(capitals, countries, population):
#     print(f'{pair[0]} is the capital of {pair[1]}, population equal {pair[2]} people.')
#


# ip = [i for i in input().split('.')]
# result = all(map(lambda x: True if x.isdigit() and 0 <= int(x) <= 255 else False, ip))
# print(result)



'''
a = int(input())
b = int(input())
numbers = [i for i in range(a, b+1)]
result = []
for x in numbers:
    nums = [int(i) for i in str(x)]
    temp = all(map(lambda y: y if '0' not in str(y) and x % y == 0 else None, nums))

    if temp == True:
        result.append(x)

print(*result)
'''

'''
import string
s = input()
result = all([any(map(lambda x: x in string.digits, s)), any(map(lambda x: x in string.ascii_lowercase, s)), any(map(lambda x: x in string.ascii_uppercase, s)), len(s) >= 7])

if result == True:
    print('YES')
else:
    print('NO')
'''


'''
n = int(input())
result = []
for _ in range(n):
    k = int(input())
    M = []
    for _ in range(k):
        s = input()
        M.append(s)
    result.append(any(map(lambda x: '5' in x, M)))

if all(result) == True:
    print('YES')
else:
    print('NO')
'''



'''
0.0 0.0
1.5 0.0
1.1 1.1
'''

# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number='17'):
#     text_message = f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\n' \
#                    f'Экзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'
#     return text_message
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))


'''def pretty_print(data, side='-', delimiter='|'):
    s = f'{delimiter} '
    for i in data:
        s += str(i) + f" {delimiter} "
    print(len(s[:-1]))
    text_message = f' {side * (len(s[:-1])-2)} \n{s[:-1]}\n {side * (len(s[:-1])-2)} '
    return text_message

print(pretty_print([1, 2, 10, 23, 123, 3000]))
pretty_print((['abc', 'def', 'ghi', '12345']))
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


def concat(*args, sep=' '):
    s = ''
    for x in args:
        s += str(x) + sep
    return s[:-len(sep)]

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))


def product_of_odds(data):
    pass

'''


'''
with open(f'file.txt', 'r', encoding='utf-8') as f:
    s = f.readlines()
    x3 = len(s)
    x2, x1 = 0, 0
    for x in s:
        M = x.split()
        x2 += len(M)
        for z in M:
            for slow in z:
                if slow in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                    x1 += 1

# 1069 letters
# 229 words
# 12 lines


print(f'Input file contains:\n{x1} letters\n{x2} words \n{x3} lines')
'''

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key*2] = value

