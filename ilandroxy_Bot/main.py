import random
import telebot
from telebot import types
import sqlite3
import csv
import time
import datetime as dt
import requests

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ` ⛔  ️✅ 📊📈🧮
bot = telebot.TeleBot('5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU')
# real 5640042697:AAGA5EIFYkt2urDf-UXlcyoVLG4x375Ntjk
# test 5734914555:AAEPdNUsCpv4n49jie8C9P7TojK_McPkCIU

"""
MondayStudents = {811476623: "Georgie.py", 826004697: 'Nikita.py'}
TuesdayStudents = {1949653479: 'Yanina.py', 1208542295: 'Sasha.py', 1537718492: 'Aleksandr.py', 789322200: 'Katya.py', 804184353: 'Islam.py'}
ThursdayStudents = {1949653479: "Yanina.py", 1477701439: "Valeria.py", 811476623: "Georgie.py", 799740089: "Bulat.py", 1537718492: "Aleksandr.py", 1454117859: 'Diana'}
FridayStudents = {1314375732: 'Vasiliy.py', 644645774: 'Stasya.py', 719571990: 'Stepan.py', 1029532016: 'Maria.py', 1649389148: 'Slava.py'}
SaturdayStudents = {871237277: 'Vladek.py', 5148819382: 'Tatyana.py', 1454117859: 'Diana'}
"""
# Синхронно моему расписанию в Google Календаре
MondayStudents = {811476623: ["Georgie.py", "20:00"], 826004697: ['Nikita.py', '22:00']}
TuesdayStudents = {1949653479: ['Yanina.py', '10:00'], 789322200: ['Katya.py', "16:00"], 1208542295: ['Sasha.py', '19:00'], 804184353: ['Islam.py', '21:00'], 1537718492: ['Aleksandr.py', '22;00']}
ThursdayStudents = {1949653479: ['Yanina.py', '10:00'], 1477701439: ["Valeria.py", '16:00'], 1454117859: ['Diana', "19:00"], 811476623:  ["Georgie.py", "20:00"], 799740089: ["Bulat.py", "21:00"], 1537718492: ["Aleksandr.py", "22:00"]}
FridayStudents = {1314375732: ['Vasiliy.py', "15:00"], 644645774: ['Stasya.py', "16:00"], 719571990: ['Stepan.py', "17:00"], 1029532016: ['Maria.py', "21:00"], 1649389148: ['Slava.py', "22:00"]}
SaturdayStudents = {1454117859: ['Diana', "19:00"], 5148819382: ['Tatyana.py', "19:00"], 871237277: ['Vladek.py', "22:00"]}

Students = MondayStudents | TuesdayStudents | ThursdayStudents | FridayStudents | SaturdayStudents

Me = {1891281816: 'ilandroxy', 438879394: 'ilandroxxy', -726393257: "Homework", -647660626: "Lessons"}
Testing = {1891281816: 'ilandroxy', 438879394: 'ilandroxxy'}

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    # Репетитор -----------------------------------------------------------------------
    if call.data == 'price':
        pic_2 = open("photo/price.PNG", "rb")
        msg = bot.send_photo(call.message.chat.id, pic_2)

        send_message2 = f"*Первое занятие БЕСПЛАТНО*,\nна нем я определю уровень знаний, и мы вместе подбираем оптимальный абонемент!\n\n" \
                        f"Работаю официально по чекам через НПД (`Самозанятый`).\n\n"
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🧑🏽‍💻 О себе", callback_data="iam"),
                   types.InlineKeyboardButton("⬇️ Программы", callback_data="downloads"),
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

        msg = bot.send_message(call.message.chat.id, send_message, parse_mode="Markdown", reply_markup=markup, disable_web_page_preview=True)
    # Репетитор -----------------------------------------------------------------------


    # Homework ------------------------------------------------------------------------
    elif call.data == "hw1":
        type = '1'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 29)
        M = [13479, 23901, 38446, 11259, 26946, 18782, 5697, 15098, 16030, 5793, 29188, 26975, 18705, 7981, 38935, 4707,
             40717, 28678, 17367, 5196, 25833, 3828, 36856, 15971, 7777, 37136, 38446, 13506, 7355, 11232]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw2":
        type = '2'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 41)
        M = [29650, 33174, 18483, 27287, 46999, 26974, 35891, 36857, 15124, 40718, 28538, 27399, 15912, 18430,
             27260, 33472, 15970, 37137, 15787, 16878, 46960, 45236, 27531, 18781, 35460, 27371, 18071, 15097,
             35976, 16431, 18578, 39231, 15814, 33504, 36015, 16805, 33081, 29109, 18614, 38936, 16029, 19051]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw3":
        type = '3'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 21)
        M = [37494, 39232, 37481, 38937, 47000, 37491, 37492, 37493, 45237, 40719, 37417, 37479, 37508, 37488, 37507, 37489,
             37415, 46961, 40978, 37480, 37485, 37490]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw4":
        type = '4'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [18617, 14691, 17323, 13351, 19054, 15942, 10499, 16808, 37139, 16881, 27290, 18553, 9791, 45238, 16380, 18581,
             47001, 15915, 10379, 16434, 26948, 17369, 13562, 15817, 26977, 11234, 15790, 36017, 18486, 28680, 18811, 18074,
             15621, 13616, 27263, 14220, 11341, 46962, 7685, 18433]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw5":
        type = '5'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [7454, 26978, 13617, 29653, 18075, 11235, 18785, 10380, 15791, 7917, 9792, 16033, 17370, 11342, 18487, 14692, 18618, 7690,
             15101, 15622, 35894, 13590, 16435, 13536, 9190, 18582, 7751, 47002, 16809, 10407, 14767, 27375, 45239, 11262, 14265, 15818,
             27264, 10309, 26949, 13563]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw6":
        type = '6'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 20)
        M = [47003, 36861, 33178, 35895, 46964, 33508, 29654, 33476, 38940, 33751, 35464, 30692, 45240, 39235, 33085,
             36019, 35980, 37141, 40722, 27403, 40981]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw7":
        type = '7'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [18078, 8097, 23907, 16438, 25839, 13355, 11110, 29194, 15821, 13620, 19058, 13593, 17327, 45241, 27538,
             16812, 28684, 9759, 15977, 26981, 18585, 11345, 9795, 14695, 17373, 38941, 10497, 33477, 10470, 35465,
             15946, 16036, 36862, 15131, 28545, 29655, 13736, 36020, 18711, 33509]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw8":
        type = '8'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [9361, 15822, 10473, 15795, 16037, 10500, 7986, 35897, 3568, 27009, 8658, 11266, 3230, 26953, 23908, 3569, 36021, 3692,
             3515, 33753, 36863, 3811, 13459, 3233, 7370, 27236, 5055, 7338, 16439, 9162, 10384, 3517,
             7694, 19059, 3227, 18622, 13567, 15947, 14696, 27295]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw9":
        type = '9'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 34)
        M = [33754, 27529, 35898, 33088, 27524, 27524, 36022, 27406, 27525, 33181, 35467, 27518, 46967, 28117, 38588, 39238, 27517, 36864,
             27526, 29657, 27523, 27519, 45243, 40725, 27528, 38943, 27522, 35983, 40984, 33511, 47006, 37144, 33479,
             27520, 27527]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw10":
        type = '10'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 33)
        M = [36865, 27582, 33480, 46968, 27590, 27589, 35899, 27588, 38944, 36023, 29658, 27580, 40726, 27586,
             37145, 27577, 40985, 27581, 33512, 45244, 27407, 27579, 27585, 33089, 33182, 35468, 27587, 27584,
             39239, 27591, 33755, 47007, 27583, 35984]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw11":
        type = '11'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [9364, 6885, 40986, 36024, 33481, 7924, 11309, 7989, 16889, 4684, 33183, 6415, 10476, 6181, 18792,
             9305, 5081, 5237, 15629, 4716, 36866, 45245, 23911, 6298, 5270, 6917, 16442, 9165, 6330, 14272,
             16816, 7785, 29198, 7758, 15853, 9197, 15825, 7670, 9763, 6451]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw12":
        type = '12'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [13571, 23912, 16890, 26986, 10290, 33514, 29660, 40987, 10317, 13517, 15630, 11350, 15854, 15951,
             15799, 13544, 28550, 45246, 35470, 33757, 10415, 18562, 18820, 27299, 27272, 47009, 38946, 9764,
             39241, 18626, 10504, 16443, 35986, 33482, 35901, 14229, 18793, 14775, 17332, 18716]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw13":
        type = '13'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [5365, 13361, 10505, 16818, 5429, 33092, 10478, 18627, 11271, 29122, 33758, 17333, 18591,
             5941, 16891, 15631, 15800, 6237, 40988, 11244, 33515, 40729, 17379, 3746, 15855, 28690,
             18496, 6269, 18563, 27300, 28551, 18084, 27544, 6309, 46971, 27273, 3285, 39242, 3294, 15110]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw14":
        type = '14'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [15801, 15828, 8664, 9766, 18718, 33093, 16892, 17380, 16391, 27301, 16819, 29123, 36027,
             38589, 29201, 9697, 36869, 18444, 15953, 18497, 27274, 33484, 46972, 15632, 13362, 47011, 18085,
             15984, 13743, 33186, 26988, 18795, 16043, 27015, 18628, 25846, 45248, 23914, 15926, 27545]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw15":
        type = '15'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 37)
        M = [13745, 8106, 35989, 34539, 34547, 18720, 33760, 34516, 8666, 33517, 34509, 15955, 34518, 27303, 11119, 33094, 34511,
             35904, 13364, 16894, 46973, 17382, 36870, 27547, 34506, 45249, 15928, 34510, 34535, 29633, 34537, 39244, 18566, 33187,
             34542, 37150, 35473, 34513]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw16":
        type = '16'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 37)
        M = [4937, 5970, 37151, 35990, 38591, 5310, 4644, 4651, 36871, 4692, 35474, 45250, 7340, 4647, 7270, 5458, 4978, 27413, 6990,
             4646, 4642, 5650, 4643, 7273, 5586, 4657, 4658, 5554, 4724, 33518, 6423, 6189, 4849, 35905, 5938, 4656, 33095, 5278]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw17":
        type = '17'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 33)
        M = [37356, 39763, 39764, 37344, 37348, 37354, 37345, 39246, 37350, 47014, 37360, 37355, 37347, 37337, 37359, 37358, 37371, 37349,
             45251, 40733, 37370, 37372, 38951, 37340, 46975, 37369, 40992, 37341, 37336, 39762, 37357, 37373, 37362, 37361]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw18":
        type = '18'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [27681, 27673, 35992, 46976, 27669, 27676, 27677, 39247, 27685, 27683, 29666, 40993, 27679, 33763, 33097, 33488, 37153,
             33520, 45252, 35907, 27682, 40734, 27670, 27671, 27680, 38593, 27675, 27678, 36873, 27415, 27672, 36031, 33190, 38952, 47015,
             27667, 27666, 35476, 27668, 27674]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw19-21":
        type = '19-21'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 19)
        M = [28096, 27832, 33764, 28001, 28035, 28099, 40994, 39248, 27771, 28090, 29667, 27797, 27932, 28077, 28102, 38597,
             27802, 28158, 27780, 27826, ]

        link = f'Задача типа (19): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
        link = f'Задача типа (20): [{M[x]+1}]({s}{M[x]+1})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)
        link = f'Задача типа (21): [{M[x]+2}]({s}{M[x]+2})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]}), [{M[x]+1}]({s}{M[x]+1}), [{M[x]+2}]({s}{M[x]+2})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw22":
        type = '22'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [5524, 26992, 10483, 6813, 35996, 13366, 15860, 14279, 18568, 13469, 9770, 15957, 3849, 38956, 5280, 15930,
             23918, 5492, 13550, 36877, 6960, 40738, 15988, 15636, 15805, 3280, 45256, 3279, 4694, 16047, 11249, 13416,
             27419, 5091, 6781, 27305, 13577, 6006, 3273, 5215]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw23":
        type = '23'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 39)
        M = [28697, 18450, 3631, 16898, 27551, 14783, 5913, 13418, 11123, 15638, 38957, 16451, 15932, 7379, 13471, 15990, 8670,
             16825, 17340, 13633, 18570, 7315, 11318, 18828, 33195, 27391, 45257, 7347, 13552, 14237, 29207, 23920, 13525, 14281,
             7998, 39252, 18634, 13579, 18598, 13368]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw24":
        type = '24'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 35)
        M = [27692, 33526, 33494, 35913, 27698, 33103, 37131, 40740, 27689, 40999, 35482, 27695, 27686, 27697, 27688, 27694, 33196,
             36879, 27696, 37159, 27421, 38958, 46982, 45258, 35998, 38602, 39253, 33769, 47021, 27699, 36037, 27691, 27690, 29672,
             27693, 27687]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw25":
        type = '25'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 35)
        M = [33527, 27852, 33104, 28120, 39254, 27854, 37160, 28122, 37130, 27857, 27422, 41000, 36038, 29673, 35999, 46983, 47022,
             33495, 33197, 33770, 28124, 38959, 45259, 35914, 28123, 27853, 28121, 27858, 36880, 35483, 27851, 38603, 27850, 40741,
             27856, 27855]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)


    elif call.data == "hw26":
        type = '26'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 33)
        M = [46984, 28132, 33528, 40742, 28141, 39255, 33771, 27884, 38960, 27888, 28140, 27886, 35915, 36881, 27423, 29674,
             36000, 35484, 36039, 28139, 27883, 41001, 47023, 27881, 27882, 33198, 27887, 27880, 33105, 28138, 33496, 37161,
             45260, 27885]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)

    elif call.data == "hw27":
        type = '27'
        s = 'inf-ege.sdamgia.ru/problem?id='
        x = random.randint(0, 30)
        M = [28133, 33529, 35485, 27424, 33497, 28131, 27891, 27991, 37162, 47024, 46985, 35916, 33106, 38961, 27889, 38604,
             36001, 39256, 28130, 40743, 27990, 41002, 36882, 28129, 29675, 27890, 27989, 33772, 36040, 45261, 33199]
        link = f'Задача типа ({type}): [{M[x]}]({s}{M[x]})'
        msg = bot.send_message(call.message.chat.id, link, parse_mode='Markdown', disable_web_page_preview=True)

        msg = bot.send_message(-726393257, f"#{call.from_user.first_name}\nПолучил домашку ({type}): [{M[x]}]({s}{M[x]})\n\n[Написать сообщение](tg://user?id={call.message.chat.id})",
                               parse_mode='Markdown', disable_web_page_preview=True)
    # Homework ------------------------------------------------------------------------


    # Useful ------------------------------------------------------------------------
    elif call.data == 'py01':
        py01 = open('files/py01.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py01)

    elif call.data == 'py02':
        py02 = open('files/py02.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py02)

    elif call.data == 'py03':
        py03 = open('files/py03.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py03)

    elif call.data == 'py04':
        py04 = open('files/py04.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py04)

    elif call.data == 'py05':
        py05 = open('files/py05.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py05)

    elif call.data == 'py06':
        py06 = open('files/py06.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py06)

    elif call.data == 'py07':
        py07 = open('files/py07.pdf', 'rb')
        msg = bot.send_document(call.message.chat.id, py07)
    # Useful ------------------------------------------------------------------------


    # Lessons ------------------------------------------------------------------------
    elif call.data == 'lesson':
        now = dt.datetime.utcnow()
        nsk_now = now + dt.timedelta(hours=7)
        timer = nsk_now.strftime('%d #%A%B%Y #%B%Y')

        msg = bot.send_message(call.message.chat.id, "Введите сообщение к уроку в форма:\n[#Name] [Описание урока]")

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = timer + '\n\n' + message.text
            msg = bot.send_message(-647660626, text_message, disable_web_page_preview=True)
        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'pay':
        now = dt.datetime.utcnow()
        nsk_now = now + dt.timedelta(hours=7)
        timer = nsk_now.strftime('%d %A #%B%Y')

        textik = '✅ #Оплачен Абонемент:\n' + timer
        msg = bot.send_message(call.message.chat.id, "Введите данные по абонементу:\n[#Name] [Тип абонемента] [Цена]")

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            text_message = textik + '\n\n' + message.text
            msg = bot.send_message(-647660626, text_message, disable_web_page_preview=True)
        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'add':
        msg = bot.send_message(call.message.chat.id, "Введите данные нового студента:\n[#Day] [ID] [Name.py]\n\n*Напишите `0`, чтобы отменить команду!*\n\n"
                                                     "#Monday\n#Tuesday\n#Thursday\n#Friday\n#Saturday")
        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                M = [i for i in message.text.split()]

                if M[0] == '#Monday':
                    MondayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"MondayStudents={MondayStudents}")

                elif M[0] == '#Tuesday':
                    TuesdayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"TuesdayStudents={TuesdayStudents}")

                elif M[0] == '#Thursday':
                    ThursdayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"ThursdayStudents={ThursdayStudents}")

                elif M[0] == '#Friday':
                    FridayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"FridayStudents={FridayStudents}")

                elif M[0] == '#Saturday':
                    SaturdayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"SaturdayStudents={SaturdayStudents}")


                msg = bot.send_message(1891281816, "Добавил нового студента в систему 🤖\n\n*Не забудьте перенести этот словарь в код программы!*", parse_mode='Markdown', disable_web_page_preview=True)
        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'del':
        msg = bot.send_message(call.message.chat.id, "Заполните форму:\n[#OldDay] [ID] [Name.py] [#NewDay]\n\n*Напишите `0`, чтобы отменить команду!*\n\n"
                                                     "#OldMonday    #NewMonday\n#OldTuesday    #NewTuesday\n#OldThursday    #NewThursday"
                                                     "\n#OldFriday    #NewFriday\n#OldSaturday    #NewSaturday")


        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != '0':
                M = [i for i in message.text.split()]

                if M[0] == '#OldMonday':
                    del MondayStudents[int(M[1])]
                    msg = bot.send_message(1891281816, f"Old: MondayStudents={MondayStudents}")

                elif M[0] == '#OldTuesday':
                    del TuesdayStudents[int(M[1])]
                    msg = bot.send_message(1891281816, f"Old: TuesdayStudents={TuesdayStudents}")

                elif M[0] == '#OldThursday':
                    del ThursdayStudents[int(M[1])]
                    msg = bot.send_message(1891281816, f"Old: ThursdayStudents={ThursdayStudents}")

                elif M[0] == '#OldFriday':
                    del FridayStudents[int(M[1])]
                    msg = bot.send_message(1891281816, f"Old: FridayStudents={FridayStudents}")

                elif M[0] == '#OldSaturday':
                    del SaturdayStudents[int(M[1])]
                    msg = bot.send_message(1891281816, f"Old: SaturdayStudents={SaturdayStudents}")

                if M[3] == '#NewMonday':
                    MondayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"New: MondayStudents={MondayStudents}")

                elif M[3] == '#NewTuesday':
                    TuesdayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"New: TuesdayStudents={MondayStudents}")

                elif M[3] == '#NewThursday':
                    ThursdayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"New: ThursdayStudents={ThursdayStudents}")

                elif M[3] == '#NewFriday':
                    FridayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"New: FridayStudents={FridayStudents}")

                elif M[3] == '#NewSaturday':
                    SaturdayStudents[int(M[1])] = M[2]
                    msg = bot.send_message(1891281816, f"New: SaturdayStudents={SaturdayStudents}")

                msg = bot.send_message(1891281816, "Изменения в расписании: перенесли дату уроков 🤖\n\n*Не забудьте перенести этот словарь в код программы!*", parse_mode='Markdown', disable_web_page_preview=True)

        bot.register_next_step_handler(call.message, message_input)
    # Lessons ------------------------------------------------------------------------






# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ` ⛔  ️✅ 📊📈🧮
'''# Публичные команды:
/help - справка по всем командам в боте
/tasks - наборы задач для отработки решений ЕГЭ по Информатике
/homework - конструктор домашних заданий для моих учеников
/calendly - форма записи на урок
/links - полезные ссылки для подготовки к экзамену
/getmyid - бот покажет ваш id пользователя Telegram
/myprojects - список моих актуальных проектов
/download - список программ необходимых для уроков
/start - перезапуск бота, на стартовую позицию
/price - получить информацию о ценах и реквизиты
/useful - шпаргалки от Яндекс практикума по Python
/getorder - команда для желающих оставить заявку на разработку бота.
'''

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Контакты')
    btn2 = types.KeyboardButton('Репетитор')
    btn3 = types.KeyboardButton('Мои проекты')
    btn4 = types.KeyboardButton('Записаться на урок')
    btn5 = types.KeyboardButton('Получить файл с урока')
    pic_1 = open("photo/hello.jpeg", 'rb')
    bot.send_photo(message.chat.id, pic_1)

    markup.add(btn1, btn2, btn3, btn4, btn5)
    message_text1 = f'👋 Доброго времени суток, *{message.from_user.first_name}*!\n\n' \
                f'*Меня зовут Андрианов Илья*. \nЯ программист – `Python developer`.\n' \
                f'А также репетитор подготовки к `ЕГЭ по Информатике` и программированию на языке `Python` 🐍\n\n' \
                f'*Рад Вас приветствовать* у себя на `"страничке"`, здесь я постараюсь коротко ' \
                f'рассказать о себе и, надеюсь, нам удастся найти общий язык 🙏 \n\n'
    bot.send_message(message.chat.id, message_text1, parse_mode='Markdown')

    message_text2 = f'Если вы мой студент, то воспользуйтесь командой 👉 /getmyid, чтобы бот 🤖 показал ваш ID пользователя. Он необходим, чтобы [я смог добавить](t.me/@ilandroxy) Вас в систему!\n\n' \
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
                   '/getorder - обсудить разработку Вашего чат бота под заказ'
    bot.send_message(message.chat.id, send_message, parse_mode="Markdown")


