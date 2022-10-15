

# Одностройчный комментарий

'''
Многострочный комментарий
'''




# Типы данных
# print(4, type(4))
# print('4', type('4'))

# Типы данных переменных
'''

a = 4  # int (integer) - целочисленные значения

b = '4'  # str (string) -  строковый тип данных, хранит слова6 буквы, цифры

c = 4.5  # float (число с плавающей точкой) - вещественные числа (дроби)

d1 = True  # bool (boolean) - элементы Булевой алгебры, математическая логика
d2 = False
print(4 < 10)
'''

# Конвртация типов данных
'''
x = 5
print(x, type(x))

x = str(x)  # новый x равен старые перевести в строку
print(x, type(x))

x = float(x)
print(x, type(x))

x = int(x)
print(x, type(x))
'''

# Ввод данных с клавиатуры
'''
name = input('Name: ')  # функция input() получает на вход строку
print('Hello,', name)

x = int(input('x: '))
print(x, type(x))

# x = float(input('x: '))
# print(x, type(x))
'''

s1 = 'hello '
s2 = 'Andrey'
print(s1 + s2)  # конкотенация строк (склеивание)

# Вывод функции print()
weather = 'облачно'
temperature = 24
# Ого, сегодня так облачно, а температура 24 градуса!
print('Ого, сегодня так', weather, ', а температура', temperature, 'градуса!')
print('Ого, сегодня так ' + weather + ', а температура ' + str(temperature) + ' градуса!')
print('Ого, сегодня так {}, а температура {} градуса!'.format(weather, temperature))
print('Ого, сегодня так %s, а температура %d градуса!'%(weather, temperature))  # для float - %f
print(f'Ого, сегодня так {weather}, а температура {temperature} градуса!')

# import decimal as d
from decimal import Decimal

for y in range(-100, 100):
    if (y - Decimal('18.2')) + Decimal('3.8') == Decimal('15.6'):
        print(y)

'''
i = -10
while i <= 10:
    if Decimal('5') * Decimal('y') + Decimal('5') - Decimal('2') * Decimal('y') == Decimal('15.5'):
        print(y)
        break
    i += Decimal('0.01')
    print(i)
'''

print(Decimal('5') * Decimal('3.5') + Decimal('5') - Decimal('2') * Decimal('3.5') == Decimal('15.5'))

# todo: На следующем уроке: Арифметика с переменными, sep и end









