

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


# region Задание 2. Криптовалюта
# Что нужно сделать
# При работе с API (application programming interface)
# сайта биржи по криптовалюте вы получили такие данные в виде словаря:
#
# data = {
# "address": "0x544444444444",
# "ETH": {
# "balance": 444,
# "totalIn": 444,
# "totalOut": 4
# },
# "count_txs": 2,
# "tokens": [
# {
# "fst_token_info": {
# "address": "0x44444",
# "name": "fdf",
# "decimals": 0,
# "symbol": "dsfdsf",
# "total_supply": "3228562189",
# "owner": "0x44444",
# "last_updated": 1519022607901,
# "issuances_count": 0,
# "holders_count": 137528,
# "price": False
# },
# "balance": 5000,
# "totalIn": 0,
# "total_out": 0
# },
# {
# "sec_token_info": {
# "address": "0x44444",
# "name": "ggg",
# "decimals": "2",
# "symbol": "fff",
# "total_supply": "250000000000",
# "owner": "0x44444",
# "last_updated": 1520452201,
# "issuances_count": 0,
# "holders_count": 20707,
# "price": False
# },
# "balance": 500,
# "totalIn": 0,
# "total_out": 0
# }
# ]
# }
# Теперь необходимо обработать эти данные.
#
# Напишите программу, которая выполняет следующий алгоритм действий:
#
# Вывести списки ключей и значений словаря.
# В ETH добавить ключ total_diff со значением 100.
# Внутри fst_token_info значение ключа name поменять с fdf на doge.
# Удалить total_out из tokens и присвоить его значение в total_out внутри ETH.
# Внутри sec_token_info изменить название ключа price на total_price.
# После выполнения алгоритма выводить результат (словарь) не нужно.
#
# Советы и рекомендации
# Если вы достали из словаря список по ключу, то можете применять к нему методы списка.
# Например:
#
# словарь[“список”].append(123)
#
# Python возьмёт из словаря объект по ключу «список» и применит к нему метод append.
# Эта же логика работает с другими типами данных. Например, если вы достали из словаря словарь,
# то к нему можно применять методы словаря, а если достали строку — методы строк.
#
# Чтобы не запутаться, распечатывайте объект, который получаете в данный момент. Также можно распечатать тип объекта:
# print(data)
# print(data[‘ключ’], type(data[‘ключ’]))
# print(data[‘ключ’][0], type(data[‘ключ’][0]))
# и так далее.
#
# Так вы всегда будете понимать, над каким объектом работаете в данный момент.
#
# Что оценивается
# Результат вычислений корректен.
# В коде соблюдается порядок действий алгоритма.
# Не используется других переменных, кроме data.

'''
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuance's_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
print('\nСписок ключей и их значений: ')
for i_elem in data:
    print(i_elem, "-", data[i_elem])
print()

print('Добавила новый ключ total_dif в ETH')
data["ETH"]["total_dif"] = 100
for i_elem in data:
    print(i_elem, "-", data[i_elem])
print()

print('Внутри ключа fst_token_info поменяла значение на с fdf на doge: ')
data["tokens"][0]["fst_token_info"]["name"] = "doge"
for i_elem in data:
    print(i_elem, "-", data[i_elem])
print()

print("Удалить total_out из tokens и присвоить его значение в total_out внутри ETH: ")
data["ETH"]["total_out"] = 0
data["tokens"][0].pop("total_out")
for i_elem in data:
    print(i_elem, "-", data[i_elem])
print()

print('Внутри sec_token_info изменить название ключа price на total_price: ')
data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"].pop("price")
for i_elem in data:
    print(i_elem, "-", data[i_elem])
print()

'''

# endregion Задание 2. Криптовалюта


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


# region # Работа с библиотеками
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


# region Задание: Словарь программиста https://stepik.org/lesson/488831/step/1?unit=480067

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

# endregion Задание: Словарь программиста https://stepik.org/lesson/488831/step/1?unit=480067