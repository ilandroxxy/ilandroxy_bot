import random
import telebot
from telebot import types
from telebot import callback_data

bot = telebot.TeleBot('5447726623:AAG_EYLjLIFqOz80fZHhZcBiMrVlylUdJcI')
QUE = []
wolit = 0
GIFT = [0, 100, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000, 200000, 400000, 800000, 1500000, 3000000]
bank = 0

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)


    if call.data == 'wolit':
        global wolit
        wolit += GIFT[len(QUE)-1]
        QUE.clear()
        msg = bot.send_message(call.message.chat.id, "денег в вашем кошельке: " + str(wolit))

    if call.data == 'que1':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'), types.InlineKeyboardButton("B", callback_data='false'), types.InlineKeyboardButton("C", callback_data='true'), types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "Кто из этих философов в 1864 году написал музыку на стихи А.С. Пушкина «Заклинание» и «Зимний вечер»?\nA: Юнг\nB: Гегель\nC: Ницше\nD: Шопенгауэр"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Один')
        btn2 = types.KeyboardButton('Два')
        btn3 = types.KeyboardButton('Три')
        btn4 = types.KeyboardButton('Четыре')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Сколько раз в сутки подзаводят куранты Спасской башни Кремля?\nA: Один\nB: Два\nC: Три\nD: Четыре"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que3':
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("A", callback_data='false'),
                   types.InlineKeyboardButton("B", callback_data='false'),
                   types.InlineKeyboardButton("C", callback_data='true'),
                   types.InlineKeyboardButton("D", callback_data='false'))
        message_text = "Кто 1-м получил Нобелевскую премию по литературе?\nA: Романист\nB: Драматург\nC: Поэт\nD: Эссеист"
        msg = bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que4':
        markup = types.InlineKeyboardMarkup(row_width=2)
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

@bot.message_handler(commands=['start'])
def start(message):
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn0 = types.KeyboardButton('Начать игру')
    btn1 = types.KeyboardButton('Заглянуть в кошелёк')
    markup0.add(btn1, btn0)
    message_text = 'Добро пожаловать в игру "Кто хочет стать миллионером", вы можете начать игру'
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
        message_text = 'вы не можете использовать эту функцию'
        bot.send_message(message.chat.id, message_text)

@bot.message_handler(commands=['show'])
def show(message):
    message_text = 'количество правильных ответов: ' + str(len(QUE)) + '\nколичество оставшихся вопросов: ' + str(15-len(QUE))
    bot.send_message(message.chat.id, message_text)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()
    if get_message_bot == 'Начать игру':
        while True:
            temp = random.randint(1, 15)
            if temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        btn = 'que' + str(temp)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("дальше", callback_data=btn))
        bot.send_message(message.chat.id, "Нажмите 'дальше' для того чтобы перейти на 1 вопрос", reply_markup=markup)

    if get_message_bot == "Заглянуть в кошелёк":
        global wolit
        bot.send_message(message.chat.id, "Привет, твой счет " + str(wolit))

    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    if get_message_bot == 'Два':
        markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Заглянуть в кошелёк')
        markup0.add(btn1)
        message_text = "Правильный ответ\nВаш выигрыш: " + str(GIFT[len(QUE)]) + ' рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup0)
        while True:
            temp = random.randint(1, 15)
            if temp not in QUE:
                QUE.append(temp)
                print(QUE)
                break
        btn = 'que' + str(temp)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Дальше", callback_data=btn),
                   types.InlineKeyboardButton("Забрать выигрыш", callback_data='wolit'))
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Один':
        QUE.clear()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Начать заного", callback_data='start_btn'))
        message_text = 'Вы проиграли:(\nВаш выигрыш: ' + str(GIFT[len(QUE)]) + ' рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Четыре':
        QUE.clear()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Начать заного", callback_data='start_btn'))
        message_text = 'Вы проиграли:(\nВаш выигрыш: ' + str(GIFT[len(QUE)]) + ' рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)

    if get_message_bot == 'Три':
        QUE.clear()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Начать заного", callback_data='start_btn'))
        message_text = 'Вы проиграли:(\nВаш выигрыш: ' + str(GIFT[len(QUE)]) + ' рублей'
        bot.send_message(message.chat.id, message_text, reply_markup=markup)
    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.polling(none_stop=True)
