

# Разбираем ДЗ

'''
a = int(input())
b = int(input())
c = int(input())

# if a < b < c or c < b < a:
#     print(b)
# elif b < a < c or c < a < b:
#     print(b)
# elif a < c < b or b < c < a:
#     print(b)
# else:
#     print('Ошибка')

# max() min() sum()

sred = (a + b + c) - max(a, b, c) - min(a, b, c)  # полезная формула поиска среднего изх трех чисел
print(sred)
'''

'''
a=int(input())
if a%2!=0:
    print('YES')
elif a%2==0 and 2<=a<=5:
    print('NO')
elif a%2==0 and 6<=a<=20:
    print('YES')
if a%2==0 and a>20:
    print('NO')
'''


# Циклы в Пайтон
# Ключевые слова: while, for, range, in, break, continue, flag
# Есть две технологии циклов: while, for
# Типы циклов:
# 1. Повтори n раз
# 2. Повтори от а до б раз
# 3. Повторяй пока условие истинно
# ...


# Цикло for - это цикл повтори n раз


# for-индексный
'''
for i in range(5):  # i - переменная по которой движется цикл, в диапазоне range -> [0, 5)
    print(i)  # повторили действие 5 раз

for i in range(1, 5):  # [1, 5)
    print(i)

for i in range(0, 10, 2):
    print(i)


for i in range(10, 0, -1):
    print(i)

M = [45, 123, "weiurfgh", True, 5]
#    0    1        2        3   4
print(M[0])
len(M) # длина списка - это кол-во элемнетов в нем
for i in range(0, len(M)):  # [0, 5)
    print(M[i], end=' ')  # просто вывели все элементы списка по индексам
'''

# for который пробегает по элементам
'''
M = [1, 2, 3, 4, 5]

for x in M:
    print(x, end=' ')
'''

# while это цикл с условием (пока условие будет истинно - выполняем тело цикла)
for i in range(0, 10+1, 2):
    print(i, end=" ")
print()


i = 0
while i <= 10:  # stop  <=  ---> +1
    print(i, end=" ")
    i += 2  # step

# Бесконечный цикл
# count = 0
# while True:
#     print(count)
#     count += 1
print()

'''
import random

password = 'qwerty'
count = 0
while True:
    pas = input("Введите Ваш пароль: ")
    if pas == password:
        break
    print("Попробуйте еще раз! Неверный пароль.")
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"Пройдите проверку на робота:\n{a} + {b} = \nОтвет: ")
        res = int(input())
        if a + b == res:
            count = 0
            print("Окей, продолжайте попытки!")
        else:
            print("Неверно")
            break   
print('Welcome')
'''

'''
for i in range(1, 20):
    if i == 5:
        break  # полностью прерывает любой цикл
    print(i)
'''

'''
for i in range(1, 11):
    if i == 5 or i == 7 or i == 9:
        continue  # прерывает итерацию и переходит на следующую +1
    print(i)
'''


# flag

# Задача 17 (Количество и максимальное значение)
# Рассматривается множество целых чисел, принадлежащих числовому отрезку [4668; 10414],
# которые делятся на 4 и не делятся на 7, 17. Найдите количество таких чисел и максимальное из них.
# В ответе запишите два целых числа: сначала количество, затем максимальное число.

count = 0
maxi = 0
mini = 0
summ = 0
flag = True

for i in range(4668, 10414+1):
    if i % 4 == 0 and i % 7 != 0 and i % 17 != 0:
        count += 1
        summ += i
        maxi = i
        if flag == True:
            mini = i
            flag = False


print(f'count = {count}, summ = {summ}, maxi = {maxi}, min = {mini}')








