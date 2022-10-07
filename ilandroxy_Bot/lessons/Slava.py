# Задание 1.
'''
m = int(input('m: '))
n = int(input('n: '))
if m < n:
    for i in range(m, n+1):
        print(i)
if m > n:
    for i in range(m, n-1, -1):
        print(i)
'''


# Задание 2.(Не получилось)
'''
a = int(input('a: '))
summ = 0
f = 1
count = 0
first = 0
last = 0
flag = True
while a > 0:
    if flag == True:
        last = a % 10
        flag = False
    summ += a % 10
    f *= (a % 10)
    count += 1
    first = a % 10
    #print(first)
    a = a // 10

print(summ)
print(count)
print(f)
print(summ/count)
print(first)
print(first + last)

'''


# break - прерывает цикл в котором находится
# continue - прерывает итерацию цикла
#Задание 3.
'''
a = int(input('a: '))
b = int(input('b: '))
for i in range(a, b + 1):
    if a == 1:
        continue
    for f in range(2, i):
        if i % f == 0:
            break
    else:
            print(i)

'''

'''
a = int(input('a: '))
b = int(input('b: '))
for i in range(a, b + 1):
    KolDel = 0
    for f in range(1, i+1):
        if i % f == 0:
            KolDel += 1
    if KolDel == 2:
        print(i)



def My_Function(x, y):
    return x + y

print(My_Function(4, 5))
'''

# Логические операции
# инверсия (отрицанние)   ¬x  <---->   (not(x))
# конъюнкция (логическое умножение)   x ∧ y   <---->  x and y
# дизъюнкция логическое сложение)   x ∨ y   <---->  x or y
# импликация  x → z  <---->   x <= z    или    (not(x)) or z
# тождество  x ≡ z   <---->  x == z

# ((not(x)) or (not(y))) and (not(x == z)) and w

# Тип 2 № 18781
'''
# Логическая функция F задаётся выражением (¬x ∨ ¬y) ∧ ¬(x ≡ z) ∧ w.
#
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
#
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(x)) or (not(y))) and (not(x == z)) and w
                if F == True:
                    print(x, y, z, w, F)
'''
# Ответ: wxyz


# Тип 2 № 15939
# Логическая функция F задаётся выражением (z ∧ y) ∨ ((x → z ) ≡ (y → w)).
#
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
#
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (z and y) or ((x <= z) == (y <= w))
                if F == False:
                    print(x, y, z, w, F)

print()
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(y <= w)) or (x == z) or x
                if F == False:
                    print(x, y, z, w, F)