# GETMYID
@bot.message_handler(commands=['getmyid'])
def getmyid(message):
    user = str(message.chat.id)
    send_message = "*Ваш user ID: *" + user
    bot.send_message(message.chat.id, send_message, parse_mode="Markdown")



# MYPROJECT
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
    message_text1 = "*Наборы разных типов задач с* [Решу ЕГЭ](https://inf-ege.sdamgia.ru/?redir=1):\n`new 2022-2023 года`\n\n" \
                    "[1.](https://inf-ege.sdamgia.ru/test?id=11297175&nt=True&pub=False)   [2.](https://inf-ege.sdamgia.ru/test?id=11297177&nt=True&pub=False)   [3.](https://inf-ege.sdamgia.ru/test?id=11297178&nt=True&pub=False)   " \
                   "[4.](https://inf-ege.sdamgia.ru/test?id=11297180&nt=True&pub=False)   [5.](https://inf-ege.sdamgia.ru/test?id=11297181&nt=True&pub=False)   [6.](https://inf-ege.sdamgia.ru/test?id=11297181&nt=True&pub=False)   [7.](https://inf-ege.sdamgia.ru/test?id=11297184&nt=True&pub=False)    " \
                   "[8.](https://inf-ege.sdamgia.ru/test?id=11297185&nt=True&pub=False)    [9.](https://inf-ege.sdamgia.ru/test?id=11297189&nt=True&pub=False)    [10.](https://inf-ege.sdamgia.ru/test?id=11297190&nt=True&pub=False)\n\n[11.](https://inf-ege.sdamgia.ru/test?id=11297191&nt=True&pub=False)   " \
                   "[12.](https://inf-ege.sdamgia.ru/test?id=11297194&nt=True&pub=False)   [13.](https://inf-ege.sdamgia.ru/test?id=11297198&nt=True&pub=False)   [14.](https://inf-ege.sdamgia.ru/test?id=11297200&nt=True&pub=False)   [15.](https://inf-ege.sdamgia.ru/test?id=11297201&nt=True&pub=False)   " \
                   "[16.](https://inf-ege.sdamgia.ru/test?id=11297204&nt=True&pub=False)   [17.](https://inf-ege.sdamgia.ru/test?id=11297205&nt=True&pub=False)   [18.](https://inf-ege.sdamgia.ru/test?id=11297208&nt=True&pub=False)\n\n[19-21.](https://inf-ege.sdamgia.ru/test?id=11297216&nt=True&pub=False)   " \
                   "[22.](https://inf-ege.sdamgia.ru/test?id=11297217&nt=True&pub=False)   [23.](https://inf-ege.sdamgia.ru/test?id=11297224&nt=True&pub=False)   [24.](https://inf-ege.sdamgia.ru/test?id=11297227&nt=True&pub=False)   [25.](https://inf-ege.sdamgia.ru/test?id=11297232&nt=True&pub=False)   " \
                   "[26.](https://inf-ege.sdamgia.ru/test?id=11297237&nt=True&pub=False)   [27.](https://inf-ege.sdamgia.ru/test?id=11297240&nt=True&pub=False)\n\n" \
                    "*Обратите внимание*, что наборы задач разного года могут отличаться!"
    bot.send_message(message.chat.id, message_text1, parse_mode="Markdown", disable_web_page_preview=True)

    message_text_old = "*Наборы разных типов задач с* [Решу ЕГЭ](https://inf-ege.sdamgia.ru/?redir=1):\n`old 2021-2022 года`\n\n" \
                       "[1.](https://clck.ru/ebsmq)   [2.](https://clck.ru/ebsnV)   [3.](https://clck.ru/ebsnt)   " \
                    "[4.](https://clck.ru/ebsoN)   [5.](https://clck.ru/ebsp8)   [6.](https://clck.ru/ebspK)   [7.](https://clck.ru/ebspX)    " \
                    "[8.](https://clck.ru/ebsq2)    [9.](https://clck.ru/ebsqH)   [10.](https://clck.ru/ebsqc)\n\n[11.](https://clck.ru/ebsrf)   " \
                    "[12.](https://clck.ru/ebsrr)   [13.](https://clck.ru/ebssH)   [14.](https://clck.ru/ebssi)   [15.](https://clck.ru/ebst4)   " \
                    "[16.](https://clck.ru/ebstT)   [17.](https://clck.ru/ebsuA)   [18.](https://clck.ru/ebsuf)\n\n[19-21.](https://clck.ru/ebsvw)   " \
                    "[22.](https://clck.ru/ebsxf)   [23.](https://clck.ru/ebsxo)   [24.](https://clck.ru/ebsyM)   [25.](https://clck.ru/ebszu)   " \
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
                   "\n*Для отработки теории на практике воспользуйтесь командой /tasks *"
    bot.send_message(message.chat.id, message_text, parse_mode="Markdown", disable_web_page_preview=True)


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


