# region Домашка:  ******************************************************************************

# Таблица умножения для числа n
'''
n = int(input())
for i in range(1, 10+1):
    print(f'{n} * {i} = {n*i}')
'''

# endregion Домашка:  ******************************************************************************


# region Урок:  ******************************************************************************

# Списки - это тип данных коллекции вида list()
# Списки упорядоченные и каждый элемент списка имеет порядковый номер - индекс, индексы начинаются с нуля

'''
# i:   0  1   2    3    4
# -i: -5 -4  -3   -2    -1
arr = [1, 2, '3', 5.6, True]
print(arr)
print(arr[0], arr[1], arr[2], arr[3], arr[4])
print(arr[-5], arr[-4], arr[-3], arr[-2], arr[-1])

print(arr[0], arr[-1])  # способ получить первый и последний элемент списка


# В списке можно изменять элементы по значению
arr[0] = '*'  # через индексы я могу изменить значение элемента списка
print(arr)

del arr[0]  # удалили элемент под индексом 0 из списка
print(arr)
'''


'''
# i: 0  1  2  3  4
M = [1, 2, 3, 4, 5]

print(len(M))  # len() - это встроенная функция возвращающая длину списка (коллекции), то есть кол-во элементов в нем

for i in range(0, len(M)):  # [0, 4]  - то есть через такой форик мы пробегаем индексы нашего списка
    M[i] = M[i] ** 2  # изменили каждый элемент нашего списка

print(M)
'''

'''
A = [3, 4, 5, 6, 7]
for i in range(0, len(A)):  # пробежали элементы списка через индексы
    print(A[i], end=' ')
print()


for x in A:  # пробежали значения списка напрямую через переменную х
    print(x, end=' ')
print()

for i in range(len(A)-1, 0-1, -1):  # пробежали элементы списка через индексы в обратном порядке
    print(A[i], end=' ')
print()

for x in A[::-1]:  # пробежали значения списка в обратном порядке через переменную х
    print(x, end=' ')
print()
'''


# Функции работающие со списками
'''
M = [4, 5, 6, 7]
print(len(M))  # # возвращает длину списка
print(sum(M))  # возвращает суммы элементов списка
print(min(M))  # возвращает максимальный элемент списка
print(max(M))
'''

# Методы списков - это функции направленный на один определенный тип объекта
'''
M = [1, 2, 3, 4]

M.append(5)  # .append() - добавить число в конец списка
M.append(2)
M.append(5)
print(M)

print(M.count(5))  # выводит кол-во вхождений элемента в список

print(M.index(5))  # выводит индекс первого вхождения элемента

M.sort()  # отсортировали список по возрастанию
print(M)

M.reverse()  # развернул список (полностью) 
print(M)
'''

# Порешаем 14 номер ЕГЭ

# Тип 14 № 40730
'''
# Значение выражения 3*125**6 + 2*25**9 + 5**12 - 625 записали в системе счисления с основанием 5.
# Сколько значащих нулей содержится в этой записи?

x = 3*125**6 + 2*25**9 + 5**12 - 625
M = []  # пустой список для записи остатков от деления
while x > 0:  # пока наше x не исчезнет
    M.append(x % 5)  # мы будем добавлять остаток от деления в список
    x //= 5  # и делить нацело, чтобы число x уменьшалось
M.reverse()  # обязательно по алгоритму разворачиваем списки в обратном порядке
print(M.count(0))
'''
# Ответ: 11


# Тип 14 № 27545
'''
# Значение выражения 49**7*7**20 − 7**8 − 28 записали в системе счисления с основанием 7.
# Сколько цифр 6 содержится в этой записи?
x = 49**7*7**20 - 7**8 - 28
M = []
while x > 0:  
    M.append(x % 7)
    x //= 7
M.reverse()
print(M.count(6))
'''
# Ответ: 31



# Тип 14 № 27385
'''
# Значение выражения 343**5 + 343**4 + 49**6 − 7**13 − 21 записали в системе счисления с основанием 7.
# Сколько различных цифр содержит эта запись?

# Пример. Запись 122233_7 содержит три различные цифры: 1, 2 и 3.

x = 343**5 + 343**4 + 49**6 - 7**13 - 21
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print('M:', M)
A = set(M)  # set() это тип коллекции МНОЖЕСТВО, он не может содержать копию значений
print('A:', A, len(A))
'''


# Порешаем 2 номер ЕГЭ

d1 = True
d2 = True  # bool (boolean)

# Теория математической логики на языке Пайтон
#  ¬y    --->  (not(y))   инверсия (отрицание)
# z ∧ x  --->  z and x   конъюнкция (логическое умножение)
# y ∨ w  --->  y or w    дизъюнкция (логическое сложение)
# y → z  --->  y <= z    импликация
# x ≡ w  ---> x == w     тождество (равны ли эти элементы)

# Тип 2 № 35891
'''
# Логическая функция F задаётся выражением (y → z) ∧ ¬((y ∨ w) → (z ∧ x)).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):   # [0, 1] или [0, 2)
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= z) and (not((y or w) <= (z and x))))
                if F == True:
                    print(x, y, z, w, F)
'''

# endregion Урок:  ******************************************************************************


# todo: Богдан = [2, 14-], на следующем уроке: Разбираем тему списков и строк (частично)
