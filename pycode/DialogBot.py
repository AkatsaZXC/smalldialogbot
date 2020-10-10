import telebot
bot = telebot.TeleBot('your token')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем могу помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши "/help" ')

bot.polling(none_stop=True, interval=0)

name = ''   # first name of person
surname = ''    # surname of person
age = 0 # age of person

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Как Вас зовут?')
        bot.register_next_step_handler(message,get_name)
    else:
        bot.send_message(message.from_user.id, 'Напишите "/reg"')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message('Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = f'Тебе {str(age)} лет, тебя зовут {name} {surname}?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

