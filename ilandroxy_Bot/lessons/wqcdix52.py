# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

X = 5  # переменная - это способ взаимодействия с данными
# print(X, type(X))  # 5 <class 'int'>

# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(type(4+4))  # <class 'int'>

b = 5.0  # float (число с плавающей точкой) - вещественные числа/дроби
print(7 / 2)  # 3.5

c = '5'  # str (string) - строковый тип данных содержит в себе символы, цифры, буквы, слова и тд
print(a*4, c*4)  # 20 5555

d1 = True
d2 = False  # bool (Boolean) - Элементы Булевой алгебры / Математическая логика
print(4 < 10)  # Вопрос: 4 меньше 10? - True
'''

# Типы данных коллекций
'''
A = [1, 2, 3]  # list (список)
# Списки содержат неограничено много значений разных типов данных
# Все элементы списка пронумерованы через индексы (начиная с нуля)
# Через индексы мы можем брать элементы и менять их

B = (1, 2, 3)  # tuple (кортеж)
# Полностью идентичен спискам, кроме момента: в кортеже нельзя менять элементы

C = {1, 2, 3, 2, 3}  # set (множество)
# В множестве не может быть двух одинаковых элементов - копии удаляются..
print(C)  # {1, 2, 3}

D = {1: 'один', 2: 'два', 3: 'три'}  # dict (словари)
# Элемент словаря состояит из двух частей: ключ и значение
# доступ к значению элемента словаря осуществлдяется через его ключ
print(D[1])  # один
D[3] = '33'
print(D)  # {1: 'один', 2: 'два', 3: '33'}
'''

'''
M = [2, 2.0, '2', True, 2+2, 7/2, '2' * 4, 4 < 10, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: 'два', 3: 'три'}]
for elem in M:
    print(elem, type(elem))
'''

# Конвертация типов данных
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)  # при переводе из строки нужно внимательно следить за символами и буквами
print(a, type(a))  # 5 <class 'str'>

a = float(a)
print(a, type(a))  # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>

# ValueError: invalid literal for int() with base 10: '5.0'
print()

A = [1, 2, 3, 2, 3]
print(A, type(A))  # [1, 2, 3, 2, 3] <class 'list'>

A = tuple(A)
print(A, type(A))  # (1, 2, 3, 2, 3) <class 'tuple'>

A = set(A)
print(A, type(A))  # {1, 2, 3} <class 'set'>

A = list(A)
print(A, type(A))  # [1, 2, 3] <class 'list'>
'''


# Ввод данных с клавиатуры
'''
x = input('Введите символ: ')  # функция input() - принимает строчные переменные
print(x, type(x))  # <class 'str'>

x = int(input('Введите целое число: '))
print(x, type(x))  # <class 'int'>
'''

# endregion Урок: ******************************************************************


# todo: Артур = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке: задачку на f-строки и базовую арифметику, условные операторы
