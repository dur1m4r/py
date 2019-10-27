import telebot

bot = telebot.TeleBot('478286981:AAEz_yMsGgQnlXx8OlH0mQe53iB1-YMFbf8')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Next game', 'League position')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Next game':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'League position':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()

