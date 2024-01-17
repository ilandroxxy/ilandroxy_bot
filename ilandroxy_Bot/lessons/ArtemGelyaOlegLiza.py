
# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = (a <= b) and (b <= c) and (c <= d)
                if F == 1:
                    print(a, b, c, d)
'''


# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
#
# Строится пятеричная запись числа N.
# Далее эта запись обрабатывается по следующему правилу:
# а) если число N делится на 25, то к этой записи
# слева дописываются три последние пятеричные цифры;
# б) если число N на 25 не делится, то остаток от деления на 25
# переводится в пятеричную запись и дописывается в конец числа.
# Полученная таким образом запись является пятеричной записью искомого числа R.
# Результат переводится в десятичную систему и выводится на экран.
#
# Укажите такое наименьшее число N, для которого число R больше числа 10000.
# В ответе запишите это число в десятичной системе счисления.
'''
def convert(x, n):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while x > 0:
        r += alphabet[x % n]
        x //= n
    return r[::-1]


for n in range(1, 10000):
    s = convert(n, 5)
    if n % 25 == 0:
        s = s[-3:] + s  # три последние пятеричные цифры
    else:
        s = s + convert(n % 5, 5)
    r = int(s, 5)
    if r > 10000:
        print(n)
        break
'''
# Ответ: 100


# Черепахе был дан для исполнения следующий алгоритм:
#
# Направо 60 Вперёд 4 Направо 120
# Повтори 4 [Вперёд 3 Направо 240 Вперёд 3 Направо 120]
# Вперёд 4 Направо 90 Вперёд 8**(1/3) Направо 90 Вперёд 8.
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом.
# Точки на линии учитывать не следует.
'''
import turtle as t
t.tracer(0)
t.left(90)
l = 60

t.right(60)
t.forward(4 * l)
t.right(120)

for i in range(4):
    t.forward(3 * l)
    t.right(240)
    t.forward(3 * l)
    t.right(120)

t.forward(4*l)
t.right(90)
t.forward(8* 3**(1/2) * l)
t.right(90)
t.forward(8 * l)

t.up()
for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x * l, y * l)
        t.dot(2, 'red')

t.done()
'''
# Ответ: 78


# Прибор автоматической фиксации нарушений ПДД делает цветные фотографии размером 2560×1440 пикселей.
# Для передачи снимки группируются в пакеты по 200 штук. На каждый пакет выделяется по одному Гбайту.
#
# Какое максимальное количество цветов может использоваться в палитре?
'''
I = (1*2**33) / 200
i = I / (2560*1440)
print(i)  # 11.650844444444445 -> 11
print(2**11)
'''
# Ответ: 2048


# Все семибуквенные слова, составленные из букв А, Е, К, П, Т, Ч,
# записаны в алфавитном порядке и пронумерованы начиная с 1.
#
# Вот начало этого списка:
#
# ААААААА
# ААААААЕ
# ААААААК
# ААААААП
# ААААААТ
# ААААААЧ
# АААААЕА
# …
# Сколько слов в списке расположено между словами АПТЕЧКА и ПЕЧАТКА?
#
# Сами слова АПТЕЧКА и ПЕЧАТКА учитывать не нужно.
'''
s = sorted('АЕКПТЧ')
num = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            slovo = a + b + c + d + e + f + g
                            # if slovo == 'АПТЕЧКА' or slovo == 'ПЕЧАТКА':
                            if slovo in ('АПТЕЧКА', 'ПЕЧАТКА'):
                                print(num, slovo)
                            num += 1

# 28921 АПТЕЧКА
# 154381 ПЕЧАТКА
print(154381 - 28921 - 1)
'''
# Ответ: 125459


# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа — углы четырёхугольника,
# записанные в произвольном порядке. Определите количество строк таблицы,
# в которых четырёхугольник может являться параллелограммом.

# Примечание. Если в четырёхугольнике противолежащие углы попарно равны, то этот четырёхугольник — параллелограмм.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M[0] == M[1] and M[2] == M[3]:
        count += 1
print(count)
'''
# Ответ: 317


# При регистрации в компьютерной системе каждому объекту присваивается идентификатор, содержащий только
# десятичные цифры и буквы латинского алфавита в произвольном регистре
# (т. е. буквы могут быть как прописные, так и строчные).
#
# В базе данных для хранения каждого идентификатора отведено одинаковое и минимально возможное целое число байт.
# При этом используется посимвольное кодирование идентификаторов,
# все символы кодируются одинаковым и минимально возможным количеством бит.
#
# Для хранения 1 000 идентификаторов отведено 10 Кбайт.
# Определите максимально возможную длину идентификатора.

'''
alphabet = 10 + 26*2
i = 6

byte = (10*2**10) / 1000
print(byte)  # 10

bit = 10 * 8
# bit = symbols * i
symbols = bit / i
print(symbols)
'''
# Ответ: 13


