# Домашка:

# Тип 2 № 36857
'''
#Логическая функция F задаётся выражением ((¬x ∨ z) ≡ (y ∧ ¬w)) → (z ∧ y).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
# содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F
# соответствует каждая из переменных x, y, z, w.

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((not(x) or z) == (y and not(w))) <= (z and y))
                if F == False:
                   print(x, y, z, w, F)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((not(x) or z) == (y and not(w))) <= (z and y)):
                   print(x, y, z, w, F)
'''

#Задание 2 (35460)
'''
#Логическая функция F задаётся выражением ¬((x ∨ y) → (z ∧ w)) ∧ (x → w).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
# содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F
# соответствует каждая из переменных x, y, z, w.

print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                F = not((x or y) <= (z and w)) and (x <= w)
                if F == True:
                   print(x, y, z, w, F)
'''

#Задание 3
'''
n = int(input('n: '))
for i in range(1, n+1):
    if i in range(5, 9+1):  # 5 <= i <= 9
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(f'{i}')
'''

'''
while True:
    s = input()  # функция input() получает сразу строку str
    if 'КОНЕЦ' in s or 'конец' in s:
        break
    print(s)
'''
'''
while True:
    s = input()  # функция input() получает сразу строку str
    if 'КОНЕЦ' in s.upper():
        break
    print(s)
# КоНеЦ
'''

# Срезы списков
"""
M = [2, 3, 4, 5, 6, 7, 8, 9]
s = '23456789'
print(M[0])
print(M[2:5])  # элемент с индексом 5 не входит в срез
print(M[2:])
print(M[:5])  # элемент с индексом 5 не входит в срез
print(M[1:8:2])
print(M[8:1:-1])  # пробежали в обратном порядке
print(M[::-1])  # в обратном порядке вывели список 
"""

# Функции списков
'''
M = [2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 5, 6, 5]
print(len(M))  # длина списков/коллекций и строк
print(sum(M))
print(max(M))
print(min(M))

A = set(M)  # при смене типа коллекции на set - из списка удалили все повторяющиеся элементы 
print(A, len(A))


# Задача о среднем
a1 = int(input())
a2 = int(input())
a3 = int(input())
M = [a1, a2, a3]

sred = sum(M) - max(M) - min(M)
print(sred)
'''


# Методы списков
"""
M = [2, 3, 4, 5, 6, 7]
M.append(0)  # добавление в конец
M.append(0)
print(M)

print(M.count(0))  # показать кол-во элементов 0 в списке
print(M.index(0))  # выводит индекс первого найденного элемента 0 из списка

M.sort()
print(M)
M.reverse()
print(M)

x = M.pop(6)  # вырезал и забрал элемент из списка по индексу
print(M, x)

B = M  # это не копирование список - по сути связь списков
A = M.copy()  # создали нормальную копию и при изменении списка M мы не изменяем список A 
print(M, B, A)
M.append(33)
print(M, B, A)

M.clear()
print(M)
"""


"""
x = 8
n = 2  # Перевести 8_10 в х_2
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)
"""

# Тип 14 № 38948
'''
# Значение выражения 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49 записали в системе счисления с основанием 16.
# Сколько разных цифр встречается в этой записи?
x = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
M = []
while x > 0:
    M.append(x % 16)
    x //= 16
M.reverse()
print(M)

# Вариант 1
A = []
for i in M:
    if i not in A:
        A.append(i)
print(A, len(A))

# Вариант 2
B = set(M)
print(B, len(B))
'''


# todo: на след. уроке: разбираем номер Тип 14 № 47218 и 5 тип задач





