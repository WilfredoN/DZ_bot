import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
homework_array = list()
homework_images = list()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    homework_array.clear()
    homework_images.clear()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_ready = types.KeyboardButton("Отправить задание")
    markup.add(button_ready)
    bot.send_message(message.chat.id, text="Привет.\nПредлагаем свои услуги по "
                                           "помощи в домашних заданиях.\nПришлите "
                                           "само задание и все необходимые данные", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def homework_append(message):
    if message.text == 'Отправить задание':
        bot.reply_to(message, "Задание успешно отправлено, ожидайте ответа!")
        forwardingMessage(homework_array, message, homework_images)
        homework_array.clear()
        homework_images.clear()
    else:
        homework_array.append(message.message_id)


@bot.message_handler(content_types=['photo'])
def image_append(message):
    homework_images.append(message.message_id)


def forwardingMessage(homework_array, message, homework_images):
    for i in range(0, len(homework_array)):
        bot.forward_message('@dzorders', message.chat.id, homework_array[i])
    for j in range(0, len(homework_images)):
        bot.forward_message('@dzorders', message.chat.id, homework_images[j])


bot.polling(none_stop=True)
