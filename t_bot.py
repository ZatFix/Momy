import telebot
import datetime
from pyowm import OWM
from pyowm.utils.config import get_default_config

owm =   OWM('23232775d430e5fe2ac9a9c2cbdb8410')
language = get_default_config()
language['language'] = 'ru'

bot = telebot.TeleBot('5564840509:AAEr9ZxfMHmN-WDsepBGJGaQ0T7UPDN6Lrg')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('hello', 'bye', 'date')
reply_markup =keybord1
temperature = owm





@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"lets gooo", reply_markup=keybord1)


@bot.message_handler(content_types=['text'])
def send_text(messege):
    global a
    if messege.text.lower() == 'hello':
        bot.send_message(messege.chat.id, 'Hi sweeties!')
    elif messege.text.lower() == 'bye':
        bot.send_message(messege.chat.id, 'See you later!')
    elif messege.text.lower() == 'date':
        bot.send_message(messege.chat.id, datetime.date.today())
    elif messege.text.lower() == 'weather':
        bot.send_message(messege.chat.id, 'choose the city')
        a = True
    elif a ==True:
        manager = owm.weather_manager()
        observation = manager.weather_at_place(messege.text)
        weather = observation.weather
        z = weather.detailed_status
        x = weather.clouds
        c = weather.temperature('celsius').get('temp')
        v = weather.temperature('celsius').get('temp_max')
        b = weather.temperature('celsius').get('temp_min')
        n = weather.rain
        m = weather.wind()
        bot.send_message(messege.chat.id, f"Сейчас {z}\nОблачность составляет {x}%\nТемпература: {c}\nМаксимальная температура: {v}\nМинимальная температура: {b}\nКоличество осадков: {n}\nВетер: {m}")
        a = False



bot.polling()