# Дана программа для Редактора:
#
# ПОКА нашлось (52) ИЛИ нашлось (2222) ИЛИ нашлось (1112)
#     ЕСЛИ нашлось (52)
#         заменить (52, 11)
#         заменить (2222, 5)
#     ИНАЧЕ
#         заменить (1112, 2)


# На вход приведённой выше программе поступает строка, начинающаяся с цифры «5»,
# а затем содержащая n цифр «2» (3 < n < 10 000).
#
# Определите наибольшее значение n, при котором сумма цифр в строке,
# получившейся в результате выполнения программы, равна 1685.
'''
for n in range(10000-1, 3, -1):
    s = '5' + '2' * n

    while '52' in s or '2222' in s or '1112' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
            s = s.replace('2222', '5', 1)
        else:
            s = s.replace('1112', '2', 1)
    summa = sum([int(x) for x in s if x.isdigit()])

    if summa == 1685:
        print(n)
        break
'''
# Ответ: 4200


# Значение арифметического выражения записали в системе счисления с основанием 49.
#
# Для найденного выражения вычислите сумму цифр и укажите её в ответе в десятичной системе счисления.
'''
x = abs(18 * 7 ** 108 - 5 * 49**76 + 343 ** 35 - 50)
M = []
while x > 0:
    print(x % 49)
    M.append(x % 49)
    x //= 49
M.reverse()
print(sum(M))
'''
# Ответ: 1134


# Для какого наименьшего целого неотрицательного числа A выражение
# (3x+y>A)∧(y<x)∧(x<30)
#
# тождественно ложно, т. е. принимает значение 0 при любых целых неотрицательных x и y?
'''
def F(x, y, A):
    return ((3 * x + y) > A) and (y < x) and (x < 30)


for A in range(0, 1000):
    if all(F(x, y, A) == False for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break
'''
# Ответ: 115


# Алгоритм вычисления значения функции
# F(n), где n — натуральное число, задан следующими соотношениями:
# F(n)= 42 при n>10 000;
# F(n)=2⋅n+F(n+3)+F(n+4)+F(n+6), если n≤10 000 и n — чётное;
# F(n)= −(n+F(n+1)+F(n+3)), если n≤10 000 и n — нечётное.
#
# Чему равно значение выражения F(9996)−F(9994)?
'''
def F(n):
    if n > 10000:
        return 42
    if n <= 10000 and n % 2 == 0:
        return 2 * n+F(n+3)+F(n+4)+F(n+6)
    if n <= 10000 and n % 2 != 0:
        return -(n+F(n+1)+F(n+3))


print(F(9996) - F(9994))
'''
# Ответ: 2


# Определите количество пар элементов последовательности, сумма которых превосходит
# каждую из сумм соседних пар, при этом все три суммы являются положительными.
#
# В ответе запишите количество найденных пар чисел, затем минимальное из произведений таких пар.
#
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# Под соседними парами подразумеваются четыре идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
mini = 9999999999
count = 0
for i in range(2, len(M)-3):
    if (M[i] + M[i+1]) > 0 and (M[i-1] + M[i-2]) > 0 and (M[i+2] + M[i+3]) > 0:
        if (M[i] + M[i+1]) > (M[i-1] + M[i-2]) and (M[i] + M[i+1]) > (M[i+2] + M[i+3]):
            count += 1
            mini = min(mini, M[i] * M[i+1])
print(count, mini)
'''
# Ответ: 610 -123157359


# Прибавить значение старшего разряда
# Прибавить 3
# Сделать нечётным

# Сколько существует программ, для которых при исходном числе 42 результатом является число 89
# и при этом траектория содержит число 73 и не содержит числа 81?

'''
def F(a, b):
    if a >= b or a == 81:
        return a == b
    return F(a + int(str(a)[0]), b) + F(a+3, b) + F(a*2-1, b)


print(F(42, 73) * F(73, 89))
'''
# Ответ: 210


# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# символ «?» означает ровно одну произвольную цифру;
# символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
#
# Среди натуральных чисел, не превышающих 10**8,
# найдите пять наибольших чисел, подходящих под все перечисленные условия:
#
# соответствуют маске ?2*4*0;
# не соответствуют маске 1*7*;
# делятся на число 42 без остатка.

R = []
from fnmatch import *
for x in range(42, 2*10**8, 42):
    if fnmatch(str(x), '?2*4*0'):
        if not fnmatch(str(x), '1*7*'):
            R.append([x, x // 42])

print(*R[-5])
print(*R[-4])
print(*R[-3])
print(*R[-2])
print(*R[-1])

# endregion Урок: ******************************************************************


# GOAL = [1.1, 2.1, 4.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке:
