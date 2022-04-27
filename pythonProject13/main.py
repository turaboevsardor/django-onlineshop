import telebot
from telebot import types
import data

bot = telebot.TeleBot('5290573945:AAEpEfM-MfuBYtKVCGFF3tY4FCQJ-AEIYHU')

# Создаем словарь для временного хранения продуктов при добавлении
product = {'name': None,
		   'photo_id': None,
		   'price': None}


@bot.message_handler(commands=['start'])
def start(message):
	user_id = message.from_user.id
	t = data.User()
	t.add_user(user_id)

	bot.send_message(user_id, 'Добро пожаловать в наш бот')


# Создаем обработчик команды /add который поможет добавлять продукты
@bot.message_handler(commands=['add'])
# Получаем имя продукта
def get_name(message):
	user_id = message.from_user.id

	bot.send_message(user_id, 'Название продукта')
	bot.register_next_step_handler(message, get_image)


# Получив имя продукта направляем на следующий этап для получения фото
def get_image(message):
	product['name'] = message.text
	user_id = message.from_user.id

	bot.send_message(user_id, 'Отправьте фото')
	bot.register_next_step_handler(message, image)


# Получили фото, направляем на следующий этап для получения цены
def image(message):
	# Проверка если наше сообщение содержит фото, то берем его айди и сохраняем в базу
	if message.content_type == "photo":
		product['photo_id'] = message.photo[-1].file_id
		user_id = message.from_user.id

		bot.send_message(user_id, 'Цена')
		bot.register_next_step_handler(message, get_price)

	else:
		pass


# Получили цену и на этоп последовательность добавления продуктов заканчивается
def get_price(message):
	product['price'] = int(message.text)
	user_id = message.from_user.id

	t = data.User()
	t.add_product(product['name'], product['photo_id'], product['price'])

	bot.send_message(user_id, 'Продукт успешно добавлен')
#######


######


bot.polling(non_stop=True)
