# region Домашка: ******************************************************************

# КЕГЭ № 8611 (Уровень: Базовый) (Л. Шастин)
# Определите количество пар последовательности, в которых только одно число является трёхзначным,
# а произведение элементов пары кратно максимальному трёхзначному элементу последовательности.
# В ответе запишите количество найденных пар, затем минимальное из произведений элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if len(str(abs(x))) == 3]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (len(str(abs(x))) == 3) != (len(str(abs(y))) == 3):
        if (x * y) % max(A) == 0:
            R.append(x * y)
print(len(R), min(R))
'''


# КЕГЭ № 2491 (Уровень: Базовый)
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите количество троек, в которых хотя бы один из трёх элементов меньше, чем среднее
# арифметическое всех чисел в файле, и десятичная запись всех трёх элементов тройки содержит цифру 9.
# В ответе запишите два числа: сначала количество найденных троек, а затем – максимальную сумму элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
avg = sum(M) / len(M)  # среднее арифметическое всех чисел в файле
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if x < avg or y < avg or z < avg:  # хотя бы один из трёх элементов меньше, чем среднее арифметическое
        if '9' in str(x) and '9' in str(y) and '9' in str(z):
            print(x, y, z)  # -2978 -4699 7996
            R.append(x + y + z)
print(len(R), max(R))
'''
# Ответ: 345 17460


# i   0    1    2    3
M = ['a', 'b', 'c', 'd']
# -i -4   -3   -2   -1


# КЕГЭ № 7038 Danov2303 (Уровень: Средний) (А.Богданов) 🌶
# – только один из элементов пары заканчивается на 1;
# – оба элемента пары меньше максимального среднего значения пары среди всех пар отвечающих предыдущему условию.
#
# В ответе запишите два числа: сначала количество пар отвечающих двум условиям, затем максимальный элемент из пар,
# включающих минимальный элемент таких пар. В задаче рассматриваются пары соседних элементов.
'''
M = [int(x) for x in open('17.txt')]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (str(x)[-1] == '1') != (str(y)[-1] == '1'):  # – только один из элементов пары заканчивается на 1;
        pass
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Тимур = [2, 5, 6, 8, 12, 14, 15, 16, 17, 23]
# КЕГЭ  = []
# на следующем уроке:
