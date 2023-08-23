

# region Задача от Clyde

# У вас есть список студентов и их оценки по предметам.
# Необходимо написать программу на Python,
# которая будет выводить средний балл каждого студента.

# Пример входных данных:
'''
students = {
    'Alice': [85, 90, 92],
    'Bob': [76, 85, 80],
    'Charlie': [90, 92, 88]
}

for key in students:
    summ = sum(students[key])
    dlina = len(students[key])
    print(f'Средний балл студента {key}: {round(summ / dlina, 2)}')


L = [123, 3455, -345, 234, 4365, -5465, 534]
M = [x for x in L if len(str(abs(x))) == 3]
print(M)  # [123, -345, 234, 534]
'''
# Ожидаемый вывод:
# Средний балл студента Alice: 89.0
# Средний балл студента Bob: 80.33333333333333
# Средний балл студента Charlie: 90.0

'''
print(students)  # {'Alice': [85, 90, 92], 'Bob': [76, 85, 80], 'Charlie': [90, 92, 88]}
print(students['Alice'])  # [85, 90, 92]
print(students.keys())  # dict_keys(['Alice', 'Bob', 'Charlie'])
print(students.values())  # dict_values([[85, 90, 92], [76, 85, 80], [90, 92, 88]])
print(students.items())  # dict_items([('Alice', [85, 90, 92]), ('Bob', [76, 85, 80]), ('Charlie', [90, 92, 88])])

for key in students.values():
    print(key)
    
    # [85, 90, 92]
    # [76, 85, 80]
    # [90, 92, 88]
'''
# endregion Задача от Clyde


# region Задание 1. Песни 2 +

# Что нужно сделать
# Продолжим писать приложение для удобного прослушивания музыки,
# но теперь песни хранятся в виде словаря, а не в виде вложенных списков.
# Каждая песня состоит из названия и продолжительности с точностью до долей минут.

# violator_songs = {
# 'World in My Eyes': 4.86,
# 'Sweetest Perfection': 4.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.9,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.20,
# 'Policy of Truth': 4.76,
# 'Blue Dress': 4.29,
# 'Clean': 5.83
# }

# Напишите программу, которая запрашивает у пользователя количество
# песен из списка и их названия, а на экран выводит общее время их звучания.

# Пример
# Сколько песен выбрать? 3
#
# Название первой песни: Halo
#
# Название второй песни: Enjoy the Silence
#
# Название третьей песни: Clean
#
# Общее время звучания песен: 14,93 минуты

# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# Решение с урока
'''
minut_count = 0
question = int(input('Сколько песен выбрать? '))
for track_count in range(0, question):  # 0 1 2
    song_name = input(f'Введите название {track_count+1} песни: ')
    # if violator_songs.get(song_name, None):
    try:  # обработчик исключений
        if song_name in song_name:
            minut_count += violator_songs[song_name]
    except KeyError:
        print('Такой песни нет в списке! ')
print(f'Общее время звучания песен: {round(minut_count, 2)}')
'''

'''
track_count = 1
minut_count = 0

question = int(input('Сколько песен выбрать? '))
for ask in range(question):
    print("Введите название ", track_count, "песни: ", end='')
    song_name = input()
    track_count += 1
    if violator_songs.get(song_name, None):
        minut_count += violator_songs[song_name]
    else:
        print('Такой песни нет в списке! ')
print('Общее время звучания песен: ', round(minut_count, 2))
'''

# endregion Задание 1. Песни — 2


