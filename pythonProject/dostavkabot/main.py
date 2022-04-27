import telebot
from telebot import types
import data

bot = telebot.TeleBot('5290573945:AAEpEfM-MfuBYtKVCGFF3tY4FCQJ-AEIYHU')

# Создаем словарь для временного хранения продуктов при добавлении
product = {'name': None,
           'photo_id': None,
           'price': None}
user_cart = {'user_id': None,
             'product_name': None,
             'product_count': None}


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    t = data.User()
    t.add_user(user_id)

    # Получаем список состящий из названием
    o = data.User().get_products()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for button in o:
        keyboard.add(*button)
    keyboard.add(types.KeyboardButton('Корзина'))

    bot.send_message(user_id, 'Добро пожаловать в наш бот', reply_markup=keyboard)


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


@bot.message_handler(content_types=['text'])
def text(message):
    # Получаем все товары из базы
    o = data.User().get_products()
    user_cart['user_id'] = message.from_user.id

    # Проверяем есть ли у нас в базе товар с именем который отправит пользователь
    if tuple([message.text]) in o:
        user_cart['product_name'] = message.text
        product = data.User().get_info(message.text)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

        # Создаем кнопки для выбора количества
        for i in range(1, 11):
            keyboard.add(str(i))

        # Если то что выбрал пользователь есть у нас в базе то отправляем ему фото, имя и цену товара
        # Метод .send_photo(кому, какое фото, текст к нему, кнопки(если есть)) отвечает за отправку фото и текст к нему(если имеется)
        bot.send_photo(message.from_user.id, f'{product[0][1]}', f'{product[0][0]}\n\nЦена: {product[0][-1]}',
                       reply_markup=keyboard)

        bot.register_next_step_handler(message, get_quantity)

    # если пользователь нажмет на кнопку корзина мв из базы достаем его товары
    elif message.text == 'Корзина':
        user_id = message.from_user.id

        # Здесь .full_cart(user_id) этот метод как аргумент будет братьайди юзера чтобы вывести конкретно его товары
        t = data.User().full_cart(user_id)
        cart_items = "Ваша корзина:\n\n{name} \n{count} шт \n\n"

        for i in t:
            korzina = cart_items.format(name=i[0],
                                        count=i[1])
        print(korzina)

        bot.send_message(user_id, korzina)


def get_quantity(message):
    user_id = message.from_user.id
    count = message.text
    user_cart['product_count'] = int(count)

    data.User().get_cart(user_cart['user_id'], user_cart['product_name'], user_cart['product_count'])
    bot.send_message(user_id, 'Продукт успешно добавлен')

    # После добавления продукта в корзину нас перекидывет на этап выбора продуктов
    start(message)

bot.polling(non_stop=True)