# USEFUL
@bot.message_handler(commands=['useful'])
def useful(message):
    if message.chat.id in Students or message.chat.id in Me:
        message_text = 'Для своих студентов я решил поделиться шпаргалками от *Яндекс Практикума*, в котором сейчас прохожу обучение по специальности `Python developer`.\n\n' \
                       'Постепенно список файлов будет пополняться, но *хочу отметить, что для успешной сдачи экзамена ЕГЭ по Информатике хватит первых 3-х файлов*:'
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("1. Знакомство с Python: Типы данных, Списки.", callback_data="py01"),
                   types.InlineKeyboardButton("2. Циклы, Ветвления, Логические выражения.", callback_data="py02"),
                   types.InlineKeyboardButton("3. Функции: Вызов, Аргументы, Возврат значений.", callback_data="py03"),
                   types.InlineKeyboardButton("4. Коллекции: Словари и Множества.", callback_data="py04"),
                   types.InlineKeyboardButton("5. Строки: Метод split() и f-string.", callback_data="py05"),
                   types.InlineKeyboardButton("6. Библиотеки: datetime, math, random..", callback_data="py06"),
                   types.InlineKeyboardButton("7. Сетевые запросы: Библиотека requests.", callback_data="py07"))
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Извините, эта функция доступна только моим ученикам, *запишитесь на урок /calendly*", parse_mode="Markdown")


# HOMEWORK
@bot.message_handler(commands=['homework'])
def homework(message):
    if message.chat.id in Me or message.chat.id in Students:
        message_text = "Эта команда просто выдает рандомное задание с Решу ЕГЭ\n\nПомимо этого, мне приходит уведомление с номерами выпавших задач.\n\nПроявите самостоятельность в выборе, а на уроке мы разбрем возникшие вопросы!\n\n[Читать правила оформления домашки](https://www.notion.so/ilandroxxy/8234ee61967a4cbe8a232b745cff0b9a)"
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
        bot.send_message(message.chat.id, "В случае ошибочной ссылки, просьба скинуть мне скриншот @ilandroxy", parse_mode="Markdown", disable_web_page_preview=True)
    else:
        bot.send_message(message.chat.id, "Извините, эта функция доступна только моим ученикам, *запишитесь на урок /calendly*", parse_mode="Markdown")

#GETORDER
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




# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ` ⛔  ️✅ 📊📈🧮
''' # Приватные команды:
/statistics - выводит статистику и файлы db напрямую в боте
/git - команда при запуске которой приходят команды для залива репазитория на GitHub
/less - чек проведенного урока и принятия оплат по абонементам, добавление ученика в систему.
/voiceall - способ отправить сообщение всем пользователям (с ссылками)
/voicestudents - способ отправить сообщение всем моим студентам
/noticestudents - опрос по именам учеников - будет ли урок сегодня (по дням)
/notice - опрос всех дневных учеников - будет ли урок сегодня (по дням)
/today - выводит список учеников по дням занятий
'''


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
        message_text = f"Общее кол-во студентов в Students: {len(Students)}\n\n" \
                       f"*MondayStudents*={MondayStudents}\n\n" \
                       f"*TuesdayStudents*={TuesdayStudents}\n\n" \
                       f"*ThursdayStudents*={ThursdayStudents}\n\n" \
                       f"*FridayStudents*={FridayStudents}\n\n" \
                       f"*SaturdayStudents*={SaturdayStudents}"
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')
        bot.send_message(message.chat.id, f"Всего пользователей в db: {len(records)}")


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


# LESS
@bot.message_handler(commands=['less'])
def less(message):
        if message.chat.id in Me:
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton("Проведен урок", callback_data='lesson'),
                       types.InlineKeyboardButton("Оплата", callback_data='pay'),
                       types.InlineKeyboardButton("Добавить ученика", callback_data='add'),
                       types.InlineKeyboardButton("Поменять расписание", callback_data='del'))
            bot.send_message(message.chat.id, 'Отчетность – это зер гуд 📊📈🧮', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")


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


# NOTICESTUDENTS
@bot.message_handler(commands=['noticestudents'])
def noticestudents(message):
    if message.chat.id == 1891281816:

        message_text = f"*MondayStudents:*\n{MondayStudents}\n\n" \
                       f"*TuesdayStudents:*\n{TuesdayStudents}\n\n" \
                       f"*ThursdayStudents:*\n{ThursdayStudents}\n\n" \
                       f"*FridayStudents:*\n{FridayStudents}\n\n" \
                       f"*SaturdayStudents:*\n{SaturdayStudents}\n\nНапишите `0`, чтобы отменить команду!"
        bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        '''
        bot.send_message(message.chat.id,
                         "Введите ID пользователей через пробел, кому надо отправить рассылку:\n\n"
                         "`1537718492` Александр\n`799740089` Булат\n`811476623` Георгий\n`1029532016` Мария\n`826004697` Никита\n`1208542295` Александра"
                         "\n`644645774` Стася\n`719571990` Степан\n`683943897` Таня\n`1477701439` Валерия\n`1314375732` Василий\n`871237277` Владек\n`1649389148` Слава
                         \n`1949653479` Янина\n`1029532016` Мария"
                         "\n\n`1891281816` ilandroxy\n`438879394` ilandroxxy", parse_mode='Markdown')
        '''

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

                        bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n\n", parse_mode='Markdown', reply_markup=markup)

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
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.\n\nСписок студентов: ", parse_mode='Markdown')
            for key in MondayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n\n", parse_mode='Markdown', reply_markup=markup)
            for key in MondayStudents:
                bot.send_message(message.chat.id, f" {MondayStudents[key][0]}: [Написать сообщение](tg://user?id={key}", parse_mode='Markdown')



        if day == 'Tuesday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.\n\nСписок студентов: ", parse_mode='Markdown')
            for key in TuesdayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n\n", parse_mode='Markdown', reply_markup=markup)
            for key in TuesdayStudents:
                bot.send_message(message.chat.id, f" {TuesdayStudents[key][0]}: [Написать сообщение](tg://user?id={key}", parse_mode='Markdown')

        if day == 'Wednesday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

        if day == 'Thursday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.\n\nСписок студентов: ", parse_mode='Markdown')
            for key in ThursdayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n\n", parse_mode='Markdown', reply_markup=markup)
            for key in ThursdayStudents:
                bot.send_message(message.chat.id, f" {ThursdayStudents[key][0]}: [Написать сообщение](tg://user?id={key}", parse_mode='Markdown')

        if day == 'Friday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.\n\nСписок студентов: ", parse_mode='Markdown')
            for key in FridayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n\n", parse_mode='Markdown', reply_markup=markup)
            for key in FridayStudents:
                bot.send_message(message.chat.id, f" {FridayStudents[key][0]}: [Написать сообщение](tg://user?id={key}", parse_mode='Markdown')


        if day == 'Saturday':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
            btn1 = types.KeyboardButton('Да, все получается ✅')
            btn2 = types.KeyboardButton('Нет, не получится ⛔')
            btn3 = types.KeyboardButton('Какая-то ошибка, у нас сегодня нет урока')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, f" 🤖 Я отправил сообщение, ждем ответов.\n\nСписок студентов: ", parse_mode='Markdown')
            for key in SaturdayStudents:
                bot.send_message(key, f" 🤖 Привет!\nСегодня занимаемся?\n\n", parse_mode='Markdown', reply_markup=markup)
            for key in SaturdayStudents:
                bot.send_message(message.chat.id, f" {SaturdayStudents[key][0]}: [Написать сообщение](tg://user?id={key}", parse_mode='Markdown')

        if day == 'Sunday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")

#TODAY
@bot.message_handler(commands=['today'])
def today(message):
    if message.chat.id in Me:
        day = time.strftime('%A')

        if day == 'Monday':
            for key in MondayStudents:
                bot.send_message(message.chat.id, f"  Урок в {MondayStudents[key][1]}  {MondayStudents[key][0]}\n[Написать сообщение](tg://user?id={key})", parse_mode='Markdown')

        if day == 'Tuesday':
            for key in TuesdayStudents:
                bot.send_message(message.chat.id, f"  Урок в {TuesdayStudents[key][1]}  {TuesdayStudents[key][0]}\n[Написать сообщение](tg://user?id={key})", parse_mode='Markdown')

        if day == 'Wednesday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

        if day == 'Thursday':
            for key in ThursdayStudents:
                bot.send_message(message.chat.id, f"  Урок в {ThursdayStudents[key][1]}  {ThursdayStudents[key][0]}\n[Написать сообщение](tg://user?id={key})", parse_mode='Markdown')

        if day == 'Friday':
            for key in FridayStudents:
                bot.send_message(message.chat.id, f"  Урок в {FridayStudents[key][1]}  {FridayStudents[key][0]}\n[Написать сообщение](tg://user?id={key})", parse_mode='Markdown')

        if day == 'Saturday':
            for key in SaturdayStudents:
                bot.send_message(message.chat.id, f"  Урок в {SaturdayStudents[key][1]}  {SaturdayStudents[key][0]}\n[Написать сообщение](tg://user?id={key})", parse_mode='Markdown')

        if day == 'Sunday':
            bot.send_message(message.chat.id, "А сегодня выходной! \nИди отдыхай  🙌 ☺️ ")

    else:
        bot.send_message(message.chat.id, "Извините, у вас нет прав доступа 👨‍💻")


