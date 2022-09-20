import random
import telebot
from telebot import types

bot = telebot.TeleBot('5447726623:AAG_EYLjLIFqOz80fZHhZcBiMrVlylUdJcI')
QUE = []
wolit = [0]
GIFT = [0, 100, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000, 200000, 400000, 800000, 1500000, 3000000]
Balance = [0]
n = 3  # диапазон рандома вопросов

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup()

    if call.data == 'wolit':
        wolit.append(Balance[0])
        QUE.clear()
        Balance[0] = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        msg = bot.send_message(call.message.chat.id, f"Новое значение денег в вашем кошельке: {sum(wolit)}", reply_markup=markup)

    if call.data == 'show':
        msg = bot.send_message(call.message.chat.id, f"Денег в вашем кошельке: {sum(wolit)}")


    if call.data == 'que1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Юнг')
        btn2 = types.KeyboardButton('Гегель')
        btn3 = types.KeyboardButton('Ницше')
        btn4 = types.KeyboardButton('Шопенгауэр')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Кто из этих философов в 1864 году написал музыку на стихи А.С. Пушкина «Заклинание» и «Зимний вечер»?\nЮнг\nГегель\nНицше\nШопенгауэр"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Один')
        btn2 = types.KeyboardButton('Два')
        btn3 = types.KeyboardButton('Три')
        btn4 = types.KeyboardButton('Четыре')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Сколько раз в сутки подзаводят куранты Спасской башни Кремля?\nОдин\nДва\nТри\nЧетыре"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Романист')
        btn2 = types.KeyboardButton('Драматург')
        btn3 = types.KeyboardButton('Поэт')
        btn4 = types.KeyboardButton('Эссеист')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Кто 1-м получил Нобелевскую премию по литературе?\nРоманист\nДраматург\nПоэт\nЭссеист"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

'''
    if call.data == 'que4':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='true'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "С какой буквы начинаются слова, опубликованные в 16-м томе последнего издания Большой советской энциклопедии?\nA: М\nB: Н\nC: О\nD: П"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que5':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='true'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "Кто из перечисленных был пажом во времена Екатерины II?\nA: Д.И. Фонвизин\nB: Г.Р. Державин\nC: А.Н. Радищев\nD: Н.М. Карамзин"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que6':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='true'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "Какой химический элемент назван в честь злого подземного гнома?\nA: Гафний\nB: Кобальт\nC: Бериллий\nD: Теллур"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que7':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='true'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "В какой из этих столиц бывших союзных республик раньше появилось метро?\nA: Тбилиси\nB: Ереван\nC: Баку\nD: Минск"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que8':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='true'))
        message_text = "Сколько морей омывают Балканский полуостров?\nA: 3\nB: 4\nC: 5\nD: 6"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que9':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='true'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "Реки с каким названием нет на территории России?\nA: Шея\nB: Уста\nC: Спина\nD: Палец"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que10':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='true'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "Что такое лобогрейка?\nA: Жнейка\nB: Шапка\nC: Болезнь\nD: Печка"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que11':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='true'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "Какой роман Фенимор Купер написал на спор с женой?\nA: «Предосторожность»\nB: «Пионеры»\nC: «Последний из могикан»\nD: «Зверобой»"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que12':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='true'))
        message_text = "Какой вид кавалерии предназначался для боевых действий как в конном, так и в пешем строю?\nA: Кирасиры\nB: Уланы\nC: Драгуны\nD: Гусары"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que13':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='true'))
        message_text = "Какое имя не принимал ни один папа римский?\nA: Валентин\nB: Евгений\nC: Георгий \nD: Виктор"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que14':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='true'))
        message_text = "В каком немецком городе родилась будущая императрица России Екатерина II?\nA: Висбаден\nB: Цербст\nC: Штеттин \nD: Дармштадт"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que15':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='false'),
                   types.InlineKeyboardButton("D", callback_data='true'))
        message_text = "Что запрещал указ, который в 1726 году подписала Екатерина I?\nA: Точить лясы\nB: Бить баклуши\nC: Пускать пыль в глаза \nD: Переливать из пустого в порожнее"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
'''

@bot.message_handler(commands=['start'])
def start(message):
    while True:
        temp = random.randint(1, n)
        if len(QUE) == n:
            break
        elif temp not in QUE:
            QUE.append(temp)
            print(QUE)
            break
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Начать игру", callback_data='que' + str(temp)))
    bot.send_message(message.chat.id, 'Добро пожаловать в игру\n *"Кто хочет стать миллионером"!*', parse_mode='Markdown', reply_markup=markup)



