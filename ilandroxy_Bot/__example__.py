
# todo: Лабораторная 1
'''
print("Введите переменные: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("c = "))

r = ((25 + (a**2)/(b**2)) / (a + (b**2 + c**3 - d**4) / 45))**0.5
print("Результат: ", r)
'''


# todo: Лабораторная 2
# Задание 1.2
'''
print("Введите переменные: ")
a = int(input("a = "))
b = int(input("b = "))
if a * b < 0:
    print("Результат: ", -2 * (a * b))
else:
    print("Результат: ", 3 * (a * b))
'''

# Задание 2.2
'''
# Решение с помощью цикла-счетчика:
print("Введите переменные: ")
a = int(input("a = "))
b = int(input("b = "))
n = b - a - 1
if n == 0:
    print('Ошибка')
else:
    for x in range(n):
        print(b-1-x, end=" ")
    print("\nКоличество целых чисел N: ", n)

# Решение с помощью цикла-предусловия (while):
print("Введите переменные: ")
a = int(input("a = "))
b = int(input("b = "))
x = 0
n = b - a - 1
if n == 0:
    print('Ошибка')
else:
    while x < n:
        print(b-1-x, end=" ")
        x += 1
    print("\nКоличество целых чисел N: ", n)

# Решение с помощью цикла-постусловия
print("Введите переменные: ")
a = int(input("a = "))
b = int(input("b = "))

n = b - a - 1
if n == 0:
    print('Ошибка')
else:
    x = 0
    while True:
        print(b - 1 - x, end=" ")
        x += 1
        if x >= n:
            break
    print("\nКоличество целых чисел N: ", n)
'''

# todo: Лабораторная 3
'''
s = input("Введем строку данных: ")

if "..." in s:
    print("Есть последовательность из трех точек")
else:
    print("Нет последовательности из трех точек")

new_s = "0"
for c in s:
    if c.isdigit():
        new_s += c

print(int(new_s), type(new_s))
'''

# todo: Лабораторная 4
'''
# Формула l = 2 * число пи * радиус
def circle_length(radius):
    return 2 * 3.14 * radius

r = int(input("Введите радиус окружности: "))
length = circle_length(r)
print("Длина окружности: " + round(length, 3))
'''


