# region Домашка: ************************************************************

# endregion Домашка: *********************************************************


# region Урок: ************************************************************


# Переменная - это удобный способ хранения данных в ячейках памяти
'''
a: int = 5
print(type(a))  # <class 'int'>

a = float(a)
print(type(a))  # <class 'float'>

print(type(7 / 2))  # <class 'float'>
'''

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные данные

b = 5.0  # float (число с плавающей точкой) - дроби/вещественные числа
print(type(7 / 2))  # <class 'float'>
print(type(4 / 2), 4 / 2)  # <class 'float'>  2.0
print(type(5 + 5.0))  # <class 'float'>

c = '5'  # str (string) - хранит в себе символы, буквы, пунктуацию, слова, тексты
print(a * 4, c * 4)  # 20 5555
print('Hello ' * 4)  # Hello Hello Hello Hello
# При умножении строки на целое число - строка дублируется

# Конкатенация строк (склеивание строк)
name = 'Герман'
print('Привет, ' + name)  # Привет, Герман

# к строке, состоящей из "1" и 100 идущих подряд цифр "9"?
s = '1' + '9' * 100
print(s)  # 19999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

d1 = True  # bool (Boolean) - Булева алгебра (математическая логика)
d2 = False

print(4 < 10)  # True
x = 4
if x % 2 == 0:  # != не равно, == равно ли
    print('Четное')
else:
    print('Нечетное ')
'''
# Четное


# Типы данных коллекций
# Коллекция/последовательность - это набор переменных
'''
A = [1, 2, 3]  # список - list()
# Неограниченное кол-во данных в разных типах
# Все элементы имеют порядковые номера - индексы
# Индексы можно считать слева-направо начиная с 0 или справа-налево начиная с -1
# Через индексы можно изменять, добавлять и удалять элементы

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка М: {M[0]} \n'
      f'Последний элемент списка М: {M[-1]}')

# Первый элемент списка М: a
# Последний элемент списка М: e

print(M)  # ['a', 'b', 'c', 'd', 'e']
print(*M)  # a b c d e


B = (1, 2, 3)  # tuple (кортеж) - полностью аналогичен спискам, только нельзя менять элементы и удалять их

C = {1, 2, 3}  # set (множество)
# Копии элементов удаляются

M = [1, 2, 1, 2, 3, 4, 4]  # list()
# Какое кол-во различных элементов в списке?
print(set(M))  # {1, 2, 3, 4}
print(len(set(M)))  # 4


D = {'один': 'one', 'два': 'two', 'три': 'three'}  # dict (словарь)
# Элементы словаря состоят из двух частей: ключ и значение
# Доступ к значению элемента осуществляется через ключ

print(D['один'])  # one
for key, value in D.items():
      print(f'Через ключ: {key} можно получить значение: {value}')
      # Через ключ: один можно получить значение: one
      # Через ключ: два можно получить значение: two
      # Через ключ: три можно получить значение: three
'''

# Конвертация типов данных
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)
print(a, type(a))  # 5 <class 'str'>
# ValueError: invalid literal for int() with base 10: '5.0'

a = float(a)
print(a, type(a))  # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>


A = [1, 2, 3, 1, 2, 3]
print(A, type(A))  # [1, 2, 3, 1, 2, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 3, 1, 2, 3) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3] <class 'list'>
'''

'''
M = [2, 2.0, '2', True, 2+2, 7/2, '2'*2, 4 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'один': 'one', 'два': 'two', 'три': 'three'}]
for elem in M:
      print(type(elem), elem)
      # <class 'int'> 2
      # <class 'float'> 2.0
      # <class 'str'> 2
      # <class 'bool'> True
      # <class 'int'> 4
      # <class 'float'> 3.5
      # <class 'str'> 22
      # <class 'bool'> True
      # <class 'list'> [1, 2, 3]
      # <class 'tuple'> (1, 2, 3)
      # <class 'set'> {1, 2, 3}
      # <class 'dict'> {'один': 'one', 'два': 'two', 'три': 'three'}
'''

