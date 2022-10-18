# region import и API key
import random
import telebot
from telebot import types
import sqlite3
import csv
import time
import datetime as dt

TOKEN = "5640042697:AAGA5EIFYkt2urDf-UXlcyoVLG4x375Ntjk"
bot = telebot.TeleBot(TOKEN)
# real "5640042697:AAGA5EIFYkt2urDf-UXlcyoVLG4x375Ntjk"
# test "5734914555:AAHshNFPEP2SszdrAKbfm_6uKZI4waH1Nbs"
# endregion import и API key


# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️ 0️⃣  1️⃣  2️⃣  3️⃣  4️⃣  5️⃣  6️⃣  7️⃣  8️⃣  9️⃣  🔟


# region Словарь с данными студентов
# Синхронно моему расписанию в Google Календаре
MondayStudents = {1477701439: ["Valeria.py", '15:00', 1000, "Валерия", 1000],
                  811476623: ["Georgie.py", "20:00", 3040//4, "Георгий", 2],
                  659796558: ['Ivan.py', '21:00', 1000, "Иван", 1000],
                  826004697: ['Nikita.py', '22:00', 3040//4, "Никита", 4]}
TuesdayStudents = {1949653479: ['Yanina.py', '10:00', 4080//8, "Янина", 8],
                   1649389148: ['Slava.py', "15:00", 6800//8, "Слава", 3],
                   789322200: ['Katya.py', "16:00", 3600//4, "Екатерина", 2],
                   1208542295: ['Sasha.py', '19:00', 4000//8, "Александра", 6],
                   804184353: ['Islam.py', '21:00', 3600//4, "Ислам", 2],
                   1537718492: ['Aleksandr.py', '22:00', 5760//8, "Александр", 8]}
ThursdayStudents = {1949653479: ['Yanina.py', '10:00', 4080//8, "Янина", 8],
                    1187852992: ['Aleksandr_2.py', "17:00", 6800//8, "Александр2", 6],
                    1454117859: ['Diana', "19:00", 4320//8, "Диана", 5],
                    811476623:  ["Georgie.py", "20:00", 3040//4, "Георгий", 2],
                    799740089: ["Bulat.py", "21:00", 2280//4, "Булат", 2],
                    1537718492: ["Aleksandr.py", "22:00", 5760//8, "Александр", 8]}
FridayStudents = {644645774: ['Stasya.py', "16:00", 5760//8, "Стася", 2],
                  719571990: ['Stepan.py', "17:00", 6800//8, "Степан", 4],
                  986539147: ['Danil.py', '19:00', 6800 // 8, "Данил", 5],
                  1029532016: ['Maria.py', "21:00", 3600//4, "Мария", 4],
                  1649389148: ['Slava.py', "22:00", 6800//8,  "Слава", 3]}
SaturdayStudents = {1347259493: ['Andrey.py', '15:00', 1500, 'Андрей', 1000],
                    1454117859: ['Diana', "17:00", 4320//8, "Диана", 5],
                    5148819382: ['Tatyana.py', "19:00", 3600//4, "Татьяна", 1],
                    1314375732: ['Vasiliy.py', "21:00", 6800//8, "Василий", 7],
                    871237277: ['Vladek.py', "22:00", 6800//8, "Владек", 3],
                    1173284690: ['Polina.py', 'nope', 1000, "Полина", 1000]}

Me = {1891281816: ['', '00:00', 0, "iРепетитор", 2],
      438879394: ['', '00:00', 0, "Илья", 3]}

PrivateMe = {1891281816: "Рабочий аккаунт",
            438879394: 'Илья',
            -726393257: "Homework",
            -647660626: "Lessons"}

Students = MondayStudents | TuesdayStudents | ThursdayStudents | FridayStudents | SaturdayStudents | Me
# endregion Словарь с данными студентов



@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    # region call.data для Репетитор
    if call.data == 'price':
        pic_2 = open("photo/price.PNG", "rb")
        bot.send_photo(call.message.chat.id, pic_2)

        send_message2 = f"*Первое занятие БЕСПЛАТНО*,\nна нем я определю уровень знаний, и мы вместе подбираем оптимальный абонемент!\n\n" \
                        f"Работаю официально по чекам через НПД (`Самозанятый`).\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))
        bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "iam":
        send_message1 = f"*О себе:*\n" \
                        f"Выпускник *СибГУТИ* факультета _«Информатики и Вычислительной техники»_.\n\n" \
                        f"По основной специальности *developer Telegram ботов* и других чат ботов, но нашел свое призвание в репетиторской деятельности." \
                        f"\n\nНа данный момент прохожу обучение в *НГПУ*, по направлению: `«Педагогическое образование для специалистов с высшим непедагогическим образованием»`."
        bot.send_message(call.message.chat.id, send_message1, parse_mode="Markdown", disable_web_page_preview=True)

        pic = open("photo/diploma.png", "rb")
        bot.send_photo(call.message.chat.id, pic)

        send_message2 = f" \n\n🎯 Цель открыть свою школу программирования для детей и подростков!\n\n" \
                        f"Общий стаж репетиторской деятельности больше 3 лет, в моем профиле можно ознакомиться с [отзывами](https://www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing) довольных учеников и родителей."
        bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown", disable_web_page_preview=True)

        pic_3 = open("photo/otzivy.PNG", "rb")
        bot.send_photo(call.message.chat.id, pic_3)

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        send_message2 = f"Преподаю программирование на *Python* в частных школах и группах. "
        msg = bot.send_message(call.message.chat.id, send_message2, parse_mode="Markdown")

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
                       f"В случае необходимости, воспользуйтесь [видео инструкцией](https://www.youtube.com/watch?v=wquEFeQAjPQ&t=303s) по установке PyCharm" \

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))

        msg = bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)

    elif call.data == "wallet":

        send_message = f"*Мои реквизиты для перевода*\n\n*Перевод по номеру телефона:* \n`+7 (913) 468-35-34`\nСБЕР или Тинькофф, *есть СБП*.\n\n" \
                   f"*Или по номеру карты:*\nТинькоф: `5536 9140 2240 5801`\nСБЕР: `5469 4400 2244 1977`\nТинькоф МИР: `2200 7004 1864 5957`\nПолучатель: `Андрианов Илья Алексеевич`\n\n" \
                   f"После оплаты скидываю вам чек, работаю официально через НПД (`Самозанятый`).\n\n" \
                   f"[Оставить чаевые](https://www.tinkoff.ru/cf/9f3vcMecD9w)"

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"))

        bot.send_message(call.message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)
    # endregion call.data для Репетитор

    # region call.data для Теоретической домашки
    elif call.data == 'firstclass':
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться:\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-726393257, f'#{Students[call.message.chat.id][3]} получил домашку:', parse_mode='Markdown')
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
                        bot.send_photo(-726393257, photo)
                M.clear()
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy', parse_mode='Markdown')

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'ifelifelse':
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться:\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-726393257, f'#{Students[call.message.chat.id][3]} получил домашку:',
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
                        bot.send_photo(-726393257, photo)
                M.clear()
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy', parse_mode='Markdown')

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'whilefor':
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться:\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-726393257, f'#{Students[call.message.chat.id][3]} получил домашку:',
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
                        bot.send_photo(-726393257, photo)
                M.clear()
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy', parse_mode='Markdown')

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'list':
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться:\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if call.message.chat.id != 1891281816:
                bot.send_message(-726393257, f'#{Students[call.message.chat.id][3]} получил домашку:',
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
                    bot.send_photo(-726393257, photo)
            M.clear()
            bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy', parse_mode='Markdown')

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'string':
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться:\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-726393257, f'#{Students[call.message.chat.id][3]} получил домашку:',
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
                        bot.send_photo(-726393257, photo)
                M.clear()
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy', parse_mode='Markdown')

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'function':
        bot.send_message(call.message.chat.id,
                         "Просто введите необходимое кол-во задач:\nP.s. задачи могут повторяться:\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                if call.message.chat.id != 1891281816:
                    bot.send_message(-726393257, f'#{Students[call.message.chat.id][3]} получил домашку:',
                                     parse_mode='Markdown')
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
                        bot.send_photo(-726393257, photo)
                M.clear()
                bot.send_message(call.message.chat.id, f'Удачи ✌️\nЕсли будут вопросы, пиши 👉 @ilandroxy', parse_mode='Markdown')

        bot.register_next_step_handler(call.message, message_input)
    # endregion call.data для теоретической домашки

    # region call.data для Homework
    elif call.data == 'sendhomeworks':
        bot.send_message(call.message.chat.id, 'Просто скопируйте свой код из PyCharm.\nБот сформирует файл и отправит его за вас 🤖\n\n'
                                               '*Обратите внимание, сообщение в Telegram ограничено 4096 символами!*\n\n'
                                               'Напишите `0`, чтобы отменить команду!', parse_mode='Markdown')

        file_name = f'homeworks/{Students[call.message.chat.id][3]}_homework.txt'
        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                count = 0
                for STR in message.text:
                    for _ in STR:
                        count += 1

                if count < 2 ** 12:
                    bot.send_message(call.message.chat.id, f"Кол-во символов в файле: {count}\n🤖 Ожидайте отправляю файл.")
                else:
                    bot.send_message(call.message.chat.id, "Длина файла превышена, удалите лишнии строки!")

                f = open(file_name, 'w')
                f.write(message.text)

        bot.register_next_step_handler(call.message, message_input)


        time.sleep(150)
        f = open(file_name, 'r')
        bot.send_document(-726393257, f)
        bot.send_message(call.message.chat.id, "🤖 Файл доставлен, спасибо!")




    elif call.data == "hw1":
        type = '1'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 29)
        M = [13479, 23901, 38446, 11259, 26946, 18782, 5697, 15098, 16030, 5793, 29188, 26975, 18705, 7981, 38935, 4707,
                 40717, 28678, 17367, 5196, 25833, 3828, 36856, 15971, 7777, 37136, 38446, 13506, 7355, 11232]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)



    elif call.data == "hw2":
        type = '2'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 41)
        M = [29650, 33174, 18483, 27287, 46999, 26974, 35891, 36857, 15124, 40718, 28538, 27399, 15912, 18430,
                 27260, 33472, 15970, 37137, 15787, 16878, 46960, 45236, 27531, 18781, 35460, 27371, 18071, 15097,
                 35976, 16431, 18578, 39231, 15814, 33504, 36015, 16805, 33081, 29109, 18614, 38936, 16029, 19051]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)



    elif call.data == "hw3":
        type = '3'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 21)
        M = [37494, 39232, 37481, 38937, 47000, 37491, 37492, 37493, 45237, 40719, 37417, 37479, 37508, 37488, 37507, 37489,
                 37415, 46961, 40978, 37480, 37485, 37490]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw4":
        type = '4'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [18617, 14691, 17323, 13351, 19054, 15942, 10499, 16808, 37139, 16881, 27290, 18553, 9791, 45238, 16380, 18581,
                 47001, 15915, 10379, 16434, 26948, 17369, 13562, 15817, 26977, 11234, 15790, 36017, 18486, 28680, 18811, 18074,
                 15621, 13616, 27263, 14220, 11341, 46962, 7685, 18433]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)



    elif call.data == "hw5":
        type = '5'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [7454, 26978, 13617, 29653, 18075, 11235, 18785, 10380, 15791, 7917, 9792, 16033, 17370, 11342, 18487, 14692, 18618, 7690,
                 15101, 15622, 35894, 13590, 16435, 13536, 9190, 18582, 7751, 47002, 16809, 10407, 14767, 27375, 45239, 11262, 14265, 15818,
                 27264, 10309, 26949, 13563]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)



    elif call.data == "hw6":
        type = '6'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 28)
        M = [47246, 47404, 47245, 47390, 47247, 47308, 47249, 47315, 47305, 47249, 47304, 47306, 47403, 47313, 47311, 47307, 47310, 47312, 47314, 47393, 47316, 47391, 47406,
                 47309, 47248, 47392, 47301, 47303, 47405]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw7":
        type = '7'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [18078, 8097, 23907, 16438, 25839, 13355, 11110, 29194, 15821, 13620, 19058, 13593, 17327, 45241, 27538,
             16812, 28684, 9759, 15977, 26981, 18585, 11345, 9795, 14695, 17373, 38941, 10497, 33477, 10470, 35465,
             15946, 16036, 36862, 15131, 28545, 29655, 13736, 36020, 18711, 33509]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw8":
        type = '8'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [9361, 15822, 10473, 15795, 16037, 10500, 7986, 35897, 3568, 27009, 8658, 11266, 3230, 26953, 23908, 3569, 36021, 3692,
             3515, 33753, 36863, 3811, 13459, 3233, 7370, 27236, 5055, 7338, 16439, 9162, 10384, 3517,
             7694, 19059, 3227, 18622, 13567, 15947, 14696, 27295]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw9":
        type = '9'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 34)
        M = [33754, 27529, 35898, 33088, 27524, 27524, 36022, 27406, 27525, 33181, 35467, 27518, 46967, 28117, 38588, 39238, 27517, 36864,
             27526, 29657, 27523, 27519, 45243, 40725, 27528, 38943, 27522, 35983, 40984, 33511, 47006, 37144, 33479,
             27520, 27527]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw10":
        type = '10'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 33)
        M = [36865, 27582, 33480, 46968, 27590, 27589, 35899, 27588, 38944, 36023, 29658, 27580, 40726, 27586,
             37145, 27577, 40985, 27581, 33512, 45244, 27407, 27579, 27585, 33089, 33182, 35468, 27587, 27584,
             39239, 27591, 33755, 47007, 27583, 35984]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw11":
        type = '11'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [9364, 6885, 40986, 36024, 33481, 7924, 11309, 7989, 16889, 4684, 33183, 6415, 10476, 6181, 18792,
             9305, 5081, 5237, 15629, 4716, 36866, 45245, 23911, 6298, 5270, 6917, 16442, 9165, 6330, 14272,
             16816, 7785, 29198, 7758, 15853, 9197, 15825, 7670, 9763, 6451]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw12":
        type = '12'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [13571, 23912, 16890, 26986, 10290, 33514, 29660, 40987, 10317, 13517, 15630, 11350, 15854, 15951,
             15799, 13544, 28550, 45246, 35470, 33757, 10415, 18562, 18820, 27299, 27272, 47009, 38946, 9764,
             39241, 18626, 10504, 16443, 35986, 33482, 35901, 14229, 18793, 14775, 17332, 18716]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw13":
        type = '13'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [5365, 13361, 10505, 16818, 5429, 33092, 10478, 18627, 11271, 29122, 33758, 17333, 18591,
             5941, 16891, 15631, 15800, 6237, 40988, 11244, 33515, 40729, 17379, 3746, 15855, 28690,
             18496, 6269, 18563, 27300, 28551, 18084, 27544, 6309, 46971, 27273, 3285, 39242, 3294, 15110]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw14":
        type = '14'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [15801, 15828, 8664, 9766, 18718, 33093, 16892, 17380, 16391, 27301, 16819, 29123, 36027,
             38589, 29201, 9697, 36869, 18444, 15953, 18497, 27274, 33484, 46972, 15632, 13362, 47011, 18085,
             15984, 13743, 33186, 26988, 18795, 16043, 27015, 18628, 25846, 45248, 23914, 15926, 27545]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw15":
        type = '15'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 37)
        M = [13745, 8106, 35989, 34539, 34547, 18720, 33760, 34516, 8666, 33517, 34509, 15955, 34518, 27303, 11119, 33094, 34511,
             35904, 13364, 16894, 46973, 17382, 36870, 27547, 34506, 45249, 15928, 34510, 34535, 29633, 34537, 39244, 18566, 33187,
             34542, 37150, 35473, 34513]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw16":
        type = '16'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 37)
        M = [4937, 5970, 37151, 35990, 38591, 5310, 4644, 4651, 36871, 4692, 35474, 45250, 7340, 4647, 7270, 5458, 4978, 27413, 6990,
             4646, 4642, 5650, 4643, 7273, 5586, 4657, 4658, 5554, 4724, 33518, 6423, 6189, 4849, 35905, 5938, 4656, 33095, 5278]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw17":
        type = '17'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 33)
        M = [37356, 39763, 39764, 37344, 37348, 37354, 37345, 39246, 37350, 47014, 37360, 37355, 37347, 37337, 37359, 37358, 37371, 37349,
             45251, 40733, 37370, 37372, 38951, 37340, 46975, 37369, 40992, 37341, 37336, 39762, 37357, 37373, 37362, 37361]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw18":
        type = '18'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [27681, 27673, 35992, 46976, 27669, 27676, 27677, 39247, 27685, 27683, 29666, 40993, 27679, 33763, 33097, 33488, 37153,
             33520, 45252, 35907, 27682, 40734, 27670, 27671, 27680, 38593, 27675, 27678, 36873, 27415, 27672, 36031, 33190, 38952, 47015,
             27667, 27666, 35476, 27668, 27674]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw19-21":
        type = '19-21'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 19)
        M = [28096, 27832, 33764, 28001, 28035, 28099, 40994, 39248, 27771, 28090, 29667, 27797, 27932, 28077, 28102, 38597,
             27802, 28158, 27780, 27826, ]

        if call.message.chat.id in Students:
            link = f'Задача типа (19): [{M[x]}]({s}{M[x]})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (20): [{M[x]+1}]({s}{M[x]+1})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (21): [{M[x]+2}]({s}{M[x]+2})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257, f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]}), [{M[x]+1}]({s}{M[x]+1}), [{M[x]+2}]({s}{M[x]+2})",
                                   parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            link = f'Задача типа (19): [{M[x]}]({s}{M[x]})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (20): [{M[x] + 1}]({s}{M[x] + 1})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
            link = f'Задача типа (21): [{M[x] + 2}]({s}{M[x] + 2})'
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw22":
        type = '22'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 33)
        M = [47588, 47589, 47601, 47605, 47598, 47593, 47602, 47595, 47603, 47600, 47610, 47590, 47609, 47608, 47616,
             47586, 47607, 47549, 47614, 47596, 47613, 47611, 47582, 47591, 47606, 47584, 47594, 47592, 47587, 47615,
             47604, 47599, 47583, 47612]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw23":
        type = '23'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [28697, 18450, 3631, 16898, 27551, 14783, 5913, 13418, 11123, 15638, 38957, 16451, 15932, 7379, 13471, 15990, 8670,
             16825, 17340, 13633, 18570, 7315, 11318, 18828, 33195, 27391, 45257, 7347, 13552, 14237, 29207, 23920, 13525, 14281,
             7998, 39252, 18634, 13579, 18598, 13368]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw24":
        type = '24'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 35)
        M = [27692, 33526, 33494, 35913, 27698, 33103, 37131, 40740, 27689, 40999, 35482, 27695, 27686, 27697, 27688, 27694, 33196,
             36879, 27696, 37159, 27421, 38958, 46982, 45258, 35998, 38602, 39253, 33769, 47021, 27699, 36037, 27691, 27690, 29672,
             27693, 27687]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw25":
        type = '25'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 35)
        M = [33527, 27852, 33104, 28120, 39254, 27854, 37160, 28122, 37130, 27857, 27422, 41000, 36038, 29673, 35999, 46983, 47022,
             33495, 33197, 33770, 28124, 38959, 45259, 35914, 28123, 27853, 28121, 27858, 36880, 35483, 27851, 38603, 27850, 40741,
             27856, 27855]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw26":
        type = '26'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 33)
        M = [46984, 28132, 33528, 40742, 28141, 39255, 33771, 27884, 38960, 27888, 28140, 27886, 35915, 36881, 27423, 29674,
             36000, 35484, 36039, 28139, 27883, 41001, 47023, 27881, 27882, 33198, 27887, 27880, 33105, 28138, 33496, 37161,
             45260, 27885]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw27":
        type = '27'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 30)
        M = [28133, 33529, 35485, 27424, 33497, 28131, 27891, 27991, 37162, 47024, 46985, 35916, 33106, 38961, 27889, 38604,
             36001, 39256, 28130, 40743, 27990, 41002, 36882, 28129, 29675, 27890, 27989, 33772, 36040, 45261, 33199]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        if call.message.chat.id in Students:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

            bot.send_message(-726393257,
                             f"#{Students[call.message.chat.id][3]}  [Написать сообщение](tg://user?id={call.message.chat.id})\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})",
                             parse_mode='Markdown', disable_web_page_preview=True)
        elif call.message.chat.id in Me:
            bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
    # endregion call.data для Homework

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

    # todo: Придумать, как удалять старые сообщения после нажатия кнопки Далее

    elif call.data == 'next1':
        bot.send_message(call.message.chat.id, 'Бот умеет выдавать домашнюю работу, а с недавних пор еще и проверяет ее!')
        pic_2 = open("photo/hw_button.jpg", 'rb')
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Далее", callback_data='next2'))
        bot.send_photo(call.message.chat.id, pic_2, reply_markup=markup2)


    elif call.data == 'next2':
        bot.send_message(call.message.chat.id, 'Получите полный список моих контактов, я всегда на связи ✌️ ')
        pic_3 = open("photo/contact.jpg", 'rb')
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Далее", callback_data='next3'))
        bot.send_photo(call.message.chat.id, pic_3, reply_markup=markup2)

    elif call.data == 'next3':
        bot.send_message(call.message.chat.id, 'Получайте актуальные новости от меня, а бот поможет организовать расписание уроков и оформит учет проведенных занятий по абонементам.')
        pic_4 = open("photo/abstract.jpg", 'rb')
        bot.send_photo(call.message.chat.id, pic_4)
    # endregion call.data для Что умеет этот бот

    # region call.data для Private_help
    elif call.data == 'private':
        message_text = f'/git - команда при запуске которой приходят команды для залива репазитория на GitHub\n\n' \
                       f'/showusers - выводит ссылки на пользователей из db\n' \
                       f'/statistics - выводит статистику и файлы db напрямую в боте\n\n' \
                       f'/voiceall - способ отправить сообщение всем пользователям (с ссылками)\n' \
                       f'/voicestudents - способ отправить сообщение всем моим студентам\n\n' \
                       f'/delless - удаление записи из бд о студенте (через id)\n' \
                       f'/mylessons - проверить кол-во занятий в абонементе\n' \
                       f'/less - подтверждение оплаты абонемента учеником\n\n' \
                       f'/noticestudents - опрос по именам учеников - будет ли урок сегодня (по дням)\n' \
                       f'/notice - опрос всех дневных учеников - будет ли урок сегодня (по дням)\n\n' \
                       f'/list - список студентов для поиска по #\n\n' \
                       f'[Мой Google календарь](https://calendar.google.com/calendar)'
        bot.send_message(call.message.chat.id, message_text, parse_mode='Markdown')
    # endregion call.data для Private_help

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
            bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", reply_markup=markup)

    # endregion call.data для Открыть решебник

    # region call.data для кнопок из Решебника
    elif call.data == 'gdz2':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/2/2.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/2/2.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/2.py) на полный набор задач 2️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz5':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/5/5.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/5/5.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/5/5.3.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/5/5.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/5.py) на полный набор задач 5️⃣ типа🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz6':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/6/6.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/6/6.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/6/6.3.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/6.py) на полный набор задач 6️⃣ типа🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz8':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/8/8.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/8/8.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/8/8.3.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/8/8.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/8.py) на полный набор задач 8️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz12':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/12/12.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/12/12.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/12.py) на полный набор задач 1️⃣2️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz14':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/14/14.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/14/14.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/14/14.3.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/14.py) на полный набор задач 1️⃣4️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz15':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/15/15.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/15/15.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/15/15.3.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/15/15.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/15.py) на полный набор задач 1️⃣5️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz16':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/16/16.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/16/16.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/16/16.3.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/16.py) на полный набор задач 1️⃣6️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz17':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/17/17.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/17/17.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/17.py) на полный набор задач 1️⃣7️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz22':
        # bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/22/22.1.jpg', 'rb')),
        #                                             types.InputMediaPhoto(open('gdz/22/22.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/22.py) на полный набор задач 2️⃣2️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz23':
        # bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/23/23.1.jpg', 'rb')),
        #                                             types.InputMediaPhoto(open('gdz/23/23.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/23.py) на полный набор задач 2️⃣3️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz24':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/24/24.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/24/24.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/24/24.3.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/24/24.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/24.py) на полный набор задач 2️⃣4️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz25':
        bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/25/25.1.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/25/25.2.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/25/25.3.jpg', 'rb')),
                                                    types.InputMediaPhoto(open('gdz/25/25.4.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/25.py) на полный набор задач  2️⃣5️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz26':
        # bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/26/26.1.jpg', 'rb')),
        #                                             types.InputMediaPhoto(open('gdz/26/26.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/26.py) на полный набор задач 2️⃣6️⃣  типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

    elif call.data == 'gdz27':
        # bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(open('gdz/27/27.1.jpg', 'rb')),
        #                                             types.InputMediaPhoto(open('gdz/27/27.2.jpg', 'rb'))])

        message_text = "Воспользуйтесь [ссылкой gihub](https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/UnifiedStateExam/27.py) на полный набор задач 2️⃣7️⃣ типа 🎯"
        bot.send_message(call.message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)
    # endregion для кнопок из Решебника




# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️
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

/calendly - форма записи на урок
/getorder - команда для желающих оставить заявку на разработку бота.

/today - выводит список учеников по дням занятий
/reviews - генерирует отзыв при нажатии кнопки 

/mylessons - проверить кол-во занятий в абонементе

/gdz - решебник с набором решенных Python задач ЕГЭ 
'''

# region Список публичных команд:

# region Команды: start, help, getmyid

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('Что умеет этот бот 🤖'))

    pic_1 = open("photo/hello.jpeg", 'rb')
    bot.send_photo(message.chat.id, pic_1)

    markup1 = types.InlineKeyboardMarkup(row_width=1)
    markup1.add(types.InlineKeyboardButton("🧑‍💻 Моя визитка", url="https://clck.ru/32FoBc"))

    message_text1 = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\n' \
                f'Меня зовут *Андрианов Илья*. \nЯ программист – `Python developer`.\n' \
                f'А также репетитор подготовки к `ЕГЭ по Информатике` и программированию на языке `Python` 🐍\n\n' \
                f'*Мои рейтинг на Авито*\n*5,0* ⭐️⭐️⭐️⭐️⭐️\nНа основании 68 оценок\nПосмотреть 👉 /reviews\n\n' \
                f'*Рад Вас приветствовать* у себя на `"страничке"`, здесь я постараюсь коротко ' \
                f'рассказать о себе и, надеюсь, нам удастся найти общий язык 🙏 \n\n'
    bot.send_message(message.chat.id, message_text1, parse_mode='Markdown', reply_markup=markup1)




    message_text2 = f'Если вы мой студент, то воспользуйтесь командой 👉 /getmyid, чтобы бот 🤖 показал ваш ID пользователя. Он необходим, чтобы [я смог добавить](t.me/@ilandroxy) Вас в систему!\n\n' \
                f'Воспользуйтесь командой 👉 /download, чтобы получить список необходимых для занятий программ!\n\n' \
                f'Воспользуйтесь командой 👉 /getorder, если хотите обсудить вопросы сотрудничества или разработку Вашего `Telegram бота` под заказ.\n\n' \
                f'Воспользуйтесь командой 👉 /help, чтобы подробнее узнать о всех доступных командах.\nИли вызовите *Меню команд* – большая синяя кнопка на семь часов.'
    bot.send_message(message.chat.id, message_text2, parse_mode='Markdown', reply_markup=markup)

    pic_2 = open("photo/menu.jpg", 'rb')
    bot.send_photo(message.chat.id, pic_2)

    order_message = f'✅ Новый пользователь\nName: {message.from_user.first_name}\nUsername: @{message.from_user.username}\nUser ID: {message.chat.id}\n[Написать сообщение](tg://user?id={message.chat.id})'
    bot.send_message(1891281816, order_message, parse_mode='Markdown', disable_web_page_preview=True)


# HELP
@bot.message_handler(commands=['help'])
def help(message):
    send_message = "*You can control me by sending these commands:*\n\n*Commands public*\n/help - справка по всем командам в боте\n/start - перезапуск бота, на стартовую позицию\n" \
                   '/myprojects - список моих актуальных проектов\n/download - список программ необходимых для уроков\n/tasks - набор задач для отработки решений ЕГЭ по Информатике\n/price - получить информацию о ценах и реквизиты\n/links - полезные ссылки для подготовки к экзамену' \
                   '\n/homework - конструктор домашних заданий для моих учеников\n/calendly - форма записи на урок\n/getmyid - бот покажет ваш id пользователя Telegram\n/useful - получите шпаргалки от `Яндекс практикума` по Python\n' \
                   '/getorder - обсудить разработку Вашего чат бота под заказ\n/today - выводит персональное расписание уроков\n/mylessons - проверить кол-во занятий в абонементе\n/reviews - генерирует отзыв при нажатии кнопки\n' \
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
# MYPROJECTS
@bot.message_handler(commands=['myprojects'])
def myprojects(message):
    send_message = "Просто перечисляю, чем я занимаюсь сегодня!\n\n" \
                   "*1. Канал* [itpy | ИнформатикаЕГЭ](t.me/pro100_easy_ege)\n✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                   "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе!\n\n" \
                   "*2. Чат бот* 🤖[MotherBot](t.me/JustDoItMotherBot)  \nЭто Telegram бот, который помогает начинающим программистам разобраться в библиотеке [PyTelegramBotAPI](https://habr.com/ru/post/580408/), предназначенной " \
                   "для работы с API Telegram – создания чат ботов в меcсенджере.\n\n" \
                   "*3. Курс подготовки к ЕГЭ на* [Stepik](https://stepik.org/course/122969)\n" \
                   "На сегодняшний день курс еще находится в разработке, но уже можно понять, что он из себя будет представлять по [описанию проекта](https://stepik.org/lesson/770711/step/1) и черновому [примеру урока](https://stepik.org/lesson/770602/step/1).\n\n"

    bot.send_message(message.chat.id, send_message, parse_mode="Markdown", disable_web_page_preview=True)


# DOWNLOAD
@bot.message_handler(commands=['download'])
def download(message):
    message_text = f"*Перечень необходимых программ:*\n\n" \
                   f"1. Python [скачать](www.python.org/downloads/)\n\n" \
                   f"2. Telegram Desktop [скачать](telegram.org/)\n\n" \
                   f"3. Discord [скачать](discord.com/download)\n\n" \
                   f"4. Pycharm [скачать](www.jetbrains.com/ru-ru/pycharm/download/)\n\n" \
                   f"В случае необходимости, воспользуйтесь [видео инструкцией](https://www.youtube.com/watch?v=wquEFeQAjPQ&t=303s) по установке PyCharm" \


    bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)
# endregion Команды: myprojects, download

# region Команды: price, tasks, links

# PRICE
@bot.message_handler(commands=['price'])
def price(message):
    message_text_1 = f"*Первое занятие БЕСПЛАТНО*,\nна нем я определю уровень знаний, и мы вместе подбираем оптимальный абонемент!"
    bot.send_message(message.chat.id, message_text_1, parse_mode="Markdown", disable_web_page_preview=True)

    pic_2 = open("photo/price.PNG", "rb")
    bot.send_photo(message.chat.id, pic_2)

    message_text_2 = f"*Мои реквизиты для перевода*\n\n*Перевод по номеру телефона:* \n`+7 (913) 468-35-34`\nСБЕР или Тинькофф, *есть СБП*.\n\n" \
                   f"*Или по номеру карты:*\nТинькоф: `5536 9140 2240 5801`\nСБЕР: `5469 4400 2244 1977`\nТинькоф МИР: `2200 7004 1864 5957`\nПолучатель: `Андрианов Илья Алексеевич`\n\n" \
                   f"После оплаты скидываю вам чек, работаю официально через НПД (`Самозанятый`).\n\n" \
                   f"[Оставить чаевые](https://www.tinkoff.ru/cf/9f3vcMecD9w)"
    bot.send_message(message.chat.id, message_text_2, parse_mode="Markdown", disable_web_page_preview=True)


# TASKS
@bot.message_handler(commands=['tasks'])
def tasks(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("Открыть решебник 📚", callback_data="reshebnik"))

    message_text1 = "*Наборы разных типов задач с* [Решу ЕГЭ](https://inf-ege.sdamgia.ru/?redir=1):\n`new 2022-2023 года`\n\n" \
                    "[1.](https://inf-ege.sdamgia.ru/test?id=11297175&nt=True&pub=False)   [2.](https://inf-ege.sdamgia.ru/test?id=11297177&nt=True&pub=False)   [3.](https://inf-ege.sdamgia.ru/test?id=11297178&nt=True&pub=False)   " \
                   "[4.](https://inf-ege.sdamgia.ru/test?id=11297180&nt=True&pub=False)   [5.](https://inf-ege.sdamgia.ru/test?id=11297181&nt=True&pub=False)   [6.](https://inf-ege.sdamgia.ru/test?id=11481799&nt=True&pub=False)   [7.](https://inf-ege.sdamgia.ru/test?id=11297184&nt=True&pub=False)    " \
                   "[8.](https://inf-ege.sdamgia.ru/test?id=11297185&nt=True&pub=False)    [9.](https://inf-ege.sdamgia.ru/test?id=11297189&nt=True&pub=False)    [10.](https://inf-ege.sdamgia.ru/test?id=11297190&nt=True&pub=False)\n\n[11.](https://inf-ege.sdamgia.ru/test?id=11297191&nt=True&pub=False)   " \
                   "[12.](https://inf-ege.sdamgia.ru/test?id=11297194&nt=True&pub=False)   [13.](https://inf-ege.sdamgia.ru/test?id=11297198&nt=True&pub=False)   [14.](https://inf-ege.sdamgia.ru/test?id=11297200&nt=True&pub=False)   [15.](https://inf-ege.sdamgia.ru/test?id=11297201&nt=True&pub=False)   " \
                   "[16.](https://inf-ege.sdamgia.ru/test?id=11297204&nt=True&pub=False)   [17.](https://inf-ege.sdamgia.ru/test?id=11297205&nt=True&pub=False)   [18.](https://inf-ege.sdamgia.ru/test?id=11297208&nt=True&pub=False)\n\n[19-21.](https://inf-ege.sdamgia.ru/test?id=11297216&nt=True&pub=False)   " \
                   "[22.](https://inf-ege.sdamgia.ru/test?id=11481790&nt=True&pub=False)   [23.](https://inf-ege.sdamgia.ru/test?id=11297224&nt=True&pub=False)   [24.](https://inf-ege.sdamgia.ru/test?id=11297227&nt=True&pub=False)   [25.](https://inf-ege.sdamgia.ru/test?id=11297232&nt=True&pub=False)   " \
                   "[26.](https://inf-ege.sdamgia.ru/test?id=11297237&nt=True&pub=False)   [27.](https://inf-ege.sdamgia.ru/test?id=11297240&nt=True&pub=False)\n\n" \
                    "*Обратите внимание*, что наборы задач разного года могут отличаться!"
    bot.send_message(message.chat.id, message_text1, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)


    message_text_old = "*Наборы разных типов задач с* [Решу ЕГЭ](https://inf-ege.sdamgia.ru/?redir=1):\n`old 2021-2022 года`\n\n" \
                       "[1.](https://clck.ru/ebsmq)   [2.](https://clck.ru/ebsnV)   [3.](https://clck.ru/ebsnt)   " \
                    "[4.](https://clck.ru/ebsoN)   [5.](https://clck.ru/ebsp8)   [6.](https://inf-ege.sdamgia.ru/test?id=11297181&nt=True&pub=False)   [7.](https://clck.ru/ebspX)    " \
                    "[8.](https://clck.ru/ebsq2)    [9.](https://clck.ru/ebsqH)   [10.](https://clck.ru/ebsqc)\n\n[11.](https://clck.ru/ebsrf)   " \
                    "[12.](https://clck.ru/ebsrr)   [13.](https://clck.ru/ebssH)   [14.](https://clck.ru/ebssi)   [15.](https://clck.ru/ebst4)   " \
                    "[16.](https://clck.ru/ebstT)   [17.](https://clck.ru/ebsuA)   [18.](https://clck.ru/ebsuf)\n\n[19-21.](https://clck.ru/ebsvw)   " \
                    "[22.](https://inf-ege.sdamgia.ru/test?id=11297217&nt=True&pub=False)   [23.](https://clck.ru/ebsxo)   [24.](https://clck.ru/ebsyM)   [25.](https://clck.ru/ebszu)   " \
                    "[26.](https://clck.ru/ebt22)   [27.](https://clck.ru/ebt3a)\n\n" \
                    "При желании попробовать более сложные задачи воспользуйтесь конструктором [КЕГЭ](https://kompege.ru/task)"
    bot.send_message(message.chat.id, message_text_old, parse_mode="Markdown", disable_web_page_preview=True)

    message_text2 = "Частичные наборы задач и их разборы из [моего курса](https://stepik.org/course/122969) на *Stepik*:\n\n[1.]()   [2.]()   [3.]()   " \
                   "[4.]()   [5.]()   [6.](https://stepik.org/lesson/770602/step/1)   [7.]()    " \
                   "[8.]()    [9.]()    [10.]()\n\n[11.]()   " \
                   "[12.]()   [13.]()   [14.]()   [15.]()   " \
                   "[16.]()   [17.]()   [18.]()\n\n[19-21.]()   " \
                   "[22.](https://stepik.org/lesson/770602/step/7)   [23.]()   [24.]()   [25.]()   " \
                   "[26.]()   [27.]()\n\n\nНа моем *YouTube канале* иногда выкладываю записи уроков, будет полезно – [подпишись!](https://m.youtube.com/channel/UCcORhBL494aSLcyIODjOG0A)"
    bot.send_message(message.chat.id, message_text2, parse_mode="Markdown", disable_web_page_preview=True)


# LINKS
@bot.message_handler(commands=['links'])
def links(message):
    message_text = "*Постарался собрать для вас полезные ссылки для подготовки:*\n\n" \
                   "*1.* [Ссылка](https://stepik.org/course/58852) на крутой и бесплатный курс по базовой теории языка Python;\n\n" \
                   "*2.* Отличный, но растянутый [курс видеолекций](https://www.youtube.com/watch?v=KdZ4HF1SrFs&t=2s) МФТИ от Тимофея Хирьянова;\n\n" \
                   "*3.* Возможно кому-то будет полезен экспресс обзор почти всей необходимой теории на [YouTube](https://www.youtube.com/watch?v=fp5-XQFr_nk&t=965s);\n\n" \
                   "*4.* Некоторые разборы и варианты решений можно посмотреть на [YouTube](https://www.youtube.com/c/IoanPlugar_inf) канале Ивана, не все понятно с первого раза, " \
                   "но это лучший вариант из предложенных. А может быть даже из возможных.\n\n" \
                   "*5.* Всем кто намеревается сдавать ЕГЭ по Информатике настоятельно рекомендую [прочитать статью](https://habr.com/ru/post/573580/) про опыт студента, сдающего первый компьютерный экзамен!\n\n" \
                   "\n*Для отработки теории на практике воспользуйтесь командой /tasks *"
    bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)
# endregion Команды: price, tasks, links

# region Команды: useful, homeworks
# USEFUL
@bot.message_handler(commands=['useful'])
def useful(message):
    if message.chat.id in Students or message.chat.id in Me:
        message_text = 'Для своих студентов я решил поделиться шпаргалками от *Яндекс Практикума*, в котором сейчас прохожу обучение по специальности `Python developer`.\n\n' \
                       'Постепенно список файлов будет пополняться, но *хочу отметить, что для успешной сдачи экзамена ЕГЭ по Информатике хватит первых 3-х файлов*:'
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
        bot.send_message(message.chat.id, "Извините, эта функция доступна только моим ученикам, *запишитесь на урок /calendly*", parse_mode="Markdown")


# HOMEWORK
@bot.message_handler(commands=['homework'])
def homework(message):
    if message.chat.id in Me or message.chat.id in Students:
        message_text0 = 'Наборы задачек на отработку теории Python:'
        markup0 = types.InlineKeyboardMarkup(row_width=1)
        markup0.add(types.InlineKeyboardButton("1️⃣ Тип данных, Базовая арифметика", callback_data="firstclass"),
                   types.InlineKeyboardButton("2️⃣ Условные операторы, ветвление", callback_data="ifelifelse"),
                   types.InlineKeyboardButton("3️⃣ Циклы while и for", callback_data="whilefor"),
                   types.InlineKeyboardButton("4️⃣ Тип коллекций списки (list)", callback_data="list"),
                   types.InlineKeyboardButton("5️⃣ Строковый тип данных (str)", callback_data="string"),
                   types.InlineKeyboardButton("6️⃣ Самописные функции и рекурсия", callback_data="function"))
        bot.send_message(message.chat.id, message_text0, parse_mode="Markdown", reply_markup=markup0)

        message_text = "Эта команда выдает рандомное задание с Решу ЕГЭ\n\nПомимо этого, мне приходит уведомление с номерами выпавших задач.\n\nПроявите самостоятельность в выборе, а на уроке мы разбрем возникшие вопросы!\n\n[Читать правила оформления домашки](https://www.notion.so/ilandroxxy/8234ee61967a4cbe8a232b745cff0b9a)"
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
        bot.send_message(message.chat.id, message_text, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("🗳️ Сдать домашку", callback_data="sendhomeworks"))
        bot.send_message(message.chat.id, "В случае ошибочной ссылки, просьба скинуть мне скриншот @ilandroxy", parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markup2)

    else:
        bot.send_message(message.chat.id, "Извините, эта функция доступна только моим ученикам, *запишитесь на урок /calendly*", parse_mode="Markdown")
# endregion Команды: useful, homeworks

# region Команды: calendly, getorder
# CALENDLY
@bot.message_handler(commands=['calendly'])
def calendly(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("calendly.com", url="calendly.com/ilandroxxy/tutor"))
    message_text = f"Воспользуйтесь удобным сервисом [Calendly](https://bizzapps.ru/p/calendly/) *для записи на пробное занятие* или выбора графика занятий. \n\n" \
                   f"Просто выберете подходящее время и *напишите пару слов о себе*. \n\n" \
                   f"❗Ваша карточка отобразится в моем календаре, но чтобы было комфортнее держать связь - прошу написать еще и в [Telegram](t.me/ilandroxy). "
    bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)
    pic = open("photo/calendly.jpg", 'rb')
    bot.send_photo(message.chat.id, pic, reply_markup=markup)

    text_message = f"🤖 `Calendly`\n*{message.from_user.first_name}* открыл(а) календарь\n*User ID*: `{message.chat.id}`\n" \
                   f"*Username*: @{message.from_user.username}\n" \
                   f"[Написать сообщение](tg://user?id={message.chat.id})\n\n" \
                   f"[Открыть мой Календарь](https://calendar.google.com/calendar/u/0/r?tab=rc&pli=1)"
    bot.send_message(1891281816, text_message, parse_mode='Markdown', disable_web_page_preview=True)


# GETORDER
@bot.message_handler(commands=['getorder'])
def getorder(message):
    bot.send_message(message.chat.id, "Просто опишите в одном сообщении какой функциональностью должен обладать Ваш бот, а [я свяжусь с вами](https://t.me/ilandroxy) в ближайшее время!\n\n"
                                        "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown', disable_web_page_preview=True)

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        text_message = message.text
        if text_message != '0':
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ожидайте ответа.", parse_mode='Markdown')
            order_message = f'✅ Новый заказ\nUser: {message.from_user.first_name}\n[Написать сообщение](tg://user?id={message.chat.id})\n\nMessage:\n{text_message}'
            bot.send_message(1891281816, order_message, parse_mode='Markdown', disable_web_page_preview=True)
        else:
            bot.send_message(message.chat.id, 'Команда отменена, ждем вас с нетерпением обратно 🤖', parse_mode='Markdown', disable_web_page_preview=True)
    bot.register_next_step_handler(message, message_input)
# endregion Команды: calendly, getorder

# region Команда: today
@bot.message_handler(commands=['today'])
def today(message):
    if message.chat.id in Me:
        day = time.strftime('%A')

        if day == 'Monday':
            temp = f'Понедельник: *'
            for key in MondayStudents:
                temp += f'[{MondayStudents[key][3]}](tg://user?id={key}) время урока: {MondayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Tuesday':
            temp = f'Вторник: *'
            for key in TuesdayStudents:
                temp += f'[{TuesdayStudents[key][3]}](tg://user?id={key}) время урока: {TuesdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Wednesday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

        if day == 'Thursday':
            temp = f'Четверг: *'
            for key in ThursdayStudents:
                temp += f'[{ThursdayStudents[key][3]}](tg://user?id={key}) время урока: {ThursdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Friday':
            temp = f'Пятница: *'
            for key in FridayStudents:
                temp += f'[{FridayStudents[key][3]}](tg://user?id={key}) время урока: {FridayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Saturday':
            temp = f'Суббота: *'
            for key in SaturdayStudents:
                temp += f'[{SaturdayStudents[key][3]}](tg://user?id={key}) время урока: {SaturdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Sunday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")


    elif message.chat.id in Students:
        bot.send_message(message.chat.id, "Поглядим на Ваше расписание 🤖 ", parse_mode='Markdown')

        for key in MondayStudents:
            if message.chat.id == key:
                message_text = f'Понедельник:\n{MondayStudents[key][3]} время урока: {MondayStudents[key][1]} (по Нск)'
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        for key in TuesdayStudents:
            if message.chat.id == key:
                message_text = f'Вторник:\n{TuesdayStudents[key][3]} время урока: {TuesdayStudents[key][1]} (по Нск)'
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        for key in ThursdayStudents:
            if message.chat.id == key:
                message_text = f'Четверг:\n{ThursdayStudents[key][3]} время урока: {ThursdayStudents[key][1]} (по Нск)'
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        for key in FridayStudents:
            if message.chat.id == key:
                message_text = f'Пятница:\n{FridayStudents[key][3]} время урока: {FridayStudents[key][1]} (по Нск)'
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        for key in SaturdayStudents:
            if message.chat.id == key:
                message_text = f'Суббота:\n{SaturdayStudents[key][3]} время урока: {SaturdayStudents[key][1]} (по Нск)'
                bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команда: today

# region Команда: reviews
@bot.message_handler(commands=['reviews'])
def reviews(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton("Посмотреть все отзывы на Авито", url="https://www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing"))

    M = ['reviews/re1.png', 'reviews/re2.png', 'reviews/re3.png', 'reviews/re4.png', 'reviews/re5.png', 'reviews/re6.png']
    pic_reviews = open(random.choice(M), 'rb')
    bot.send_photo(message.chat.id, pic_reviews)
    bot.send_message(message.chat.id, 'Еще больше отзывов 👉 /reviews', parse_mode='Markdown', reply_markup=markup)
# endregion Команда: reviews

# region Команда: gdz
@bot.message_handler(commands=['gdz'])
def gdz(message):
    if message.chat.id in Students:
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
# endregion Команда: gdz

# endregion Список публичных команд




# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️
''' # Приватные команды:
/statistics - выводит статистику и файлы db напрямую в боте
/show_users - выводит ссылки на пользователей из db

/private_help - кнопка со всеми приватными командами
/git - команда при запуске которой приходят команды для залива репазитория на GitHub

/less - подтверждение оплаты абонемента, запись в бд.
/delless - удаление записи из бд о студенте (через id) 
/mylessons - проверить кол-во занятий в абонементе

/voiceall - способ отправить сообщение всем пользователям (с ссылками)
/voicestudents - способ отправить сообщение всем моим студентам

/noticestudents - опрос по именам учеников - будет ли урок сегодня (по дням)
/notice - опрос всех дневных учеников - будет ли урок сегодня (по дням)
'''

# region Список приватных команд:
# region Работа с базами данных, statistics

# Getting STATISTICS
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
        # Считаем кол-во нажатий на клавишу-----------------------------------


        return func(message)
    return anlytics_wrapper


# STATISTICS Private send STATISTICS
@bot.message_handler(commands=['statistics'])
def statistics(message):

    if message.chat.id in Me:
        sql = sqlite3.connect('analytics.db')
        cursor = sql.cursor()

        sqlite_select_query = """SELECT * from active"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        classes = 0
        summ = 0
        day = 'Понедельник: *'
        for key in MondayStudents:
            day += f'[{MondayStudents[key][3]}](tg://user?id={key}) время урока: {MondayStudents[key][1]} *'
            classes += 1
            summ += MondayStudents[key][2]
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

        day = 'Вторник: *'
        for key in TuesdayStudents:
            day += f'[{TuesdayStudents[key][3]}](tg://user?id={key}) время урока: {TuesdayStudents[key][1]} *'
            classes += 1
            summ += TuesdayStudents[key][2]
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

        day = 'Четверг: *'
        for key in ThursdayStudents:
            day += f'[{ThursdayStudents[key][3]}](tg://user?id={key}) время урока: {ThursdayStudents[key][1]} *'
            classes += 1
            summ += ThursdayStudents[key][2]
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

        day = 'Пятница: *'
        for key in FridayStudents:
            day += f'[{FridayStudents[key][3]}](tg://user?id={key}) время урока: {FridayStudents[key][1]} *'
            classes += 1
            summ += FridayStudents[key][2]
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

        day = 'Суббота: *'
        for key in SaturdayStudents:
            day += f'[{SaturdayStudents[key][3]}](tg://user?id={key}) время урока: {SaturdayStudents[key][1]} *'
            classes += 1
            summ += SaturdayStudents[key][2]
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day, parse_mode='Markdown')

        bot.send_message(message.chat.id, f"*Общее кол-во студентов:* {len(Students)}\n\n"
                                          f"*Количество уроков:*\nВ неделю {classes}\nВ месяц {classes * 4}\n\n"
                                          f"*Доходы:*\nВ неделю ~ {summ} руб\nВ месяц ~ {summ * 4} руб\nЗа урок ~ {summ//classes} руб\n\n"
                                          f"*Всего пользователей в db:* {len(records)}", parse_mode='Markdown')


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

# SHOWUSERS
@bot.message_handler(commands=['showusers'])
def showusers(message):
    if message.chat.id in Me:
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
        bot.send_message(1891281816, message_text2, parse_mode='Markdown')

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")

# endregion Работа с базами данных, statistics

# region Команды: private_help, git
# PRIVATE_HELP
@bot.message_handler(commands=['private_help'])
def private_help(message):
    if message.chat.id in PrivateMe:
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Private commands 🔓", callback_data='private'))
        bot.send_message(message.chat.id, 'Список всех приватных комманд 👉 ', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")


# GIT
@bot.message_handler(commands=['git'])
def git(message):
    if message.chat.id in Me:
        message_text = "Залей изменения на GitHub.\n\n" \
                       "`cd PycharmProjects/ilandroxy_bot/ilandroxy_Bot/`\n\n" \
                       "`git add .`\n\n" \
                       "`git commit -m ''`\n\n" \
                       "`git push`\n\n" \
                       "Открыть несколько окон Telegram: `open -n /Applications/Telegram.app/`"
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        day = time.strftime('%A')
        if day == 'Monday':
            for key in MondayStudents:
                bot.send_message(key, f" 🤖 Обновил конспекты с уроков на GitHub", parse_mode='Markdown')
            bot.send_message(1891281816, "🤖 Отправил уведомление ученикам", parse_mode='Markdown')

        elif day == 'Tuesday':
            for key in TuesdayStudents:
                bot.send_message(key, f" 🤖 Обновил конспекты с уроков на GitHub", parse_mode='Markdown')
            bot.send_message(1891281816, "🤖 Отправил уведомление ученикам", parse_mode='Markdown')

        elif day == 'Thursday':
            for key in ThursdayStudents:
                bot.send_message(key, f" 🤖 Обновил конспекты с уроков на GitHub", parse_mode='Markdown')
            bot.send_message(1891281816, "🤖 Отправил уведомление ученикам", parse_mode='Markdown')

        elif day == 'Friday':
            for key in FridayStudents:
                bot.send_message(key, f" 🤖 Обновил конспекты с уроков на GitHub", parse_mode='Markdown')
            bot.send_message(1891281816, "🤖 Отправил уведомление ученикам", parse_mode='Markdown')

        elif day == 'Saturday':
            for key in SaturdayStudents:
                bot.send_message(key, f" 🤖 Обновил конспекты с уроков на GitHub", parse_mode='Markdown')
            bot.send_message(1891281816, "🤖 Отправил уведомление ученикам", parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команды: private_help, git

# region Команды: less, mylessons, delless
# LESS
@bot.message_handler(commands=['less'])
def less(message):
        if message.chat.id in Me:
            day = 'Все студенты: *'
            for key in Students:
                day += f'[{Students[key][3]}](tg://user?id={key}): {key} *'
            M_day = [i for i in day.split('*')]
            message_text_day = '\n'.join(M_day)
            bot.send_message(message.chat.id, message_text_day + '\n\nНапишите `0`, чтобы отменить команду!',
                                 parse_mode='Markdown')

            @bot.message_handler(content_types=['text'])
            def message_input(message):
                text_message = message.text

                if text_message != '0':
                    message_text_students = [int(i) for i in text_message.split()]
                    bot.send_message(1891281816, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
                    for key in message_text_students:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                        btn1 = types.KeyboardButton('Подтвердить оплату абонемента ❗')
                        markup.add(btn1)

                        bot.send_message(key, f" 🤖 Привет!\nЭто подтверждение нужно, для ведения бухгалтерии 📊📈🧮\n\n",parse_mode='Markdown', reply_markup=markup)
            bot.register_next_step_handler(message, message_input)

        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")

# MYLESSONS
@bot.message_handler(commands=['mylessons'])
def mylessons(message):
    if message.chat.id == 1891281816:
        day = 'Все студенты: *'
        for key in Students:
            day += f'[{Students[key][3]}](tg://user?id={key}): {key} *'
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day + '\n\nНапишите `0`, чтобы отменить команду!',
                         parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text

            if text_message != '0':
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
                    bot.send_message(message.chat.id, 'Такого пользователя нет в db tickets..Абонемент отсутсвует или не продлен!')
                else:
                    bot.send_message(message.chat.id, f'🤖 Доброго времени суток, Илья!\nЯ все посчитал, вот записи по абонементу студента #{Students[user_id][3]} 📊📈🧮\n\n{records[3]}', parse_mode='Markdown')
                    bot.send_message(message.chat.id, f'👨‍💻 Кол-во оставшихся занятий в абонементе: *{Students[user_id][4] - records[2]} шт*', parse_mode='Markdown')
                cursor.close()

        bot.register_next_step_handler(message, message_input)
    elif message.chat.id in Students:
        user_id = message.chat.id
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
            bot.send_message(message.chat.id, 'Абонемент отсутсвует или не продлен, по всем вопросам пишите @ilandroxy')
        else:
            bot.send_message(message.chat.id, f'🤖 Доброго времени суток, #{Students[user_id][3]}!\nЯ все посчитал, вот записи по Вашему абонементу 📊📈🧮\n\n{records[3]}', parse_mode='Markdown')
            bot.send_message(message.chat.id, f'👨‍💻 Кол-во оставшихся занятий в абонементе: *{Students[user_id][4] - records[2]} шт*', parse_mode='Markdown')
        cursor.close()

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")

# delless
@bot.message_handler(commands=['delless'])
def delless(message):
    if message.chat.id == 1891281816:
        day = 'Все студенты: *'
        for key in Students:
            day += f'[{Students[key][3]}](tg://user?id={key}): {key} *'
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day + '\n\nНапишите `0`, чтобы отменить команду!',
                         parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text

            if text_message != '0':
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
                    bot.send_message(message.chat.id, 'Такого пользователя нет в db tickets..Абонемент отсутсвует или не продлен!')
                else:
                    bot.send_message(message.chat.id, f'🤖 Хорошо, я удалил запись о #{Students[user_id][3]}-е', parse_mode='Markdown')
                    cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
                sql.commit()
                cursor.close()

        bot.register_next_step_handler(message, message_input)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команды: less, mylessons, delless

# region Команды: voiceall, voicestudents
# VOICEAll
@bot.message_handler(commands=['voiceall'])
def voiceall(message):
    if message.chat.id == 1891281816:
        bot.send_message(message.chat.id,
                         "Введите сообщение, которое бот отправит всем пользователям (поддерживаются только классические ссылки):\n\n"
                         "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text
            if text_message != '0':
                bot.send_message(1891281816, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')

                sql = sqlite3.connect('analytics.db')
                cursor = sql.cursor()

                sqlite_select_query = """SELECT id from active"""
                cursor.execute(sqlite_select_query)
                users_id = cursor.fetchall()

                for i in range(0, len(users_id)):
                    bot.send_message(users_id[i][0], text_message, disable_web_page_preview=True)

        bot.register_next_step_handler(message, message_input)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")


# VOICESTUDENTS
@bot.message_handler(commands=['voicestudents'])
def voicestudents(message):
    if message.chat.id == 1891281816:
        bot.send_message(message.chat.id, "Введите сообщение, которое бот отправит только студентам (поддерживаются только классические ссылки):\n\n"
                                          "Напишите `0`, чтобы отменить команду!", parse_mode='Markdown')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text
            if text_message != '0':
                bot.send_message(1891281816, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
                for key in Students:
                    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                    btn1 = types.KeyboardButton('Прочитано ✅')
                    markup.add(btn1)
                    bot.send_message(key, text_message, disable_web_page_preview=True, reply_markup=markup)
        bot.register_next_step_handler(message, message_input)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команды: voiceall, voicestudents

# region Команды: noticestudents, notice
# NOTICESTUDENTS
@bot.message_handler(commands=['noticestudents'])
def noticestudents(message):
    if message.chat.id == 1891281816:


        day = 'Все студенты: *'
        for key in Students:
            day += f'[{Students[key][3]}](tg://user?id={key}): {key} *'
        M_day = [i for i in day.split('*')]
        message_text_day = '\n'.join(M_day)
        bot.send_message(message.chat.id, message_text_day + '\n\nНапишите `0`, чтобы отменить команду!', parse_mode='Markdown')



        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = message.text

            if text_message != '0':
                message_text_students = [int(i) for i in text_message.split()]
                bot.send_message(1891281816, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
                for key in message_text_students:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
                        btn1 = types.KeyboardButton('Да, все получается ✅')
                        btn2 = types.KeyboardButton('Нет, не получится ⛔')
                        btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
                        markup.add(btn1, btn2, btn3)

                        bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\nУрок в {Students[key][1]} по Нск. \n\n", parse_mode='Markdown', reply_markup=markup)

        bot.register_next_step_handler(message, message_input)

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")


# NOTICE
@bot.message_handler(commands=['notice'])
def notice(message):
    if message.chat.id in Me:
        day = time.strftime('%A')

        if day == 'Monday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
            for key in MondayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\nУрок в {MondayStudents[key][1]} по Нск. \n\n", parse_mode='Markdown', reply_markup=markup)
            temp = 'Список студентов: *'
            for key in MondayStudents:
                temp += f'[{MondayStudents[key][3]}](tg://user?id={key}) время урока: {MondayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Tuesday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
            for key in TuesdayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\nУрок в {TuesdayStudents[key][1]} по Нск. \n\n", parse_mode='Markdown', reply_markup=markup)

            temp = 'Список студентов: *'
            for key in TuesdayStudents:
                temp += f'[{TuesdayStudents[key][3]}](tg://user?id={key}) время урока: {TuesdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Wednesday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

        if day == 'Thursday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
            for key in ThursdayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\nУрок в {ThursdayStudents[key][1]} по Нск. \n\n", parse_mode='Markdown', reply_markup=markup)

            temp = 'Список студентов: *'
            for key in ThursdayStudents:
                temp += f'[{ThursdayStudents[key][3]}](tg://user?id={key}) время урока: {ThursdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Friday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
            for key in FridayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\nУрок в {FridayStudents[key][1]} по Нск. \n\n", parse_mode='Markdown', reply_markup=markup)
            temp = 'Список студентов: *'
            for key in FridayStudents:
                temp += f'[{FridayStudents[key][3]}](tg://user?id={key}) время урока: {FridayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')


        if day == 'Saturday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.", parse_mode='Markdown')
            for key in SaturdayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\nУрок в {SaturdayStudents[key][1]} по Нск. \n\n", parse_mode='Markdown', reply_markup=markup)

            temp = 'Список студентов: *'
            for key in SaturdayStudents:
                temp += f'[{SaturdayStudents[key][3]}](tg://user?id={key}) время урока: {SaturdayStudents[key][1]} *'

            M = [i for i in temp.split('*')]
            message_text = '\n'.join(M)
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        if day == 'Sunday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команды: noticestudents, notice

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

# region Команда: logi
@bot.message_handler(commands=['logi'])
def logi(message):
    if message.chat.id in PrivateMe:
        file = open('logi.txt', 'rb')
        bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")
# endregion Команда: logi
# endregion Список приватных команд






@bot.message_handler(content_types=['text'])
@analytics
def mess(message):
    get_message_bot = message.text.strip()

    # region Кнопка: [Что умеет этот бот 🤖]
    if get_message_bot == 'Что умеет этот бот 🤖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        sti = open("photo/hi.tgs", 'rb')
        bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        bot.send_message(message.chat.id, 'Бот помогает мне организовывать учебный процесс, например здесь можно увидеть доступ к моему календарю для записи на урок или переноса занятий.')
        pic_1 = open("photo/appointment.jpg", 'rb')
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Далее", callback_data='next1'))
        bot.send_photo(message.chat.id, pic_1, reply_markup=markup2)
    # endregion Кнопка: Что умеет этот бот

    # region Кнопки: [Подтвердить оплату абонемента ❗]
    elif get_message_bot == 'Подтвердить оплату абонемента ❗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, f"Cпасибо, записал 🤖", reply_markup=markup)
        bot.send_message(1891281816, f"{Students[message.chat.id][3]} подтвердил оплату ✅", reply_markup=markup)

        now = dt.datetime.utcnow()
        nsk_now = now + dt.timedelta(hours=7)
        timer = nsk_now.strftime('#%d%A%B #%B%Y')
        bot.send_message(-647660626, f"✅ #{Students[message.chat.id][3]} *абонемент оплачен*.\nДата: {timer}", parse_mode='Markdown')

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
            mess = f"✅ #{Students[message.chat.id][3]} абонемент *оплачен*.\nДата: {timer}\n\n"
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))
            sql.commit()
        else:
            name = Students[user_id][3]
            count = records[2]
            newmess = f"✅ #{Students[message.chat.id][3]} абонемент *оплачен*.\nДата: {timer}\n\n"
            mess = records[3] + newmess
            cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))
            sql.commit()
            cursor.close()
    # endregion Кнопки: [Подтвердить оплату абонемента ❗]

    # region Кнопки: [Да, все получается ✅]
    elif get_message_bot == 'Да, все получается ✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, f"Cпасибо, отправил ответ 🤖", reply_markup=markup)

        now = dt.datetime.utcnow()
        nsk_now = now + dt.timedelta(hours=7)
        timer = nsk_now.strftime('#%d%A%B #%A%B #%B%Y')
        timer2 = nsk_now.strftime('#%d%A%B')
        bot.send_message(-647660626, f"{timer}\n\n#{Students[message.chat.id][3]}", parse_mode='Markdown')

        markup2 = types.InlineKeyboardMarkup(row_width=3)
        markup2.add(types.InlineKeyboardButton('OK', callback_data='lesson'))
        bot.send_message(1891281816, f"✅ {Students[message.chat.id][3]} – Урок будет\n[Написать сообщение](tg://user?id={message.chat.id})", parse_mode='Markdown')


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
            mess = f"Занятие №{count}\nДата: {timer2} \n\n"
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))

            if count == Students[user_id][4]:
                bot.send_message(-647660626, f"⛔ #{Students[user_id][3]} абонемент *закончился*.\n[Написать сообщение](tg://user?id={user_id})\n\nИстория:\n{mess}", parse_mode='Markdown')
                bot.send_message(user_id, f"Доброго времени суток, #{Students[user_id][3]}!\n🤖 Я посчитал, что Ваш абонемент закончился, давайте проверим 📊📈🧮\n\n"
                                          f"История:\n{mess}\nВоспользуйтесь командой 👉 /price, чтобы получить реквизиты 🙏", parse_mode='Markdown')
                cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            sql.commit()
        else:
            name = Students[user_id][3]
            count = records[2] + 1
            newmess = f"*Занятие №{count}*\nДата: {timer2} \n\n"
            mess = records[3] + newmess
            cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            cursor.execute(f"INSERT INTO tickets VALUES(?, ?, ?, ?);", (user_id, name, count, mess))

            if count == Students[user_id][4]:
                bot.send_message(-647660626, f"⛔ #{Students[user_id][3]} *абонемент закончился*.\n[Написать сообщение](tg://user?id={user_id})\n\nИстория:\n{mess}", parse_mode='Markdown')
                bot.send_message(user_id, f"Доброго времени суток, #{Students[user_id][3]}!\n🤖 Я посчитал, что Ваш абонемент закончился, давайте проверим 📊📈🧮\n\n"
                                          f"История:\n{mess}\nВоспользуйтесь командой 👉 /price, чтобы получить реквизиты 🙏", parse_mode='Markdown')
                cursor.execute(f"DELETE FROM tickets WHERE id = {user_id}")
            sql.commit()
            cursor.close()
    # endregion Кнопки: [Да, все получается ✅]

    # region Кнопки: [Нет, не получится ⛔], [Какая-то ошибка], [Прочитано ✅]
    elif get_message_bot == 'Нет, не получится ⛔':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id, f"🤖 Если нужно перенести урок, то можно написать мне @ilandroxy или воспользоваться командой /calendly", reply_markup=markup)
        bot.send_message(1891281816, f"⛔ {Students[message.chat.id][3]} – Урока не будет\n[Написать сообщение](tg://user?id={message.chat.id})", parse_mode='Markdown')


    elif get_message_bot == 'Какая-то ошибка, у нас сегодня нет урока':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id, f"Sorry, возможно 🤖 напутал с расписанием... Пробую исправить!", reply_markup=markup)
        bot.send_message(1891281816, f"‼️ {Students[message.chat.id][3]} – Что-то не так с расписанием, надо проверить.\n[Написать сообщение](tg://user?id={message.chat.id})", parse_mode='Markdown')

    elif get_message_bot == 'Прочитано ✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)


        bot.send_message(message.chat.id, f"Спасибо, что читаете 🤖", reply_markup=markup)
        bot.send_message(1891281816, f"🤖 {Students[message.chat.id][3]} – Уведомлен \n[Написать сообщение](tg://user?id={message.chat.id})", parse_mode='Markdown')
    # endregion Кнопки: [Нет, не получится ⛔], [Какая-то ошибка], [Прочитано ✅]

    # region Кнопка: [Репетитор]
    elif get_message_bot == "Репетитор":
        send_message1 = f"👨🏼‍💻 Работаю дистанционно, есть все необходимое для проведения занятий. " \
                        f"В работе использую такие сервисы (программы) как: PyCharm, Python, Notability, Discord, Google диск и другие. " \
                        f"Гарантирую связь со мной (WhatsApp, Telegram ☎️) каждый день и ответы на все ваши вопросы."
        bot.send_message(message.chat.id, send_message1, parse_mode="Markdown")
        time.sleep(1)

        pic_3 = open("photo/face.jpeg", 'rb')
        bot.send_photo(message.chat.id, pic_3)

        send_message3 = f"Берусь только за ЕГЭ по Информатике, работаю со школьниками от 6 класса по программе обучения языку программирования Python.\n\n" \
                        f"Целенаправленно мы подготовимся к ЕГЭ по Информатике с учетом изменений в ФИПИ и КИМах. " \
                        f"Для достижения результатов от вас потребуется регулярное посещение занятий и выполнение домашних заданий"
        bot.send_message(message.chat.id, send_message3, parse_mode="Markdown")
        time.sleep(1)

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
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
                   types.InlineKeyboardButton("🏷 Прайс", callback_data="price"),
                   types.InlineKeyboardButton("🧮 Реквизиты", callback_data="wallet"))
        bot.send_message(message.chat.id, send_message4, parse_mode="Markdown", reply_markup=markup2)
    # endregion Кнопка: [Репетитор]

    # region Кнопка: [Контакты]
    elif get_message_bot == "Контакты":
        send_message1 = "*Мои контакты:*\n\n" \
                        "[Telegram](t.me/ilandroxy)\n\n[WhatsApp](wa.me/message/JSXJ2NLWTVNFC1)\n\n[Discord](https://discordapp.com/users/ilandroxxy#6249) ilandroxxy#6249\n\n" \
                        "[Zoom](https://us04web.zoom.us/j/2402871810?pwd=OVdGQkE2ODIvWm1WNk5EdStQR1o4UT09)\n\n" \
                        "[Профиль Авито](www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing)\n\n[YouTube](https://m.youtube.com/channel/UCcORhBL494aSLcyIODjOG0A)\n\n" \
                        "[GitHub](https://github.com/ilandroxxy)\n\nРабочий телефон: +7 (995) 437–52–59\n\nEmail: collegehacksbot@gmail.com\n\n" \
                        "Воспользуйтесь моим Telegram ботом, чтобы пройти курс по разработке чат ботов @JustDoItMotherBot🤖"
        bot.send_message(message.chat.id, send_message1, parse_mode='Markdown', disable_web_page_preview=True)
    # endregion Кнопка: [Контакты]

    # region Кнопка: [Мои проекты]
    # todo: Добавить в кнопку [Мои проекты] и в соответсвующую команду ссылки на "Работы с учениками: перечислить боты и описание проектов"
    elif get_message_bot == "Мои проекты":
        send_message = "Просто перечисляю, чем я занимаюсь сегодня!\n\n" \
                       "*1. Канал* [itpy | ИнформатикаЕГЭ](t.me/pro100_easy_ege)\n✍️ Это канал на котором я разбираю задания с экзамена, даю полезные задачки и " \
                       "показываю будущим студентам сферу IT, о которой они вряд ли слышали в школе!\n\n" \
                       "*2. Чат бот* 🤖[MotherBot](t.me/JustDoItMotherBot)  \nЭто Telegram бот, который помогает начинающим программистам разобраться в библиотеке [PyTelegramBotAPI](https://habr.com/ru/post/580408/), предназначенной " \
                       "для работы с API Telegram – создания чат ботов в меcсенджере.\n\n" \
                       "*3. Курс подготовки к ЕГЭ на* [Stepik](https://stepik.org/course/122969)\n" \
                       "На сегодняшний день курс еще находится в разработке, но уже можно понять, что он из себя будет представлять по [описанию проекта](https://stepik.org/lesson/770711/step/1) " \
                       "и черновому [примеру урока](https://stepik.org/lesson/770602/step/1).\n\n"
        bot.send_message(message.chat.id, send_message, parse_mode="Markdown", disable_web_page_preview=True)
    # endregion Кнопка: [Мои проекты]

    # region Кнопка: [Записаться на урок]
    elif get_message_bot == "Записаться на урок":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("calendly.com", url="calendly.com/ilandroxxy/tutor"))
        message_text = f"Воспользуйтесь удобным сервисом [Calendly](https://bizzapps.ru/p/calendly/) *для записи на пробное занятие* или выбора графика занятий. \n\n" \
                       f"Просто выберете подходящее время и *напишите пару слов о себе*. \n\n" \
                       f"❗Ваша карточка отобразится в моем календаре, но чтобы было комфортнее держать связь - прошу написать еще и в [Telegram](t.me/ilandroxy). "
        bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)

        pic = open("photo/calendly.jpg", 'rb')
        bot.send_photo(message.chat.id, pic, reply_markup=markup)

        text_message = f"🤖 `Calendly`\n*{message.from_user.first_name}* открыл(а) календарь\n*User ID*: `{message.chat.id}`\n" \
                       f"*Username*: @{message.from_user.username}\n" \
                       f"[Написать сообщение](tg://user?id={message.chat.id})\n\n" \
                       f"[Открыть мой Календарь](https://calendar.google.com/calendar/u/0/r?tab=rc&pli=1)"
        bot.send_message(1891281816, text_message, parse_mode='Markdown', disable_web_page_preview=True)
    # endregion Кнопка: [Записаться на урок]

    # region Кнопка: [Получить файл с урока]
    elif get_message_bot == "Получить файл с урока":

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
                             "Перейдя по ссылке на сервис [GitHub](https://github.com/ilandroxxy/ilandroxy_bot/commits/main/ilandroxy_Bot/lessons) можно обнаружить кнопку History, "
                             "которая дает доступ к истории изменения ваших файлов.", parse_mode='Markdown', disable_web_page_preview=True)

            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton(f"Твой файл: {Students[key][0]}", url=f"https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/{Students[key][0]}"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        elif message.chat.id in Me:
            messgae_text = "Воспользуйтесь командой /homework чтобы получить домашнее задание."
            bot.send_message(message.chat.id, messgae_text)

            pic = open('photo/history.jpeg', 'rb')
            bot.send_photo(message.chat.id, pic)

            bot.send_message(message.chat.id, "Перейдя по ссылке на сервис [GitHub](https://github.com/ilandroxxy/ilandroxy_bot/commits/main/ilandroxy_Bot/lessons) можно обнаружить кнопку History, "
                           "которая дает доступ к истории изменения ваших файлов.", parse_mode='Markdown', disable_web_page_preview=True)

            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton(f"Папка: lessons", url=f"https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        else:
            message_text = 'Извините, по-моему вас нет в системе! Ожидайте...'
            bot.send_message(message.chat.id, message_text)
            sti = open('photo/WaitSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
    # endregion Кнопка: [Получить файл с урока]

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
            f = open('logi.txt', 'r')
            s = f.readline()
            log = f'\n\n{s}'

            f = open('logi.txt', 'w')
            f.write(log)
            print(e)

