import telebot
import datetime


bot = telebot.TeleBot('5564840509:AAEr9ZxfMHmN-WDsepBGJGaQ0T7UPDN6Lrg')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('hello', 'bye')
reply_markup =keybord1
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"lets gooo", reply_markup=keybord1)


@bot.message_handler(content_types=['text'])
def send_text(messege):
    if messege.text.lower() == 'hello':
        bot.send_message(messege.chat.id, 'Hi sweeties!')
    elif messege.text.lower() == 'bye':
        bot.send_message(messege.chat.id, 'See you later!')


bot.polling()
