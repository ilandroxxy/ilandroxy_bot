
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************

# Логическая функция F задаётся выражением: (x ≡ ¬y) → ((z → ¬w) ∧ (w → y))

# Номер 2
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not y)) <= ((z <= (not w)) and (w <= y))
                print(x, y, z, w, F)
'''


# Номер 5
'''
# Алгоритм получает на вход натуральное число N и строит по нему новое
# число R следующим образом:
# 1. Строится двоичная запись числа N.
# 2. Если сумма цифр десятичной записи заданного числа нечётна, то в конец
# двоичной записи дописывается 1, если чётна – 0.
# 3–4. Пункт 2 повторяется для вновь полученных чисел ещё два раза.
# 5.  Результатом работы алгоритма становится десятичная запись полученного
# числа R.

# Определите наименьшее возможное значение R > 1028, которое может
# получиться в результате работы алгоритма.

for n in range(1, 1000):
    s = bin(n)[2:]  # 1. Строится двоичная запись числа N.

    for _ in range(3):  # 3–4. Пункт 2 повторяется для вновь полученных чисел ещё два раза.
        if sum([int(i) for i in str(int(s, 2))]) % 2 != 0:  # 2. Если сумма цифр десятичной записи заданного числа нечётна
            s += '1'
        else:
            s += '0'

    r = int(s, 2)  # Строится десятичная запись из двоичной
    if r > 1028:
        print(r)
        break
  '''
# Ответ: 1028

# Номер 6

# Черепаха выполнила следующую программу:
# Повтори 4 [Вперёд 7 Направо 90 Вперёд 7 Налево 90 Вперёд 7 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться
# внутри области, ограниченной линией, полученной при выполнении данной
# программы. Точки, расположенные на линии, не учитывать.

# Вариант 1
'''
import turtle as t

t.left(90)
t.speed(10)
l = 20

for _ in range(4):
    t.forward(7*l)
    t.right(90)
    t.forward(7*l)
    t.left(90)
    t.forward(7*l)
    t.right(90)

t.pu()
for x in range(0, 20):
    for y in range(-8, 20):
        t.goto(x*l, y*l)
        t.dot(3, 'red')

t.done()
'''

# Вариант 2
'''
import turtle as t

t.left(90)
t.speed(10)
l = 20

t.begin_fill()
for _ in range(4):
    t.forward(7*l)
    t.right(90)
    t.forward(7*l)
    t.left(90)
    t.forward(7*l)
    t.right(90)
t.end_fill()

canvas = t.getcanvas()
count = 0
for x in range(-100*l, 100*l, l):
    for y in range(-100*l, 100*l, l):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) >= 1 and item[0] == 5:
            count += 1
print(count)
t.done()
'''
# 204


# Номер 8
'''
# Вероника составляет коды из букв слова ВЕРОНИКА. Код должен состоять
# из 6 букв, любую букву можно использовать произвольное число раз или не
# использовать вовсе. Вероника хочет, чтобы гласных в каждом коде было
# больше, чем согласных. Сколько кодов, удовлетворяющих этому условию,
# она сможет составить?

s = 'ВЕРОНИКА'
sogl = 'ВРНК'
glas = 'ЕОИА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        temp = a + b + c + d + e + f
                        B = [i for i in temp if i in sogl]
                        A = [i for i in temp if i in glas]
                        if len(A) > len(B):
                            count += 1
print(count)
'''
# Ответ: 90112


# Номер 9
'''
# В каждой строке электронной таблицы записаны пять натуральных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# – все числа в строке различны;
# – нечётных чисел больше, чем чётных;
# – сумма нечётных чисел меньше суммы чётных.
# В ответе запишите число – количество строк, для которых выполнены эти условия.

count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == len(M):  # – все числа в строке различны;
        Nechet = [i for i in M if i % 2 != 0]
        Chet = [i for i in M if i % 2 == 0]
        if len(Nechet) > len(Chet):  # – нечётных чисел больше, чем чётных;
            if sum(Nechet) < sum(Chet):  # – сумма нечётных чисел меньше суммы чётных.
                count += 1
print(count)
'''
# Ответ: 303


# Номер 14
'''
# В выражении 123x_37 + 4x59_37 x обозначает некоторую цифру из алфавита
# системы счисления с основанием 37. Определите наименьшее значение x,
# при котором значение данного выражения кратно 36.  Для найденного x
# вычислите частное от деления данного выражения на 36 и запишите его
# в ответе в десятичной системе счисления.

# print(int('12341412', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0

for x in range(0, 37):
    A = [1, 2, 3, x]
    B = [4, x, 5, 9]

    a = 0
    A.reverse()
    for i in range(0, len(A)):
        a += A[i] * 37 ** i

    b = 0
    B.reverse()
    for i in range(0, len(B)):
        b += B[i] * 37 ** i

    if (a + b) % 36 == 0:
        print((a + b) // 36)
        break
'''
# Ответ: 7348


# Номер 15
'''
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без
# остатка на натуральное число m».
# Укажите наименьшее целое значение A, для которого формула
# (ДЕЛ(144, x)→ ¬ДЕЛ(x, y)) ∨ (x + y > 100) ∨ (A – x > y)
# тождественно истинна при любых натуральных значениях переменных x и y.

def F(x, y):
    return ((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (A - x > y)

for A in range(1, 1000):
    if all(F(x, y) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''
# Ответ: 97



# endregion Урок: ******************************************************************




# todo: Валерия = [2, 5, 6, 8, 12, 14+, 15+, 16, 17, 23, 24, 25]
# на прошлом уроке: Прорешивали 1 вариант статграда от 15.12.22 года, остановились на 16 номере
# на следующем уроке: Начать на 10 минут раньше, 9 номер через Python, 12 номер разобрать (статград), продолжить с 16 номера.
