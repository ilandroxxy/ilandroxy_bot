
# region Домашка: ******************************************************************

# список чисел
'''
num = int(input("Введите число m: "))
result = list(range(1, num+1))
print(result)
'''

# список делителей
'''
num = int(input("Введите число п: "))
divisors = []
for i in range(1, num+1):
    if num % i == 0:
        divisors.append(i)

print(divisors)  # сортировка чисел
'''

'''
numbers_str = input("Введите строку с числами через пробел: ")
numbers_list = [int(num) for num in numbers_str.split()]
# numbers_list = list(map(int, numbers_str.split()))
# print(list(map(int, numbers_str.split())))
print(numbers_list)

min_index = numbers_list.index(min(numbers_list))
max_index = numbers_list.index(max(numbers_list))
numbers_list[min_index], numbers_list[max_index] = numbers_list[max_index], numbers_list[min_index]
print(numbers_list)  # список четных
'''

'''
num = int(input("Введите четное число n: "))
# evennumbers = list(range(2, num+1, 2))
evennumbers = [num for num in range(2, num+1, 2)]
print(evennumbers)
'''

'''
print(numbers_list)
numbers_str = input("Введите строку с числами: ")
num = int(input("Введите четное число п: "))
evennumbers = list(range(2, num+1, 2))
print(evennumbers)
numbers_list = list(map(int, numbers_str.split()))

ascending_order = sorted(numbers_list)
descending_order = sorted(numbers_list, reverse=True)

print("По возрастанию:", ascending_order)
print("По убыванию:", descending_order)
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = 
                if not F == :
                    print(x, y, z, w, F)
'''

# № 9825 Основная волна 27.06.23 (Уровень: Базовый)
# (x→(z≡w))∨¬(y→w)
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x <= (z == w)) or (not(y <= w))
                if not F:
                    print(x, y, z, w, F)
'''


# № 9771 Основная волна 20.06.23 (Уровень: Базовый)
# F=(y→x)∧¬z∧w
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (y <= x) and (not z) and w
                if F:
                    print(x, y, z, w, F)
'''

# № 7023 Danov2303 (Уровень: Базовый)
# (А.Богданов) ¬(((¬w→¬y)→¬z)→x)
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not((((not w) <= (not y)) <= (not z)) <= x))
                print(x, y, z, w, F)
'''


#
# № 9736 Основная волна 19.06.23 (Уровень: Базовый)
# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
# а) если число N делится на 3, то в этой записи дописываются справа три последние двоичные цифры;
# б) если число N на 3 не делится, то остаток от деления умножается на 3,
# переводится в двоичную запись и дописывается в конец числа.
# Полученная таким образом запись является двоичной записью искомого числа R.
# 3. Результат переводится в десятичную систему и выводится на экран.

# Например, для исходного числа 12 = 11002 результатом является число
# 11001002 = 100, а для исходного числа 4 = 1002 результатом является число 100112 = 19.
# Укажите максимальное число R, не превышающее 170,
# которое может быть получено с помощью описанного алгоритма.

# В ответе запишите это число в десятичной системе счисления.

result = []
for n in range(1, 1000):
    s = bin(n)[2:]  # 1. Строится двоичная запись числа N.
    if n % 3 == 0:
        s += s[-3:]
    else:
        s += bin((n % 3) * 3)[2:]
    r = int(s, 2)
    if r < 170:
        result.append(r)
print(max(result))

# Показать ответ: 166

# endregion Урок: ******************************************************************


# todo: Василий = [2]
# todo:   КЕГЭ  = []
# на прошлом уроке: Прорешали полностью 2 номер и затронули 5-ый (чуть-чуть)
# на следующем уроке:
