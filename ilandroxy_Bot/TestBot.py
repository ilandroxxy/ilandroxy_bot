import random
import telebot
from telebot import types

# id: [Имя заказчика, Номер телефона, Город, Сроки, Описание]
Customer = {}

bot = telebot.TeleBot('5734914555:AAHshNFPEP2SszdrAKbfm_6uKZI4waH1Nbs')
# test 5734914555:AAHshNFPEP2SszdrAKbfm_6uKZI4waH1Nbs

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup()

    if call.data == 'next1':
        bot.send_message(call.message.chat.id, 'Оставьте свой рабочий номер для контактов')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Далее", callback_data='next2'))

            text_message = message.text
            Customer[message.chat.id].append(text_message)
            bot.send_message(message.chat.id, 'Номер записан.', reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'next2':
        bot.send_message(call.message.chat.id, 'Какой будет город проведения работ?')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Далее", callback_data='next3'))

            text_message = message.text
            Customer[message.chat.id].append(text_message)
            bot.send_message(message.chat.id, 'Город записан.', reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'next3':
        bot.send_message(call.message.chat.id, 'В какие сроки надо уложиться?')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Далее", callback_data='next4'))

            text_message = message.text
            Customer[message.chat.id].append(text_message)
            bot.send_message(message.chat.id, 'Сроки записан.', reply_markup=markup)

        bot.register_next_step_handler(call.message, message_input)

    elif call.data == 'next4':
        bot.send_message(call.message.chat.id, 'Опишите задачу или ТЗ в одном сообщение (можно указать ссылку)')

        @bot.message_handler(content_types=['text'])
        def message_input(message):

            text_message = message.text
            Customer[message.chat.id].append(text_message)
            bot.send_message(message.chat.id, 'Спасибо за регистрацию Заказа, ищем исполнителей и предложим вам решения!')

        bot.register_next_step_handler(call.message, message_input)



@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Составить заказ для исполнителя')
    btn2 = types.KeyboardButton('Мои заказы')
    btn3 = types.KeyboardButton('Зарегистрироваться как Исполнитель')
    markup.add(btn1, btn2, btn3)

    text_message = f'Добро пожаловать, пройдите этап *регистрации*:'
    bot.send_message(message.chat.id,  text_message, parse_mode='Markdown', reply_markup=markup)





@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Составить заказ для исполнителя':

        Customer[message.chat.id] = []
        bot.send_message(message.chat.id, 'Представьтесь как вас зовут (ФИО)')

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Далее", callback_data='next1'))

            text_message = message.text
            Customer[message.chat.id].append(text_message)
            bot.send_message(message.chat.id, 'ФИО записали, идем дальше', reply_markup=markup)

        bot.register_next_step_handler(message, message_input)

    if get_message_bot == 'Мои заказы':
        message_text = "\n\n".join(Customer[message.chat.id])
        bot.send_message(message.chat.id, f'Здравствуйте, {Customer[message.chat.id][0]}!\nВот твои заказы:\n{message_text}')

    if get_message_bot == 'Зарегистрироваться как Исполнитель':
        bot.send_message(message.chat.id, 'Пока находится в разработке')










bot.polling(none_stop=True)