# - однострочный комментарий

'''
"""
тут еще один комментарий 
"""
многострочные комментарии 
'''

# region Так можно скрывать часть кода

print('Читал сегодня книгу "Война и мир".')
# Читал сегодня книгу "Война и мир".

# endregion Так можно скрывать часть кода

# todo Сделать домашку: 234

# region Тип 12 №11310
# ПОКА нашлось (19) ИЛИ нашлось (299) ИЛИ нашлось (3999)
#   ЕСЛИ нашлось (19)
#       ТО заменить (19, 2)
#   ЕСЛИ нашлось (299)
#       ТО заменить (299, 3)
#   ЕСЛИ нашлось (3999)
#       ТО заменить (3999, 1)
#
# Какая строка получится в результате применения
# приведённой ниже программы к строке, состоящей из "1"
# и 100 идущих подряд цифр "9"? В ответе запишите полученную строку.
'''
s = '1' + '9' * 100
while '19' in s or '299' in s or '3999' in s:
    if '19' in s:
        s = s.replace('19', '2', 1)
    if '299' in s:
        s = s.replace('299', '3', 1)
    if '3999' in s:
        s = s.replace('3999', '1', 1)
print(s)
'''
# Ответ: 39
# endregion Тип 12 №11310


# Ввод данных с клавиатуры
'''
name = input('Введите свое имя: ')
print(name, type(name))  # Герман <class 'str'>
# print('Доброго времени суток, ' + name + '!')
print(f'Доброго времени суток, {name}!')
'''

# Функция input() - принимает значение с клавиатуры в виде строки
'''
x = int(input('Введите число: '))
print(type(x))
print(x * 2)
'''

'''
# Если мы хотим ввести текст:
s = input('Введите текст: ')
print(type(s))

# Если мы хотим ввести целое число:
x = int(input('Введите целое число: '))
print(type(x))

# Если мы хотим ввести дробное число:
d = float(input('Введите дробное число: '))
print(type(d))
'''

# Задание вывести сообщение:
'''
# "Сегодня отличная погода, облачно, а температура 24 градуса!"
weather = 'облачно'
temperature = 24
print("Сегодня отличная погода, ", weather, ", а температура ", temperature, " градуса!")
print("Сегодня отличная погода, " + weather + ", а температура " + str(temperature) + " градуса!")
print("Сегодня отличная погода, {}, а температура {} градуса!".format(weather, temperature))
print(f"Сегодня отличная погода, {weather}, а температура {temperature} градуса!")
# TypeError: can only concatenate str (not "int") to str
'''


# Базовая арифметика:
'''
a = 7
b = 2
print(f'{a} + {b} = {a + b} \n'  # \n - символ переноса строки
      f'{a} - {b} = {a - b} \n'
      f'{a} * {b} = {a * b}')

print()  # В каждом print() есть переход на новую строку \n

print(f'{a} / {b} = {a / b} \n'  # / - вещественное деление (то есть дроби) - всегда результат в виде float
      f'{a} // {b} = {a // b} \n'  # // - взять только целую часть от деления 
      f'{a} % {b} = {a % b}')  # % - остаток от деления

print(f'Возведите число {a} в степень {b}: {a} ** {b} = {a**b}')  # возведение в степень
print(f'Квадратный корень от числа 16: 16 ** (0.5) = {16 ** (0.5)}')
print(f'Кубический корень от числа 27: 27 ** (1/3) = {27 ** (1/3)}')
'''

'''
а = 7 ** 2  # 49
b = 10
с = а - b  # 39
а = 5  # переприсваивание 
print(а)  # 5
'''

# Напишите программу, которая считывает два целых числа a и b
# и выводит на экран куб суммы (a+b)**3, а затем куб разности (a−b)**3
'''
a = int(input())
b = int(input())
print((a+b)**3)
print((a-b)**3)
'''


# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************

# Герман = []
# КЕГЭ = []
# на следующем уроке:
