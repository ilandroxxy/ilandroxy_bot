# region Домашка: ******************************************************************
'''
s = input()
summ = 0
for x in range(10):
    summ += s.count(str(x)) * x
print(summ)
'''

# Лучший способ решить задачу "посчитайте сумму цифр строки"
'''
s = '>23456432234 5'
print(sum([int(x) for x in s if x.isdigit()]))
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Списки - list()
# - Могут содержать неограниченное кол-во элементов, разных типов
# - Каждый элемент списка имеет порядковый номер - индекс
# - Индексы считаются слева-направо начиная с 0 или справа-налево начиная с -1
# - Через индесы можно изменять элементы списков
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка: {M[0]} \n'
      f'Последний элемент списка: {M[-1]}')
'''

# Срезы списков (аналогичны строка)
'''
print(M[:3])  # ['a', 'b', 'c']
print(M[3:])  # ['d', 'e']
print(M[::2])  # ['a', 'c', 'e']
print(M[::-1])   # ['e', 'd', 'c', 'b', 'a'] - аналог метода .reverse()

M.reverse()
print(M)  # ['e', 'd', 'c', 'b', 'a']
'''

# Функции списков:
'''
M = [3, 5, 8, 3, 5]

print(len(M))  # 5
print(sum(M))  # 24
print(max(M))  # 8
print(min(M))  # 3

print(set(M))  # удаляем все копии элементов
print(len(set(M)))  # "сколько различных элементов было в списке"
print({1, 2, 3, 4} | {3, 4, 5, 6})  # {1, 2, 3, 4, 5, 6} - объединение множеств 

print(sorted(M))  # [3, 3, 5, 5, 8]
print(sorted(M, reverse=True))  # [8, 5, 5, 3, 3]

M.sort()  # встроенный метод для списков
print(M)  # [3, 3, 5, 5, 8]

M.sort(reverse=True)
print(M)  # [8, 5, 5, 3, 3]
'''

# Методы списков - частный случай функций для определенного объекта (типа данных)
'''
M = [4, 5, 67, 2, 4, 4.0]

print(M.count(4))   # 2 - кол-во вхождений элемента в список
print(M.index(4))   # 0 - индекс первого вхождения элемента

M.append(10)  # добавляет новый элемент в конец списка
print(M)

M += [2, 3, 4]  # добавили несколько элементов в конец списка
print(M)  # [4, 5, 67, 2, 4, 4.0, 10, 2, 3, 4]

M = [1, 2, 3] + M   # добавили несколько элементов слева от списка
print(M)  # [1, 2, 3, 4, 5, 67, 2, 4, 4.0, 10, 2, 3, 4]

M.sort()
M.reverse()
'''

# Методы .split() и .join() для строк
'''
ip = '23.123.9.45'
print(ip.split('.'))  # ['23', '123', '9', '45']
# Метод .split() разбивает строку на список строк

IP = [int(x) for x in ip.split('.')]
print(IP)  # [23, 123, 9, 45]

new_ip = ' * '.join(ip.split('.'))
print(new_ip)  # 23 * 123 * 9 * 45
# Метод .join() склеивает список строк обратно в строку
'''

# Генераторы списков
'''
M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x**2 for x in range(10)]
print(M)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]
'''

# Ввод чисел в список с клавиатуры
'''
print([int(x) for x in input('Введите числа через пробел: ').split() if x.isdigit()])
'''

# Тип 17 № 55604
# Файл содержит последовательность целых чисел, модуль которых находится в интервале от 100 до 10000.
# Назовём парой два идущих подряд элемента последовательности.
#
# Определите количество пар, для которых выполняются следующие условия:
# — последняя цифра записи одного из элементов пары совпадает с предпоследней цифрой записи другого элемента;
# — ровно один элемент из пары делится без остатка на 7;
# — сумма квадратов элементов пары не превышает квадрат наименьшего из элементов последовательности,
# две последние цифры в записи которого одинаковы.
#
# В ответе запишите два числа: сначала количество найденных пар, затем максимальную
# величину суммы квадратов элементов этих пар.
'''
M = [int(x) for x in open('17.txt')]
MINI = min([x for x in M if str(x)[-2] == str(x)[-1]])
count, maxi = 0, -999999
for i in range(0, len(M)-1):
    x, y = M[i], M[i+1]
    if (str(x)[-1] == str(y)[-2]) or (str(x)[-2] == str(y)[-1]):
        if (x % 7 == 0 and y % 7 != 0) or (x % 7 != 0 and y % 7 == 0):
            if (x ** 2 + y ** 2) <= MINI ** 2:
                count += 1
                maxi = max(maxi, x ** 2 + y ** 2)
print(count, maxi)
'''

# Тип 5 №55592
# Алгоритм получает на вход натуральное число N и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. Подсчитывается количество чётных и нечётных цифр в десятичной записи заданного числа.
# Если в десятичной записи больше чётных цифр, то в конец двоичной записи дописывается 1, если нечётных
# — 0. Если чётных и нечётных цифр в десятичной записи поровну, то в конец двоичной записи дописывается 0,
# если данное число чётное, и 1 — если нечётное.
# 3−4. Пункт 2 повторяется для вновь полученных чисел ещё два раза.
#
# 5. Результатом работы алгоритма становится десятичная запись полученного числа R.

# Определите количество принадлежащих отрезку [123455; 987654321] чисел,
# которые могут получиться в результате работы этого алгоритма.

count = 0
for n in range(1, 100000000000):
    s = bin(n)[2:]  # Строится двоичная запись числа N.

    for i in range(3):
        temp = int(s, 2)
        chet = [int(x) for x in str(temp) if int(x) % 2 == 0]
        nechet = [int(x) for x in str(temp) if int(x) % 2 != 0]
        if len(chet) > len(nechet):
            s += '1'
        elif len(chet) < len(nechet):
            s += '0'
        else:
            if temp % 2 == 0:
                s += '0'
            else:
                s += '1'

    r = int(s, 2)
    if 123455 <= r <= 987654321:
        count += 1
print(count)


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Дарья = [2.1, 6.1]
# КЕГЭ  = []
# на следующем уроке:
