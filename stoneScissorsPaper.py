import telebot
import random

from telebot import types

bot = telebot.TeleBot('6303626612:AAEqfKVfl5rVw4-yiZts0QJoVr6CkvOP6Qs')
print('Бот запущен')
winHuman = [0]
winBot = [0]


# Обработка команды start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Камень')
    btn2 = types.KeyboardButton('Ножницы')
    btn3 = types.KeyboardButton('Бумага')
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton('Правила')
    markup.row(btn4)
    print('......')
    file = open('./all.png', 'rb')
    bot.send_photo(message.chat.id, file, 'Выбери камень, ножницы или бумага 🤭', reply_markup=markup)


def button_rek(message, winHuman1 = winHuman, winBot1 = winBot):
    roshambo = ['Камень', 'Ножницы', 'Бумага']
    random_roshambo = random.choice(roshambo)
    # Действия с кнопкапками
    win1 = random_roshambo == 'Камень' and message.text == 'Бумага'
    win2 = random_roshambo == 'Бумага' and message.text == 'Ножницы'
    win3 = random_roshambo == 'Ножницы' and message.text == 'Камень'
    lose1 = random_roshambo == 'Камень' and message.text == 'Ножницы'
    lose2 = random_roshambo == 'Бумага' and message.text == 'Камень'
    lose3 = random_roshambo == 'Ножницы' and message.text == 'Бумага'
    if random_roshambo == message.text:
        bot.send_message(message.chat.id, random_roshambo)
        bot.send_message(message.chat.id, 'Ничья, попробуй снова!')
        bot.send_message(message.chat.id, f'Счет {winHuman1[0]}: {winBot1[0]}')
    elif win1 or win2 or win3:
        bot.send_message(message.chat.id, random_roshambo)
        bot.send_message(message.chat.id, 'Ура! Победа!')
        winHuman1 = [winHuman1[0] + 1]
        winHuman.clear()
        winHuman.append(winHuman1[0])
        bot.send_message(message.chat.id, f'Счет {winHuman1[0]}: {winBot1[0]}')
    elif lose1 or lose2 or lose3:
        bot.send_message(message.chat.id, random_roshambo)
        bot.send_message(message.chat.id, 'Извини, ты проиграл)')
        winBot1 = [winBot1[0] + 1]
        winBot.clear()
        winBot.append(winBot1[0])
        bot.send_message(message.chat.id, f'Счет {winHuman1[0]}: {winBot1[0]}')
    else:
        bot.send_message(message.chat.id, 'Чтобы сыграть введи команду <b><i>/start</i></b>', parse_mode='html')


# Обработка команды link
@bot.message_handler(commands=['link'])
def link(message):
    bot.send_message(message.chat.id, 'https://t.me/last_pc_bot')


# Обработка введенного текста
@bot.message_handler()
def info(message):
     if message.text.lower() == 'привет':
         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
     else:
         button_rek(message)


bot.polling(none_stop=True)