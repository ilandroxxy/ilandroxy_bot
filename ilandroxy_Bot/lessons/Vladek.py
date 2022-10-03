
# Домашка
'''
x = int(input())
a = x // 1000
b = (x // 100) % 10
c = (x // 10) % 10
d = x % 10
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

# Вариант решения через строки:
x = int(input())
x = str(x)
# 2345  ->  '2345'
print('Цифра в позиции тысяч равна', x[0])
print('Цифра в позиции сотен равна', x[1])
print('Цифра в позиции десятков равна', x[2])
print('Цифра в позиции единиц равна', x[3])
'''

'''

name = input()
print('Привет,', name)
'''

'''
a = int(input())
b = int(input())
c = int(input())
if a < b < c or a > b > c:
    print(b)
elif b < c < a or b > c > a:
    print(c)
else:
    print(a)
'''



'''
x = int(input())
a = x <= 60
b = 60 < x <= 64
c = 64 < x <= 69
print('Легкий вес', a, type(a))
print('Первый полусредний вес', b)
print('Полусредний вес', c)
'''

'''
x = int(input())
if x < 60:
    print('Легкий вес')
elif x < 64:
    print('Первый полусредний вес')
elif x < 69:
    print('Полусредний вес')
'''



# Ход коня
'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
if x1 == x2 and y1 == y2:
    print("Стоять на месте нельзя!")
elif (x1+1 == x2 and y1+2 == y2):
    print('YES')
elif (x1+1 == x2 or y1-2 == y2):
    print('YES')
elif (x1+2 == x2 or y1+1 == y2):
    print('YES')
elif (x1-2 == x2 or y1+1 == y2):
    print('YES')
elif (x1+2 == x2 or y1-1 == y2):
    print('YES')
elif (x1-2 == x2 or y1-1 == y2):
    print('YES')
elif (x1-1 == x2 or y1+2 == y2):
    print('YES')
elif (x1-1 == x2 or y1-2 == y2):
    print('YES')
else:
    print("NO")
'''


# Ход короля
'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
if x1 == x2 and y1 == y2:
    print("Стоять на месте нельзя!")
elif (x1+1 == x2 and y1 == y2):
    print('YES')
elif (x1-1 == x2 and y1 == y2):
    print('YES')
elif (x1 == x2 and y1+1 == y2):
    print('YES')
elif (x1 == x2 and y1-1 == y2):
    print('YES')
elif (x1+1 == x2 and y1+1 == y2):
    print('YES')
elif (x1-1 == x2 and y1-1 == y2):
    print('YES')
elif (x1-1 == x2 and y1+1 == y2):
    print('YES')
elif (x1+1 == x2 and y1-1 == y2):
    print('YES')
else:
    print("NO")
'''


# Циклы:
# Ключевые слова: while, for, range, break, continue, flag


# Варианты циклов: 1. Повторить n раз, 2. Повторять от a до b раз, 3. Повторять пока условие истинно, 4. Бесконечный цикл

#s = '123 456'
#print(s, len(s))  # len() - это функция, которая возвращает длину (кол-во элементов в нем): строки, списка, кортежа и тд

# цикл for - помогает перебирать элементы коллекции
'''
for x in s:  # тут переменная х принимает значение элементов строки
    print(x)

print()
# цикл for пробегает строку по индексам
for i in range(0, len(s)):  # [0, len(s) ) or [0, len(s)-1]
    print(s[i])

n = 10
# функция range:
for i in range(n+1):  # [0, n)   n - stop
    print(i, end=" ")
print()

for i in range(0, n+1):  # [0, n)   0 - start, n = stop
    print(i, end=" ")
print()

for i in range(0, n+1, 2):  # 0 - start, n - stop, 2 - step
    print(i, end=" ")
print()
'''


# цикл while - цикл с условием
'''
n = 10

for i in range(0, n+1, 2):  # 0 - start, n - stop, 2 - step
    print(i, end=" ")
print()


i = 0  # START
while i <= n:  # пока условие выполняется (истинно) # STOP
    print(i, end=" ")
    i += 2  # STEP
    # i = i + 1  - аналогичная запись
print()

# Пример: 
x = int(input())
summ = 0
M = []
while x > 0:
    summ += x % 10  # summ = summ + (x % 10)
    M.append(x % 10)  # добавления элемента в конец списка
    x //= 10  # x = x // 10
print(summ)
M.reverse()
print(f"Сам список: {M}\nСумма элементов списка: {sum(M)}\nМинимальный элемент списка: {min(M)}\n"
      f"Максимальный элемент списка: {max(M)}\nДлина списка (или кол-во элементов в нем): {len(M)}")
'''




# Бесконечный цикл
'''  
import random

password = 'qwerty'
count = 0
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('Welcome!')
        break
    print("Пароль неверный, попробуйте снова!")
    count += 1
    if count == 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(f'Пройдите капчу, решив пример:')
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            count = 0
            continue
        else:
            print('Вам бан!')
            break
'''

import telebot
from telebot import types
import time


# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ` ⛔  ️✅ 📊📈🧮
bot = telebot.TeleBot('5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU')
# real 5640042697:AAGA5EIFYkt2urDf-UXlcyoVLG4x375Ntjk
# test 5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU


# START
@bot.message_handler(commands=['start'])
def start(message):
    text = 'Привет, этот бот нужен для перевода в разные системы счисления!'
    bot.send_message(message.chat.id, text)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Перевод из 10-ной в n-ную')
    markup.add(btn1)
    bot.send_message(message.chat.id, f'Твой ID: {message.chat.id}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Перевод из 10-ной в n-ную':
        bot.send_message(message.chat.id,
                         "Просто напишите число и систему, через запитую, а бот переведет его в эту систему.\n\n"
                         "Число должно быть введено в виде: [Число 10-ное] [n-ная система]\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text
            if text_message != '0':
                M = [int(i) for i in text_message.split()]
                x = M[0]
                n = M[1]
                A = []
                while x > 0:
                    A.append(str(x % n))
                    x //= n
                A.reverse()
                res = "".join(A)
                bot.send_message(message.chat.id, f'Число {x} в десятичной системе счисления, при прееводе в {n}-ную равняется: {res}')

            else:
                bot.send_message(message.chat.id, 'Команда отменена, ждем вас с нетерпением обратно 🤖',)

        bot.register_next_step_handler(message, message_input)



if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)