# region Задание 3. Товары +
# Что нужно сделать
# В базе данных магазина вся необходимая информация по товарам
# делится на два словаря: первый отвечает за коды товаров,
# второй — за списки количества разнообразных товаров на складе:
#
# goods = {
# 'Лампа': '12345',
# 'Стол': '23456',
# 'Диван': '34567',
# 'Стул': '45678',
# }
# store = {
# '12345': [
# {'quantity': 27, 'price': 42},
# ],
# '23456': [
# {'quantity': 22, 'price': 510},
# {'quantity': 32, 'price': 520},
# ],
# '34567': [
# {'quantity': 2, 'price': 1200},
# {'quantity': 1, 'price': 1150},
# ],
# '45678': [
# {'quantity': 50, 'price': 100},
# {'quantity': 12, 'price': 95},
# {'quantity': 43, 'price': 97},
# ],
# }
# Каждая запись второго словаря отображает, сколько
# и по какой цене закупалось товаров. Цена указана за одну штуку.
#
# Напишите программу, которая рассчитывает общую стоимость
# позиций для каждого товара на складе и выводит эту информацию на экран.
#
# Результат работы программы:
#
# Лампа — 27 штук, стоимость 1134 рубля.
#
# Стол — 54 штуки, стоимость 27 860 рублей.
#
# Диван — 3 штуки, стоимость 3550 рублей.
#
# Стул — 105 штук, стоимость 10 311 рублей.
#
# Что оценивается
# Результат вычислений корректен.
# Формат вывода соответствует указанному в задаче.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

'''
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ]
}
for title, code in goods.items():
    total_quantity = 0
    total_price = 0
    for goods in store[code]:
        total_quantity += goods['quantity']
        total_price += goods['price'] * goods['quantity']
    print(f'{title} - {total_quantity} шт, {total_price} руб')
    # print(title, " - ", total_quantity, " шт, ", total_price, " руб")
'''

# endregion Задание 3. Товары


# region Задание 4. Гистограмма частоты 2 +

# Что нужно сделать
# Вы уже писали программу для лингвистов, которая получала на вход текст и считала,
# сколько раз каждый символ встречается в строке.
# Теперь задание изменилось: максимальную частоту выводить не нужно,
# но необходимо написать функцию, которая будет инвертировать полученный словарь.
# То есть в качестве ключа будет частота, а в качестве значения — список символов с этой частотой.
#
# По итогу нужно реализовать следующие подзадачи:
# получить текст и создать из него оригинальный словарь частот;
# создать новый словарь и заполнить его данными из оригинального словаря частот,
# используя количество повторов в качестве ключей,
# а буквы — в качестве значений, добавляя их в список для хранения.

# Пример
# Введите текст: здесь что-то написано
#
# Оригинальный словарь частот:
#
# : 2
# - : 1
# З : 1
# а : 2
# д : 1
# е : 1
# и : 1
# н : 2
# о : 3
# п : 1
# с : 2
# т : 2
# ч : 1
# ь : 1
#
# Инвертированный словарь частот:
#
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
#
# 2 : ['с', ' ', 'т', 'н', 'а']
#
# 3 : ['о']
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельных функциях.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

'''
text = input("Введите текст: ")

frequency = {}
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1
print(frequency)
'''

'''
my_list = [int(x) ** 2 for x in input().split() if len(x) > 2]  # 234   2354  234
print(my_list)

text = input("Введите текст: ")
frequency = {symbol: text.count(symbol) for symbol in text}
print(frequency)

for letter, freq in frequency.items():
    print(f'{letter} : {freq}')

print("Максимальная частота: ", max(frequency.values()))
'''

'''
frequency = {'З': 1, 'д': 1, 'е': 1, 'с': 2, 'ь': 1, ' ': 2, 'ч': 1, 'т': 2, 'о': 3, '-': 1, 'н': 2, 'а': 2, 'п': 1,
             'и': 1}
new_frequency = {val: [] for val in set(frequency.values())}

for val in set(frequency.values()):
    for key in frequency:
        if val == frequency[key]:
            new_frequency[val].append(key)

for elem, new_freq in new_frequency.items():
    print(f'{elem} : {new_freq}')
'''
# endregion Задание 4. Гистограмма частоты — 2


# region Задание 5. Словарь синонимов +
# Что нужно сделать
# Одна библиотека поручила вам написать программу для оцифровки словарей синонимов.
# На вход в программу подаётся N пар слов. Каждое слово является синонимом для своего парного слова.
#
# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны),
# затем запрашивает у пользователя слово и выводит на экран его синоним.
# Обеспечьте контроль ввода: если такого слова нет, выведите ошибку и запросите слово ещё раз.
# При этом проверка не должна зависеть от регистра символов.
#
# Пример
#
# Введите количество пар слов: 3
#
# Первая пара: Привет — Здравствуйте
#
# Вторая пара: Печально — Грустно
#
# Третья пара: Весело — Радостно
#
# Введите слово: интересно
#
# Такого слова в словаре нет.
#
# Введите слово: здравствуйте
#
# Синоним: Привет
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

