import telebot
from telebot import types
from telebot import callback_data
import sqlite3
import csv
import emoji
from time import sleep

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯
bot = telebot.TeleBot('5441155715:AAECB2FwzKK1LhRYLYPsrjrjXHKAErC3gwE')
# real 5640042697:AAE5kvgBf31LJJgiTrhIZB0hqOA1_tPA738
# test 5441155715:AAECB2FwzKK1LhRYLYPsrjrjXHKAErC3gwE

''' #приватные команды
/statistics - выводит статистику и файлы db напрямую в боте
/voice - способ отправить сообщение всем пользователям 
/voicehard - способ отправить сложное сообщение всем пользователям используя ссылки, картинки и тд
'''

'''# публичные команды
/help - справка по всем командам боте
/start - перезапуск бота, на стартовую позицию
/myprojects - расслыка по всем моим проектам
'''

# VOICEHARD
@bot.message_handler(commands=['voicehard'])
def voicehard(message):

    if message.chat.id == 438879394 or message.chat.id == 1891281816:
        bot.send_message(message.chat.id, "Введите сообщение, которое бот отправит всем пользователям. \n\n(Напоминаю, что ссылку надо добавить в коде программы)\n")


        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text

            sql = sqlite3.connect('analytics.db')
            cursor = sql.cursor()

            sqlite_select_query = """SELECT id from active"""
            cursor.execute(sqlite_select_query)
            users_id = cursor.fetchall()

            for i in range(0, len(users_id)):
                markup = types.InlineKeyboardMarkup(row_width=1)
                # Тут добавляем ссылку которую будем отправлять
                markup.add(types.InlineKeyboardButton("Ссылка", url="https://inf-ege.sdamgia.ru/test?id=11274364&nt=True&pub=False"))
                bot.send_message(users_id[i][0], text_message, reply_markup=markup)

        bot.register_next_step_handler(message, message_input)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)


    # Репетитор -----------------------------------------------------------------------
    if call.data == 'price':
        pic_2 = open("photo/price.PNG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_2)

        send_message2 = f"*Первое занятие БЕСПЛАТНО*,\nна нем я определю уровень знаний, и мы вместе подбираем оптимальный абонемент.\n\n_Работаю официально по чекам через НПД (Самозанятый)._\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))
        msg = bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "iam":
        send_message1 = f"*О себе:*\n" \
                        f"Выпускник *СибГУТИ* факультета _«Информатики и Вычислительной техники»_.\n\n" \
                        f"По основной специальности *developer Telegram ботов* и других чат ботов, но нашел свое призвание в репетиторской деятельности." \
                        f"\n\nНа данный момент прохожу обучение в *НГПУ*, по направлению: _«Педагогическое образование для специалистов с высшим непедагогическим образованием»_." \
                        f" \n\n🎯 Цель открыть свою школу программирования для детей и подростков!\n\n" \
                        f"Общий стаж репетиторской деятельности больше 3 лет, в моем профиле можно ознакомиться с [отзывами](https://www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing) довольных учеников и родителей."
        msg = bot.send_message(call.message.chat.id, send_message1, parse_mode="Markdown", disable_web_page_preview=True)

        pic_3 = open("photo/otzivy.PNG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_3)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        send_message2 = f"Преподаю программирование на *Python* в частных школах и группах. "
        msg = bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown")

        pic_4 = open("photo/kids2.JPG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_4)

        pic_5 = open("photo/kids1.JPG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_5,  reply_markup=markup2)


    elif call.data == "download":
        send_message = f"*Перечень необходимых программ:*\n\n" \
                       f"1. Python [скачать](www.python.org/downloads/)\n\n" \
                       f"2. Pycharm [скачать](www.jetbrains.com/ru-ru/pycharm/download/#section=mac)\n\n" \
                       f"3. Discord [скачать](discord.com/download)\n\n" \
                       f"4. Telegram Desktop [скачать](telegram.org/)"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        msg = bot.send_message(call.message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)

    elif call.data == "wallet":

        send_message = f"Перевод по номеру телефона: \n+7 (913) 468-35-34\nСБЕР или Тинькофф, есть СБП.\n\n" \
                       f"Или по номеру карты\nТинькоф: 5536 9140 2240 5801\nСБЕР: 5469 4400 2244 1977\nТинькоф МИР: 2200 7004 1864 5957\nПолучатель: _Андрианов Илья Алексеевич_\n\n" \
                       f"После оплаты скидываю вам чек, работаю официально через НПД (Самозанятый).\n\n" \
                       f"[Оставить чаевые](https://www.tinkoff.ru/cf/9f3vcMecD9w)"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"))

        msg = bot.send_message(call.message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)
    # Репетитор -----------------------------------------------------------------------



# START
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Контакты')
    btn2 = types.KeyboardButton('Репетитор')
    btn3 = types.KeyboardButton('Мои проекты')
    btn4 = types.KeyboardButton('Записаться на урок')
    btn5 = types.KeyboardButton('Получить файл с урока')
    markup.add(btn1, btn2, btn3, btn4, btn5)
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
@bot.message_handler(commands=['myprojects'])
def myprojects(message):
    send_message = "Просто перечисляю, чем я занимаюсь сегодня!\n\n" \
                   "*1. Канал* [itpy | ИнформатикаЕГЭ](t.me/pro100_easy_ege)\n✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                   "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе!\n\n" \
                   "*2. Чат бот* 🤖[MotherBot](t.me/JustDoItMotherBot)  \nЭто Telegram бот, который помогает начинающим программистам разобраться в библиотеке [PyTelegramBotAPI](https://habr.com/ru/post/580408/), предназначенной " \
                   "для работы с API Telegram – создания чат ботов в меcсенджере.\n\n" \
                   "*3. Курс подготовки к ЕГЭ на* [Stepik](https://stepik.org/course/122969/syllabus?auth=login)\n" \
                   "На сегодняшний день курс еще находится в разработке, но уже можно понять, что он из себя будет представлять по [описанию проекта](https://stepik.org/lesson/770711/step/1) и черновому [примеру урока](https://stepik.org/lesson/770602/step/1).\n\n" \
                   "*4.Открыть свой компьютерный класс*\nСейчас я прохожу дополнительное обучение, чтобы получить разрешение на групповую работу с детьми. \n\nИдея заключается в том, чтобы купить 6-8 компьютеров, сделать хорошее помещение и установить классный проектор. " \
                   "Утром я бы хотел заниматься с детьми 5–8 классы, а вечером проводить групповые занятия по подготовке к ЕГЭ!\nКак вам идея!? "

    bot.send_message(message.chat.id, send_message, parse_mode="Markdown", disable_web_page_preview=True)

# Getting STATISTICS
def analytics(func: callable):
    total_users = 0
    users = [['total_users', 'user_id', 'username', 'contact', 'tutor', 'myproject', 'clandly', 'getfile']]
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
                                Calendly BOOLEAN,
                                Getfile BOOLEAN
                            )""")
        sql.commit()

        people_id = message.chat.id
        cursor.execute(f"SELECT id FROM active WHERE id = {people_id}")
        data = cursor.fetchone()

        if data is None:
            user_id = message.chat.id
            total_users += 1
            username = message.from_user.username

            cursor.execute(f"INSERT INTO active VALUES(?, ?, ?, ?, ?, ?, ?, ?);", (total_users, user_id, username, False, False, False, False, False))
            sql.commit()
        else:
            cursor.execute(f"DELETE FROM active WHERE id = {people_id}")
            user_id = message.chat.id
            username = message.from_user.username
            users.append([total_users, user_id, username, False, False, False, False, False])

            if message.text == "Контакты":
                users[total_users][3] = True
            if message.text == "Репетитор":
                users[total_users][4] = True
            if message.text == "Мои проекты":
                users[total_users][5] = True
            if message.text == "Записаться на урок":
                users[total_users][6] = True
            if message.text == "Получить файл с урока":
                users[total_users][7] = True



            cursor.execute(f"INSERT INTO active VALUES(?, ?, ?, ?, ?, ?, ?, ?);", (total_users, user_id, username, users[total_users][3], users[total_users][4], users[total_users][5], users[total_users][6], users[total_users][7]))
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
        count3 = count4 = count5 = count6 = count7 = 0
        for row in records:
            if row[3] == True:
                count3 += 1
            if row[4] == True:
                count4 += 1
            if row[5] == True:
                count5 += 1
            if row[6] == True:
                count6 += 1
            if row[7] == True:
                count7 += 1

        statistics_message = 'Нажатий на клавиши: \n1. Контакты:  *{}*\n2. Репетитор:  *{}*\n' \
                             '3. Мои проекты:  *{}*\n4. Записаться на урок:  *{}*\n5. Получить файл с урока: *{}*'.format(count3, count4, count5, count6, count7)
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

        send_message1 = f"👨🏼‍💻 Работаю дистанционно, есть все необходимое для проведения занятий. " \
                        f"В работе использую такие сервисы (программы) как: PyCharm, Python, Notability, Discord, Google диск и другие. " \
                        f"Гарантирую связь со мной (WhatsApp, Telegram ☎️) каждый день и ответы на все ваши вопросы."


        bot.send_message(message.chat.id, send_message1, parse_mode="Markdown")
        sleep(1)

        pic_3 = open("photo/face.jpeg", 'rb')
        bot.send_photo(message.chat.id, pic_3)

        send_message3 = f"Берусь только за ЕГЭ по Информатике, работаю со школьниками от 6 класса по программе обучения языку программирования Python.\n\n" \
                        f"Целенаправленно мы подготовимся к ЕГЭ по Информатике с учетом изменений в ФИПИ и КИМах. " \
                        f"Для достижения результатов от вас потребуется регулярное посещение занятий и выполнение домашних заданий"
        bot.send_message(message.chat.id, send_message3, parse_mode="Markdown")
        sleep(1)


        pic_4 = open("photo/paint.jpeg", 'rb')
        bot.send_photo(message.chat.id, pic_4)


        send_message4 = f"🙋‍♂️ Если ты целеустремлённый - тебе точно ко мне! " \
                        f"При подготовке от 6 месяцев и выполнении всех моих требований - результат в 80+ баллов гарантирован, " \
                        f"но оставляю за собой право отказать от подготовки на этапе пробного занятия. " \
                        f"Средний балл моих учеников 70-90 баллов в зависимости от отработки домашних заданий❗\n\n" \
                        f"Чему будем уделять большую часть внимания? Изучению и практике на Python 🐍\n\n" \
                        f"За последние 2 года ЕГЭ по Информатике сильно изменилось, были добавлены хорошие прикладные Задачи по программированию, поэтому, если есть цель набрать 80+ баллов, то без этого никуда! " \
                        f"Научу ПРОГРАММИРОВАТЬ на Python с нуля."
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="download"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        bot.send_message(message.chat.id, send_message4, parse_mode="Markdown", reply_markup=markup2)

    if get_message_bot == "Контакты":

        send_message1 = "*Мои контакты:*\n\n" \
                        "[Telegram](t.me/ilandroxy)\n\n[WhatsApp](wa.me/message/JSXJ2NLWTVNFC1)\n\n[Discord](https://discordapp.com/users/ilandroxxy#6249) ilandroxxy#6249\n\n" \
                        "[Профиль Авито](www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing)\n\n[YouTube](https://m.youtube.com/channel/UCcORhBL494aSLcyIODjOG0A)\n\n" \
                        "[GitHub](https://github.com/ilandroxxy)\n\nРабочий телефон: +7 (995) 437–52–59\n\nEmail: collegehacksbot@gmail.com\n\n" \
                        "Воспользуйтесь моим Telegram ботом, чтобы пройти курс по разработке чат ботов @JustDoItMotherBot🤖"

        bot.send_message(message.chat.id, send_message1, parse_mode='Markdown', disable_web_page_preview=True)

    if get_message_bot == "Мои проекты":
        send_message = "Просто перечисляю, чем я занимаюсь сегодня!\n\n" \
                       "*1. Канал* [itpy | ИнформатикаЕГЭ](t.me/pro100_easy_ege)\n✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                       "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе!\n\n" \
                       "*2. Чат бот* 🤖[MotherBot](t.me/JustDoItMotherBot)  \nЭто Telegram бот, который помогает начинающим программистам разобраться в библиотеке [PyTelegramBotAPI](https://habr.com/ru/post/580408/), предназначенной " \
                       "для работы с API Telegram – создания чат ботов в меcсенджере.\n\n" \
                       "*3. Курс подготовки к ЕГЭ на* [Stepik](https://stepik.org/course/122969/syllabus?auth=login)\n" \
                       "На сегодняшний день курс еще находится в разработке, но уже можно понять, что он из себя будет представлять по [описанию проекта](https://stepik.org/lesson/770711/step/1) и черновому [примеру урока](https://stepik.org/lesson/770602/step/1).\n\n" \
                       "*4.Открыть свой компьютерный класс*\nСейчас я прохожу дополнительное обучение, чтобы получить разрешение на групповую работу с детьми. \n\nИдея заключается в том, чтобы купить 6-8 компьютеров, сделать хорошее помещение и установить классный проектор. " \
                       "Утром я бы хотел заниматься с детьми 5–8 классы, а вечером проводить групповые занятия по подготовке к ЕГЭ!\nКак вам идея!? "

        bot.send_message(message.chat.id, send_message, parse_mode="Markdown", disable_web_page_preview=True)



    if get_message_bot == "Записаться на урок":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("calendly.com", url="calendly.com/ilandroxxy/tutor"))
        message_text = f"Воспользуйтесь удобным сервисом [Calendly](https://bizzapps.ru/p/calendly/) *для записи на пробник* или выбора графика занятий. \n\n" \
                       f"Просто выберете подходящее время и *напишите пару слов о себе*. \n\n" \
                       f"❗Ваша карточка отобразится в моем календаре, но чтобы было комфортнее держать связь - прошу написать еще и в [Telegram](t.me/ilandroxy). "
        bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)
        pic = open("photo/calendly.jpg", 'rb')
        bot.send_photo(message.chat.id, pic, reply_markup=markup)

    if get_message_bot == "Получить файл с урока":
        if message.chat.id == 438879394 or message.chat.id == 1891281816:  # Я
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("ilandroxy_bot", url="https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/__example__.py"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        elif message.chat.id == 683943897:  # Таня
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Tanya.py", url="https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/Tanya.py"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        elif message.chat.id == 1314375732:  # Василий
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Vasiliy.py", url="https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/Vasiliy.py"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        elif message.chat.id == 1537718492:  # Александр
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Aleksandr.py", url="https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/Aleksandr.py"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)
        elif message.chat.id == 871237277:  # Владек
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Vladek.py", url="https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/Vladek.py"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)
        elif message.chat.id == 826004697:  # Никита
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Nikita.py", url="https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/Nikita.py"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)
        elif message.chat.id == 1208542295:  # Саша Казакова
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Sasha.py", url="https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/Sasha.py"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        else:
            message_text = 'Извините, по-моему вас нет в системе! Ожидайте...'
            bot.send_message(message.chat.id, message_text)
            sti = open('photo/WaitSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)


bot.polling(none_stop=True)

