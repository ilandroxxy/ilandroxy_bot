
# region Домашка: ******************************************************************


# Бесконечный цикл
'''
ALPHABET = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")

while True:
    case = int(input('\n\ncase 1: Перевод из 10-ной в N-ную\n'
                     'case 2: Перевод из N-ной в 10-ную\n'
                     'case 0: exit\n'
                     'case: '))
    if case == 1:
        x = int(input('Введите число для перевода: '))
        temp = x
        n = int(input('В какую систему счисления будем переводить: '))
        M = []
        while x > 0:
            M.append(ALPHABET[x % n])
            x //= n
        M.reverse()
        print(f'Перевели число {temp} из 10-ной в {n}-ную систему счисления, результат: {"".join(M)}')

    elif case == 2:
        # todo: Попробовать реализовать дома или на след. уроке
        pass

    elif case == 0:
        break
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Списки - list()  # тип данных коллекций
'''
M = []  # пустой список
A = list()  # IndexError: list index out of range

# i  0  1  2  3  4   5
B = [1, 2, 3, 4, 8, 12]
#   -6 -5 -4 -3 -2  -1

print(B[2], B[-3])

B[2] = 99
print(B)  # [1, 2, 99, 4, 8, 12]
'''



# Срезы списков (строки, кортежи, множества)
'''
print(B[3:])  # [4, 8, 12]
print(B[:3])  # [1, 2, 99] крайний правый не берется
print(B[2:4])  # [99, 4]

print(B[::])  # [1, 2, 99, 4, 8, 12]
print(B[::2])  # [1, 99, 8]
print(B[::-1])  # [12, 8, 4, 99, 2, 1]
'''


B = [1, 2, 3, 4, 8, 12, 4, 5]
# Функция работающие со списками
'''
print(max(B))  # 12
print(min(B))
print(sum(B))  # 39 сумма всех элементов списка
print(len(B))  # 8 кол-во элементов списка 
print(sum(B) / len(B))  # 4.875
print(set(B))  # {1, 2, 3, 4, 5, 8, 12}
# превращаем список в множество (тем самым убирая копии числа)
print(sorted(set(B)))  # [1, 2, 3, 4, 5, 8, 12]
'''



# Методы работающие со списками
'''
print(B.count(4))  # 2  показывает кол-во вхождений того или иного элемента

B.append(10)  # добавить новый один элемент в конец списка
print(B)  # [1, 2, 3, 4, 8, 12, 4, 5, '4', 10]

B += [1, 2, 3]
print(B)  # [1, 2, 3, 4, 8, 12, 4, 5, '4', 10, 1, 2, 3]

B.reverse()
print(B)  # [3, 2, 1, 10, '4', 5, 4, 12, 8, 4, 3, 2, 1]

B.sort()
print(B)    # TypeError: '<' not supported between instances of 'str' and 'int'

# [1, 1, 2, 2, 3, 3, 4, 4, 5, 8, 10, 12]
print(B.index(4))  # 6 - находит индекс первого вхождения элемента в список

A = [1, 2, 3, 4]
B = A  # это не копирование, это взаимосвязь
D = A.copy()   # создание независимой копии числа
print(A, B)  # [1, 2, 3, 4] [1, 2, 3, 4]
A.append(5)
print(A, B)  # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
print(D)  # [1, 2, 3, 4]
'''


# Способ открыть документацию Питона прямо на экзамене
'''
print(B.extend.__doc__)  # Extend list by appending elements from the iterable.

print(help(B.extend))
# extend(iterable, /) method of builtins.list instance
#     Extend list by appending elements from the iterable.


import useful
print(useful.MyConvert.__doc__)
# Функция для перевода из 10-ной в n-ную систему счисления
#     :param x: 10-ное число, которое будем переводить
#     :param n: система счисления в которое будем переводить x
#     :return: Возвращает переведенное число в виде str
'''


# Списочные генераторы или списочные выражения
'''
n = int(input('Введите кол-во элементов будущего списка: '))
M = []
for i in range(n):
    x = int(input(f'x{i+1}: '))
    M.append(x)
print(M)
'''
# M = [что кладем | откуда берем | при каком условии]
'''
M = [int(i) ** 2 for i in input('Введите числа через пробел: ').split() if int(i) % 2 == 0]
print(M)
'''

'''
numbers = [int(i) for i in input('Введите числа: ').split()]
chet = [i for i in numbers if i % 2 == 0]
nechet = [i for i in numbers if i % 2 != 0]
'''

'''
numbers = [int(i) for i in open('17.txt')]
print(numbers)


for s in open('9.txt'):
    numbers = [int(i) for i in s.split()]
    print(numbers)
'''


# endregion Урок: ******************************************************************


# todo: Василий = []
# todo:   КЕГЭ  = []
# на прошлом уроке: Обсуждали теорию списков, функции, индексы, срезы, методы и генераторы списков.
# на следующем уроке: Повторить 2 номер и начать разбирать 5 номер
