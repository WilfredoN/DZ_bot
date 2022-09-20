import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_ready = types.KeyboardButton("Отправить задание✅")
    markup.add(button_ready)
    bot.send_message(message.chat.id, text="Привет.\nПредлагаем свои услуги по "
                                           "помощи в домашних заданиях.\nПришлите "
                                           "само задание и все необходимые данные", reply_markup=markup)


homeworkArray = list()


@bot.message_handler(func=lambda m: True)
def homework_append(message):
    while message.text != 'Отправить задание✅':
        homeworkArray.append(message.text)
        bot.forward_message('@dzorders', message.chat.id, 'homeworkArray)


bot.polling(none_stop=True)