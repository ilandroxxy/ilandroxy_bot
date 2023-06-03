# region Домашка: ************************************************************

# endregion Домашка: ************************************************************



# region Урок: ************************************************************

# Тип 9 № 35898
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Определите, сколько раз за время измерений результат очередного
# измерения оказывался ниже результата предыдущего на 2 и более градусов.
'''
# Вариант 1
M = []
for s in open('9.txt'):
    M += [float(i) for i in s.replace(',', '.').split()]
count = 0
for i in range(0, len(M)-1):
    if M[i] - M[i+1] >= 2:
        count += 1
print(count)

# Вариант 2
M = [float(i) for i in open('9.txt').read().replace(',', '.').split()]
count = 0
for i in range(0, len(M)-1):
    if M[i] - M[i+1] >= 2:
        count += 1
print(count)
'''
# M = [float(i.replace(',', '.')) for i in open('9.txt').read()]
# print(M)

# Ответ: 458


# Тип 24 № 36037
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')
M = [len(i) for i in s.split()]
print(max(M))  # 1713
#   XZZ ZZY.......XZZ ZZY....XZZ ZZY
'''
# Ответ: 1713


# Тип 25 № 35914
# Найдите все натуральные числа, принадлежащие отрезку [45000000;50000000], у которых ровно пять
# различных нечётных делителей (количество чётных делителей может быть любым).
# В ответе перечислите найденные числа в порядке возрастания.
'''
def Divisors(x):
    divisors = set()
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            if j % 2 != 0:
                divisors.add(j)
            if (x // j) % 2 != 0:
                divisors.add(x // j)
            if len(divisors) > 5:
                return sorted(divisors)
    return sorted(divisors)

for x in range(45000000, 50000000+1):
    divisors = Divisors(x)
    if len(divisors) == 5:
        print(x)
'''
# Ответ:
# 45212176
# 45265984
# 47458321
# 48469444

# endregion Урок: ************************************************************




# todo:   Василий    = [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# todo: Василий КЕГЭ = [25]
# на прошлом уроке: Разобрали домашку с номерами, которые не получились: 4, 9, 13, 20, 21, 24, 25
# на следующем уроке:
