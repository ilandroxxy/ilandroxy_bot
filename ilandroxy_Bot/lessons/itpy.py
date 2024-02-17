


# Тип 13 №16815
# Для узла с IP-адресом 98.162.71.94 адрес сети равен 98.162.71.64.
# Чему равно наибольшее количество возможных адресов в этой сети?


from ipaddress import *
for mask in range(32+1):
    net = ip_network(f'98.162.71.94/{mask}', 0)
    print(net, net.num_addresses)

    # 98.162.71.64/26 64
    # 98.162.71.64/27 32





# todo Никита shnit_n Стград почему b+1?
# Исполнитель преобразует число на экране.
# A. Вычесть 1
# B. Умножить на 2
# C. Умножить на 3
# Сколько существует программ, которые преобразуют исходное число 3
# в число 20 и при этом не содержат двух команд A подряд?

'''
def F(a, b, flag):
    if a >= b:
        return a == b
    if flag == 'A':
        return F(a*2, b, 'B') + F(a*3, b, 'C')
    return F(a-1, b, 'A') + F(a*2, b, 'B') + F(a*3, b, 'C')


print(F(3, 20, 0))


def F(a, b, flag):
    if a >= b or flag == 2:
        return a == b
    return F(a-1, b, flag+1) + F(a*2, b, 0) + F(a*3, b, 0)


print(F(3, 20, 0))


def F(a, b, flag):
    if a > b+1 or flag == 2:
        return 0
    if a == b:
        return 1
    return F(a-1, b, flag+1) + F(a*2, b, 0) + F(a*3, b, 0)


print(F(3, 20, 0))
'''

#todo Никита shnit_n Статград

# Обозначим через a%b остаток от деления натурального числа a на натуральное
# число b, а через a//b – целую часть от деления a на b.
# Функция F(n), где n – неотрицательное целое число, задана следующими
# соотношениями:
# F(n) = 0, если n = 0;
# F(n) = F(n//10) + n%10, если n > 0 и n чётно;
# F(n) = F(n//10), если n нечётно.
# Определите количество таких целых k, что 109 ≤ k ≤ 2·109 и F(k) = 0.


#todo Никита shnit_n Статград

# Алгоритм получает на вход натуральное число N и строит по нему новое
# число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. В конец двоичной записи добавляется двоичный код остатка от деления
# числа N на 4.
# 3. Результатом работы алгоритма становится десятичная запись полученного
# числа R.

# Назовем доступными числа, которые могут получиться в результате работы
# этого алгоритма. Например, числа 27 и 58 – доступные.
# Какое наибольшее количество доступных чисел может быть на отрезке,
# содержащем 49 натуральных чисел?
'''
R = [0] * 10000
for x in range(1, 1000):
    s = bin(x)[2:]
    s += bin((x % 4))[2:]
    r = int(s, 2)
    R[r] += 1

print(R)
'''



# todo Разбираем 13 номера
'''
print('.'.join(f'{x:>08b}' for x in [192, 168, 10, 66]))
# 11000000.10101000.00001010.01000010
'''


# todo Марк 18 номер Тип 18 №51987

# Разобраться КЕГЭ № 1363 в чем проблема ДЗ 8.3 (4 задача) +
# region

# КЕГЭ № 1363 Джобс 16.05.2021 (Уровень: Сложный)
# Сколько существует четных пятеричных чисел длиной 6, начинающихся с цифры 3?
'''
from itertools import product
count = 0
for s in product('01234', repeat=6):
    slovo = ''.join(s)
    if slovo[0] == '3' and slovo[0] != '0':
        if sum([int(x) for x in slovo]) % 2 == 0:
            count += 1
print(count)
'''
# Примечание: Четность числа в нечетной системе счисления определеяется четностью суммы ее цифр

# Ответ: 1562
# endregion


# todo Разобрать КЕГЭ № 7038 Danov2303 (Уровень: Средний) (А.Богданов)
# region

# endregion


# todo Разобраться почему три варианта решения 17, 18, 19
# region
'''
s = open('24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A').replace('9', '8')

while 'AA' in s: s = s.replace('AA', 'A A')
while '88' in s: s = s.replace('88', '8 8')
print(max(len(x) for x in s.split()))
'''
# endregion


# Интересное решение 24 номера Тип 24 №27689 +
# region
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
'''
import re
f = open('24.txt').read()
r = re.findall(r'(?:XYZ)+(?:XY|X)?', f)
# r = map(lambda x: len(x), r)
print(max(len(x) for x in r))
'''
# endregion

# todo Интересный новый номер 24: Тип 24 №56552
# region
# Текстовый файл содержит строки различной длины, содержащие только заглавные буквы латинского алфавита (ABC…Z).
# Будем называть цепочкой группу идущих подряд одинаковых букв в одной строке.
# Определите, сколько раз буква, образующая самую длинную цепочку в файле,
# встречается в строке, содержащей эту цепочку. Если в файле есть несколько цепочек одинаковой максимальной длины,
# нужно выбрать ту из них, для которой общее количество образующих цепочку букв в соответствующей строке будет меньше.
'''
maxi_global = 0
maxi_s = 0
for s in open('24.txt'):
    k = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            k += 1
            if maxi_s < k:
                maxi_s = k
                maxi_global = s.count(s[i])
            if maxi_s == k:
                maxi_global = min(s.count(s[i]), maxi_global)
        else:
            k = 1
print(maxi_global)
'''
# endregion


# Интересное решение 22 номера через Пайтон +
# region
'''
def f(n):  # определим функцию, которая возвращает время работы процесса n - номер процесса
    if n == 0:  # если номер равен 0, то время выполнения 0 (начало всех процессов)
        return 0

    # иначе максимальное время выполнения для всех предыдущих процессов плюс время выполнения процесса n
    return max([f(x) for x in pr[n][1]]) + pr[n][0]


file = open('22.txt').read().replace(';', ' ')
nums = [[int(x) for x in s.split()] for s in file.split('\n')]  # преобразуем данные в список строк из чисел
pr = {c[0]: (c[1], c[2:]) for c in nums}  # создадим словарь вида №процесса: (время выполнения, процессы)
print(max([f(x) for x in pr]))  # находим максимальное значение


def f(n):
    if n == 0:
        return 0
    return max([f(x) for x in pr[n][1]]) + pr[n][0]


file = open('22.txt').read().replace(';', ' ')
nums = [[int(x) for x in s.split()] for s in file.split('\n')]
pr = {c[0]: (c[1], c[2:]) for c in nums}
print(max([f(x) for x in pr]))
'''

'''
def calculate_process_time(process_number):
    if process_number == 0:
        return 0

    sub_process_times = [calculate_process_time(sub_process) for sub_process in pr[process_number][1]]
    return max(sub_process_times) + pr[process_number][0]

def read_input(file_path):
    with open(file_path) as file:
        content = file.read().replace(';', ' ')
        rows = [list(map(int, line.split())) for line in content.split('\n') if line]
        return {row[0]: (row[1], row[2:]) for row in rows}

file_path = '22.txt'
pr = read_input(file_path)
max_process_time = max(calculate_process_time(process) for process in pr)
print(max_process_time)
'''

'''
def calculate_maximum_score(node):
    if node == 0:
        return 0
    return pr[node][0] + max(calculate_maximum_score(child) for child in pr[node][1])

def parse_input(file_path):
    with open(file_path) as file:
        content = file.read().replace(';', ' ')
        rows = [list(map(int, line.split())) for line in content.split('\n') if line]
        return {row[0]: (row[1], row[2:]) for row in rows}

file_path = '22.txt'
pr = parse_input(file_path)
result = max(calculate_maximum_score(node) for node in pr)
print(result)
'''
# endregion


# todo Разобрать задачку, почему ответы не сходятся
# region
# Тип 17 №59722
# Элементы ряда могут принимать целые значения в диапазоне [−10000; 10000].
# Определите количество троек элементов последовательности, в которой только одно число трехзначное,
# а сумма тройки меньше наибольшего числа, оканчивающегося на 17.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 100 == 17]
count = 0
for i in range(0, len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (len(str(abs(x))) == 3) ^ (len(str(abs(y))) == 3) ^ (len(str(abs(z))) == 3):
        if (x + y + z) < max(A):
            # print(x, y, z, (x + y + z) < max(A))
            count += 1
print(count)


M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 100 == 17]
count = 0
for i in range(0, len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    flag1, flag2, flag3 = False, False, False
    if (len(str(abs(x)))) == 3:
        flag1 = True
    if (len(str(abs(y)))) == 3:
        flag2 = True
    if (len(str(abs(z)))) == 3:
        flag3 = True
    if flag1 + flag2 + flag3 == 1:
        if (x + y + z) < max(A):
                # print(x, y, z, (x + y + z) < max(A))
                count += 1
print(count)


l = [int(x) for x in open('17.txt')]
max_dvy = max([x for x in M if abs(x) % 100 == 17])
count = 0
for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1],  l[i+2]]
    for x in s:
        if 99 < abs(x) < 1000:
            c += 1
    if c == 1 and sum(s) < max_dvy:
        count += 1
print(count)
'''
# endregion


# todo придумать как положить сразу два числа в список через генератор
# region
'''
n = int(input())
# divisors = {i for i in range(1, n + 1) if n % i == 0}     # не оптимизированный
divisors = sorted({i for i in range(1, int(n**0.5) + 1) if n % i == 0})
print(divisors)   # 24: {1, 2, 3, 4, 24**0.5,  6, 8, 12, 24}
'''
# endregion
