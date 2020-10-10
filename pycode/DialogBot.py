import telebot
bot = telebot.TeleBot('1275323193:AAHhG1UN1O-cSgcWNTg3db08c95TDgOOLY0')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши "/help" ')

bot.polling(none_stop=True, interval=0)