# Задание с урока:
'''
n = int(input(" Введите количество пар слов: "))
synonym_dict = {}

for i in range(n):
    word1, word2 = input(f" Пара {i + 1}: ").split(" - ")
    synonym_dict[word1.lower()] = word2
    synonym_dict[word2.lower()] = word1
print(synonym_dict)
while True:
    word = input('\n Введите слово: ').lower()
    if word in synonym_dict:
        print(f"Синоним: {synonym_dict[word]}")
        break
    else:
        print('Такого слова нет в словаре!')
'''

# endregion Задание 5. Словарь синонимов


# region Задание 6. Пицца +
# Что нужно сделать
# В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто,
# что и сколько заказывал у них в определённый период.
# Вам нужно структурировать эту информацию и определить, сколько всего пицц купил каждый заказчик.
#
# На вход в программу подаётся N заказов.
# Каждый заказ представляет собой строку вида «Покупатель — название
# пиццы — количество заказанных пицц». Реализуйте код, который выводит список
# покупателей и их заказов по алфавиту. Учитывайте,
# что один человек может заказать одну и ту же пиццу несколько раз.
#
# Пример
#
# Введите количество заказов: 6
#
# Первый заказ: Иванов Пепперони 1
#
# Второй заказ: Петров Де-Люкс 2
#
# Третий заказ: Иванов Мясная 3
#
# Четвёртый заказ: Иванов Мексиканская 2
#
# Пятый заказ: Иванов Пепперони 2
#
# Шестой заказ: Петров Интересная 5
#
# Иванов:
#
# Мексиканская: 2
#
# Мясная: 3
#
# Пепперони: 3
#
# Петров:
#
# Де-Люкс: 2
#
# Интересная: 5
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру (перед названием пиццы пять пробелов).
# Переменные и функции имеют значимые имена, не только a, b, c, d.


# Решение с урока:
'''
orders_count = int(input('Введите кол-во заказов: '))
orders = {}

for i in range(orders_count):  # PEP8  flake8 rules
    order = input(f'{i+1}-заказ:')
    customer, pizza, count = order.split()  # ['Иванов', 'Пепперони', '2']
    if customer not in orders:
        orders[customer] = {}
    if pizza not in orders[customer]:
        orders[customer][pizza] = int(count)
    else:
        orders[customer][pizza] += int(count)

sorted_customer = sorted(orders.keys())
for customer in sorted_customer:
    print(f'\n{customer}:')
    for pizza, count in orders[customer].items():
        print(f'{pizza}: {count}')
    
'''

'''
orders = {}
N = int(input('Введите количество заказов: '))

for _ in range(N):
    order = input('Введите заказ в формате:'
                  ' Покупатель'
                  ' Название пиццы '
                  'Количество заказанных пицц, через пробел: ').split()
    buyer = order[0]
    pizza = order[1]
    quantity = int(order[2])

    if buyer not in orders:
        orders[buyer] = []

    orders[buyer].append((pizza, quantity))

buyers = sorted(orders.keys())

for buyer in buyers:
    print(f'{buyer}:')
    for pizza, quantity in orders[buyer]:
        print(f'  {pizza} - {quantity}')
'''
# endregion Задание 6. Пицца


# region Задание 7. Три списка +
# Что нужно сделать
# Даны три списка.
#
# array_1 = [1, 5, 10, 20, 40, 80, 100]
#
# array_2 = [6, 7, 20, 80, 100]
#
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# Нужно выполнить две задачи:
#
# найти элементы, которые есть в каждом списке;
# найти элементы из первого списка, которых нет во втором и третьем списках.
# Каждую задачу нужно выполнить двумя способами:
#
# без использования множеств;
# с использованием множеств.
# Пример выполнения на других данных:
#
# array_1 = [1, 2, 3, 4]
#
# array_2 = [2, 4]
#
# array_3 = [2, 3]
#
# Вывод:
#
# Задача 1:
#
# Решение без множеств: 2
#
# Решение с множествами: 2
#
# Задача 2:
#
# Решение без множеств: 1
#
# Решение с множествами: 1
#
# Что оценивается
# Результат вычислений корректен.
# Обе задачи решены двумя предложенными способами. Один из способов — обязательно с использованием множеств и операций над множествами.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельной функции.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

'''
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


elements_with_set = sorted(set(array_1) & set(array_2) & set(array_3))
'''

'''
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Решение задачи при помощи множеств:
array_1_new = set(array_1)
array_2_new = set(array_2)
array_3_new = set(array_3)

# Решение задачи без множеств:
dif_list = []
gen_list = []

for el in array_1:
    if el in array_2 and el in array_3:
        gen_list.append(el)
    if el not in array_2 and el not in array_3:
        dif_list.append(el)


print("Задача 1:")
print("Решение задачи  без множеств: ", gen_list)
print("Решение задачи с множествами: ", sorted(array_1_new & array_2_new & array_3_new))
print()
print("Задача 2:")
print("Решение задачи  без множеств: ", dif_list)
print("Решение задачи c множествами: ", sorted(array_1_new.difference(array_2_new, array_3_new)))
'''

# endregion Задание 7. Три списка


# region Задание 8. Снова палиндром +
# Что нужно сделать
# Пользователь вводит строку. Необходимо написать программу, которая определяет,
# существует ли у этой строки перестановка, при которой она станет палиндромом.
# Затем она должна выводить соответствующее сообщение.

# Пример 1
#
# Введите строку: aab
#
# Можно сделать палиндромом

# Пример 2
#
# Введите строку: aabc
#
# Нельзя сделать палиндромом
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Формат вывода соответствует примеру.
# Основной функционал описан в отдельной функции.
# Переменные и функции имеют значимые имена, не только a, b, c, d.

'''
slovo = input('Введите строку: ')
if slovo == slovo[::-1]:
    print('Палиндром')
else:
    print('Нет')
'''


'''
from itertools import permutations
slovo = input('Введите строку: ')
for s in permutations(slovo):
    if s == s[::-1]:
        print('YES')
        print(s)
        exit()
print('NO')
'''

# Решение Марии:
'''
from itertools import permutations

word = input("Введите слово: ")
for vers in permutations(word):
    if vers == vers[::-1]:
        print("Можно сделать палиндромом")
        break
else:
    print("Нельзя cделать палиндромом")
'''

# endregion Задание 8. Снова палиндром


# region # Работа с библиотеками +
'''
import math
print(math.sqrt(16))

import math as m
print(m.sqrt(16))

from math import sqrt, log, fabs
print(sqrt(16))

from math import *
print(sqrt(16))
'''
# endregion # Работа с библиотеками


# region Задание: Словарь программиста +
# https://stepik.org/lesson/488831/step/1?unit=480067
'''
n = int(input('Введите кол-во слов в словаре программиста: '))
programmer_dict = {}
for i in range(n):
    key, value = input(f'Введите значение {i+1}: ').split(': ')
    programmer_dict[key.lower()] = value

# print(programmer_dict)
m = int(input('Введите кол-во запрашиваемых слов: '))
keys = []
for i in range(m):
    keys.append(input().lower())

for key in keys:
    try:
        print(programmer_dict[key])
    except KeyError:
        print('Не найдено')
'''

# Решение со Степика
'''
mydict = {}

for _ in range(int(input())):
    key, value = input().split(': ')
    mydict[key.lower()] = value

for _ in range(int(input())):
    print(mydict.get(input().lower(), 'Не найдено'))
'''

# endregion Задание: Словарь программиста https://stepik.org/lesson/488831/step/1?unit=480067 +


# region Задача про палиндром +
'''
def is_poly(string: str) -> int:
    char_dict: dict = {}
    for i_sym in string:    # 12312345
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
        print(char_dict)  # {'1': 2, '2': 2, '3': 2, '4': 1, '5': 1}

    odd_count: int = 0
    for i_value in char_dict.values():  # 2, 2, 2, 1, 1
        if i_value % 2 != 0:
            odd_count += 1  
    return odd_count


my_string: str = input('Введите строку: ')  # 12312345
if is_poly(my_string) <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
'''
# endregion Задача про палиндром


