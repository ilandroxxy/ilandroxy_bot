
# region Домашка: ******************************************************************

'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

sum = num1 + num2 + num3

print(sum)
'''


'''
num = int(input())

nextnum = num + 1
prevnum = num - 1

print("Следующее число после", num, ":", nextnum)
print("Предыдущее число перед", num, ":", prevnum)
'''


'''
edge_length = int(input())

volume = edge_length ** 3
surface_area = 6 * (edge_length ** 2)


# print("Объем куба:", volume)
# print("Площадь полной поверхности куба:", surface_area)

print(f"Объем куба: {volume}")
print(f"Площадь полной поверхности куба: {surface_area}")
'''


# № 8941 Джобс 02.06.2023 (Уровень: Средний)
'''
team_name = input()

length = len(team_name)

print(f"Футбольная команда {team_name} имеет длину {length} символов.")
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Проверьте, что число трехзначное:
"""
x = int(input('x: '))
'''
if 100 <= abs(x) <= 999:
    print('YES')
else:
    print('NO')
'''
if len(str(abs(x))) == 3:
    print('YES')
else:
    print('NO')
"""

# Циклы for, while: повтори n раз, циклы с условием, бесконечные

# Циклы for

# i  0  1  2  3  4  5  6  7  8  9
M = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# print(M[7])
# print(M[-7])
'''
print(f'Первый элемент списка: {M[0]} и последний элемент списка: {M[-1]}')

for x in M:  # просто пробигаем все элементы списка (строки, кортежа, множества) напрямую
    print(x)

for i in range(len(M)):  # пробежали элементы списка через его индексы
    print(M[i])
'''

'''
for i in range(10):  # range(START=0, STOP=(10-1), STEP=1)
    print(i)

for i in range(2, 10):  # range(START=2, STOP=(10-1), STEP=1)
    print(i)

for i in range(2, 10, 2):  # range(START=2, STOP=(10-1), STEP=2)
    print(i)

for i in range(10, 2, -1):  # range(START=10, STOP=(2-1), STEP=-1)
    print(i)   # если есть потребность пройти от большего к меньшему
'''


# Перебор элементов последовательности для 17-го номера
'''
M = [1, 2, 3, 4, 5]

# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(0, len(M)-1):
    print(f"{M[i]}{M[i+1]}", end=' ')
print()

    # IndexError: list index out of range

# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345
for i in range(0, len(M)-2):
    print(f"{M[i]}{M[i+1]}{M[i+2]}", end=' ')
print()

# В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(f"{M[i]}{M[j]}", end=' ')
    print()
'''


# Цикл while с условием:
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=(10-1), STEP=2)
    print(i, end=' ')
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
'''

# Бесконечный цикл
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


# endregion Урок: ******************************************************************


# todo: Василий = []
# todo:   КЕГЭ  = []
# на прошлом уроке: Поговорили про комментарии, устройства проекта PyCharm и разобрали циклы for, while
# на следующем уроке:
