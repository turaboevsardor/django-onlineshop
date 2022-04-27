import telebot
from telebot import types

bot = telebot.TeleBot('5157144805:AAHqwIlxZ5AJmUr6LOEKNfyNLfq4c4U2qko')
users = {}
@bot.message_handler(commands=['start'])
def start(message):



    user_id = message.from_user.id
    kn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kn1 = types.KeyboardButton('registratsiya')
    kn2 = types.KeyboardButton('polzovatel')
    kn3 = types.KeyboardButton('raqami')
    kn.add(kn1,kn2,kn3)
    text = 'Hello ,nice to meet you'
    bot.send_message(user_id,text, reply_markup = kn)





@bot.message_handler(commands=['help'])
def help (message):
    user_id = message.from_user.id
    text = 'Can I help you'
    bot.send_message(user_id, text)


@bot.message_handler(commands=['stickers'])
def stickers(message):
    user_id = message.from_user.id
    stickers = 'stickers'
    user_id = message(user_id,stickers)






@bot.message_handler(content_types=['text'])
def text (message):
    user_id = message.from_user.id
    if 'registratsiya' in message.text:
        text = 'kimmi qoshamz'
        bot.send_message(user_id, text)
        bot.register_next_step_handler(message,get_name)
    elif 'polzovatel'  in message.text:
        i = []
        for k,v in users.items():
            i.append([k,v])
        print(i)
        bot.send_message(user_id,'{} {}'.format(i[0],i[1]))



    else:
        bot.send_message(user_id,message.text)

def get_name(message):
    user_id = message.from_user.id
    users['name'] = user_id
    bot.send_message(user_id,'kontakt')
    bot.register_next_step_handler(message,get_contact)

def get_contact(message):
    user_id = message.from_user.id
    user_contact = message.text
    users['kontakt'] = user_contact
    bot.send_message(user_id,'polzovatel qoshildi')








bot.polling(none_stop=True)