# region Задача 3. Универсальная программа
# Что нужно сделать
# Напишите функцию, возвращающую список элементов итерируемого объекта
# (кортежа, строки, списка, словаря), у которых индекс — это простое число.
#
# Для проверки на простое число напишите отдельную функцию is_prime.
#
# Необязательное усложнение: сделайте так, чтобы основная
# функция состояла только из оператора return и так же возвращала список.
#
# Пример вызова функции:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ответ в консоли: [2, 3, 5, 7]
#
# Пример вызова функции:
# print(crypto('О Дивный Новый мир!'))
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']
#
# Советы и рекомендации
# Для нумерации элементов используйте функцию enumerate. Это позволит работать одинаково со всеми структурами данных.
'''
def old_get_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return sorted(divisors)


def get_divisors(num):
    divisors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return sorted(divisors)
    
x = 2000000000
print(get_divisors(x))
print(old_get_divisors(x))
'''

'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def crypto(iterable):
    if isinstance(iterable, dict):
        iterable = iterable.values()
    return [elem for i, elem in enumerate(iterable) if is_prime(i)]


print(crypto({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
'''
# endregion Хочу разобрать эту задачу: Задача 2. Универсальная программа


# region Задача 2. Универсальная программа +
#
# Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
# При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
#
# Напишите функцию, которая возвращает список из элементов итерируемого
# объекта (кортежа, строки, списка, словаря), у которых индекс чётный.
#
# Пример 1:
# Допустим, есть такая строка: 'О Дивный Новый мир!'
# Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']
#
#
#
# Пример 2:
# Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
# Результат: [100, 300, 0, 'а']
#
#
#
# Примечание: для проверки типа можно использовать функцию
#
# isinstance(<элемент>, <тип данных>), которая возвращает True, если элемент принадлежит к этому типу данных,
# и возвращает False в противном случае.
'''
def return_even_elements(data):
    result = []
    if isinstance(data, dict):
        data = data.values()
    for index, value in enumerate(data):
        if index % 2 == 0:
            result.append(value)
    return result

print(return_even_elements('О Дивный Новый мир!'))
print(return_even_elements([100, 200, 300, 'буква', 0, 2, 'а']))
print(return_even_elements({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))
'''
# endregion Задача 3. Универсальная программа


# region Как убрать все символы пунктуации +
'''
import string
message = input()
get_message_bot = message.lower().strip()
for sym in string.punctuation:
    get_message_bot = get_message_bot.replace(sym, '')
print(get_message_bot)
'''
# endregion как убрать все символы пунктуации


# region Задача 3. Неправильный код +
# Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
# Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный индекс
# и случайное значение, а затем по этим индексу и значению меняет сам кортеж.
# Функция должна возвращать кортеж и случайное значение.
#
# В основном коде функция используется два раза, и на экран два раза выводится новый
# кортеж и случайное значение. Причём второй раз выводится сумма первого случайного значения и второго.
#
# Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.
'''
import random


def change(nums: tuple):  # (1, 2, 3, 4, 5)
    index = random.randint(0, len(nums)-1)
    value = random.randint(100, 1000)
    nums = list(nums)  # В списках можно менять значения по индексу, а в кортежах нельзя
    nums[index] = value
    return tuple(nums), value


# i        0  1  2  3  4
my_nums = (1, 2, 3, 4, 5)
print(my_nums)
new_nums, rand_val_1 = change(my_nums)
print(new_nums, rand_val_1)
new_nums_2, rand_val_2 = change(new_nums)
print(new_nums_2, rand_val_1 + rand_val_2)
'''
# endregion Задача 3. Неправильный код

# region Задача 5. Сортировка кортежа +
'''
def tpl_sort(my_tuple: tuple) -> tuple:
    for num in my_tuple:
        if not isinstance(num, int):
            return my_tuple
    return tuple(sorted(my_tuple))
'''
# endregion Задача 5.


# todo: Мария
# на прошлом уроке:  Прорешали все задачи с вопросами скиллбокс, а именно: Задача про палиндром, Задача 3. Универсальная программа, Как убрать все символы пунктуации, Задача 3. Неправильный код, Задача 5. Сортировка кортежа.
# на следующем уроке: