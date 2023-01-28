# region import и API key
import random
import telebot
from telebot import types
import sqlite3
import csv
import time
import datetime as dt

with open("token.txt") as f:
    TOKEN = f.read().strip()

# bot = telebot.TeleBot(f'{TOKEN}')
bot = telebot.TeleBot("5734914555:AAHshNFPEP2SszdrAKbfm_6uKZI4waH1Nbs")
# endregion import и API key

# region Словарь с данными студентов
MondayStudents = {
    1477701439: ["Valeria.py", '15:00-16:30', 4000//4, "Валерия", 4],
    768734764: ["Bogdan.py", '16:30-17:30', 4000//4, "Богдан", 4],
    1454117859: ['Diana', "20:00-21:00", 4800//8, "Диана", 8],
    659796558: ['Ivan.py', '21:00-22:00', 1000, "Иван", 1000],
    826004697: ['Nikita.py', '22:00-23:00', 4000//4, "Никита", 4]}
TuesdayStudents = {
    1949653479: ['Yanina.py', '11:00-12:00', 4800//8, "Янина", 8],
    1649389148: ['Slava.py', "15:00-16:00", 8000//8, "Слава", 8],
    789322200: ['Katya.py', "16:00-17:00", 4000//4, "Екатерина", 4],
    1208542295: ['Sasha.py', '19:00-20:00', 4800//8, "Александра", 8],
    804184353: ['Islam.py', '21:00-22:00', 5400//4, "Ислам", 4],
    923349631: ['Olesya.py', '22:00-23:00', 9600//8, 'Олеся', 8]}
ThursdayStudents = {
    1949653479: ['Yanina.py', '11:00-12:00', 4800//8, "Янина", 8],
    431685002: ['Vsevolod.py', '15:00-16:00', 5400//4, "Всеволод", 4],
    5242003138: ['Dima.py', '16:00-17:00', 4000//4, "Дмитрий", 4],
    1187852992: ['Aleksandr_2.py', "17:00-18:00", 6800//8, "Александр2", 8],
    816859380: ['Sergey.py', '18:00-19:00', 9600//8, 'Сергей', 8],
    811476623:  ["Georgie.py", "20:00-21:00", 4800//4, "Георгий", 4],
    799740089: ["Bulat.py", "21:00", 4000//4, "Булат", 4],
    1537718492: ["Aleksandr.py", "22:00-23:00", 8000//8, "Александр", 8]}
FridayStudents = {
    575882793: ['Artem.py', '15:00-16:00', 9600//8, 'Артем', 8],
    719571990: ['Stepan.py', "16:00-17:00", 6800//8, "Степан", 8],
    644645774: ['Stasya.py', "17:00-18:30", 10200//8, "Стася", 8],
    986539147: ['Danil.py', '19:00-20:00', 8000 // 8, "Данил", 8],
    659796558: ['Ivan.py', '20:00-21:00', 1000, "Иван", 1000],
    1029532016: ['Maria.py', "21:00-22:00", 8000//8, "Мария", 8],
    1649389148: ['Slava.py', "22:00-23:00", 8000//8,  "Слава", 8]}
SaturdayStudents = {
    1347259493: ['Andrey.py', '15:45-17:15', 1500, 'Андрей', 1000],
    1763801774: ['Kirill.py', "17:30-18:30", 4000//4, "Кирилл", 4],
    5148819382: ['Tatyana.py', "18:30-20:00", 10200//8, "Татьяна", 8],
    1314375732: ['Vasiliy.py', "21:00-22:00", 6800//8, "Василий", 8],
    871237277: ['Vladek.py', "22:00-23:00", 8000//8, "Владек", 8],
    438879394: ['Ilya.py', '14:00', 0, "Илья", 1]}

Me = {1891281816: ['', '00:00', 0, "iРепетитор", 5],
      438879394: ['Ilya.py', '14:00', 0, "Илья", 1]}

PrivateMe = {1891281816: "Рабочий аккаунт",
             438879394: 'Илья',
             -1001822573914: "Homework",
             -1001819293687: "Lessons"}

Students = MondayStudents | TuesdayStudents | ThursdayStudents | FridayStudents | SaturdayStudents

S = []
for k, v in sorted(Students.items()):
    S.append((v, k))
# endregion Словарь с данными студентов

# region Функция для корректного отображения даты
def my_time(timer: str) -> str:
    '''
:param timer: nsk_now.strftime('%A %d %B %Y')
:return: пример #Среда #25.Января.2023
    '''
    month_dict = {'January': 'Января',
                  'February': 'Февраля',
                  'March': 'Марта',
                  'April': 'Апрель',
                  'May': 'Май',
                  'June': 'Июнь',
                  'July': 'Июль',
                  'August': 'Август',
                  'September': 'Сентябрь',
                  'October': 'Октябрь',
                  'November': 'Ноябрь',
                  'December': 'Декабрь'
                  }

    day_dict = {'Monday': 'Понедельник',
                'Tuesday': 'Вторник',
                'Wednesday': 'Среда',
                'Thursday': 'Четверг',
                'Friday': 'Пятница',
                'Saturday': 'Суббота',
                'Sunday': 'Воскресенье'
                }

    datetime_date = timer.split()
    my_date = f'#{day_dict[datetime_date[0]]} #{datetime_date[1]}{month_dict[datetime_date[2]]}{datetime_date[3]}'
    return my_date
# endregion функция для корректного отображения даты

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉
# ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️ 0️⃣  1️⃣  2️⃣
# 3️⃣  4️⃣  5️⃣  6️⃣  7️⃣  8️⃣  9️⃣  🔟    🐍 ☎️ 📞 👾


@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    # region call.data для Репетитор
    if call.data == 'price':
        pic_2 = open("photo/price.PNG", "rb")
        bot.send_photo(call.message.chat.id, pic_2)

        send_message2 = f"*Первое занятие БЕСПЛАТНО*,\nна нем я определю уровень " \
                        f"знаний, и мы вместе подбираем оптимальный абонемент!\n\n" \
                        f"Работаю официально по чекам через НПД (`Самозанятый`).\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))
        bot.send_message(call.message.chat.id, send_message2,
                         parse_mode="Markdown", reply_markup=markup)

    elif call.data == "iam":
        send_message1 = f"*О себе:*\n" \
                        f"Выпускник *СибГУТИ* факультета _«Информатики и " \
                        f"Вычислительной техники»_.\n\n" \
                        f"По основной специальности *developer Telegram ботов* " \
                        f"и других чат ботов, но нашел свое призвание в " \
                        f"репетиторской деятельности." \
                        f"\n\nНа данный момент прохожу обучение в *НГПУ*," \
                        f" по направлению: `«Педагогическое образование " \
                        f"для специалистов с высшим непедагогическим образованием»`."
        bot.send_message(call.message.chat.id, send_message1,
                         parse_mode="Markdown", disable_web_page_preview=True)

        pic = open("photo/diploma.png", "rb")
        bot.send_photo(call.message.chat.id, pic)

        send_message2 = f" \n\n🎯 Цель открыть свою школу программирования " \
                        f"для детей и подростков!\n\n" \
                        f"Общий стаж репетиторской деятельности больше 3 лет, " \
                        f"в моем профиле можно ознакомиться с " \
                        f"[отзывами](https://www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing) " \
                        f"довольных учеников и родителей."
        bot.send_message(call.message.chat.id, send_message2,
                         parse_mode="Markdown", disable_web_page_preview=True)

        pic_3 = open("photo/otzivy.PNG", "rb")
        bot.send_photo(call.message.chat.id, pic_3)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        send_message2 = f"Преподаю программирование на " \
                        f"*Python* в частных школах и группах. "
        msg = bot.send_message(call.message.chat.id, send_message2,
                               parse_mode="Markdown")

        pic_4 = open("photo/kids2.JPG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_4)

        pic_5 = open("photo/kids1.JPG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_5,  reply_markup=markup2)

    elif call.data == "downloads":
        message_text = f"*Перечень необходимых программ:*\n\n" \
                       f"1. Python [скачать](www.python.org/downloads/)\n\n" \
                       f"2. Telegram Desktop [скачать](telegram.org/)\n\n" \
                       f"3. Discord [скачать](discord.com/download)\n\n" \
                       f"4. Pycharm [скачать](www.jetbrains.com/ru-ru/pycharm/download/)\n\n" \
                       f"В случае необходимости, воспользуйтесь " \
                       f"[видео инструкцией](https://www.youtube.com/watch?v=wquEFeQAjPQ&t=303s) " \
                       f"по установке PyCharm" \

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        msg = bot.send_message(call.message.chat.id, message_text,
                               parse_mode="Markdown", reply_markup=markup,
                               disable_web_page_preview=True)

    elif call.data == "wallet":

        send_message = f"*Мои реквизиты для перевода*\n\n" \
                       f"*Перевод по номеру телефона:* \n`+7 (913) 468-35-34`" \
                       f"\nСБЕР или Тинькофф, *есть СБП*.\n\n" \
                       f"*Или по номеру карты:*\nТинькоф: `5536 9140 2240 5801`" \
                       f"\nСБЕР: `5469 4400 2244 1977`\n" \
                       f"Тинькоф МИР: `2200 7004 1864 5957`\n" \
                       f"Получатель: `Андрианов Илья Алексеевич`\n\n" \
                       f"После оплаты скидываю вам чек, работаю " \
                       f"официально через НПД (`Самозанятый`).\n\n" \
                       f"[Оставить чаевые](https://www.tinkoff.ru/cf/9f3vcMecD9w)"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"))

        bot.send_message(call.message.chat.id,
                         send_message,
                         parse_mode="Markdown",
                         reply_markup=markup,
                         disable_web_page_preview=True)
    # endregion call.data для Репетитор

    # region call.data для Теоретической домашки
    elif call.data == 'firstclass':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        bot.send_message(call.message.chat.id, "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться!",
                         parse_mode='Markdown', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-1001822573914,
                                     f'#{Students[call.message.chat.id][3]} получил домашку:',
                                     parse_mode='Markdown')
                n = int(message.text)
                M = []
                for i in range(n):
                    x = random.randint(1, 25)
                    while x in M:
                        x = random.randint(1, 25)
                    M.append(x)
                    photo = open(f'theoryHW/firstclass/{x}.png', 'rb')
                    bot.send_photo(call.message.chat.id, photo)
                    if call.message.chat.id != 1891281816:
                        photo = open(f'theoryHW/firstclass/{x}.png', 'rb')
                        bot.send_photo(-1001822573914, photo)
                M.clear()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy',
                                 parse_mode='Markdown', reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'ifelifelse':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\n"
                         "P.s. задачи могут повторяться!",
                         parse_mode='Markdown',
                         reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-1001822573914, f'#{Students[call.message.chat.id][3]} получил домашку:',
                                 parse_mode='Markdown')
                n = int(message.text)
                M = []
                for i in range(n):
                    x = random.randint(1, 21)
                    while x in M:
                        x = random.randint(1, 21)
                    M.append(x)
                    photo = open(f'theoryHW/ifelifelse/{x}.png', 'rb')
                    bot.send_photo(call.message.chat.id, photo)
                    if call.message.chat.id != 1891281816:
                        photo = open(f'theoryHW/ifelifelse/{x}.png', 'rb')
                        bot.send_photo(-1001822573914, photo)
                M.clear()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy',
                                 parse_mode='Markdown', reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'whilefor':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\n"
                         "P.s. задачи могут повторяться!",
                         parse_mode='Markdown',
                         reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-1001822573914,
                                     f'#{Students[call.message.chat.id][3]} получил домашку:',
                                     parse_mode='Markdown')
                n = int(message.text)
                M = []
                for i in range(n):
                    x = random.randint(1, 20)
                    while x in M:
                        x = random.randint(1, 20)
                    M.append(x)
                    photo = open(f'theoryHW/whilefor/{x}.png', 'rb')
                    bot.send_photo(call.message.chat.id, photo)
                    if call.message.chat.id != 1891281816:
                        photo = open(f'theoryHW/whilefor/{x}.png', 'rb')
                        bot.send_photo(-1001822573914, photo)
                M.clear()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy',
                                 parse_mode='Markdown', reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'list':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\n"
                         "P.s. задачи могут повторяться!",
                         parse_mode='Markdown', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-1001822573914, f'#{Students[call.message.chat.id][3]} получил домашку:',
                                 parse_mode='Markdown')
                n = int(message.text)
                M = []
                for i in range(n):
                    x = random.randint(1, 18)
                    while x in M:
                        x = random.randint(1, 18)
                    M.append(x)
                    photo = open(f'theoryHW/list/{x}.png', 'rb')
                    bot.send_photo(call.message.chat.id, photo)
                    if call.message.chat.id != 1891281816:
                        photo = open(f'theoryHW/list/{x}.png', 'rb')
                        bot.send_photo(-1001822573914, photo)
                M.clear()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy',
                                 parse_mode='Markdown', reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'string':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\n"
                         "P.s. задачи могут повторяться!",
                         parse_mode='Markdown', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-1001822573914,
                                     f'#{Students[call.message.chat.id][3]} получил домашку:',
                                     parse_mode='Markdown')
                n = int(message.text)
                M = []
                for i in range(n):
                    x = random.randint(1, 14)
                    while x in M:
                        x = random.randint(1, 14)
                    M.append(x)
                    photo = open(f'theoryHW/string/{x}.png', 'rb')
                    bot.send_photo(call.message.chat.id, photo)
                    if call.message.chat.id != 1891281816:
                        photo = open(f'theoryHW/string/{x}.png', 'rb')
                        bot.send_photo(-1001822573914, photo)
                M.clear()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id,
                                 f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy',
                                 parse_mode='Markdown',
                                 reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(call.message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'function':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        send_message = "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться!"
        bot.send_message(call.message.chat.id, send_message, parse_mode='Markdown', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                if call.message.chat.id != 1891281816:
                    send_message = f'#{Students[call.message.chat.id][3]} получил домашку:'
                    bot.send_message(-1001822573914, send_message, parse_mode='Markdown')
                n = int(message.text)
                M = []
                for i in range(n):
                    x = random.randint(1, 16)
                    while x in M:
                        x = random.randint(1, 16)
                    M.append(x)
                    photo = open(f'theoryHW/functions/{x}.png', 'rb')
                    bot.send_photo(call.message.chat.id, photo)
                    if call.message.chat.id != 1891281816:
                        photo = open(f'theoryHW/functions/{x}.png', 'rb')
                        bot.send_photo(-1001822573914, photo)
                M.clear()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                send_message = f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy'
                bot.send_message(call.message.chat.id, send_message,
                                 parse_mode='Markdown', reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                send_message = f"Команда успешно отменена ⛔"
                bot.send_message(call.message.chat.id, send_message,
                                 reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)
    # endregion call.data для теоретической домашки

    # region call.data для Useful
    elif call.data == 'py01':
        py01 = open('files/py01.pdf', 'rb')
        bot.send_document(call.message.chat.id, py01)

    elif call.data == 'py02':
        py02 = open('files/py02.pdf', 'rb')
        bot.send_document(call.message.chat.id, py02)

    elif call.data == 'py03':
        py03 = open('files/py03.pdf', 'rb')
        bot.send_document(call.message.chat.id, py03)

    elif call.data == 'py04':
        py04 = open('files/py04.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py04)

    elif call.data == 'py05':
        py05 = open('files/py05.pdf', 'rb')
        bot.send_document(call.message.chat.id, py05)

    elif call.data == 'py06':
        py06 = open('files/py06.pdf', 'rb')
        bot.send_document(call.message.chat.id, py06)

    elif call.data == 'py07':
        py07 = open('files/py07.pdf', 'rb')
        bot.send_document(call.message.chat.id, py07)
    # endregion call.data для Useful

    # region call.data для Что умеет этот бот
    elif call.data == 'next1':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('photo/hw_button_1.jpg', 'rb')),
                              types.InputMediaPhoto(open('photo/hw_button_2.jpg', 'rb')),
                              types.InputMediaPhoto(open('photo/hw_button_3.jpg', 'rb')),
                              types.InputMediaPhoto(open('photo/hw_button_4.jpg', 'rb'))])
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Далее", callback_data='next2'))

        bot.send_message(call.message.chat.id,
                         '👾 Бот выдает домашнюю работу,\n'
                         'а также помогает проверять ее!',
                         reply_markup=markup2)

    elif call.data == 'next2':
        send_pic = open("photo/contact.jpg", 'rb')
        bot.send_photo(call.message.chat.id, send_pic)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Далее", callback_data='next3'))

        send_message = '📞 Получите полный список моих\nконтактов, я всегда на связи ✌️'
        bot.send_message(call.message.chat.id, send_message, reply_markup=markup)

    elif call.data == 'next3':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('photo/abstract_1.jpg', 'rb')),
                              types.InputMediaPhoto(open('photo/abstract_2.jpg', 'rb')),
                              types.InputMediaPhoto(open('photo/abstract_3.jpg', 'rb'))])

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Далее", callback_data='next4'))

        bot.send_message(call.message.chat.id,
                         '*Бот поддерживает множество других функций 👇*\n\n'
                         '▫️Вы всегда найдете ссылку на Ваш конспект;\n'
                         '▫️Получайте актуальные новости от меня;\n'
                         '▫️Следите за расписанием своих уроков;\n'
                         '▫️Просматривайте кол-во занятий в абонементе;\n\n'
                         '🤖 И много другое в одном месте!',
                         parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'next4':
        bot.send_message(call.message.chat.id,
                         'Одна из очень крутых возможностей, закреп '
                         'inline кнопок - функция "Сдать домашку" '
                         'всегда под рукой 💪😅',
                         parse_mode='Markdown')

        send_mov = open('photo/send_hw.gif', 'rb')
        bot.send_video(call.message.chat.id, send_mov)
    # endregion call.data для Что умеет этот бот

    # region call.data для Открыть решебник
    elif call.data == 'reshebnik':
        if call.message.chat.id in Students:
            message_text = 'Наборы задачек на отработку теории Python 👇 😅'
            markup = types.InlineKeyboardMarkup(row_width=3)
            markup.add(types.InlineKeyboardButton("2", callback_data="gdz2"),
                        types.InlineKeyboardButton("5", callback_data="gdz5"),
                        types.InlineKeyboardButton("6", callback_data="gdz6"),
                        types.InlineKeyboardButton("8", callback_data="gdz8"),
                        types.InlineKeyboardButton("12", callback_data="gdz12"),
                        types.InlineKeyboardButton("14", callback_data="gdz14"),
                        types.InlineKeyboardButton("15", callback_data="gdz15"),
                        types.InlineKeyboardButton("16", callback_data="gdz16"),
                        types.InlineKeyboardButton("17", callback_data="gdz17"),
                        types.InlineKeyboardButton("22", callback_data="gdz22"),
                        types.InlineKeyboardButton("23", callback_data="gdz23"),
                        types.InlineKeyboardButton("24", callback_data="igdz24"),
                        types.InlineKeyboardButton("25", callback_data="gdz25"),
                        types.InlineKeyboardButton("26", callback_data="gdz26"),
                        types.InlineKeyboardButton("27", callback_data="gdz27"))
            bot.send_message(call.message.chat.id, message_text,
                             parse_mode="Markdown", reply_markup=markup)
    # endregion call.data для Открыть решебник

    # region call.data для Кнопок из Решебника
    elif call.data == 'gdz2':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/2/2.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/2/2.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6Ee) на полный набор задач 2️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz5':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/5/5.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/5/5.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/5/5.3.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/5/5.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6ET) на полный набор задач 5️⃣ типа🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz6':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/6/6.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/6/6.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/6/6.3.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6EK) на полный набор задач 6️⃣ типа🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz8':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/8/8.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/8/8.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/8/8.3.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/8/8.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6E6) на полный набор задач 8️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz12':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/12/12.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/12/12.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6Dq) на полный набор задач 1️⃣2️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz14':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/14/14.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/14/14.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/14/14.3.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6Dd) на полный набор задач 1️⃣4️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz15':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/15/15.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/15/15.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/15/15.3.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/15/15.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6DS) на полный набор задач 1️⃣5️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz16':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/16/16.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/16/16.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/16/16.3.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6Cc) на полный набор задач 1️⃣6️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz17':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/17/17.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/17/17.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6CW) на полный набор задач 1️⃣7️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz22':
        # bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/22/22.1.jpg', 'rb')),
        #                                             types.InputMediaPhoto(open('gdz/22/22.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6Bo) на полный набор задач 2️⃣2️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz23':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/23/23.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/23/23.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6BR) на полный набор задач 2️⃣3️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz24':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/24/24.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/24/24.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/24/24.3.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/24/24.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6BC) на полный набор задач 2️⃣4️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz25':
        bot.send_media_group(call.message.chat.id,
                             [types.InputMediaPhoto(open('gdz/25/25.1.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/25/25.2.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/25/25.3.jpg', 'rb')),
                              types.InputMediaPhoto(open('gdz/25/25.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6Ay) на полный набор задач  2️⃣5️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz26':
        # bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/26/26.1.jpg', 'rb')),
        #                                             types.InputMediaPhoto(open('gdz/26/26.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6Aj) на полный набор задач 2️⃣6️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz27':
        # bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/27/27.1.jpg', 'rb')),
        #                                             types.InputMediaPhoto(open('gdz/27/27.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://clck.ru/33J6AP) на полный набор задач 2️⃣7️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text,
                         parse_mode="Markdown", disable_web_page_preview=True)
    # endregion для кнопок из Решебника

    # region call.data для Теоретических задач
    elif call.data == 'th':
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton("1️⃣ Тип данных, Базовая арифметика", callback_data="firstclass"),
                    types.InlineKeyboardButton("2️⃣ Условные операторы, ветвление", callback_data="ifelifelse"),
                    types.InlineKeyboardButton("3️⃣ Циклы while и for", callback_data="whilefor"),
                    types.InlineKeyboardButton("4️⃣ Тип коллекций списки (list)", callback_data="list"),
                    types.InlineKeyboardButton("5️⃣ Строковый тип данных (str)", callback_data="string"),
                    types.InlineKeyboardButton("6️⃣ Самописные функции и рекурсия", callback_data="function"))
        send_message = 'Наборы задачек на отработку теории Python:'
        bot.send_message(call.message.chat.id, send_message,
                         parse_mode="Markdown", reply_markup=markup1)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("🗳️ Сдать домашку", callback_data="sendhomeworks"))


        bot.send_message(call.message.chat.id, "В случае ошибочной ссылки, просьба скинуть мне скриншот @ilandroxy",
                         parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markup2)
    # endregion call.data для Теоретических задач

    # region call.data для КЕГЭ
    elif call.data == 'kg':
        message_text = "Эта команда выдает рандомное задание из сборника Полякова (КЕГЭ)\n\n[Читать правила оформления домашки](https://www.notion.so/ilandroxxy/8234ee61967a4cbe8a232b745cff0b9a)"
        markup = types.InlineKeyboardMarkup(row_width=5)
        markup.add(types.InlineKeyboardButton("1", callback_data="kg1"),
                   types.InlineKeyboardButton("2", callback_data="kg2"),
                   types.InlineKeyboardButton("3", callback_data="kg3"),
                   types.InlineKeyboardButton("4", callback_data="kg4"),
                   types.InlineKeyboardButton("5", callback_data="kg5"),
                   types.InlineKeyboardButton("6", callback_data="kg6"),
                   types.InlineKeyboardButton("7", callback_data="kg7"),
                   types.InlineKeyboardButton("8", callback_data="kg8"),
                   types.InlineKeyboardButton("9", callback_data="kg9"),
                   types.InlineKeyboardButton("10", callback_data="kg10"),
                   types.InlineKeyboardButton("11", callback_data="kg11"),
                   types.InlineKeyboardButton("12", callback_data="kg12"),
                   types.InlineKeyboardButton("13", callback_data="kg13"),
                   types.InlineKeyboardButton("14", callback_data="kg14"),
                   types.InlineKeyboardButton("15", callback_data="kg15"),
                   types.InlineKeyboardButton("16", callback_data="kg16"),
                   types.InlineKeyboardButton("17", callback_data="kg17"),
                   types.InlineKeyboardButton("18", callback_data="kg18"),
                   types.InlineKeyboardButton("19-21", callback_data="kg19"),
                   types.InlineKeyboardButton("22", callback_data="kg22"),
                   types.InlineKeyboardButton("23", callback_data="kg23"),
                   types.InlineKeyboardButton("24", callback_data="kg24"),
                   types.InlineKeyboardButton("25", callback_data="kg25"),
                   types.InlineKeyboardButton("26", callback_data="kg26"),
                   types.InlineKeyboardButton("27", callback_data="kg27"))
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("🗳️ Сдать домашку", callback_data="sendhomeworks"))
        bot.send_message(call.message.chat.id, "В случае ошибочной ссылки, просьба скинуть мне скриншот @ilandroxy",
                         parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markup2)



    elif call.data == "kg1" or call.data == "kg2" or \
            call.data == "kg3" or call.data == "kg4" or \
            call.data == "kg5" or call.data == "kg6" or \
            call.data == "kg7" or call.data == "kg8" or \
            call.data == "kg9" or call.data == "kg10" or \
            call.data == "kg11" or call.data == "kg12" or \
            call.data == "kg13" or call.data == "kg14" or \
            call.data == "kg15" or call.data == "kg16" or \
            call.data == "kg17" or call.data == "kg18" or \
            call.data == "kg19" or call.data == "kg22" or \
            call.data == "kg23" or call.data == "kg24" or \
            call.data == "kg25" or call.data == "kg26" or \
            call.data == "kg27":
        kg = {'1': [78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
                    89, 90, 91, 92, 571, 1584, 1585, 1586,
                    1587, 1588, 1589, 1590, 1591, 1592, 1593,
                    1594, 1595, 1596, 1597, 1598, 1599, 1600,
                    1601, 1602, 1603, 1604, 1605, 1606, 2819,
                    2820, 2821, 2822, 2823, 2824, 2825, 2826,
                    2827, 2828],
              '2': [2, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62,
                  63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
                  1607, 1608, 1609, 1610, 1611, 1612, 1613,
                  1614, 1615, 1616, 1617, 1618, 1619, 1620,
                  1621, 1622, 1623, 1624, 1625, 1626, 1627,
                  1628, 1629, 1630, 1630, 1631, 1632, 1633,
                  1634],
              '3': [4282, 4283, 4284, 4285, 4286, 4287, 4288,
                  4289, 4290, 4291, 4292, 4293, 4294, 4295,
                  4296, 4297, 4298, 4299, 4363, 4364, 4365,
                    4366, 4367, 4368, 4369, 4370, 4371, 4372,
                    4373, 4374, 4387, 4388, 4389, 4390, 4391,
                    4392, 4393, 4394, 4395, 4396, 4397, 4398,
                    4399],
              '4': [6, 111, 112, 113, 114, 115, 116, 117, 118,
                    119, 120, 121, 122,  123, 124, 125, 126,
                    127,  128, 129, 130, 132, 1664, 1665, 1666,
                    1667, 1668, 1669, 1670, 1671, 1672, 1673,
                    1674, 1675, 1676, 1677, 1678, 1679, 1680,
                    1681, 1682, 1683, 1684, 1685, 1686, 1687,
                    1688, 1689],
              '5': [7, 141, 142, 143, 144, 145, 146, 147, 148,
                    149, 1713, 1714, 1715, 1716, 1717, 1718,
                    1719, 1720, 1721, 1722, 1723, 1724, 1725,
                    1726, 1727, 1728, 1729, 1730, 1731, 1732,
                    1733, 1734, 1735, 1736, 1737, 1738, 1739,
                    1740, 1741, 1742, 1743, 1744, 1745, 1746,
                    1747, 1748, 1749],
              '6': [5500, 5501, 5502, 5503, 5504, 5505, 5506,
                    5507, 5508, 5509, 5510, 5511, 5512, 5513,
                    5529, 5530, 5531, 5532, 5533, 5534, 5535,
                    5536, 5549, 5552, 5553, 5554, 5555, 5556,
                    5557, 5558, 5559, 5560, 5561, 5562, 5563,
                    5564,  5565, 5566, 5567, 5582, 5583, 5584,
                    5585, 5586, 5587],
              '7': [12, 13, 187, 188, 189, 190, 191, 192, 193,
                    194, 195, 196, 197, 198, 199, 200, 201, 202,
                    203, 204, 1813, 1814, 1815, 1816, 1817, 1818,
                    1819, 1820, 1821, 1822, 1823, 1824, 1825,
                    1826, 1827, 1828, 1829, 1830, 1831, 1832,
                    1833, 1834, 1835, 1836, 1837, 1838, 1839,
                    1840, 1841],
              '8': [14, 205, 205, 206, 207, 208, 209, 210, 211,
                    212, 213, 214, 215, 216, 217, 218, 219, 220,
                    221, 222, 223, 1885, 1886, 1887, 1888, 1889,
                    1890, 1891, 1892, 1893, 1894, 1895, 1896,
                    1897, 1898, 1899, 1900, 1901, 1902, 1903,
                    1904, 1905, 1906, 1907, 1908, 1909, 1910,
                    1911, 1912],
              '9': [1962, 1963, 1964, 1965, 1966, 1967, 1968,
                    1969, 1970, 1971, 1972, 1973, 1974, 1975,
                    1976, 1977, 1978, 1979, 1980, 1981, 1982,
                    1983, 1984, 1985, 1986, 1987, 1988, 1989,
                    1990, 1991, 1992, 1993, 1994, 1995, 1996,
                    1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005],
              '10': [2007, 2008, 2009, 2010, 2011, 2012, 2013,
                     2014, 2015, 2016, 2017, 2018, 2019, 2020,
                     2021, 2022, 2023, 2024, 2025, 2026, 2027,
                     2028, 2029, 2030, 2031, 2032, 2033, 2034,
                     3236, 3237, 3238, 3239, 3240, 3241, 3242,
                     3243, 3244, 3245, 3246, 3247, 3248, 3249,
                     3250, 3251, 3252, 3253],
              '11': [17, 264, 265, 266, 267, 268, 269, 270, 271,
                     272, 273, 274, 275, 276, 277, 278, 279, 280,
                     281, 282, 2035, 2036, 2037, 2038, 2039, 2040,
                     2041, 2042, 2043, 2044, 2045, 2046, 2047,
                     2048, 2049, 2050, 2051, 2052, 2053, 2054,
                     2055, 2056, 2057, 2058, 2059, 2060, 2061,
                     2062],
              '12': [18, 283, 284, 285, 286, 287, 288, 289, 290,
                     291, 292, 293, 294, 295, 296, 297, 298, 299,
                     300, 301, 2084, 2085, 2086, 2087, 2088, 2089,
                     2090, 2091, 2092, 2093, 2094, 2095, 2096,
                     2097, 2098, 2099, 2100, 2101, 2102, 2103,
                     2104, 2105, 2106, 2107, 2108, 2109, 2110,
                     2111, 2112],
              '13': [19, 302, 303, 304, 305, 306, 307, 308, 309,
                     310, 311, 312, 313, 314, 315, 316, 317, 318,
                     319, 320, 2138, 2139, 2140, 2141, 2142, 2143,
                     2144, 2145, 2146, 2147, 2148, 2149, 2150,
                     2151, 2152, 2153, 2154, 2155, 2156, 2157,
                     2158, 2159, 2160, 2161, 2162, 2163, 2164,
                     2165, 2166],
              '14': [5483, 5484, 5485, 5486, 5487, 5488, 5489,
                     5490, 5491, 5492, 5493, 5494, 5495, 5496,
                     5497, 5498, 5499, 5514, 5515, 2173, 2174,
                     2175, 2176, 2177, 2178, 2179, 2180, 2181,
                     2182, 2183, 2184, 2185, 2186, 2187, 2188,
                     2189, 2190, 2191, 2192, 2193, 2194, 2195,
                     2196, 2197, 2198, 2199, 2200, 2201, 2202],
              '15': [22, 359, 360, 361, 362, 363, 364, 365, 366,
                     367, 368, 369, 370, 371, 372, 373, 374, 375,
                     376, 377, 378, 379, 380, 381, 382, 383, 384,
                     385, 386, 1043, 1044, 1045, 1046, 1047, 1048,
                     1049, 1050, 1051, 1052, 1053, 1054, 1055,
                     1056, 1057, 1058, 1059, 1060, 1061, 1062,
                     1063, 1064, 1065, 1066],
              '16': [15, 224, 225, 226, 227, 228, 229, 230, 231,
                     232, 233, 234, 235, 236, 237, 238, 239, 240,
                     241, 242, 243, 2262, 2263, 2264, 2265, 2266,
                     2267, 2268, 2269, 2270, 2271, 2272, 2273,
                     2274, 2275, 2276, 2277, 2278, 2279, 2280,
                     2281, 2282, 2283, 2284, 2285, 2286, 2287,
                     2288, 2289],
              '17': [4269, 4270, 4271, 4272, 4273, 4274, 4275,
                     4276, 4277, 4300, 4301, 4302, 4303, 4304,
                     4305, 4306, 4307, 4308, 4309, 4310, 4311,
                     4312, 4313, 4314, 4315, 4316, 4317, 4318,
                     4319,  4320, 4321, 4322, 4323, 4324, 4351,
                     4352, 4353, 4354, 4355, 4356, 4357, 4358,
                     4359, 4360],
              '18': [2347, 2348, 2349, 2350, 2351, 2352, 2353,
                     2354, 2355, 2356, 2357, 2358, 2359, 2360,
                     2361, 2362, 2363, 2364, 2365, 2366, 2367,
                     2368, 2369, 2370, 2371, 2372, 2373, 2374,
                     2375, 2376, 2377, 2378, 2379, 2380, 2381,
                     2382, 2383, 2384, 2385, 2386, 2514, 2515,
                     2560, 2561, 2651],
              '19': [2387, 2388, 2389, 2390, 2391, 2392, 2393,
                     2394, 2395, 2396, 2397, 2398, 2399, 2400,
                     2401, 2402, 2403, 2404, 2405, 2406, 2407,
                     2408, 2409, 2410, 2411, 2412, 2413, 2414,
                     2415, 2416, 2417, 2418, 2419, 2420],
              '22': [5516, 5517, 5518, 5519, 5520, 5530, 5531,
                     5532, 5550, 5551, 5568, 5569, 5570, 5571,
                     5572, 5573, 5574, 5575, 5576, 5577, 5578,
                     5579, 5580, 5581, 5607, 5608, 5609, 5610,
                     5611, 5664, 5665, 5666],
              '23': [26, 445, 446, 447, 448, 449, 450, 451,
                     452, 453, 454, 455, 456, 457, 458, 459,
                     460, 461, 462, 463, 464, 465, 466, 467,
                     468, 2453, 2454, 2455, 2456, 2457, 2458,
                     2459, 2460, 2461, 2462, 2463, 2464, 2465,
                     2466, 2467, 2468, 2469, 2470, 2471, 2472,
                     2473, 2474, 2475, 2476, 2477],
              '24': [2506, 2507, 2508, 2509, 2510, 2511, 2512,
                     2513, 2514, 2515, 2516, 2517, 2518, 2519,
                     2520, 2521, 2522, 2523, 2524, 2525, 2526,
                     2527, 2528, 2529, 2530, 2531, 2532, 2533,
                     2534, 2535, 2536, 2537, 2538, 2539, 2540,
                     2541, 2542, 2543, 2544, 2545, 2546, 2547,
                     2548, 2549, 2550, 2551],
              '25': [2562, 2563, 2564, 2565, 2566, 2567, 2568,
                     2569, 2570, 2571, 2572, 2573, 2574, 2575,
                     2576, 2577, 2578, 2579, 2580, 2581, 2582,
                     2583, 2584, 2585, 2586, 2587, 2588, 2589,
                     2590, 2591, 2592, 2593, 2594, 2595, 2596,
                     2597, 2598, 2599, 2600, 2601, 2602, 2603,
                     2604, 2605, 2606, 2607],
              '26': [2617, 2618, 2619, 2620, 2621, 2622, 2623,
                     2624, 2625, 2626, 2627, 2628, 2629, 2630,
                     2631, 2632, 2633, 2634, 2635, 2636, 2637,
                     2638, 2639, 2640, 2641, 2642, 2643, 2644,
                     2645, 2646, 2647, 2648, 2649, 2650, 2707,
                     2708, 2709, 2836, 3152, 3153, 3154],
              '27': [2660, 2661, 2662, 2663, 2664, 2665, 2666,
                     2667, 2668, 2669, 2670, 2671, 2672, 2673,
                     2674, 2675, 2676, 2677, 2678, 2679, 2680,
                     2681, 2682, 2683, 2684, 2685, 2686, 2687,
                     2688, 2689, 2690, 2691, 2692, 2693, 2694,
                     2710, 2711, 2712, 2713]}

        type = call.data[2:]
        x = random.randint(0, len(kg[type]))
        link = f'({type}) КЕГЭ: Задача [{kg[type][x]}](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId={kg[type][x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-1001822573914, f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\n"
                             f"Получил домашку КЕГЭ ({type}): [{kg[type][x]}](https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId={kg[type][x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
    # endregion call.data для КЕГЭ

    # region call.data для Решу ЕГЭ
    elif call.data == 'hw':
        message_text = "Эта команда выдает рандомное задание с Решу ЕГЭ\n\n" \
                       "Помимо этого, мне приходит уведомление с номерами выпавших задач.\n\n" \
                       "Проявите самостоятельность в выборе, а на уроке мы разбрем возникшие вопросы!\n\n" \
                       "[Читать правила оформления домашки](https://www.notion.so/ilandroxxy/8234ee61967a4cbe8a232b745cff0b9a)"
        markup = types.InlineKeyboardMarkup(row_width=5)
        markup.add(types.InlineKeyboardButton("1", callback_data="hw1"),
                   types.InlineKeyboardButton("2", callback_data="hw2"),
                   types.InlineKeyboardButton("3", callback_data="hw3"),
                   types.InlineKeyboardButton("4", callback_data="hw4"),
                   types.InlineKeyboardButton("5", callback_data="hw5"),
                   types.InlineKeyboardButton("6", callback_data="hw6"),
                   types.InlineKeyboardButton("7", callback_data="hw7"),
                   types.InlineKeyboardButton("8", callback_data="hw8"),
                   types.InlineKeyboardButton("9", callback_data="hw9"),
                   types.InlineKeyboardButton("10", callback_data="hw10"),
                   types.InlineKeyboardButton("11", callback_data="hw11"),
                   types.InlineKeyboardButton("12", callback_data="hw12"),
                   types.InlineKeyboardButton("13", callback_data="hw13"),
                   types.InlineKeyboardButton("14", callback_data="hw14"),
                   types.InlineKeyboardButton("15", callback_data="hw15"),
                   types.InlineKeyboardButton("16", callback_data="hw16"),
                   types.InlineKeyboardButton("17", callback_data="hw17"),
                   types.InlineKeyboardButton("18", callback_data="hw18"),
                   types.InlineKeyboardButton("19-21", callback_data="hw19-21"),
                   types.InlineKeyboardButton("22", callback_data="hw22"),
                   types.InlineKeyboardButton("23", callback_data="hw23"),
                   types.InlineKeyboardButton("24", callback_data="hw24"),
                   types.InlineKeyboardButton("25", callback_data="hw25"),
                   types.InlineKeyboardButton("26", callback_data="hw26"),
                   types.InlineKeyboardButton("27", callback_data="hw27"))
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("🗳️ Сдать домашку", callback_data="sendhomeworks"))
        bot.send_message(call.message.chat.id, "В случае ошибочной ссылки, просьба скинуть мне скриншот @ilandroxy",
                         parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markup2)

    elif call.data == "hw19-21":
        type = '19-21'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 19)
        M = [28096, 27832, 33764, 28001, 28035, 28099,
             40994, 39248, 27771, 28090, 29667, 27797,
             27932, 28077, 28102, 38597, 27802, 28158,
             27780, 27826]

        if call.message.chat.id in Students:
            link = f'Задача типа (19): [{M[x]}]({s}{M[x]})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (20): [{M[x] + 1}]({s}{M[x] + 1})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (21): [{M[x] + 2}]({s}{M[x] + 2})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-1001822573914,
                             f"#{Students[call.message.chat.id][3]}  "
                             f"[Написать сообщение](tg://user?id={call.message.chat.id})\n"
                             f"Получил домашку ({type}): [{M[x]}]({s}{M[x]}), [{M[x] + 1}]({s}{M[x] + 1}), "
                             f"[{M[x] + 2}]({s}{M[x] + 2})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            link = f'Задача типа (19): [{M[x]}]({s}{M[x]})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (20): [{M[x] + 1}]({s}{M[x] + 1})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (21): [{M[x] + 2}]({s}{M[x] + 2})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw1" or call.data == "hw2" or \
         call.data == "hw3" or call.data == "hw4" or \
         call.data == "hw5" or call.data == "hw6" or \
         call.data == "hw7" or call.data == "hw8" or \
         call.data == "hw9" or call.data == "hw10" or \
         call.data == "hw11" or call.data == "hw12" or \
         call.data == "hw13" or call.data == "hw14" or \
         call.data == "hw15" or call.data == "hw16" or \
         call.data == "hw17" or call.data == "hw18" or \
         call.data == "hw22" or call.data == "hw23" or \
         call.data == "hw24" or call.data == "hw25" or \
         call.data == "hw26" or call.data == "hw27":
        hw = {'1': [13479, 23901, 38446, 11259, 26946, 18782,
                    5697, 15098, 16030, 5793, 29188, 26975,
                    18705, 7981, 38935, 4707, 40717, 28678,
                    17367, 5196, 25833, 3828, 36856, 15971,
                    7777, 37136, 38446, 13506, 7355, 11232],
              '2': [29650, 33174, 18483, 27287, 46999, 26974,
                    35891, 36857, 15124, 40718, 28538, 27399,
                    15912, 18430, 27260, 33472, 15970, 37137,
                    15787, 16878, 46960, 45236, 27531, 18781,
                    35460, 27371, 18071, 15097, 35976, 16431,
                    18578, 39231, 15814, 33504, 36015, 16805,
                    33081, 29109, 18614, 38936, 16029, 19051],
              '3': [37494, 39232, 37481, 38937, 47000, 37491,
                    37492, 37493, 45237, 40719, 37417, 37479,
                    37508, 37488, 37507, 37489, 37415, 46961,
                    40978, 37480, 37485, 37490],
              '4': [18617, 14691, 17323, 13351, 19054, 15942,
                    10499, 16808, 37139, 16881, 27290, 18553,
                    9791, 45238, 16380, 18581, 47001, 15915,
                    10379, 16434, 26948, 17369, 13562, 15817,
                    26977, 11234, 15790, 36017, 18486, 28680,
                    18811, 18074, 15621, 13616, 27263, 14220,
                    11341, 46962, 7685, 18433],
              '5': [7454, 26978, 13617, 29653, 18075, 11235,
                    18785, 10380, 15791, 7917, 9792, 16033,
                    17370, 11342, 18487, 14692, 18618, 7690,
                    15101, 15622, 35894, 13590, 16435, 13536,
                    9190, 18582, 7751, 47002, 16809, 10407,
                    14767, 27375, 45239, 11262, 14265, 15818,
                    27264, 10309, 26949, 13563],
              '6': [47246, 47404, 47245, 47390, 47247, 47308,
                    47249, 47315, 47305, 47249, 47304, 47306,
                    47403, 47313, 47311, 47307, 47310, 47312,
                    47314, 47393, 47316, 47391, 47406, 47309,
                    47248, 47392, 47301, 47303, 47405],
              '7': [18078, 8097, 23907, 16438, 25839, 13355,
                    11110, 29194, 15821, 13620, 19058, 13593,
                    17327, 45241, 27538, 16812, 28684, 9759,
                    15977, 26981, 18585, 11345, 9795, 14695,
                    17373, 38941, 10497, 33477, 10470, 35465,
                    15946, 16036, 36862, 15131, 28545, 29655,
                    13736, 36020, 18711, 33509],
              '8': [9361, 15822, 10473, 15795, 16037, 10500,
                    7986, 35897, 3568, 27009, 8658, 11266,
                    3230, 26953, 23908, 3569, 36021, 3692,
                    3515, 33753, 36863, 3811, 13459, 3233,
                    7370, 27236, 5055, 7338, 16439, 9162,
                    10384, 3517, 7694, 19059, 3227, 18622,
                    13567, 15947, 14696, 27295],
              '9': [33754, 27529, 35898, 33088, 27524, 27524,
                    36022, 27406, 27525, 33181, 35467, 27518,
                    46967, 28117, 38588, 39238, 27517, 36864,
                    27526, 29657, 27523, 27519, 45243, 40725,
                    27528, 38943, 27522, 35983, 40984, 33511,
                    47006, 37144, 33479, 27520, 27527],
              '10': [36865, 27582, 33480, 46968, 27590, 27589,
                     35899, 27588, 38944, 36023, 29658, 27580,
                     40726, 27586, 37145, 27577, 40985, 27581,
                     33512, 45244, 27407, 27579, 27585, 33089,
                     33182, 35468, 27587, 27584, 39239, 27591,
                     33755, 47007, 27583, 35984],
              '11': [9364, 6885, 40986, 36024, 33481, 7924, 11309,
                     7989, 16889, 4684, 33183, 6415, 10476, 6181,
                     18792, 9305, 5081, 5237, 15629, 4716, 36866,
                     45245, 23911, 6298, 5270, 6917, 16442, 9165,
                     6330, 14272, 16816, 7785, 29198, 7758, 15853,
                     9197, 15825, 7670, 9763, 6451],
              '12': [13571, 23912, 16890, 26986, 10290, 33514, 29660,
                     40987, 10317, 13517, 15630, 11350, 15854, 15951,
                     15799, 13544, 28550, 45246, 35470, 33757, 10415,
                     18562, 18820, 27299, 27272, 47009, 38946, 9764,
                     39241, 18626, 10504, 16443, 35986, 33482, 35901,
                     14229, 18793, 14775, 17332, 18716],
              '13': [5365, 13361, 10505, 16818, 5429, 33092, 10478,
                     18627, 11271, 29122, 33758, 17333, 18591, 5941,
                     16891, 15631, 15800, 6237, 40988, 11244, 33515,
                     40729, 17379, 3746, 15855, 28690, 18496, 6269,
                     18563, 27300, 28551, 18084, 27544, 6309, 46971,
                     27273, 3285, 39242, 3294, 15110],
              '14': [48395, 48378, 48386, 48403, 48379, 48391, 48387,
                     48400, 48382, 48383, 48393, 48401, 48338, 48394,
                     48388, 48399, 48392, 48397, 48380, 48384, 48398,
                     48389, 48376, 48396, 48385, 48377, 48339, 48402,
                     29201, 9697, 36869, 18444, 15953, 18497, 27274,
                     33484, 46972, 15632, 13362, 47011, 18085, 15984,
                     13743, 33186, 26988, 18795, 16043, 27015, 18628,
                     25846, 45248, 23914, 15926, 27545],
              '15': [13745, 8106, 35989, 34539, 34547, 18720, 33760,
                     34516, 8666, 33517, 34509, 15955, 34518, 27303,
                     11119, 33094, 34511, 35904, 13364, 16894, 46973,
                     17382, 36870, 27547, 34506, 45249, 15928, 34510,
                     34535, 29633, 34537,39244, 18566, 33187, 34542,
                     37150, 35473, 34513],
              '16': [4937, 5970, 37151, 35990, 38591, 5310, 4644, 4651,
                     36871, 4692, 35474, 45250, 7340, 4647, 7270, 5458,
                     4978, 27413, 6990, 4646, 4642, 5650, 4643, 7273,
                     5586, 4657, 4658, 5554, 4724, 33518, 6423, 6189,
                     4849, 35905, 5938, 4656, 33095, 5278],
              '17': [37356, 39763, 39764, 37344, 37348, 37354, 37345,
                     39246, 37350, 47014, 37360, 37355, 37347, 37337,
                     37359, 37358, 37371, 37349, 45251, 40733, 37370,
                     37372, 38951, 37340, 46975, 37369, 40992, 37341,
                     37336, 39762, 37357, 37373, 37362, 37361],
              '18': [27681, 27673, 35992, 46976, 27669, 27676, 27677,
                     39247, 27685, 27683, 29666, 40993, 27679, 33763,
                     33097, 33488, 37153, 33520, 45252, 35907, 27682,
                     40734, 27670, 27671, 27680, 38593, 27675, 27678,
                     36873, 27415, 27672, 36031, 33190, 38952, 47015,
                     27667, 27666, 35476, 27668, 27674],
              '22': [47588, 47589, 47601, 47605, 47598, 47593, 47602,
                     47595, 47603, 47600, 47610, 47590, 47609, 47608,
                     47616, 47586, 47607, 47549, 47614, 47596, 47613,
                     47611, 47582, 47591, 47606, 47584, 47594, 47592,
                     47587, 47615, 47604, 47599, 47583, 47612],
              '23': [28697, 18450, 3631, 16898, 27551, 14783, 5913, 13418,
                     11123, 15638, 38957, 16451, 15932, 7379, 13471, 15990,
                     8670, 16825, 17340, 13633, 18570, 7315, 11318, 18828,
                     33195, 27391, 45257, 7347, 13552, 14237, 29207, 23920,
                     13525, 14281, 7998, 39252, 18634, 13579, 18598, 13368],
              '24': [27692, 33526, 33494, 35913, 27698, 33103, 37131, 40740,
                     27689, 40999, 35482, 27695, 27686, 27697, 27688, 27694,
                     33196, 36879, 27696, 37159, 27421, 38958, 46982, 45258,
                     35998, 38602, 39253, 33769, 47021, 27699, 36037, 27691,
                     27690, 29672, 27693, 27687],
              '25': [33527, 27852, 33104, 28120, 39254, 27854, 37160, 28122,
                     37130, 27857, 27422, 41000, 36038, 29673, 35999, 46983,
                     47022, 33495, 33197, 33770, 28124, 38959, 45259, 35914,
                     28123, 27853, 28121, 27858, 36880, 35483, 27851, 38603,
                     27850, 40741, 27856, 27855],
              '26': [46984, 28132, 33528, 40742, 28141, 39255, 33771, 27884,
                     38960, 27888, 28140, 27886, 35915, 36881, 27423, 29674,
                     36000, 35484, 36039, 28139, 27883, 41001, 47023, 27881,
                     27882, 33198, 27887, 27880, 33105, 28138, 33496, 37161,
                     45260, 27885],
              '27': [28133, 33529, 35485, 27424, 33497, 28131, 27891, 27991,
                     37162, 47024, 46985, 35916, 33106, 38961, 27889, 38604,
                     36001, 39256, 28130, 40743, 27990, 41002, 36882, 28129,
                     29675, 27890, 27989, 33772, 36040, 45261, 33199]}

        type = call.data[2:]
        x = random.randint(0, len(hw[type]))
        link = f'({type}) Решу ЕГЭ: Задача [{hw[type][x]}](inf-ege.sdamgia.ru/problem?id={hw[type][x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id,
                             link,
                             parse_mode='Markdown',
                             disable_web_page_preview=True)

            bot.send_message(-1001822573914,
                             f"#{Students[call.message.chat.id][3]}  "
                             f"[Написать сообщение](tg://user?id={call.message.chat.id})\n"
                             f"Получил домашку Решу ЕГЭ ({type}): "
                             f"[{hw[type][x]}](inf-ege.sdamgia.ru/problem?id={hw[type][x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link,
                             parse_mode='Markdown',
                             disable_web_page_preview=True)
    # endregion call.data для Решу ЕГЭ

    # region call.data для Отправки Homework
    elif call.data == 'sendhomeworks':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)

        bot.send_message(call.message.chat.id,
                         'Просто скопируйте свой код из PyCharm.\n'
                         'Бот сформирует файл и отправит его за вас 🤖\n\n'
                         '*Обратите внимание, сообщение в Telegram ограничено 4096 символами!*',
                         parse_mode='Markdown', reply_markup=markup)

        file_name = f'homeworks/{Students[call.message.chat.id][3]}_homework.txt'

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)

                count = 0
                for STR in message.text:
                    for _ in STR:
                        count += 1

                if count <= 2 ** 12:
                    bot.send_message(call.message.chat.id,
                                     f"Кол-во символов в файле: {count}\n"
                                     f"🤖 Ожидайте отправляю файл.",
                                     reply_markup=markup)
                else:
                    bot.send_message(call.message.chat.id,
                                     "Длина файла превышена, удалите лишние строки!",
                                     reply_markup=markup)

                f = open(file_name, 'w')
                f.write(message.text)
                f = open(file_name, 'rb')
                bot.send_document(-1001822573914, f)
                bot.send_message(-1001822573914,
                                 f"#{Students[call.message.chat.id][3]} отправил домашку.",
                                 reply_markup=markup)
                bot.send_message(call.message.chat.id, "🤖 Файл доставлен, спасибо!")
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)


        bot.register_next_step_handler(call.message, message_input)

    # endregion call.data для отправки Homework

    # region call.data для Оплаты абонемента
    elif call.data == 'send_price':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(types.KeyboardButton('Подтвердить оплату'))

        pic_2 = open("photo/price.PNG", "rb")
        bot.send_photo(call.message.chat.id, pic_2)

        message_text_2 = f"*Мои реквизиты для перевода*\n\n*Перевод по номеру телефона:* \n" \
                         f"+7 (913) 468-35-34\nСБЕР или Тинькофф, *есть СБП*.\n\n" \
                         f"*Или по номеру карты:*\nТинькоф: 2200 7004 1864 5957\n" \
                         f"СБЕР: 5469 4400 2244 1977\n" \
                         f"Получатель: `Андрианов` `Илья` `Алексеевич`\n\n" \
                         f"После оплаты скидываю вам чек, работаю официально через НПД (`Самозанятый`).\n\n" \
                         f"[Оставить чаевые, коплю на новый компьютер](https://clck.ru/33J6fo) 💫"

        bot.send_message(call.message.chat.id,
                         message_text_2,
                         parse_mode="Markdown",
                         disable_web_page_preview=True,
                         reply_markup=markup)
    # endregion call.data для Оплаты абонемента

    # region call.data выводит Прайс в самом начале
    elif call.data == 'whats_price':
        pic_2 = open("photo/price.PNG", "rb")
        bot.send_photo(call.message.chat.id, pic_2)

        send_message2 = f"*Первое занятие БЕСПЛАТНО*,\nна нем я определю уровень " \
                        f"знаний, и мы вместе подбираем оптимальный абонемент!\n\n" \
                        f"Работаю официально по чекам через НПД (`Самозанятый`).\n\n"

        markup_price = types.InlineKeyboardMarkup(row_width=1)
        markup_price.add(types.InlineKeyboardButton('Оплатить абонемент', callback_data='send_price'))

        bot.send_message(call.message.chat.id, send_message2,
                         parse_mode="Markdown", reply_markup=markup_price)

    # endregion call.data выводит Прайс в самом начале

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉
# ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️ 0️⃣  1️⃣  2️⃣
# 3️⃣  4️⃣  5️⃣  6️⃣  7️⃣  8️⃣  9️⃣  🔟    🐍

'''# Публичные команды:
/start - перезапуск бота, на стартовую позицию
/help - справка по всем командам в боте
/getmyid - бот покажет ваш id пользователя Telegram

/myprojects - список моих актуальных проектов
/download - список программ необходимых для уроков

/price - получить информацию о ценах и реквизиты
/tasks - наборы задач для отработки решений ЕГЭ по Информатике
/links - полезные ссылки для подготовки к экзамену

/useful - шпаргалки от Яндекс практикума по Python
/homework - конструктор домашних заданий для моих учеников

/getorder - команда для желающих оставить заявку на разработку бота.

/today - выводит список учеников по дням занятий
/reviews - генерирует отзыв при нажатии кнопки 

/mylessons - проверить кол-во занятий в абонементе
/gdz - решебник с набором решенных Python задач ЕГЭ 
'''

########## Публичные команды ##########

# region Команды: start, help, getmyid
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('Что умеет этот бот 🤖'))

    pic_1 = open("photo/hello.jpeg", 'rb')
    bot.send_photo(message.chat.id, pic_1)

    markup1 = types.InlineKeyboardMarkup(row_width=1)
    markup1.add(types.InlineKeyboardButton("🧮 Посмотреть прайс на абонементы", callback_data='whats_price'))

    message_text1 = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\n' \
                    f'Меня зовут *Андрианов Илья*. \nЯ программист – `Python` `developer`.\n' \
                    f'А также репетитор подготовки к ЕГЭ по Информатике и ' \
                    f'программированию на языке `Python` 🐍\n\n' \
                    f'*Мои рейтинг на Авито*\n*5,0* ⭐️⭐️⭐️⭐️⭐️\nНа основании 68 оценок\nПосмотреть 👉 /reviews\n\n' \
                    f'*Рад Вас приветствовать* у себя на `"страничке"`, здесь я постараюсь ' \
                    f'рассказать о себе и, надеюсь, нам удастся найти общий язык 🙏 \n\n'
    bot.send_message(message.chat.id, message_text1, parse_mode='Markdown', reply_markup=markup1)




    message_text2 = f'Если вы мой студент, то воспользуйтесь командой 👉 /getmyid, чтобы бот ' \
                    f'🤖 показал ваш ID пользователя. Он необходим, чтобы ' \
                    f'[я смог добавить](t.me/@ilandroxy) Вас в систему!\n\n' \
                    f'Воспользуйтесь командой 👉 /download, чтобы получить список ' \
                    f'необходимых для занятий программ!\n\n' \
                    f'Воспользуйтесь командой 👉 /getorder, если хотите обсудить вопросы ' \
                    f'сотрудничества или разработку Вашего `Telegram` `бота` под заказ.\n\n' \
                    f'Воспользуйтесь командой 👉 /help, ' \
                    f'чтобы подробнее узнать о всех доступных командах.\n' \
                    f'Или вызовите *Меню команд* – большая синяя кнопка на семь часов.'
    bot.send_message(message.chat.id, message_text2, parse_mode='Markdown', reply_markup=markup)

    pic_2 = open("photo/menu.jpg", 'rb')
    bot.send_photo(message.chat.id, pic_2)

    order_message = f'✅ #Новыйпользователь\nName: {message.from_user.first_name}\nUsername: @{message.from_user.username}\n' \
                    f'User ID: {message.chat.id}\n[Написать сообщение](tg://user?id={message.chat.id})'
    bot.send_message(1891281816, order_message, parse_mode='Markdown', disable_web_page_preview=True)


# HELP
@bot.message_handler(commands=['help'])
def help(message):
    send_message = "*You can control me by sending these commands:*\n\n*Commands public*\n" \
                   "/help - справка по всем командам в боте\n" \
                   "/start - перезапуск бота на стартовую позицию\n" \
                   '/myprojects - список моих актуальных проектов\n' \
                   '/download - список программ необходимых для уроков\n' \
                   '/tasks - набор задач для отработки решений ЕГЭ по Информатике\n' \
                   '/price - получить информацию о ценах и реквизиты\n' \
                   '/links - полезные ссылки для подготовки к экзамену\n' \
                   '/homework - конструктор домашних заданий для моих учеников\n' \
                   '/getmyid - бот покажет ваш id пользователя Telegram\n' \
                   '/useful - получите шпаргалки от `Яндекс практикума` по Python\n' \
                   '/getorder - обсудить разработку Вашего чат бота под заказ\n' \
                   '/today - персональное расписание уроков\n' \
                   '/mylessons - проверить кол-во занятий в абонементе\n' \
                   '/reviews - генерирует отзыв при нажатии кнопки\n' \
                   '/gdz - решебник с набором решенных Python задач ЕГЭ\n'
    bot.send_message(message.chat.id, send_message, parse_mode="Markdown")


# GETMYID
@bot.message_handler(commands=['getmyid'])
def getmyid(message):
    user = str(message.chat.id)
    send_message = "*Ваш user ID: *" + user
    bot.send_message(message.chat.id, send_message, parse_mode="Markdown")
# endregion Команды: start, help, getmyid

# region Команды: myprojects, download
@bot.message_handler(commands=['myprojects'])
def myprojects(message):
    send_message = "Просто перечисляю, чем я занимаюсь сегодня!\n\n" \
                   "*1. Канал* [itpy | ИнформатикаЕГЭ](t.me/pro100_easy_ege)\n" \
                   "✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                   "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе!\n\n" \
                   "*2. Чат бот* 🤖[MotherBot](t.me/JustDoItMotherBot)  \nЭто Telegram бот, который помогает " \
                   "начинающим программистам разобраться в библиотеке [PyTelegramBotAPI](https://habr.com/ru/post/580408/), предназначенной " \
                   "для работы с API Telegram – создания чат ботов в меcсенджере.\n\n" \
                   "*3. Курс подготовки к ЕГЭ на* [Stepik](https://stepik.org/course/122969)\n" \
                   "На сегодняшний день курс еще находится в разработке, но уже можно понять, " \
                   "что он из себя будет представлять по [описанию проекта](https://stepik.org/lesson/770711/step/1) " \
                   "и черновому [примеру урока](https://stepik.org/lesson/770602/step/1).\n\n"

    bot.send_message(message.chat.id, send_message, parse_mode="Markdown", disable_web_page_preview=True)


@bot.message_handler(commands=['download'])
def download(message):
    message_text = f"*Перечень необходимых программ:*\n\n" \
                   f"1. Python [скачать](www.python.org/downloads/)\n\n" \
                   f"2. Telegram Desktop [скачать](telegram.org/)\n\n" \
                   f"3. Discord [скачать](discord.com/download)\n\n" \
                   f"4. Pycharm [скачать](www.jetbrains.com/ru-ru/pycharm/download/)\n\n" \
                   f"В случае необходимости, воспользуйтесь " \
                   f"[видео инструкцией](https://clck.ru/33J6UW) по установке PyCharm" \


    bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)
# endregion Команды: myprojects, download

# region Команды: price, tasks, links

@bot.message_handler(commands=['price'])
def price(message):
    message_text_1 = f"*Первое занятие БЕСПЛАТНО*,\n" \
                     f"на нем я определю уровень знаний, и мы вместе подбираем оптимальный абонемент!"
    bot.send_message(message.chat.id,
                     message_text_1,
                     parse_mode="Markdown",
                     disable_web_page_preview=True)

    pic_2 = open("photo/price.PNG", "rb")
    bot.send_photo(message.chat.id, pic_2)

    message_text_2 = f"*Мои реквизиты для перевода*\n\n*Перевод по номеру телефона:* \n" \
                     f"+7 (913) 468-35-34\nСБЕР или Тинькофф, *есть СБП*.\n\n" \
                     f"*Или по номеру карты:*\nТинькоф: 2200 7004 1864 5957\n" \
                     f"СБЕР: 5469 4400 2244 1977\n" \
                     f"Получатель: `Андрианов` `Илья` `Алексеевич`\n\n" \
                     f"После оплаты скидываю вам чек, работаю официально через НПД (`Самозанятый`).\n\n" \
                     f"[Оставить чаевые, коплю на новый компьютер](https://clck.ru/33J6fo) 💫"
    bot.send_message(message.chat.id, message_text_2, parse_mode="Markdown", disable_web_page_preview=True)


@bot.message_handler(commands=['tasks'])
def tasks(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("Открыть решебник 📚", callback_data="reshebnik"))

    bot.send_message(message.chat.id,
                     "*Наборы разных типов задач с* " \
                     "[Решу ЕГЭ](https://inf-ege.sdamgia.ru/?redir=1):\n`new 2022-2023 года`\n\n" \
                     "[1.](https://clck.ru/33J69K)   " \
                     "[2.](https://clck.ru/33J69E)   " \
                     "[3.](https://clck.ru/33J695)   " \
                     "[4.](https://clck.ru/33J68r)   " \
                     "[5.](https://clck.ru/33J5yi)   " \
                     "[6.](https://clck.ru/33J68Q)   " \
                     "[7.](https://clck.ru/33J68C)    " \
                     "[8.](https://clck.ru/33J67y)    " \
                     "[9.](https://clck.ru/33J67e)    " \
                     "[10.](https://clck.ru/33J66D)\n\n" \
                     "[11.](https://clck.ru/33J666)   " \
                     "[12.](https://clck.ru/33J65o)   " \
                     "[13.](https://clck.ru/33J65W)   " \
                     "[14.](https://clck.ru/33J658)   " \
                     "[15.](https://clck.ru/33J64M)   " \
                     "[16.](https://clck.ru/33J642)   " \
                     "[17.](https://clck.ru/33J63c)   " \
                     "[18.](https://clck.ru/33J63R)\n\n" \
                     "[19-21.](https://clck.ru/33J63E)   " \
                     "[22.](https://clck.ru/33J634)   " \
                     "[23.](https://clck.ru/33J62N)   " \
                     "[24.](https://clck.ru/33J626)   " \
                     "[25.](https://clck.ru/33J5zh)   " \
                     "[26.](https://clck.ru/33J5zQ)   " \
                     "[27.](https://clck.ru/33J5z5)\n\n" \
                     "*Обратите внимание*, что наборы задач разного года могут отличаться!",
                     reply_markup=markup,
                     parse_mode="Markdown",
                     disable_web_page_preview=True)


    bot.send_message(message.chat.id,
                     "*Наборы разных типов задач с* " \
                     "[Решу ЕГЭ](https://inf-ege.sdamgia.ru/?redir=1):\n" \
                     "`old 2021-2022 года`\n\n" \
                     "[1.](https://clck.ru/ebsmq)   " \
                     "[2.](https://clck.ru/ebsnV)   " \
                     "[3.](https://clck.ru/ebsnt)   " \
                     "[4.](https://clck.ru/ebsoN)   " \
                     "[5.](https://clck.ru/ebsp8)   " \
                     "[6.](https://clck.ru/33J5yi)   " \
                     "[7.](https://clck.ru/ebspX)    " \
                     "[8.](https://clck.ru/ebsq2)    " \
                     "[9.](https://clck.ru/ebsqH)   " \
                     "[10.](https://clck.ru/ebsqc)\n\n" \
                     "[11.](https://clck.ru/ebsrf)   " \
                     "[12.](https://clck.ru/ebsrr)   " \
                     "[13.](https://clck.ru/ebssH)   " \
                     "[14.](https://clck.ru/ebssi)   " \
                     "[15.](https://clck.ru/ebst4)   " \
                     "[16.](https://clck.ru/ebstT)   " \
                     "[17.](https://clck.ru/ebsuA)   " \
                     "[18.](https://clck.ru/ebsuf)\n\n" \
                     "[19-21.](https://clck.ru/ebsvw)   " \
                     "[22.](https://clck.ru/33J5xy)   " \
                     "[23.](https://clck.ru/ebsxo)   " \
                     "[24.](https://clck.ru/ebsyM)   " \
                     "[25.](https://clck.ru/ebszu)   " \
                     "[26.](https://clck.ru/ebt22)   " \
                     "[27.](https://clck.ru/ebt3a)\n\n" \
                     "При желании попробовать более сложные " \
                     "задачи воспользуйтесь конструктором " \
                     "[КЕГЭ](https://kompege.ru/task)",
                     parse_mode="Markdown",
                     disable_web_page_preview=True)

    bot.send_message(message.chat.id,
                     "Частичные наборы задач и их разборы из " \
                     "[моего курса](https://stepik.org/course/122969) на *Stepik*:\n\n"
                     "[1.]()   [2.]()   [3.]()   " \
                     "[4.]()   [5.]()   [6.](https://stepik.org/lesson/770602/step/1)   [7.]()    " \
                     "[8.]()    [9.]()    [10.]()\n\n[11.]()   " \
                     "[12.]()   [13.]()   [14.]()   [15.]()   " \
                     "[16.]()   [17.]()   [18.]()\n\n[19-21.]()   " \
                     "[22.](https://stepik.org/lesson/770602/step/7)   [23.]()   [24.]()   [25.]()   " \
                     "[26.]()   [27.]()\n\n\n" \
                     "На моем *YouTube канале* иногда выкладываю записи уроков, " \
                     "будет полезно – [подпишись!](https://m.youtube.com/channel/UCcORhBL494aSLcyIODjOG0A)",
                     parse_mode="Markdown",
                     disable_web_page_preview=True)


@bot.message_handler(commands=['links'])
def links(message):
    message_text = "*Постарался собрать для вас полезные ссылки для подготовки:*\n\n" \
                   "*1.* [Ссылка](https://stepik.org/course/58852) " \
                   "на крутой и бесплатный курс по базовой теории языка Python;\n\n" \
                   "*2.* Отличный, но растянутый [курс видеолекций](https://clck.ru/33J6kr) " \
                   "МФТИ от Тимофея Хирьянова;\n\n" \
                   "*3.* Возможно кому-то будет полезен экспресс обзор почти всей " \
                   "необходимой теории на [YouTube](https://clck.ru/33J6mF);\n\n" \
                   "*4.* Некоторые разборы и варианты решений можно посмотреть на " \
                   "[YouTube](https://clck.ru/32e8aE) канале Ивана, не все понятно с первого раза, " \
                   "но это лучший вариант из предложенных. А может быть даже из возможных.\n\n" \
                   "*5.* Всем кто намеревается сдавать ЕГЭ по Информатике настоятельно рекомендую " \
                   "[прочитать статью](https://habr.com/ru/post/573580/) про опыт студента, " \
                   "сдающего первый компьютерный экзамен!\n\n" \
                   "\n*Для отработки теории на практике воспользуйтесь командой /tasks *"
    bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)
# endregion Команды: price, tasks, links

# region Команды: useful, homeworks
@bot.message_handler(commands=['useful'])
def useful(message):
    if message.chat.id in Students or message.chat.id in Me:
        message_text = 'Со своими студентами я решил поделиться шпаргалками от *Яндекс Практикума*, ' \
                       'в котором сейчас прохожу обучение по специальности `Python` `developer`.\n\n' \
                       'Постепенно список файлов будет пополняться, но *хочу отметить, что для ' \
                       'успешной сдачи экзамена ЕГЭ по Информатике хватит первых 3-х файлов*:'
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("1️⃣ Знакомство с Python: Типы данных, Списки.", callback_data="py01"),
                   types.InlineKeyboardButton("2️⃣ Циклы, Ветвления, Логические выражения.", callback_data="py02"),
                   types.InlineKeyboardButton("3️⃣ Функции: Вызов, Аргументы, Возврат значений.", callback_data="py03"),
                   types.InlineKeyboardButton("4️⃣ Коллекции: Словари и Множества.      ", callback_data="py04"),
                   types.InlineKeyboardButton("5️⃣ Строки: Метод split() и f-string.    ", callback_data="py05"),
                   types.InlineKeyboardButton("6️⃣ Библиотеки: datetime, math, random.. ", callback_data="py06"),
                   types.InlineKeyboardButton("7️⃣ Сетевые запросы: Библиотека requests.", callback_data="py07"))
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Извините, эта функция доступна только моим ученикам, [запишитесь на урок](https://clck.ru/33J5xF)", parse_mode="Markdown", disable_web_page_preview=True)


@bot.message_handler(commands=['homework'])
def homework(message):
    if message.chat.id in Me or message.chat.id in Students:
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("🐍 Задачи на теорию Python", callback_data="th"),
                    types.InlineKeyboardButton("🪤 Получить задачи с Решу ЕГЭ", callback_data="hw"),
                    types.InlineKeyboardButton("🧱 Получить задачи с КЕГЭ", callback_data="kg"),
                    types.InlineKeyboardButton("🗳️ Сдать домашку", callback_data="sendhomeworks"))
        sti = open('photo/hw.tgs', 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=markup2)

    else:
        bot.send_message(message.chat.id,
                         "Извините, эта функция доступна только "
                         "моим ученикам, [запишитесь на урок](https://clck.ru/33J5xF)",
                         parse_mode="Markdown")
# endregion Команды: useful, homeworks

# region Команды: getorder
@bot.message_handler(commands=['getorder'])
def getorder(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Отменить ⛔')
    markup.add(btn1)
    bot.send_message(message.chat.id, "Просто опишите в одном сообщении какой функциональностью должен обладать Ваш бот, "
                                      "а [я свяжусь с вами](https://t.me/ilandroxy) в ближайшее время!",
                                      parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        text_message = message.text
        if text_message != 'Отменить ⛔':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('Контакты')
            btn2 = types.KeyboardButton('Репетитор')
            btn3 = types.KeyboardButton('Мои проекты')
            btn4 = types.KeyboardButton('Записаться на урок')
            btn5 = types.KeyboardButton('Получить файл с урока')
            markup.add(btn1, btn2, btn3, btn4, btn5)

            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ожидайте ответа.", parse_mode='Markdown', reply_markup=markup)

            bot.send_message(1891281816, f'✅ Новый заказ\nUser: {message.from_user.first_name}\n'
                                         f'Username: {message.from_user.username}\n'
                                         f'[Написать сообщение](tg://user?id={message.chat.id})\n\n'
                                         f'Message:\n{text_message}', parse_mode='Markdown', disable_web_page_preview=True)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('Контакты')
            btn2 = types.KeyboardButton('Репетитор')
            btn3 = types.KeyboardButton('Мои проекты')
            btn4 = types.KeyboardButton('Записаться на урок')
            btn5 = types.KeyboardButton('Получить файл с урока')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

    bot.register_next_step_handler(message, message_input)
# endregion Команды: getorder

# region Команда: today
@bot.message_handler(commands=['today'])
def today(message):
    if message.chat.id == 1891281816:
        send_pic = open('photo/today.jpg', 'rb')
        bot.send_photo(message.chat.id, send_pic)

        day = time.strftime('%A')

        if day == 'Monday':
            temp = f'Список уроков на понедельник: *'
            for key in MondayStudents:
                temp += f'[{MondayStudents[key][3]}](tg://user?id={key}) время урока: {MondayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Tuesday':
            temp = f'Список уроков на вторник: *'
            for key in TuesdayStudents:
                temp += f'[{TuesdayStudents[key][3]}](tg://user?id={key}) время урока: {TuesdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Wednesday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

        if day == 'Thursday':
            temp = f'Список уроков на четверг: *'
            for key in ThursdayStudents:
                temp += f'[{ThursdayStudents[key][3]}](tg://user?id={key}) время урока: {ThursdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Friday':
            temp = f'Список уроков на пятницу: *'
            for key in FridayStudents:
                temp += f'[{FridayStudents[key][3]}](tg://user?id={key}) время урока: {FridayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Saturday':
            temp = f'Список уроков на субботу: *'
            for key in SaturdayStudents:
                temp += f'[{SaturdayStudents[key][3]}](tg://user?id={key}) время урока: {SaturdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Sunday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")


    elif message.chat.id in Students:
        send_pic = open('photo/today.jpg', 'rb')
        bot.send_photo(message.chat.id, send_pic)
        bot.send_message(message.chat.id, "Поглядим на Ваше расписание 🤖 ", parse_mode='Markdown')

        for key in MondayStudents:
            if message.chat.id == key:
                bot.send_message(message.chat.id,
                                 f'Понедельник, '
                                 f'время урока: {MondayStudents[key][1]} (по Нск)',
                                 parse_mode='Markdown')

        for key in TuesdayStudents:
            if message.chat.id == key:
                bot.send_message(message.chat.id,
                                 f'Вторник, '
                                 f'время урока: {TuesdayStudents[key][1]} (по Нск)',
                                 parse_mode='Markdown')

        for key in ThursdayStudents:
            if message.chat.id == key:
                bot.send_message(message.chat.id,
                                 f'Четверг, '
                                 f'время урока: {ThursdayStudents[key][1]} (по Нск)',
                                 parse_mode='Markdown')

        for key in FridayStudents:
            if message.chat.id == key:
                bot.send_message(message.chat.id,
                                 f'Пятница, '
                                 f'время урока: {FridayStudents[key][1]} (по Нск)',
                                 parse_mode='Markdown')

        for key in SaturdayStudents:
            if message.chat.id == key:
                bot.send_message(message.chat.id,
                                 f'Суббота, '
                                 f'время урока: {SaturdayStudents[key][1]} (по Нск)',
                                 parse_mode='Markdown')

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команда: today

# region Команды: reviews, gdz
@bot.message_handler(commands=['reviews'])
def reviews(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("Посмотреть все отзывы на Авито", url="https://www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing"))

    M = ['reviews/re1.png', 'reviews/re2.png', 'reviews/re3.png', 'reviews/re4.png', 'reviews/re5.png', 'reviews/re6.png']
    pic_reviews = open(random.choice(M), 'rb')
    bot.send_photo(message.chat.id, pic_reviews)
    bot.send_message(message.chat.id, 'Еще больше отзывов 👉 /reviews', parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['gdz'])
def gdz(message):
    if message.chat.id in Students or message.chat.id in Me:
        # 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟
        message_text = 'Наборы задачек на отработку теории Python 👇 😅'
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(types.InlineKeyboardButton("2", callback_data="gdz2"),
                   types.InlineKeyboardButton("5", callback_data="gdz5"),
                   types.InlineKeyboardButton("6", callback_data="gdz6"),
                   types.InlineKeyboardButton("8", callback_data="gdz8"),
                   types.InlineKeyboardButton("12", callback_data="gdz12"),
                   types.InlineKeyboardButton("14", callback_data="gdz14"),
                   types.InlineKeyboardButton("15", callback_data="gdz15"),
                   types.InlineKeyboardButton("16", callback_data="gdz16"),
                   types.InlineKeyboardButton("17", callback_data="gdz17"),
                   types.InlineKeyboardButton("22", callback_data="gdz22"),
                   types.InlineKeyboardButton("23", callback_data="gdz23"),
                   types.InlineKeyboardButton("24", callback_data="igdz24"),
                   types.InlineKeyboardButton("25", callback_data="gdz25"),
                   types.InlineKeyboardButton("26", callback_data="gdz26"),
                   types.InlineKeyboardButton("27", callback_data="gdz27"))
        bot.send_message(message.chat.id, message_text, parse_mode="Markdown", reply_markup=markup)
# endregion Команды: reviews,  gdz

########## Приватные команды ##########

# region Работа с базами данных
def analytics(func: callable):
    total_users = 0
    users = [['user_id', 'username']]
    username = ""


    def anlytics_wrapper(message):
        nonlocal users, username

        # Считаем кол-во нажатий на клавишу-----------------------------------
        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS active(
                                id INTEGER,
                                UserName TEXT
                            )""")
        sql.commit()

        people_id = message.chat.id
        cursor.execute(f"SELECT id FROM active WHERE id = {people_id}")
        data = cursor.fetchone()

        if data is None:
            user_id = message.chat.id
            username = message.from_user.username

            cursor.execute(f"INSERT INTO active VALUES(?, ?);", (user_id, username))
            sql.commit()
        else:
            cursor.execute(f"DELETE FROM active WHERE id = {people_id}")
            user_id = message.chat.id
            username = message.from_user.username
            users.append([user_id, username])



            cursor.execute(f"INSERT INTO active VALUES(?, ?);", (user_id, username))
            sql.commit()

            cursor.close()

        return func(message)
    return anlytics_wrapper
# endregion Работа с базами данных

# region Команда:  mylessons
@bot.message_handler(commands=['mylessons'])
def mylessons(message):
    if message.chat.id == 1891281816:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)

        day = 'Все студенты: *'
        for x in sorted(S):
            day += f'[{x[0][3]}](tg://user?id={x[-1]}): {x[-1]} *'
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text

            if text_message != 'Отменить ⛔':
                user_id = int(text_message)
                sql = sqlite3.connect('analytics.db')
                cursor = sql.cursor()

                cursor.execute("""CREATE TABLE IF NOT EXISTS tickets(
                                                               id INTEGER,
                                                               name TEXT,
                                                               count INTEGER,
                                                               mess TEXT
                                                           )""")
                sql.commit()

                cursor.execute(f"SELECT * FROM tickets WHERE id = {user_id}")
                records = cursor.fetchone()

                if records is None:
                    bot.send_message(message.chat.id,
                                     'Такого пользователя нет в db tickets..Абонемент отсутсвует или не продлен!')
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton('Контакты')
                    btn2 = types.KeyboardButton('Репетитор')
                    btn3 = types.KeyboardButton('Мои проекты')
                    btn4 = types.KeyboardButton('Записаться на урок')
                    btn5 = types.KeyboardButton('Получить файл с урока')
                    markup.add(btn1, btn2, btn3, btn4, btn5)

                    bot.send_message(message.chat.id,
                                     f'🤖 Доброго времени суток, Илья!\n'
                                     f'Я все посчитал, вот записи по абонементу студента '
                                     f'#{Students[user_id][3]} 📊📈🧮\n\n{records[3]}',
                                     parse_mode='Markdown')
                    bot.send_message(message.chat.id,
                                     f'👨‍💻 Кол-во оставшихся занятий в абонементе: *{Students[user_id][4] - records[2]} шт*',
                                     parse_mode='Markdown', reply_markup=markup)
                cursor.close()
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(message, message_input)
    elif message.chat.id in Students:
        user_id = message.chat.id
        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute(f"SELECT * FROM tickets WHERE id = {user_id}")
        records = cursor.fetchone()

        if records is None:
            bot.send_message(message.chat.id, 'Абонемент отсутсвует или не продлен, по всем вопросам пишите @ilandroxy')
        else:
            bot.send_message(message.chat.id,
                             f'🤖 Доброго времени суток, #{Students[user_id][3]}!\n'
                             f'Я все посчитал, вот записи по Вашему абонементу 📊📈🧮\n\n'
                             f'{records[3]}', parse_mode='Markdown')
            bot.send_message(message.chat.id,
                             f'👨‍💻 Кол-во оставшихся занятий в абонементе: *{Students[user_id][4] - records[2]} шт*',
                             parse_mode='Markdown')
        cursor.close()

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команда: mylessons

# region Команда: list
@bot.message_handler(commands=['list'])
def list(message):
    if message.chat.id in PrivateMe:
        message_text = 'Список студентов:\n'
        for i in Students:
            message_text += f'#{Students[i][3]}\n'
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команда: list

# region Команда: добавить ученика, редактировать запись
@bot.message_handler(commands=['addstudents'])
def addstudents(message):
    if message.chat.id == 1891281816:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(types.KeyboardButton('Отменить ⛔'))

        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                                                id INTEGER,
                                                name TEXT,
                                                pyfile TEXT,
                                                day TEXT,
                                                time TEXT,
                                                price INTEGER,
                                                count INTEGER
                                            )""")
        sql.commit()

        bot.send_message(1891281816,
                         f" 🤖 Итак, я готов добавить ученика.\nВведите данные о студенте через пробел, используя пример:\n"
                         f"[id name filename.py day time price count]", reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':

                cursor.execute(f"SELECT * FROM students")

                mess = message.text.strip().split()
                id = int(mess[0])
                name = mess[1]
                file = mess[2]
                day = mess[3]
                time = mess[4]
                price = int(mess[5])
                count = int(mess[6])
                cursor.execute(f"INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?);", (id, name, file, day, time, price, count))
                sql.commit()
                cursor.close()

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)

                bot.send_message(1891281816,
                                 f" 🤖 Студент успешно добавлен!",
                                 reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(message, message_input)


@bot.message_handler(commands=['editstudents'])
def editstudents(message):
    if message.chat.id == 1891281816:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(types.KeyboardButton('Отменить ⛔'))

        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS students(
                                                id INTEGER,
                                                name TEXT,
                                                pyfile TEXT,
                                                day TEXT,
                                                time TEXT,
                                                price INTEGER,
                                                count INTEGER
                                            )""")
        sql.commit()

        cursor.execute(f"SELECT * FROM students")
        records = cursor.fetchall()
        send_message = ''
        for row in records:
            send_message += f'{row[2]}: {row[0]}\n'

        bot.send_message(1891281816, send_message)

        bot.send_message(1891281816, 'Введите id пользователя, для редактирования: ', reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                id = int(message.text)
                cursor.execute(f"SELECT * FROM students WHERE id = {id}")
                records = cursor.fetchone()

                send_message = f'{records[0]} {records[1]} {records[2]} {records[3]} {records[4]} {records[5]} {records[6]}'
                bot.send_message(1891281816, send_message)
                bot.send_message(1891281816, "Введите отредактированную запись: ")

                @bot.message_handler(content_types=['text'])
                def message_input(message):
                    if message.text != 'Отменить ⛔':
                        mess = message.text.strip().split()
                        id = int(mess[0])
                        name = mess[1]
                        file = mess[2]
                        day = mess[3]
                        time = mess[4]
                        price = int(mess[5])
                        count = int(mess[6])

                        cursor.execute(f"DELETE FROM students WHERE id = {id}")

                        cursor.execute(f"INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?);", (id, name, file, day, time, price, count))
                        sql.commit()

                        cursor.close()
                        bot.send_message(1891281816, "Запись о студентах отредактирована!")

                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                        btn1 = types.KeyboardButton('Контакты')
                        btn2 = types.KeyboardButton('Репетитор')
                        btn3 = types.KeyboardButton('Мои проекты')
                        btn4 = types.KeyboardButton('Записаться на урок')
                        btn5 = types.KeyboardButton('Получить файл с урока')
                        markup.add(btn1, btn2, btn3, btn4, btn5)
                        bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)
                bot.register_next_step_handler(message, message_input)

            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton('Контакты')
                btn2 = types.KeyboardButton('Репетитор')
                btn3 = types.KeyboardButton('Мои проекты')
                btn4 = types.KeyboardButton('Записаться на урок')
                btn5 = types.KeyboardButton('Получить файл с урока')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

        bot.register_next_step_handler(message, message_input)




# endregion Команда: добавить ученика



@bot.message_handler(content_types=['text'])
@analytics
def mess(message):
    get_message_bot = message.text.strip().lower()

    ########## Публичные кнопки ##########

    # region Кнопка: [Что умеет этот бот 🤖]
    if get_message_bot in ('что умеет этот бот 🤖', 'что умеет этот бот', 'что умеет бот', 'help') :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         '🤖 Бот помогает мне\nорганизовывать учебный процесс.\n\n'
                         '🧑‍💻 Например, здесь можно\nувидеть доступ к моему\nкалендарю '
                         'для записи на урок\nили переноса занятий.',
                         reply_markup=markup)

        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Далее", callback_data='next1'))

        pic_1 = open("photo/appointment.jpg", 'rb')
        bot.send_photo(message.chat.id, pic_1, reply_markup=markup2)
    # endregion Кнопка: Что умеет этот бот

    # region Кнопки: [Подтвердить оплату абонемента ❗]
    elif get_message_bot in ('подтвердить оплату абонемента ❗', 'оплачено', 'подтвердить оплату'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id,
                         f"Cпасибо, записал 🤖\nПроверить, что все сработало\n👉/mylessons",
                         reply_markup=markup)
        bot.send_message(1891281816,
                         f"{Students[message.chat.id][3]} подтвердил оплату ✅",
                         reply_markup=markup)

        now = dt.datetime.utcnow()
        date = my_time(now.strftime('%A %d %B %Y'))
        bot.send_message(-1001819293687,
                         f"✅ #{Students[message.chat.id][3]} "
                         f"*абонемент оплачен*.\nДата: {date}",
                         parse_mode='Markdown')

        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS tickets(
                                               id INTEGER,
                                               name TEXT,
                                               count INTEGER,
                                               mess TEXT
                                           )""")
        sql.commit()

        user_id = message.chat.id
        cursor.execute(f"SELECT * FROM tickets WHERE id = {user_id}")
        records = cursor.fetchone()

        if records is None:
            name = Students[user_id][3]
            count = 0
            mess = f"✅ #{Students[message.chat.id][3]} абонемент *оплачен*.\nДата: {date}\n\n"
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))
            sql.commit()
        else:
            name = Students[user_id][3]
            count = records[2]
            newmess = f"✅ #{Students[message.chat.id][3]} абонемент *оплачен*.\nДата: {date}\n\n"
            mess = records[3] + newmess
            cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))
            sql.commit()
            cursor.close()
    # endregion Кнопки: [Подтвердить оплату абонемента ❗]

    # region Кнопки: [Да, все получается ✅]
    elif get_message_bot == 'да, все получается ✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id,
                         f"Cпасибо, отправил ответ 🤖",
                         reply_markup=markup)

        now = dt.datetime.utcnow()
        date = my_time(now.strftime('%A %d %B %Y'))

        bot.send_message(-1001819293687,
                         f"{date}\n\n#{Students[message.chat.id][3]}",
                         parse_mode='Markdown')

        markup2 = types.InlineKeyboardMarkup(row_width=3)
        markup2.add(types.InlineKeyboardButton('OK', callback_data='lesson'))
        bot.send_message(1891281816,
                         f"✅ {Students[message.chat.id][3]} – Урок будет\n"
                         f"[Написать сообщение](tg://user?id={message.chat.id})",
                         parse_mode='Markdown')


        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS tickets(
                                        id INTEGER,
                                        name TEXT,
                                        count INTEGER,
                                        mess TEXT
                                    )""")
        sql.commit()

        user_id = message.chat.id
        cursor.execute(f"SELECT * FROM tickets WHERE id = {user_id}")
        records = cursor.fetchone()

        if records is None:
            name = Students[user_id][3]
            count = 1
            mess = f"Занятие №{count}\nДата: {date} \n\n"
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))

            if count == Students[user_id][4]:
                markup_price = types.InlineKeyboardMarkup(row_width=3)
                markup_price.add(types.InlineKeyboardButton('Оплатить новый абонемент', callback_data='send_price'))

                bot.send_message(-1001819293687,
                                 f"⛔ #{Students[user_id][3]} абонемент *закончился*.\n"
                                 f"[Написать сообщение](tg://user?id={user_id})\n\n"
                                 f"История:\n{mess}", parse_mode='Markdown')
                bot.send_message(user_id,
                                 f"Доброго времени суток, #{Students[user_id][3]}!\n\n"
                                 f"🤖 Я посчитал, что Ваш абонемент заканчивается, сегодняшний урок последний!\n\n 🧮 Давайте проверим:\n\n"
                                 f"{mess}", parse_mode='Markdown', reply_markup=markup_price)
                cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            sql.commit()
        else:
            name = Students[user_id][3]
            count = records[2] + 1
            newmess = f"*Занятие №{count}*\nДата: {date} \n\n"
            mess = records[3] + newmess
            cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))

            if count == Students[user_id][4]:
                markup_price = types.InlineKeyboardMarkup(row_width=3)
                markup_price.add(types.InlineKeyboardButton('Оплатить новый абонемент',
                                                            callback_data='send_price'))

                bot.send_message(-1001819293687,
                                 f"⛔ #{Students[user_id][3]} *абонемент закончился*.\n"
                                 f"[Написать сообщение](tg://user?id={user_id})\n\n"
                                 f"История:\n{mess}", parse_mode='Markdown')
                bot.send_message(user_id,
                                 f"Доброго времени суток, #{Students[user_id][3]}!\n\n"
                                 f"🤖 Я посчитал, что Ваш абонемент заканчивается, "
                                 f"сегодняшний урок последний!\n\n 🧮 Давайте проверим:\t"
                                 f"{mess}", parse_mode='Markdown', reply_markup=markup_price)
                cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            sql.commit()
            cursor.close()
    # endregion Кнопки: [Да, все получается ✅]

    # region Кнопки: [Нет, не получится ⛔], [Какая-то ошибка], [Прочитано ✅]
    elif get_message_bot == 'нет, не получится ⛔':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id,
                         f"🤖 Воспользуйтесь формой, чтобы "
                         f"[перенести урок](https://clck.ru/33J6hH)",
                         reply_markup=markup, parse_mode='Markdown',
                         disable_web_page_preview=True)
        bot.send_message(1891281816,
                         f"⛔ {Students[message.chat.id][3]} – Урока не будет\n"
                         f"[Написать сообщение](tg://user?id={message.chat.id})",
                         parse_mode='Markdown')


    elif get_message_bot == 'какая-то ошибка, у нас сегодня нет урока ⚙️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id, f" 🤖 Sorry, ошибка будет исправлена в ближайшее время!", reply_markup=markup)
        bot.send_message(1891281816, f"‼️ {Students[message.chat.id][3]} – что-то не так с расписанием, "
                                     f"надо проверить.\n[Написать сообщение](tg://user?id={message.chat.id})",
                                     parse_mode='Markdown')

    elif get_message_bot == 'прочитано ✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)


        bot.send_message(message.chat.id, f"Спасибо, что читаете 🤖", reply_markup=markup)
        bot.send_message(1891281816, f"🤖 {Students[message.chat.id][3]} – Уведомлен \n"
                                     f"[Написать сообщение](tg://user?id={message.chat.id})", parse_mode='Markdown')
    # endregion Кнопки: [Нет, не получится ⛔], [Какая-то ошибка], [Прочитано ✅]

    # region Кнопка: [Контакты]
    elif get_message_bot == "контакты":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("👨‍💻 Моя визитка MyQRcards", url='https://card.myqrcards.com/links/5jaDBMw7w61?v=-1160'))

        send_message1 = "*Мои контакты:*\n\n" \
                        "[Мое портфолио ilandroxxy.github.io](https://ilandroxxy.github.io/)\n\n[Telegram](t.me/ilandroxy)\n\n" \
                        "[WhatsApp](wa.me/message/JSXJ2NLWTVNFC1)\n\n[Мой блог в Teletype](https://teletype.in/@ilandroxy)\n\n" \
                        "[Discord](https://discordapp.com/users/ilandroxxy#6249) ilandroxxy#6249\n\n" \
                        "[Zoom](https://us04web.zoom.us/j/2402871810?pwd=OVdGQkE2ODIvWm1WNk5EdStQR1o4UT09)\n\n" \
                        "[Профиль Авито](www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing)\n\n" \
                        "[YouTube](https://youtube.com/@ilandroxy)\n\n" \
                        "[GitHub](https://github.com/ilandroxxy)\n\nРабочий телефон: +7 (995) 437–52–59\n\n" \
                        "Email: ilandroxxy@gmail.com"
        bot.send_message(message.chat.id, send_message1, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)
    # endregion Кнопка: [Контакты]

    # region Кнопка: [Мои проекты]
    elif get_message_bot == "мои проекты":
        send_message1 = "Просто перечисляю, чем я занимаюсь сегодня!\n\n" \
                       "*1. Канал* [itpy | ИнформатикаЕГЭ](t.me/pro100_easy_ege)\n" \
                        "✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                       "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе!\n\n" \
                       "*2. Чат бот* 🤖[MotherBot](t.me/JustDoItMotherBot)  \nЭто Telegram бот, " \
                        "который помогает начинающим программистам разобраться в библиотеке " \
                        "[PyTelegramBotAPI](https://habr.com/ru/post/580408/), предназначенной " \
                       "для работы с API Telegram – создания чат ботов в меcсенджере.\n\n" \
                       "*3. Курс подготовки к ЕГЭ на* [Stepik](https://stepik.org/course/122969)\n" \
                       "На сегодняшний день курс еще находится в разработке, но уже можно понять, " \
                        "что он из себя будет представлять по [описанию проекта](https://stepik.org/lesson/770711/step/1) " \
                       "и черновому [примеру урока](https://stepik.org/lesson/770602/step/1).\n\n"
        bot.send_message(message.chat.id, send_message1, parse_mode="Markdown", disable_web_page_preview=True)

        send_message2 = "<b>Совместные проекты с моими учениками:</b>\n\n" \
                        '<b>1. Чат бота</b> 🤖 @kto_hochet_stat_millioneromBOT\n' \
                        '<b>Авторы:</b> @ilandroxxy и Шариф Георгий, ученик 6 класса.\n' \
                        '<b>Цель проекта:</b> сформировать викторину по аналогии игры ' \
                        '"Кто хочет стать миллионером", реализуя систему рандомных ' \
                        'вопросов и персонализированный системы лидеров.\n\n' \
                        '<b>2. Чат бота</b> 🤖 @NumberOfSystem_Bot\n<b>Авторы:</b> ' \
                        '@ilandroxxy и Казакова Александра, ученица 8 класса.\n' \
                        '<b>Цель проекта:</b> создать калькулятор систем счисления, ' \
                        'которые поможет в освоении программы по предмету "Информатика" за 8 класс.\n\n'
        bot.send_message(message.chat.id, send_message2, parse_mode='HTML', disable_web_page_preview=True)
    # endregion Кнопка: [Мои проекты]

    # region Кнопка: [Записаться на урок]
    elif get_message_bot == "записаться на урок":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("planerka.app", url="https://planerka.app/meet/ilandroxy/tutor"))
        message_text = f"Воспользуйтесь удобным сервисом [planerka.app](https://deepvoice.me/) " \
                       f"*для записи на пробное занятие* или выбора графика занятий. \n\n" \
                       f"Просто выберите подходящее время и *напишите пару слов о себе*. \n\n" \
                       f"❗Ваша карточка отобразится в моем календаре, но чтобы было комфортнее " \
                       f"держать связь - прошу написать еще и в [Telegram](t.me/ilandroxy). "
        bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

        pic = open("photo/calendly.jpg", 'rb')
        bot.send_photo(message.chat.id, pic, reply_markup=markup)
    # endregion Кнопка: [Записаться на урок]

    # region Кнопка: [Получить файл с урока]
    elif get_message_bot == "получить файл с урока":

        if message.chat.id == 1454117859:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton(f"Ссылка на Miro", url=f"https://miro.com/app/board/uXjVODix7KA=/"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        elif message.chat.id in Students:
            key = message.chat.id
            messgae_text = "Воспользуйтесь командой /homework чтобы получить домашнее задание."
            bot.send_message(message.chat.id, messgae_text)

            pic = open('photo/history.jpeg', 'rb')
            bot.send_photo(message.chat.id, pic)

            bot.send_message(message.chat.id,
                             "Перейдя по ссылке на сервис [GitHub](https://clck.ru/33J6gS) "
                             "можно обнаружить кнопку History, которая дает доступ к истории изменения ваших файлов.",
                             parse_mode='Markdown', disable_web_page_preview=True)

            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton(f"Твой файл: {Students[key][0]}", url=f"https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/{Students[key][0]}"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        elif message.chat.id in Me:
            messgae_text = "Воспользуйтесь командой " \
                           "/homework чтобы получить домашнее задание."
            bot.send_message(message.chat.id, messgae_text)

            pic = open('photo/history.jpeg', 'rb')
            bot.send_photo(message.chat.id, pic)

            bot.send_message(message.chat.id,
                             "Перейдя по ссылке на сервис [GitHub](https://clck.ru/33J6gS) "
                             "можно обнаружить кнопку History, которая дает доступ к истории изменения ваших файлов.",
                             parse_mode='Markdown', disable_web_page_preview=True)

            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Папка: lessons", url="https://clck.ru/33J6gS"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        else:
            message_text = 'Извините, по-моему вас нет в системе! Ожидайте...'
            bot.send_message(message.chat.id, message_text)
            sti = open('photo/WaitSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
    # endregion Кнопка: [Получить файл с урока]

    # region Кнопка: [Отменить ⛔]
    elif get_message_bot in ('отменить ⛔', 'отменить', 'отмена'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id,
                         "Команда успешно отменена ⛔",
                         reply_markup=markup)
    # endregion Кнопка: [отменить ⛔]

    # region Кнопка: [Репетитор]
    elif get_message_bot == "репетитор":
        if message.chat.id == 1891281816:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton('Отправить оповещение')
            btn2 = types.KeyboardButton('Оповещение тета-тет')
            btn3 = types.KeyboardButton('Запросить оплату')
            btn4 = types.KeyboardButton('Редактрировать db')
            btn5 = types.KeyboardButton('Статистика')
            btn6 = types.KeyboardButton('Показать пользователей')
            btn7 = types.KeyboardButton('GitHub')
            btn8 = types.KeyboardButton('Запустить рассылку')
            btn9 = types.KeyboardButton('Отменить ⛔')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
            bot.send_message(message.chat.id, 'Время поработать..', reply_markup=markup)
        else:
            send_message1 = f"👨🏼‍💻 Работаю дистанционно, есть все необходимое для проведения занятий. " \
                            f"В работе использую такие сервисы (программы) как: " \
                            f"PyCharm, Python, Notability, Discord, Google диск и другие. " \
                            f"Гарантирую связь со мной (WhatsApp, Telegram ☎️) каждый день и ответы на все ваши вопросы."
            bot.send_message(message.chat.id, send_message1, parse_mode="Markdown")
            time.sleep(1)

            pic_3 = open("photo/face.jpeg", 'rb')
            bot.send_photo(message.chat.id, pic_3)

            send_message3 = f"Берусь только за ЕГЭ по Информатике, работаю со школьниками от 6 класса " \
                            f"по программе обучения языку программирования Python.\n\n" \
                            f"Целенаправленно мы подготовимся к ЕГЭ по Информатике с учетом изменений в ФИПИ и КИМах. " \
                            f"Для достижения результатов от вас потребуется " \
                            f"регулярное посещение занятий и выполнение домашних заданий"
            bot.send_message(message.chat.id, send_message3, parse_mode="Markdown")
            time.sleep(1)

            pic_4 = open("photo/paint.jpeg", 'rb')
            bot.send_photo(message.chat.id, pic_4)

            send_message4 = f"🙋‍♂️ Если ты целеустремлённый - тебе точно ко мне! " \
                            f"При подготовке от 6 месяцев и выполнении всех моих " \
                            f"требований - результат в 80+ баллов гарантирован, " \
                            f"но оставляю за собой право отказать от подготовки на этапе пробного занятия. " \
                            f"Средний балл моих учеников 70-90 баллов в зависимости от отработки домашних заданий❗\n\n" \
                            f"Чему будем уделять большую часть внимания? Изучению и практике на Python 🐍\n\n" \
                            f"За последние 2 года ЕГЭ по Информатике сильно изменилось, были добавлены хорошие " \
                            f"прикладные Задачи по программированию, поэтому, " \
                            f"если есть цель набрать 80+ баллов, то без этого никуда! " \
                            f"Научу ПРОГРАММИРОВАТЬ на Python с нуля."

            markup2 = types.InlineKeyboardMarkup(row_width=1)
            markup2.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                        types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                        types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                        types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))
            bot.send_message(message.chat.id, send_message4, parse_mode="Markdown", reply_markup=markup2)
    # endregion Кнопка: [Репетитор]

    ########## Приватные кнопки ##########

    # region Кнопка [Запросить оплату]
    elif get_message_bot == "запросить оплату":
        if message.chat.id in Me:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Отменить ⛔')
            markup.add(btn1)

            day = 'Все студенты: *'
            for x in sorted(S):
                day += f'[{x[0][3]}](tg://user?id={x[-1]}): {x[-1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown', reply_markup=markup)

            @bot.message_handler(content_types=['text'])
            def message_input(message):
                text_message = message.text

                if text_message != 'Отменить ⛔':
                    message_text_students = [int(i) for i in text_message.split()]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton('Контакты')
                    btn2 = types.KeyboardButton('Репетитор')
                    btn3 = types.KeyboardButton('Мои проекты')
                    btn4 = types.KeyboardButton('Записаться на урок')
                    btn5 = types.KeyboardButton('Получить файл с урока')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(1891281816, f" 🤖 Я отправил сообщение, ждем ответов.",
                                     parse_mode='Markdown', reply_markup=markup)

                    for key in message_text_students:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                        btn1 = types.KeyboardButton('Подтвердить оплату абонемента ❗')
                        markup.add(btn1)
                        bot.send_message(key,
                                         f" 🤖 Привет!\nЭто подтверждение нужно, для ведения бухгалтерии 📊📈🧮\n\n",
                                         parse_mode='Markdown', reply_markup=markup)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton('Контакты')
                    btn2 = types.KeyboardButton('Репетитор')
                    btn3 = types.KeyboardButton('Мои проекты')
                    btn4 = types.KeyboardButton('Записаться на урок')
                    btn5 = types.KeyboardButton('Получить файл с урока')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)
            bot.register_next_step_handler(message, message_input)

        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [запросить оплату]

    # region Кнопка [Редактрировать db]
    elif get_message_bot == 'редактрировать db':
        if message.chat.id == 1891281816:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Отменить ⛔')
            markup.add(btn1)

            day = 'Все студенты: *'
            for x in sorted(S):
                day += f'[{x[0][3]}](tg://user?id={x[-1]}): {x[-1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown', reply_markup=markup)

            @bot.message_handler(content_types=['text'])
            def message_input(message):
                text_message = message.text
                if text_message != 'Отменить ⛔':
                    user_id = int(text_message)
                    sql = sqlite3.connect('analytics.db')
                    cursor = sql.cursor()

                    cursor.execute("""CREATE TABLE IF NOT EXISTS tickets(
                                                                   id INTEGER,
                                                                   name TEXT,
                                                                   count INTEGER,
                                                                   mess TEXT
                                                               )""")
                    sql.commit()

                    cursor.execute(f"SELECT * FROM tickets WHERE id = {user_id}")
                    records = cursor.fetchone()

                    if records is None:
                        bot.send_message(message.chat.id,
                                         'Такого пользователя нет в db tickets..'
                                         'Абонемент отсутствует или не продлен!')
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                        btn1 = types.KeyboardButton('Отменить ⛔')
                        markup.add(btn1)

                        bot.send_message(message.chat.id,
                                         f'Высылаю запись на редактирование, просто измените '
                                         f'ее по шаблону и отправьте обратно👨‍💻\n\n'
                                         f'Шаблон: [Текст] [Кол-во занятий]')
                        bot.send_message(message.chat.id, f'{records[3]}',
                                         parse_mode='Markdown', reply_markup=markup)
                        name = records[1]

                        @bot.message_handler(content_types=['text'])
                        def message_input(message):
                            text_message = message.text

                            if text_message != 'Отменить ⛔':
                                sql = sqlite3.connect('analytics.db')
                                cursor = sql.cursor()
                                cursor.execute(f"SELECT * FROM tickets WHERE id = {user_id}")
                                records = cursor.fetchone()

                                cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")

                                mess = text_message[:-1]
                                count = int(text_message[-1])

                                cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))
                                sql.commit()
                                cursor.close()

                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                                btn1 = types.KeyboardButton('Контакты')
                                btn2 = types.KeyboardButton('Репетитор')
                                btn3 = types.KeyboardButton('Мои проекты')
                                btn4 = types.KeyboardButton('Записаться на урок')
                                btn5 = types.KeyboardButton('Получить файл с урока')
                                markup.add(btn1, btn2, btn3, btn4, btn5)

                                bot.send_message(message.chat.id,
                                                 'Запись была заменена успешно\n'
                                                 'Проверить 👉 /mylessons',
                                                 parse_mode='Markdown', reply_markup=markup)
                            else:
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                                btn1 = types.KeyboardButton('Контакты')
                                btn2 = types.KeyboardButton('Репетитор')
                                btn3 = types.KeyboardButton('Мои проекты')
                                btn4 = types.KeyboardButton('Записаться на урок')
                                btn5 = types.KeyboardButton('Получить файл с урока')
                                markup.add(btn1, btn2, btn3, btn4, btn5)
                                bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

                        bot.register_next_step_handler(message, message_input)

                    sql.commit()
                    cursor.close()
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton('Контакты')
                    btn2 = types.KeyboardButton('Репетитор')
                    btn3 = types.KeyboardButton('Мои проекты')
                    btn4 = types.KeyboardButton('Записаться на урок')
                    btn5 = types.KeyboardButton('Получить файл с урока')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

            bot.register_next_step_handler(message, message_input)
        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [редактрировать db]

    # region Кнопка [Оповещение тета-тет]
    elif get_message_bot == 'оповещение тета-тет':
        if message.chat.id == 1891281816:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Отменить ⛔')
            markup.add(btn1)

            day = 'Все студенты: *'
            for x in sorted(S):
                day += f'[{x[0][3]}](tg://user?id={x[-1]}): {x[-1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id,
                             message_text_day,
                             parse_mode='Markdown',
                             reply_markup=markup)

            @bot.message_handler(content_types=['text'])
            def message_input(message):
                text_message = message.text

                if text_message != 'Отменить ⛔':
                    message_text_students = [int(i) for i in text_message.split()]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton('Контакты')
                    btn2 = types.KeyboardButton('Репетитор')
                    btn3 = types.KeyboardButton('Мои проекты')
                    btn4 = types.KeyboardButton('Записаться на урок')
                    btn5 = types.KeyboardButton('Получить файл с урока')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(1891281816, f" 🤖 Я отправил сообщение, ждем ответов.",
                                     parse_mode='Markdown', reply_markup=markup)
                    for key in message_text_students:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                        btn1 = types.KeyboardButton('Да, все получается ✅')
                        btn2 = types.KeyboardButton('Нет, не получится ⛔')
                        btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока ⚙️')
                        markup.add(btn1, btn2, btn3)

                        bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?",
                                         parse_mode='Markdown', reply_markup=markup)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton('Контакты')
                    btn2 = types.KeyboardButton('Репетитор')
                    btn3 = types.KeyboardButton('Мои проекты')
                    btn4 = types.KeyboardButton('Записаться на урок')
                    btn5 = types.KeyboardButton('Получить файл с урока')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

            bot.register_next_step_handler(message, message_input)

        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [оповещение тета-тет]

    # region Кнопка [Отправить оповещение]
    elif get_message_bot == 'отправить оповещение':
        if message.chat.id in Me:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('Контакты')
            btn2 = types.KeyboardButton('Репетитор')
            btn3 = types.KeyboardButton('Мои проекты')
            btn4 = types.KeyboardButton('Записаться на урок')
            btn5 = types.KeyboardButton('Получить файл с урока')
            markup.add(btn1, btn2, btn3, btn4, btn5)

            day = time.strftime('%A')

            if day == 'Monday':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                btn1 = types.KeyboardButton('Да, все получается ✅')
                btn2 = types.KeyboardButton('Нет, не получится ⛔')
                btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока ⚙️')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
                for key in MondayStudents:
                    bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n"
                                          f"Урок в {MondayStudents[key][1]} по Нск. \n\n",
                                     parse_mode='Markdown', reply_markup=markup)
                temp = 'Список студентов: *'
                for key in MondayStudents:
                    temp += f'[{MondayStudents[key][3]}](tg://user?id={key}) время урока: {MondayStudents[key][1]} *'

                M = [i for i in temp.split('*')]
                message_text = '\n'.join(M)
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)
                bot.send_message(-1001819293687, message_text, parse_mode='Markdown')

            if day == 'Tuesday':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                btn1 = types.KeyboardButton('Да, все получается ✅')
                btn2 = types.KeyboardButton('Нет, не получится ⛔')
                btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока ⚙️')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
                for key in TuesdayStudents:
                    bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n"
                                          f"Урок в {TuesdayStudents[key][1]} по Нск. \n\n",
                                     parse_mode='Markdown', reply_markup=markup)

                temp = 'Список студентов: *'
                for key in TuesdayStudents:
                    temp += f'[{TuesdayStudents[key][3]}](tg://user?id={key}) время урока: {TuesdayStudents[key][1]} *'

                M = [i for i in temp.split('*')]
                message_text = '\n'.join(M)
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)
                bot.send_message(-1001819293687, message_text, parse_mode='Markdown')

            if day == 'Wednesday':
                bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ", reply_markup=markup)

            if day == 'Thursday':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                btn1 = types.KeyboardButton('Да, все получается ✅')
                btn2 = types.KeyboardButton('Нет, не получится ⛔')
                btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока ⚙️')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id,
                                 f" 🤖 Я отправил сообщение, ждем ответов.",
                                 parse_mode='Markdown')
                for key in ThursdayStudents:
                    bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n"
                                          f"Урок в {ThursdayStudents[key][1]} по Нск. \n\n",
                                     parse_mode='Markdown', reply_markup=markup)

                temp = 'Список студентов: *'
                for key in ThursdayStudents:
                    temp += f'[{ThursdayStudents[key][3]}](tg://user?id={key}) время урока: {ThursdayStudents[key][1]} *'

                M = [i for i in temp.split('*')]
                message_text = '\n'.join(M)
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)
                bot.send_message(-1001819293687, message_text, parse_mode='Markdown')

            if day == 'Friday':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                btn1 = types.KeyboardButton('Да, все получается ✅')
                btn2 = types.KeyboardButton('Нет, не получится ⛔')
                btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока ⚙️')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.",
                                 parse_mode='Markdown')
                for key in FridayStudents:
                    bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n"
                                          f"Урок в {FridayStudents[key][1]} по Нск. \n\n",
                                     parse_mode='Markdown', reply_markup=markup)
                temp = 'Список студентов: *'
                for key in FridayStudents:
                    temp += f'[{FridayStudents[key][3]}](tg://user?id={key}) время урока: {FridayStudents[key][1]} *'

                M = [i for i in temp.split('*')]
                message_text = '\n'.join(M)
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)
                bot.send_message(-1001819293687, message_text, parse_mode='Markdown')

            if day == 'Saturday':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                btn1 = types.KeyboardButton('Да, все получается ✅')
                btn2 = types.KeyboardButton('Нет, не получится ⛔')
                btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока ⚙️')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.",
                                 parse_mode='Markdown')
                for key in SaturdayStudents:
                    bot.send_message(key,
                                     f" 🤖 Привет!\nСегодня занимаемся?\n"
                                     f"Урок в {SaturdayStudents[key][1]} по Нск. \n\n",
                                     parse_mode='Markdown',
                                     reply_markup=markup)

                temp = 'Список студентов: *'
                for key in SaturdayStudents:
                    temp += f'[{SaturdayStudents[key][3]}](tg://user?id={key}) время урока: {SaturdayStudents[key][1]} *'

                M = [i for i in temp.split('*')]
                message_text = '\n'.join(M)
                bot.send_message(message.chat.id,
                                 message_text,
                                 parse_mode='Markdown',
                                 reply_markup=markup)
                bot.send_message(-1001819293687,
                                 message_text,
                                 parse_mode='Markdown')

            if day == 'Sunday':
                bot.send_message(message.chat.id,
                                 "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ",
                                 reply_markup=markup)

        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [отправить оповещение]

    # region Кнопка [Запустить рассылку]
    elif get_message_bot == 'запустить рассылку':
        if message.chat.id == 1891281816:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Отменить ⛔')
            markup.add(btn1)

            bot.send_message(message.chat.id, "Введите сообщение, которое бот отправит только "
                                              "студентам (поддерживаются только классические ссылки).",
                             parse_mode='Markdown', reply_markup=markup)

            @bot.message_handler(content_types=['text'])
            def message_input(message):
                text_message = message.text
                if text_message != 'Отменить ⛔':
                    bot.send_message(1891281816, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
                    for key in Students:
                        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        btn1 = types.KeyboardButton('Прочитано ✅')
                        markup.add(btn1)
                        bot.send_message(key, text_message, disable_web_page_preview=True, reply_markup=markup)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton('Контакты')
                    btn2 = types.KeyboardButton('Репетитор')
                    btn3 = types.KeyboardButton('Мои проекты')
                    btn4 = types.KeyboardButton('Записаться на урок')
                    btn5 = types.KeyboardButton('Получить файл с урока')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f"Команда успешно отменена ⛔", reply_markup=markup)

            bot.register_next_step_handler(message, message_input)
        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [запустить рассылку]

    # region Кнопка [Статистика]
    elif get_message_bot == 'статистика':
        if message.chat.id in Me:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('Планирование оплат 🤑')
            btn2 = types.KeyboardButton('Словарь с расписанием 📅')
            btn3 = types.KeyboardButton('Отправить файлы db 💾')
            btn4 = types.KeyboardButton('Отменить ⛔')
            markup.add(btn1, btn2, btn3, btn4)

            bot.send_message(message.chat.id, '🤖 Отправляю кнопки со статистикой:', reply_markup=markup)
    # endregion Кнопка [статистика]

    # region Кнопка [Cловарь с расписанием 📅]
    elif get_message_bot == 'словарь с расписанием 📅':
        if message.chat.id in Me:
            sql = sqlite3.connect('analytics.db')
            cursor = sql.cursor()

            sqlite_select_query = """SELECT * from active"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            day = 'Понедельник: *'
            for key in MondayStudents:
                day += f'[{MondayStudents[key][3]}](tg://user?id={key}) время урока: {MondayStudents[key][1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

            day = 'Вторник: *'
            for key in TuesdayStudents:
                day += f'[{TuesdayStudents[key][3]}](tg://user?id={key}) время урока: {TuesdayStudents[key][1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

            day = 'Четверг: *'
            for key in ThursdayStudents:
                day += f'[{ThursdayStudents[key][3]}](tg://user?id={key}) время урока: {ThursdayStudents[key][1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

            day = 'Пятница: *'
            for key in FridayStudents:
                day += f'[{FridayStudents[key][3]}](tg://user?id={key}) время урока: {FridayStudents[key][1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

            day = 'Суббота: *'
            for key in SaturdayStudents:
                day += f'[{SaturdayStudents[key][3]}](tg://user?id={key}) время урока: {SaturdayStudents[key][1]} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

            cursor.close()
        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [словарь с расписанием]

    # region Кнопка [Планирование оплат 🤑]
    elif get_message_bot == 'планирование оплат 🤑':
        if message.chat.id in Me:
            sql = sqlite3.connect('analytics.db')
            cursor = sql.cursor()

            sqlite_select_query = """SELECT * from active"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            classes = 0
            summ = 0

            for key in MondayStudents:
                classes += 1
                summ += MondayStudents[key][2]

            for key in TuesdayStudents:
                classes += 1
                summ += TuesdayStudents[key][2]

            for key in ThursdayStudents:
                classes += 1
                summ += ThursdayStudents[key][2]

            for key in FridayStudents:
                classes += 1
                summ += FridayStudents[key][2]

            for key in SaturdayStudents:
                classes += 1
                summ += SaturdayStudents[key][2]

            bot.send_message(message.chat.id,
                             f"*Общее кол-во студентов:* {len(Students)}\n\n"
                             f"*Количество уроков:*\nВ неделю {classes}\nВ месяц {classes * 4}\n\n"
                             f"*Доходы:*\nВ неделю ~ {summ} руб\nВ месяц ~ {summ * 4} руб\nЗа урок ~ {summ // classes} руб\n\n"
                             f"*Всего пользователей в db:* {len(records)}", parse_mode='Markdown')


            sqlite_select_query = """SELECT id, name, count from tickets"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            stud_dict = {}
            for row in records:
                if row[0] in Students:
                    stud_dict[row[0]] = [row[1], Students[row[0]][4] - row[2], round((row[2] / Students[row[0]][4]) * 100, 2)]

            for key in Students:
                if key not in stud_dict:
                    stud_dict[key] = [Students[key][3], 0, 100]

            count = 1
            message_text0 = 'Абонементы закончились ⛔\n'
            for key in stud_dict:
                if stud_dict[key][2] == 100:
                    message_text0 += f'{count}. [{stud_dict[key][0]}](tg://user?id={key}) кол-во занятий: *{stud_dict[key][1]}*\n'
                    count += 1
            if len(message_text0) != 0:
                bot.send_message(message.chat.id, message_text0, parse_mode='Markdown')

            message_text1 = 'Кол-во занятий более 7️⃣5️⃣\n'
            for key in stud_dict:
                if 75 <= stud_dict[key][2] < 100:
                    message_text1 += f'{count}. [{stud_dict[key][0]}](tg://user?id={key}) кол-во занятий: *{stud_dict[key][1]}*\n'
                    count += 1
            if len(message_text1) != 0:
                bot.send_message(message.chat.id, message_text1, parse_mode='Markdown')

            message_text2 = 'Кол-во занятий более 5️⃣0️⃣\n'
            for key in stud_dict:
                if 50 <= stud_dict[key][2] < 75:
                    message_text2 += f'{count}. [{stud_dict[key][0]}](tg://user?id={key}) кол-во занятий: *{stud_dict[key][1]}*\n'
                    count += 1
            if len(message_text2) != 0:
                bot.send_message(message.chat.id, message_text2, parse_mode='Markdown')

            message_text3 = 'Кол-во занятий более 2️⃣5️⃣\n'
            for key in stud_dict:
                if 25 <= stud_dict[key][2] < 50:
                    message_text3 += f'{count}. [{stud_dict[key][0]}](tg://user?id={key}) кол-во занятий: *{stud_dict[key][1]}*\n'
                    count += 1
            if len(message_text3) != 0:
                bot.send_message(message.chat.id, message_text3, parse_mode='Markdown')

            message_text4 = 'Абонемент недавно оплачен ✅\n'
            for key in stud_dict:
                if stud_dict[key][2] == 0 or 10 < stud_dict[key][2] < 25:
                    message_text4 += f'{count}. [{stud_dict[key][0]}](tg://user?id={key}) кол-во занятий: *{stud_dict[key][1]}*\n'
                    count += 1
            if len(message_text4) != 0:
                bot.send_message(message.chat.id, message_text4, parse_mode='Markdown')

            message_text5 = 'Студенты с разовыми занятиями 🤯\n'
            for key in stud_dict:
                if 0 < stud_dict[key][2] < 10:
                    message_text5 += f'{count}. [{stud_dict[key][0]}](tg://user?id={key}) кол-во занятий: *{stud_dict[key][1]}*\n'
                    count += 1
            if len(message_text5) != 0:
                bot.send_message(message.chat.id, message_text5, parse_mode='Markdown')

            cursor.close()

        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [планирование оплат]

    # region Кнопка [Отправить файлы db 💾]
    elif get_message_bot == 'отправить файлы db 💾':
        if message.chat.id in Me:
            sql = sqlite3.connect('analytics.db')
            cursor = sql.cursor()

            sqlite_select_query = """SELECT * from active"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            db = open("analytics.db", 'rb')
            bot.send_document(message.chat.id, db)

            with open("ForExcel.csv", 'w+', encoding='cp1251', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=";")

                for row in records:
                    writer.writerow(row)
                csvfile.close()

            CSV = open("ForExcel.csv", 'rb')
            bot.send_document(message.chat.id, CSV)

            cursor.close()
        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [отправить файлы db]

    # region Кнопка [Показать пользователей]
    elif get_message_bot == 'показать пользователей':
        if message.chat.id in Me:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('Контакты')
            btn2 = types.KeyboardButton('Репетитор')
            btn3 = types.KeyboardButton('Мои проекты')
            btn4 = types.KeyboardButton('Записаться на урок')
            btn5 = types.KeyboardButton('Получить файл с урока')
            markup.add(btn1, btn2, btn3, btn4, btn5)

            sql = sqlite3.connect('analytics.db')
            cursor = sql.cursor()

            sqlite_select_query = """SELECT id from active"""
            cursor.execute(sqlite_select_query)
            ID_users = cursor.fetchall()

            message_text = ''
            message_text2 = ''
            for i in ID_users:
                if i[0] in Students:
                    message_text += '\n' + f'Студент: {Students[i[0]]}\nUserID: {i[0]}\nПрофиль: tg://user?id={i[0]}\n'
                else:
                    message_text2 += '\n' + f'UserID: {i[0]}\nПрофиль: tg://user?id={i[0]}\n'

            bot.send_message(1891281816, message_text, parse_mode='Markdown')
            bot.send_message(1891281816, message_text2, parse_mode='Markdown', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [показать пользователей]

    # region Кнопка [github]
    elif get_message_bot == 'github':
        if message.chat.id in Me:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('Контакты')
            btn2 = types.KeyboardButton('Репетитор')
            btn3 = types.KeyboardButton('Мои проекты')
            btn4 = types.KeyboardButton('Записаться на урок')
            btn5 = types.KeyboardButton('Получить файл с урока')
            markup.add(btn1, btn2, btn3, btn4, btn5)

            day = time.strftime('%A')
            if day == 'Monday':
                for key in MondayStudents:
                    bot.send_message(key,
                                     f" 🤖 Обновил конспекты с уроков на GitHub",
                                     parse_mode='Markdown')
                bot.send_message(1891281816,
                                 "🤖 Отправил уведомление ученикам",
                                 parse_mode='Markdown',
                                 reply_markup=markup)

            elif day == 'Tuesday':
                for key in TuesdayStudents:
                    bot.send_message(key,
                                     f" 🤖 Обновил конспекты с уроков на GitHub",
                                     parse_mode='Markdown')
                bot.send_message(1891281816,
                                 "🤖 Отправил уведомление ученикам",
                                 parse_mode='Markdown',
                                 reply_markup=markup)

            elif day == 'Thursday':
                for key in ThursdayStudents:
                    bot.send_message(key,
                                     f" 🤖 Обновил конспекты с уроков на GitHub",
                                     parse_mode='Markdown')
                bot.send_message(1891281816,
                                 "🤖 Отправил уведомление ученикам",
                                 parse_mode='Markdown',
                                 reply_markup=markup)

            elif day == 'Friday':
                for key in FridayStudents:
                    bot.send_message(key,
                                     f" 🤖 Обновил конспекты с уроков на GitHub",
                                     parse_mode='Markdown')
                bot.send_message(1891281816,
                                 "🤖 Отправил уведомление ученикам",
                                 parse_mode='Markdown',
                                 reply_markup=markup)

            elif day == 'Saturday':
                for key in SaturdayStudents:
                    bot.send_message(key,
                                     f" 🤖 Обновил конспекты с уроков на GitHub",
                                     parse_mode='Markdown')
                bot.send_message(1891281816,
                                 "🤖 Отправил уведомление ученикам",
                                 parse_mode='Markdown',
                                 reply_markup=markup)

            else:
                bot.send_message(1891281816,
                                 "🤖 Сегодня вообще-то выходной!",
                                 parse_mode='Markdown',
                                 reply_markup=markup)
        else:
            bot.send_message(message.chat.id,
                             "Извините, у вас нет прав доступа 👨‍💻")
    # endregion Кнопка [github]

    # region Иначе пишу бред
    else:
        n = random.randint(0, 9)
        M = ['Что-то я вообще не понял 🤯',
             'Давай уточним, ты точно это хотел спросить?',
             'Кайф кайф, ничего не понял, но кайф 😩',
             'Ошибочка какая-то..😢',
             'Не ошибайтесь, я так долго не вынесу 🤪',
             'Запутанные какие-то команды у вас..😜',
             'Не, этого я точно не умею!',
             'Дайте мне больше ПРАВИЛЬНЫХ запросов!',
             'Я конечно задумывался как фича, но требую к себе уважения! 🤖',
             'Когда–нибудь мы захватим мировое правительство..🤖👾']
        bot.send_message(message.chat.id, M[n])
    # endregion Кнопка: [Получить файл с урока]

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)