@bot.message_handler(commands=['show_list'])
def show_list(message):
    if message.chat.id == 811476623 or message.chat.id == 1891281816:
        message_text = 'Вопросы на которые вы ответили правильно: '
        Temp = QUE[:-1]
        Temp.sort()
        for i in range(0, len(Temp)):
            message_text += str(Temp[i]) + ', '
        message_text = message_text[:-2]
        bot.send_message(message.chat.id, message_text)
    else:
        bot.send_message(message.chat.id, 'Вы не можете использовать эту функцию')



@bot.message_handler(commands=['show'])
def show(message):
    bot.send_message(message.chat.id, f'*Промежуточные результаты:*\nКоличество правильных ответов: {len(QUE)-1}\nКоличество оставшихся вопросов: {16-len(QUE)}', parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Начать заново':
        while True:
            temp = random.randint(1, n)
            if len(QUE) == n:
                break
            elif temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Следующий вопрос", callback_data='que' + str(temp)))
        bot.send_message(message.chat.id, "Запустите игру заново нажатием клавиши:", reply_markup=markup)

    # que1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if get_message_bot == 'Юнг':
        QUE.clear()    # Если ответ неправильный, то мы опустошаем список
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))   # Генерим кнопку для перезапуска игры
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)  # А тут просто в одну строку выводи кол-во денег: Список[кол-во ответов]

    if get_message_bot == 'Гегель':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    if get_message_bot == 'Шопенгауэр':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    if get_message_bot == 'Ницше':
        Balance[0] = GIFT[len(QUE)]  # В списке Balance, на 0 позиции будет храниться кол-во очков заработанных на данный момент игры
        while True:
            temp = random.randint(1, n)  # рандомим вопрос - n символизирует кол-во готовых вопросов (меняется наверху программы)
            if len(QUE) == n:  # Если длина равна n, то у нас кончились все вопросы. Таким образом мы избегаем зацикливания как у нас было раньше
                break
            elif temp not in QUE:  # Если нарандомили вопрос которого нет, до добавляем его в список и выходи из цикла
                QUE.append(temp)
                print(QUE)
                break
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Следующий вопрос", callback_data='que' + str(temp)),
                    types.InlineKeyboardButton("Заглянуть в кошелёк", callback_data='show'),  # тут кол-во денег в кошельке (не равно балансу)
                    types.InlineKeyboardButton("Забрать выигрыш", callback_data='wolit'))   # тут мы обнулим баланс и перенесем деньги в кошелек
        bot.send_message(message.chat.id, f"Правильный ответ\nВаш выигрыш: {Balance[0]} рублей", reply_markup=markup)  # Ну и переменную с балансом выводим на экран
    # que1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if get_message_bot == 'Два':
        Balance[0] = GIFT[len(QUE)]
        while True:
            temp = random.randint(1, n)
            if len(QUE) == n:
                break
            elif temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Следующий вопрос", callback_data='que' + str(temp)),
                   types.InlineKeyboardButton("Заглянуть в кошелёк", callback_data='show'),
                   types.InlineKeyboardButton("Забрать выигрыш", callback_data='wolit'))
        bot.send_message(message.chat.id, f"Правильный ответ\nВаш выигрыш: {Balance[0]} рублей", reply_markup=markup)

    if get_message_bot == 'Один':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    if get_message_bot == 'Четыре':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    if get_message_bot == 'Три':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)
    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if get_message_bot == 'Поэт':
        Balance[0] = GIFT[len(QUE)]
        while True:
            temp = random.randint(1, n)
            if len(QUE) == n:
                break
            elif temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Следующий вопрос", callback_data='que' + str(temp)),
                   types.InlineKeyboardButton("Заглянуть в кошелёк", callback_data='show'),
                   types.InlineKeyboardButton("Забрать выигрыш", callback_data='wolit'))
        bot.send_message(message.chat.id, f"Правильный ответ\nВаш выигрыш: {Balance[0]} рублей", reply_markup=markup)

    if get_message_bot == 'Романист':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    if get_message_bot == 'Драматург':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    if get_message_bot == 'Эссеист':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)
    # que3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.polling(none_stop=True)
