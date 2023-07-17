
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Задача: Принадлежность 1
'''
x = int(input('x: '))
# if x > -1 and x < 17:
if -1 < x < 17:
    print(True)
else:
    print(False)
'''


# Високосный год
'''
year = int(input('Введите год: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(True)
else:
    print(False)
'''

# Dog Age
'''
dog_age = int(input("Введите возраст вашей собаки: "))
if dog_age <= 2:
    print(f'Возраст вашей собаки в человеческих годах: {dog_age * 10.5}')
else:
    print('Возраст вашей собаки в человеческих годах:', 2 * 10.5 + (dog_age - 2) * 4)
'''



'''
m = int(input('m: '))
p = int(input('p: '))  # две аналогичные записи
n = int(input('n: '))
'''
# Популяция
'''
m, p, n = [int(i) for i in input().split()]

for day in range(1, n+1):  # range(START, STOP, STEP)
    print(day, m)
    m += (m / 100) * p
'''

# Без нулей
'''
result = 1
for _ in range(10):
    x = int(input())
    if x != 0:
        result *= x  # result = result * x
print(f'Произведение всех чисел не равных нулю: {result}')
'''

# Задачка с коде варс
'''
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
'''

'''
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
'''

# Кол-во пятерок
'''
count = 0
while True:
    x = int(input())
    if 1 <= x <= 5:
        if x == 5:
            count += 1
    else:
        break
print(count)
'''

# Список чисел
'''
n = int(input())
L = [i for i in range(1, n+1)]
print(L)

n = int(input())
L = []
for i in range(1, n+1):
    L.append(i)
print(L)
'''


# Список делителей
'''
divisors = set()
n = int(input())
for j in range(1, int(n**0.5)+1):
    if n % j == 0:
        divisors.add(j)
        divisors.add(n // j)
print(sorted(divisors))


divisors = []
n = int(input())
for j in range(1, n + 1):
    if n % j == 0:
        divisors.append(j)
print(divisors)
'''


# endregion Урок: ******************************************************************


# todo: Василий = []
# todo:   КЕГЭ  = []
# на прошлом уроке: Прорешивали задания на темы: условные операторы, циклы, списки. Догоняем программу с прошлого урока.
# на следующем уроке: Повторить 2 номер и начать разбирать 5 номер
