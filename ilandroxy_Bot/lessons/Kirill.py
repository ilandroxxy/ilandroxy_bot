# region Домашка:  **************************************************



# endregion Домашка: **************************************************


# region Урок:  **************************************************

#
# № 8489 Апробация 17.05 (Уровень: Базовый)
# Миша заполнял таблицу истинности логической функции
# F= ((w→y)→(x≡y))∨¬z, но успел заполнить лишь фрагмент из трёх различных её строк,
# даже не указав, какому столбцу таблицы соответствует каждая из переменных w,x,y,z.
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((w <= y) <= (x == y)) or (not z)
                if F == False:
                    print(x, y, z, w)
'''


# № 8493 Апробация 17.05 (Уровень: Средний)
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если число N делится на 3, то к этой записи дописываются три последние двоичные цифры;
# б) если число N на 3 не делится, то остаток от деления умножается на 3,
# переводится в двоичную запись и дописывается в конец числа.
# Полученная таким образом запись является двоичной записью искомого числа R.
# 3. Результат переводится в десятичную систему и выводится на экран.

# Укажите максимальное число N, после обработки которого с помощью этого алгоритма получается число R, меньшее чем 76.
'''
for n in range(1, 1000):
    s = bin(n)[2:]

    if n % 3 == 0:
        s += s[-3:]
    else:
        s += bin((n % 3) * 3)[2:]
    r = int(s, 2)
    if r < 76:
        print(n)
'''
# Показать ответ: 16


# № 8494 Апробация 17.05 (Уровень: Базовый)
# Черепахе был дан для исполнения следующий алгоритм:
# Направо 315 Повтори 7 [Вперёд 12 Направо 45 Вперёд 6 Направо 135].
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.
'''
import turtle as t
t.left(90)
t.speed(100)
l = 20

t.right(315)
for i in range(7):
    t.forward(12 * l)
    t.right(45)
    t.forward(6 * l)
    t.right(135)

t.up()
for x in range(-15, 1):
    for y in range(0, 15):
        t.goto(x*l, y*l)
        t.dot(2, 'red')
t.done()
'''
# Показать ответ: 40


# № 8497 Апробация 17.05 (Уровень: Средний)
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – все числа различны;
# – утроенная сумма минимального и максимального чисел строки не меньше, чем удвоенная сумма трёх её оставшихся чисел.
# В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if len(M) == len(set(M)):
        if 3 * (M[0] + M[-1]) >= 2 * (M[1] + M[2] + M[3]):
            count += 1
print(count)
'''
# Ответ: 7695



# № 8499 Апробация 17.05 (Уровень: Базовый)
# При регистрации в компьютерной системе каждому объекту присваиваетсяидентификатор, состоящий из 213 символов
# и содержащий только десятичные цифры и символы из 2021-символьного специального алфавита.
# В базе данных для хранения каждого идентификатора отведено одинаковое и минимально возможное целое число байт.
# При этом используется посимвольное кодирование идентификаторов,
# все символы кодируются одинаковым и минимально возможным количеством бит.
# Определите объём памяти (в Кбайт), необходимый для хранения 16 384 идентификаторов.
# В ответе запишите только целое число – количество Кбайт.
'''
symbols = 213
alphabet = 2021 + 10  # 2**i = 2031
i = 11  # бит на 1 символ
byte = 293

bit = symbols * i
print(bit / 8)
I = (16384 * byte) / (2**10)
print(I)  # 4688.0
'''
# Показать ответ: 4688


# № 8500 Апробация 17.05 (Уровень: Средний)
# Дана программа для редактора:
#
# ПОКА нашлось (25) ИЛИ нашлось (355) ИЛИ нашлось (555)
#   ЕСЛИ нашлось (25)
#     ТО заменить (25, 5)
#   ЕСЛИ нашлось (355)
#     ТО заменить (355, 52)
#   ЕСЛИ нашлось (555)
#     ТО заменить (555, 3)

# На вход приведённой выше программе поступает строка, начинающаяся с цифры "2", а затем содержащая n цифр "5" (n > 3).
# Определите наименьшее значение n, при котором в строке,
# получившейся в результате выполнения программы, количество цифр «3» равно 2.
'''
for n in range(4, 1000):
    s = '2' + '5' * n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)

    if s.count('3') == 2:
        print(n)
        break
'''
# Показать ответ: 18


# № 8502 Апробация 17.05 (Уровень: Базовый)
# Операнды арифметического выражения записаны в системе счисления с основанием 15.

# 99658x29_15 + 102x023_15

# В записи чисел переменной х обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
# Определите наибольшее значение х, при котором значение данного арифметического выражения кратно 14.
# Для найденного значения х вычислите частное от деления значения арифметического выражения на 14
# и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.
'''
for x in '0123456789ABCDE':
    A = int(f'99658{x}29', 15)
    B = int(f'102{x}023', 15)
    if (A + B) % 14 == 0:
        print((A + B) // 14)
'''
# Показать ответ: 118330623


#
# № 8503 Апробация 17.05 (Уровень: Базовый)
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 11102& 01012 = 01002 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
#
# ((x & 52 ≠ 0) /\ (x & 36 = 0)) → ¬ (x & А = 0)
#
# тождественно истинна (т.е. принимает значение 1) при любом неотрицательном целом значении переменной х?
'''
def F(x, A):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & A == 0))

for A in range(0, 10000):
    if all(F(x, A) for x in range(0, 1000)):
        print(A)
        break
'''
# Показать ответ: 16


# № 7846 Danov2304 (Уровень: Базовый)
# (А.Богданов) На числовой прямой даны два отрезка: P = [13; 19] и Q = [17; 23].
# Укажите наибольшую возможную длину такого отрезка A, что формула
#
# ¬(¬(x ∈ P) → (x ∈ Q)) → ((x ∈ A) →(¬(x ∈ Q)→(x ∈ P)))
#
# тождественно истинна, то есть принимает значение 1 при любых x.
'''
def F(x, a1, a2):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not((not P) <= Q)) <= (A <= ((not Q) <= P))
R = []
M = [i/4 for i in range(0*4, 30*4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2-a1)
print(max(R))
'''
# Показать ответ: 10

# endregion Урок:  **************************************************

import useful
print(useful.Who_Is_Name())

# todo: Кирилл = [1, 2, 3, 4, 5, 8, 9, 12, 13, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25], на следующем уроке:
# на прошлом уроке: Разбирали вариант апробации и прорешивали номера, которые не получились на досроке: 2, 5, 6, 9, 11, 12, 14, 15
# на следующем уроке: 15 номера прорешать с отрезками подробнее.
