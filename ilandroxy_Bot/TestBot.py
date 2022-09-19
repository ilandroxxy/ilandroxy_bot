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
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)


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
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup0.add(types.KeyboardButton('Начать игру'))

    message_text = 'Добро пожаловать в игру "Кто хочет стать миллионером"!'
    bot.send_message(message.chat.id, message_text, reply_markup=markup0)

@bot.message_handler(commands=['show_list'])
def show_list(message):
    if message.chat.id == 811476623:
        message_text = 'Вопросы на которые вы ответили правильно: '
        QUE.sort()
        for i in range(0, len(QUE)):
            message_text += str(QUE[i]) + ', '
        message_text = message_text[:-2]
        bot.send_message(message.chat.id, message_text)
    else:
        bot.send_message(message.chat.id, 'вы не можете использовать эту функцию')

@bot.message_handler(commands=['show'])
def show(message):
    message_text = 'количество правильных ответов: ' + str(len(QUE)) + '\nколичество оставшихся вопросов: ' + str(15-len(QUE))
    bot.send_message(message.chat.id, message_text)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Начать игру' or get_message_bot == 'Начать заново':
        while True:
            temp = random.randint(1, n)
            if len(QUE) == n:
                break
            elif temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        btn = 'que' + str(temp)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("GO", callback_data=btn))
        bot.send_message(message.chat.id, "Нажмите GO для того чтобы перейти на 1 вопрос", reply_markup=markup)



    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if get_message_bot == 'Два':
        message_text = "Правильный ответ\nВаш выигрыш: " + str(GIFT[len(QUE)]) + ' рублей'
        Balance[0] = GIFT[len(QUE)]
        while True:
            temp = random.randint(1, n)
            if len(QUE) == n:
                break
            elif temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        btn = 'que' + str(temp)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("GO", callback_data=btn),
                   types.InlineKeyboardButton("Заглянуть в кошелёк", callback_data='show'),
                   types.InlineKeyboardButton("Забрать выигрыш", callback_data='wolit'))
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Один':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Четыре':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Три':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)
    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if get_message_bot == 'Юнг':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Гегель':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Шопенгауэр':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Ницше':
        message_text = "Правильный ответ\nВаш выигрыш: " + str(GIFT[len(QUE)]) + ' рублей'
        Balance[0] = GIFT[len(QUE)]
        while True:
            temp = random.randint(1, n)
            if len(QUE) == n:
                break
            elif temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        btn = 'que' + str(temp)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("GO", callback_data=btn),
                   types.InlineKeyboardButton("Заглянуть в кошелёк", callback_data='show'),
                   types.InlineKeyboardButton("Забрать выигрыш", callback_data='wolit'))
        bot.send_message(message.chat.id, message_text, reply_markup=markup)
    # que1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    # que3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if get_message_bot == 'Поэт':
        message_text = f"Правильный ответ\nВаш выигрыш: {GIFT[len(QUE)]} рублей"
        Balance[0] = GIFT[len(QUE)]
        while True:
            temp = random.randint(1, n)
            if len(QUE) == n:
                break
            elif temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        btn = 'que' + str(temp)
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("GO", callback_data=btn),
                   types.InlineKeyboardButton("Заглянуть в кошелёк", callback_data='show'),
                   types.InlineKeyboardButton("Забрать выигрыш", callback_data='wolit'))
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Романист':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Драматург':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Эссеист':
        QUE.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))

        message_text = f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)
    # que3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.polling(none_stop=True)