@bot.message_handler(content_types=['text'])
@analytics
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Да, все получается ✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, f"Cпасибо, отправил ответ 🤖", reply_markup=markup)

        markup2 = types.InlineKeyboardMarkup(row_width=3)
        markup2.add(types.InlineKeyboardButton('OK', callback_data='lesson'))
        bot.send_message(1891281816, f"{message.from_user.first_name} ✅ Урок будет\n[Написать сообщение](tg://user?id={message.chat.id})\n\nВоспользуйтесь командой /less", parse_mode='Markdown')

    elif get_message_bot == 'Нет, не получится ⛔':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id, f"🤖 Если нужно перенести урок, то можно написать мне @ilandroxy или воспользоваться командой /calendly", reply_markup=markup)
        bot.send_message(1891281816, f"{message.from_user.first_name} ⛔ Урока не будет\n[Написать сообщение](tg://user?id={message.chat.id})\n\nВоспользуйтесь командой /less", parse_mode='Markdown')


    elif get_message_bot == 'Какая-то ошибка, у нас сегодня нет урока':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id, f"Sorry, возможно 🤖 напутал с расписанием... Пробую исправить!", reply_markup=markup)
        bot.send_message(1891281816, f"{message.from_user.first_name} ‼️ Что-то не так с расписанием, надо проверить.\n[Написать сообщение](tg://user?id={message.chat.id})\n\nВоспользуйтесь командой /less", parse_mode='Markdown')

    elif get_message_bot == 'Прочитано ✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Контакты')
        btn2 = types.KeyboardButton('Репетитор')
        btn3 = types.KeyboardButton('Мои проекты')
        btn4 = types.KeyboardButton('Записаться на урок')
        btn5 = types.KeyboardButton('Получить файл с урока')
        markup.add(btn1, btn2, btn3, btn4, btn5)


        bot.send_message(message.chat.id, f"Спасибо, что читаете 🤖", reply_markup=markup)
        bot.send_message(1891281816, f"{message.from_user.first_name} Уведомлен ✅🤖\n\n[Написать сообщение](tg://user?id={message.chat.id})", parse_mode='Markdown')

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

    elif get_message_bot == "Контакты":
        send_message1 = "*Мои контакты:*\n\n" \
                        "[Telegram](t.me/ilandroxy)\n\n[WhatsApp](wa.me/message/JSXJ2NLWTVNFC1)\n\n[Discord](https://discordapp.com/users/ilandroxxy#6249) ilandroxxy#6249\n\n" \
                        "[Zoom](https://us04web.zoom.us/j/2402871810?pwd=OVdGQkE2ODIvWm1WNk5EdStQR1o4UT09)\n\n" \
                        "[Профиль Авито](www.avito.ru/user/590293c00d3ab79d83e929a6731df164/profile?src=sharing)\n\n[YouTube](https://m.youtube.com/channel/UCcORhBL494aSLcyIODjOG0A)\n\n" \
                        "[GitHub](https://github.com/ilandroxxy)\n\nРабочий телефон: +7 (995) 437–52–59\n\nEmail: collegehacksbot@gmail.com\n\n" \
                        "Воспользуйтесь моим Telegram ботом, чтобы пройти курс по разработке чат ботов @JustDoItMotherBot🤖"
        bot.send_message(message.chat.id, send_message1, parse_mode='Markdown', disable_web_page_preview=True)

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


# Добавляем файлы учеников
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
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton(f"Твой файл: {Students[key]}", url=f"https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons/{Students[key]}"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        elif message.chat.id in Me:
            message_text = "Воспользуйтесь командой /homework чтобы получить домашнее задание."
            bot.send_message(message.chat.id, message_text)
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton(f"Папка: lessons", url=f"https://github.com/ilandroxxy/ilandroxy_bot/blob/main/ilandroxy_Bot/lessons"))
            sti = open('photo/SendFileSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti, reply_markup=markup)

        else:
            message_text = 'Извините, по-моему вас нет в системе! Ожидайте...'
            bot.send_message(message.chat.id, message_text)
            sti = open('photo/WaitSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)

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

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)
