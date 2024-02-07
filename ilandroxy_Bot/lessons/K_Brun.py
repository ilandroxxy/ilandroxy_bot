# region Домашка: ******************************************************************


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

'''
ip = '123.34.45.9'
IP = [int(x) for x in ip.split('.')]
print(IP)  # [123, 34, 45, 9]
'''


'''
M = [x for x in open('9.txt')]
print(M)  # '66\t90\t52\t74\t66\n'
'''


# Тип 9 №51978
# В каждой строке электронной таблицы записаны пять целых положительных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
#
# — все числа в строке различны;
# — нечётных чисел больше, чем чётных;
# — сумма нечётных чисел меньше суммы чётных.
# В ответе запишите число — количество строк, для которых выполнены эти условия.

#  1. Для которых выполнены следующие условия:
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(M) == len(set(M)):  # — все числа в строке различны;
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
                count += 1
print(count)
'''
# Ответ: 303


#  2. Для которых выполнено только одно из условий:
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) > len(chet):
        flag += 1
    if sum(nechet) < sum(chet):
        flag += 1
    if flag == 1:
        count += 1

print(count)
'''
# Ответ: 2547


#  3. Для которых выполнено хотя бы одно из условий:
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) > len(chet):
        flag += 1
    if sum(nechet) < sum(chet):
        flag += 1
    if flag > 0:
        count += 1

print(count)
'''
# Ответ: 6269


#  4. Для которых выполнено только два условия:
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) > len(chet):
        flag += 1
    if sum(nechet) < sum(chet):
        flag += 1
    if flag == 2:
        count += 1

print(count)
'''
# Ответ: 3419


# Тип 9 №59834
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — в строке есть только два равных числа, остальные 4 различны;
# — сумма повторяющихся чисел меньше чем среднее арифметическое остальных чисел строки.
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]  # len(M) == 6
    A = [x for x in M if M.count(x) == 2]
    B = [x for x in M if M.count(x) == 1]
    if len(A) == 2:
        if sum(A) < (sum(B) / len(B)):
            count += 1
print(count)
'''
# Ответ: 613


# Тип 9 №56509
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — в строке есть как повторяющиеся, так и неповторяющиеся числа;
# — среднее арифметическое всех неповторяющихся чисел строки больше,
# чем среднее арифметическое всех повторяющихся чисел этой строки.
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    A = [x for x in M if M.count(x) > 1]
    B = [x for x in M if M.count(x) == 1]
    if len(B) > 0 and len(A) > 0:
        if (sum(B) / len(B)) > (sum(A) / len(A)):
            count += 1
print(count)
'''
# Ответ: 2102


# endregion Урок: ******************************************************************


# Екатерина = [2.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 25.1]
# КЕГЭ  = []
# на следующем уроке: Рассмотреть задачи 9 номера с температурой и еще базовых*
