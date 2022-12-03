
# region Пост: Как проверить, что число простое

# Вариант 1
x = int(input('x: '))
dl = 0  # создаем счетчик для подсчета кол-ва делителей
for i in range(1, x+1):  # пробегаем все числа, которые могут претендовать на делитель
    if x % i == 0:
        dl += 1  # если находим такое число, то увеличиваем счетчик на +1
if dl == 2:
    print(True)  # если же делителей ровно два, то выводим истину
else:
    print(False)

# Вариант 2
x = int(input('x: '))
if len([i for i in range(1, x+1) if x % i == 0]) == 2:
    print(True)
else:
    print(False)


# Вариант 3
def MySimpler(x):  # для удобства вычислений, можно вынести скрипт в отдельную функцию
    if x == 1:  # единица не является простым, хотя и не содержит других делителей
        return False
    for i in range(2, int(x**0.5) + 1):  # это интересная штука, о ней читайте ниже
        if x % i == 0:  # если нашелся делитель, то прерываем программу
            return False
    return True

x = int(input('x: '))
print(MySimpler(x))

# Вариант 4
def Simpler(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

x = int(input('x: '))
print(Simpler(x))

# endregion Пост: Как проверить, что число простое

