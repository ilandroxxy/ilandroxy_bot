import telebot
from telebot import types
from telebot import callback_data
import sqlite3
import csv
import emoji
from time import sleep

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯
bot = telebot.TeleBot('5640042697:AAE5kvgBf31LJJgiTrhIZB0hqOA1_tPA738')



@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)


    # Репетитор -----------------------------------------------------------------------
    if call.data == 'price':

        pic_2 = open("photo/price.PNG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_2)

        send_message2 = f"*ПЕРВОЕ пробное занятие БЕСПЛАТНО*, на нем я определю уровень знаний, и мы вместе подбираем оптимальный абонемент.\n\n_Работаю официально по чекам через НПД (Самозанятый)._\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))
        msg = bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "iam":
        send_message1 = f"*О себе:*\n" \
                        f"Выпускник _«Сибирского Государственного университета телекоммуникаций и информатики»_ факультета _«Информатики и Вычислительной техники»_.\n\n" \
                        f"По основной специальности *developer Telegram ботов* и других чат ботов, но нашел свое призвание в репетиторской деятельности. \n\n🎯 Цель открыть свою школу программирования для детей и подростков!\n\n" \
                        f"Общий стаж репетиторской деятельности больше 3 лет, в моем профиле можно ознакомиться с ОТЗЫВАМИ довольных учеников и родителей."
        msg = bot.send_message(call.message.chat.id, send_message1, parse_mode="Markdown")

        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton("Отзывы", url = 'https://www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing'))

        pic_3 = open("photo/otzivy.PNG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_3, reply_markup=markup1)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        send_message2 = f"Преподаю программирование на _Python_ в частных школах и группах. "
        msg = bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown")

        pic_4 = open("photo/kids2.JPG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_4)

        pic_5 = open("photo/kids1.JPG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_5)


        send_message3 = f"Люблю и умею учиться, развиваться. Прохожу курсы по повышению квалификации.\n\n" \
                        f'На данный момент обучаюсь по программе: _"Дополнительное педагогическое образование для специалистов с высшим (непедагогическим) образованием"_\nВ НГПУ - *Новосибирский Педагогический университет*.'
        msg = bot.send_message(call.message.chat.id, send_message3, parse_mode="Markdown", reply_markup=markup2)

    elif call.data == "download":
        send_message = f"*Ссылки для скачивания программ:*\n\n" \
                       f"Python www.python.org/downloads/\n\n" \
                       f"Pycharm www.jetbrains.com/ru-ru/pycharm/download/#section=mac\n\n" \
                       f"Discord discord.com/download\n\n" \
                       f"Telegram Desktop telegram.org/"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        msg = bot.send_message(call.message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "wallet":

        send_message = f"*Мои реквизиты*: :\n\n" \
                       f"По номеру телефона+79134683534 (это мой личный номер) СБЕР или Тинькофф, есть СБП.\n\n" \
                       f"По номеру карты\nТинькоф: 5536 9140 2240 5801\nСБЕР: 5469 4400 2244 1977\nТинькоф МИР: 2200 7001 6877 9568\nПолучатель: Андрианов Илья Алексеевич\n\n" \
                       f"_После оплаты скидываю вам чек, работаю официально через НПД (Самозанятый)._\n\n" \
                       f"Чаевые опционально: https://www.tinkoff.ru/cf/9f3vcMecD9w"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"))

        msg = bot.send_message(call.message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup)
    # Репетитор -----------------------------------------------------------------------



# START
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Контакты')
    btn2 = types.KeyboardButton('Репетитор')
    btn3 = types.KeyboardButton('Мои проекты')
    btn4 = types.KeyboardButton('Создать бота под заказ')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\n' \
                f'*Меня зовут Андрианов Илья*. \nЯ программист developer Telegram ботов.\n' \
                f'А также репетитор Программирования на языке Python 🐍 и подготовке к ЕГЭ по Информатике 👨‍🏫\n\n' \
                f'*Рад Вас приветствовать* у себя на _"страничке"_, здесь я постараюсь коротко ' \
                f'рассказать о себе и, надеюсь, нам удастся найти общий язык 🙏 \n\n' \
                f'Используйте команду 👉 /help , чтобы подробнее узнать о всех доступных командах или вызовите *Меню команд* - большая синяя кнопка на семь часов.'


    pic_1 = open("photo/hello.jpeg", 'rb')
    bot.send_photo(message.chat.id, pic_1)
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)

# HELP
@bot.message_handler(commands=['help'])
def help(message):
    send_message = "I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual.\n\n" \
                   "You can control me by sending these commands:\n\n*Commands*\n/help - навигация по командам\n/start - перезапустить бота\n" \
                   '/myproject - список моих актуальных проектов'
    bot.send_message(message.chat.id, send_message, parse_mode="Markdown")

# MYPROJECT
@bot.message_handler(commands=['myproject'])
def myproject(message):
    send_message = "Не стану перечислять провальные проекты, просто перечислю, чем я занимаюсь сегодня!\n\n" \
                   "*1. itpy | ИнформатикаЕГЭ*\n✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                   "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе. \nА это для будущих программистов - куда важнее экзаменов.\n\n" \
                   "*2. @MotherBot*\n🤖 Это Telegram бот, который помогает начинающим программистам разобраться в библиотеке PyTelegramBotAPI, предназначенной " \
                   "для работы с API Telegram - создания Ботов в меcсенджере. \nКурс рассчитан на поверхностные знания языка Python, без возрастных ограничений.\n"

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("Канал подготовки к ЕГЭ по Информатике", url="t.me/pro100_easy_ege"),
               types.InlineKeyboardButton("@MotherBot курс по разработке ботов", url="t.me/JustDoItMotherBot"))

    bot.send_message(message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup)

# Getting STATISTICS
def analytics(func: callable):
    total_users = 0
    users = [['total_users', 'user_id', 'username', 'contact', 'tutor', 'myproject', 'botorder']]
    username = ""


    def anlytics_wrapper(message):
        nonlocal users, total_users, username

        # Считаем кол-во нажатий на клавишу-----------------------------------
        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS active(
                                total_users INTEGER,
                                id INTEGER,
                                UserName TEXT,
                                Contact BOOLEAN,
                                Tutor BOOLEAN,
                                Myproject BOOLEAN,
                                Botorder BOOLEAN
                            )""")
        sql.commit()

        people_id = message.chat.id
        cursor.execute(f"SELECT id FROM active WHERE id = {people_id}")
        data = cursor.fetchone()

        if data is None:
            user_id = message.chat.id
            total_users += 1
            username = message.from_user.username

            cursor.execute(f"INSERT INTO active VALUES(?, ?, ?, ?, ?, ?, ?);", (total_users, user_id, username, False, False, False, False))
            sql.commit()
        else:
            cursor.execute(f"DELETE FROM active WHERE id = {people_id}")
            user_id = message.chat.id
            username = message.from_user.username
            users.append([total_users, user_id, username, False, False, False, False])

            if message.text == "Контакты":
                users[total_users][3] = True
            if message.text == "Репетитор":
                users[total_users][4] = True
            if message.text == "Мои проекты":
                users[total_users][5] = True
            if message.text == "Создать бота под заказ":
                users[total_users][6] = True



            cursor.execute(f"INSERT INTO active VALUES(?, ?, ?, ?, ?, ?, ?);", (total_users, user_id, username, users[total_users][3], users[total_users][4], users[total_users][5], users[total_users][5]))
            sql.commit()

            cursor.close()
        # Считаем кол-во нажатий на клавишу-----------------------------------


        return func(message)
    return anlytics_wrapper

# STATISTICS Private send STATISTICS
@bot.message_handler(commands=['statistics'])
def statistics(message):

    if message.chat.id == 438879394 or message.chat.id == 1891281816:
        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        sqlite_select_query = """SELECT * from active"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        bot.send_message(message.chat.id, "Всего пользователей:  " + str(len(records)) + "\nВывод статистики по кнопкам:")
        count3 = count4 = count5 = count6 = 0
        for row in records:
            if row[3] == True:
                count3 += 1
            if row[4] == True:
                count4 += 1
            if row[5] == True:
                count5 += 1
            if row[6] == True:
                count6 += 1

        statistics_message = 'Нажатий на клавиши: \n1. Контакты:  *{}*\n2. Репетитор:  *{}*\n' \
                             '3. Мои проекты:  *{}*\n4. Создать бота под заказ:  *{}*'.format(count3, count4, count5,
                                                                                              count6)
        bot.send_message(message.chat.id, statistics_message, parse_mode="Markdown")

        db = open("analytics.db", 'rb')
        bot.send_document(message.chat.id, db)


        with open("ForExcel.csv", 'w+', encoding='cp1251', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=";")

            for row in records:
                writer.writerow(row)
            csvfile.close()

        CSV = open("ForExcel.csv", 'rb')
        bot.send_document(message.chat.id, CSV)


        cursor.close()
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")



# VOICE
@bot.message_handler(commands=['voice'])
def voice(message):

    if message.chat.id == 438879394 or message.chat.id == 1891281816:
        bot.send_message(message.chat.id, "Введите сообщение, которое бот отправит всем пользователям: \n\n")


        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text

            sql = sqlite3.connect('analytics.db')
            cursor = sql.cursor()

            sqlite_select_query = """SELECT id from active"""
            cursor.execute(sqlite_select_query)
            users_id = cursor.fetchall()

            for i in range(0, len(users_id)):
                bot.send_message(users_id[i][0], text_message)

        bot.register_next_step_handler(message, message_input)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")




@bot.message_handler(content_types=['text'])
@analytics
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Репетитор":
        markup0 = types.InlineKeyboardMarkup(row_width=1)
        markup0.add(types.InlineKeyboardButton("Канал: itpy | ИнформатикаЕГЭ", url='t.me/pro100_easy_ege'))

        send_message1 = f"Я работаю дистанционно, есть все необходимое для проведения занятий. \n" \
                        f"В работе использую такие сервисы (программы) как: _PyCharm, Python, Notability, Discord, Google диск_ и другие. \n\n" \
                        f"Веду полезный _Telegram канал_ и сервер в _Discord_ с материалами для подготовки к экзамену."


        bot.send_message(message.chat.id, send_message1, parse_mode="Markdown", reply_markup=markup0)
        sleep(1)

        pic_3 = open("photo/face.jpeg", 'rb')
        bot.send_photo(message.chat.id, pic_3)

        send_message2 = f"Гарантирую связь со мной (_WhatsApp, Telegram_ ☎️) каждый день и ответы на все ваши вопросы. С отзывами на мою работу вы можете ознакомиться в Профиле."
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton("Авито профиль", url='www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing'))
        bot.send_message(message.chat.id, send_message2, parse_mode="Markdown", reply_markup=markup1)

        send_message3 = f"Берусь только за ЕГЭ по Информатике и школьников от 5 класса в обучении Python.\n\n" \
                        f"Целенаправленная подготовка к ЕГЭ по Информатике с учетом изменений в ФИПИ и КИМах однако для достижения результатов от вас потребуется регулярное посещение занятий " \
                        f"и выполнение домашних заданий."
        bot.send_message(message.chat.id, send_message3, parse_mode="Markdown")
        sleep(1)


        pic_4 = open("photo/paint.jpeg", 'rb')
        bot.send_photo(message.chat.id, pic_4)


        send_message4 = f"🙋‍♂️Если ты целеустремлённый тебе точно ко мне! При подготовке от 6+ месяцев гарантирую результат в 75+, от 10+ месяцев - результат в 90+ баллов\n\nНо оставляю за собой право отказаться от учеников, если не увижу самоотдачи. Я замотивирован в самых лучших результатах.\n\n" \
                        f"Средний балл моих учеников 70-90 баллов в зависимости от отработки домашних заданий. Сейчас активно веду набор на летние занятия для 10-классников! \n\n❗ *Выходные дни*: *Среда и Воскресенье*, во все остальные дни провожу занятия в период *с 14:00 до 23:00 по Новосибирскому времени* (ориентированно на Европейскую часть России).\n\n" \
                        f"Чему будем уделять большую часть внимания при подготовке?\nИзучению и практике на Python 🐍\n\nЗа последние 2 года ЕГЭ по Информатике сильно изменилось, были добавлены хорошие прикладные Задачи по программированию, поэтому, если есть цель набрать 80+ баллов, то без этого никуда! Научу 💻ПРОГРАММИРОВАТЬ на Python с нуля."

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        bot.send_message(message.chat.id, send_message4, parse_mode="Markdown", reply_markup=markup2)

    if get_message_bot == "Контакты":

        send_message1 = "*Мои контакты:*\nРабочий телефон: +7 (995) 437-52-59\n\n" \
                        "WhatsApp: wa.me/message/JSXJ2NLWTVNFC1\n\nTelegram: t.me/ilandroxy\n\nEmail: collegehacksbot@gmail.com\n\n" \
                        "YouTube: clck.ru/rbQhY\n\n" \
                        "Воспользуйтесь моим Telegram ботом, чтобы пройти курс по разработке таких ботов 🤖 t.me/@JustDoItMotherBot"

        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton("Профиль Авито", url='www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing'))
        bot.send_message(message.chat.id, send_message1, parse_mode='Markdown', reply_markup=markup1)

    if get_message_bot == "Мои проекты":
        send_message = "Не стану перечислять провальные проекты, просто перечислю, чем я занимаюсь сегодня!\n\n" \
                       "*1. itpy | ИнформатикаЕГЭ*\n✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                       "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе. \nА это для будущих программистов - куда важнее экзаменов.\n\n" \
                       "*2. @MotherBot*\n🤖 Это Telegram бот, который помогает начинающим программистам разобраться в библиотеке PyTelegramBotAPI, предназначенной " \
                       "для работы с API Telegram - создания Ботов в меcсенджере. \nКурс рассчитан на поверхностные знания языка Python, без возрастных ограничений.\n"


        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Канал подготовки к ЕГЭ по Информатике", url="t.me/pro100_easy_ege"),
                   types.InlineKeyboardButton("@MotherBot курс по разработке ботов", url="t.me/JustDoItMotherBot"))

        bot.send_message(message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup)



    if get_message_bot == "Создать бота под заказ":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔮 Хочу вернуться назад')
        markup.add(btn1)

        send_message0 = "Здесь я собираю заявки на создание ботов под заказ. Все, что мне нужно - это описание Вашей идеи и немножечко времени, чтобы ее переварить 😅 \n\n" \
                        " ✍️ Просто опишите свою идею в одном сообщение (критично важно)."
        bot.send_message(message.chat.id, send_message0, parse_mode='Markdown', reply_markup=markup)


        @bot.message_handler(content_types=['text'])
        def message_input(message):
            user_id = message.chat.id
            user_name = message.from_user.username

            if message.text != "🔮 Хочу вернуться назад":
                text_message = "Пришла новая заявка на создание бота: \n*user:* @" + user_name + "\n\n_Письмо:_\n" + message.text
                bot.send_message(438879394, text_message, parse_mode='Markdown')

                bot.send_message(message.chat.id, "❗Заявка улетела ко мне (@ilandroxxy), постараюсь связаться с Вами в ближайшее время 🙏")
            if message.text == "🔮 Хочу вернуться назад":
                bot.send_message(message.chat.id, "Поздравляю, вы нашли уязвимость, просто тапните по клавише второй раз ✊", parse_mode='Markdown')

        bot.register_next_step_handler(message, message_input)

    if get_message_bot == "🔮 Хочу вернуться назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Создать бота под заказ')
        markup.add(btn1, btn2, btn3, btn4)
        send_mess = '👇 Вернул в начало, не благодарите'

        bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup)

bot.polling(none_stop=True)

