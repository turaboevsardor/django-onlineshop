import telebot
from telebot import types
bot = telebot.TeleBot('5290573945:AAEpEfM-MfuBYtKVCGFF3tY4FCQJ-AEIYHU')
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    text = 'OK no problem'
    bot.send_message(user_id, text)


@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.from_user.id
    text = 'Can I help you'
    bot.send_message(user_id, text)
    knp = types.InlineKeyboardMarkup()
    url1 = types.InlineKeyboardButton(text='Order', callback_data='Order')
    url2 = types.InlineKeyboardButton(text='HOW many', callback_data='HOW many')
    knp.add(url1, url2)
    bot.send_message(user_id, 'FOOD', reply_markup=knp)

@bot.message_handler(commands=['photo'])
def photo(message):
    user_id = message.from_user.id
    text = 'Look at the photo '
    bot.send_message(user_id, text)
    keyboard = types.InlineKeyboardMarkup()
    url1 = types.InlineKeyboardButton(text='EVOS', url='https://app.evos.uz/')
    keyboard.add(url1)
    bot.send_message(user_id, 'this link', reply_markup=keyboard)



@bot.message_handler(commands=['view'])
def view(message):
    user_id = message.from_user.id
    text = 'Halal or Haram '
    keyboard = types.InlineKeyboardMarkup()
    url1 = types.InlineKeyboardButton(text='Halal or Haram', url='HALAL')
    keyboard.add(url1)
    bot.send_message(user_id,text, 'GOOD', reply_markup=keyboard)


bot.polling(none_stop=True)
