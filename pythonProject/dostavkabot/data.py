import sqlite3

#
# conn = sqlite3.connect('dostavka.db')
# sql = conn.cursor()
# sql.execute('CREATE TABLE products (name TEXT , photo_id TEXT, price REAL);')
# sql.execute('CREATE TABLE users (user_id INTEGER);')
# sql.execute('CREATE TABLE cart (user_id INTEGER, product TEXT, quantity INTEGER);')
# conn.commit()
# conn.close()

# Создаем класс для удобной работы с базой данных
class User:
    # Создаем метод добавления пользователя в базу
    def add_user(self, user_ids):
        # Сначала подключаемся к самой базе
        conn = sqlite3.connect('dostavka.db')
        sql = conn.cursor()
        u = sql.execute('SELECT * FROM users;')

        # Проверяем есть нет ли пользователя в базе
        if user_ids not in u:
            sql.execute(f'INSERT INTO users (user_id) VALUES ("{user_ids}");')
            # Сохраняем действия
            conn.commit()
        else:
            pass

    # Создаем метод добавления продуктов
    def add_product(self, text, photo_ids, prices):
        # Сначала подключаемся к самой базе
        conn = sqlite3.connect('dostavka.db')
        sql = conn.cursor()

        # Отправляем SQL запрос добавления имени, фото и цены продукта в базу
        sql.execute(f'INSERT INTO products VALUES ("{text}", "{photo_ids}", "{prices}");')

        # Сохраняем действия
        conn.commit()

    # Получаем все названия товаров из базы чтобы пользователи смогли видеть их
    def get_products(self):
        # Сначала подключаемся к самой базе
        conn = sqlite3.connect('dostavka.db')
        sql = conn.cursor()

        # Отправляем SQL запрос для получения только названия продуктов
        p = sql.execute('SELECT name FROM products;')

        k = list(p.fetchall())

        # Сохраняем действия
        conn.commit()

        return k

    # Если пользователь нажал на определенный товар, то ему отправляем инфо про него
    def get_info(self, name):
        # Сначала подключаемся к самой базе
        conn = sqlite3.connect('dostavka.db')
        sql = conn.cursor()

        # Отправляем SQL запрос для получения фото и цену конкретного товара
        p = sql.execute(f'SELECT * FROM products WHERE name = "{name}";')

        k = list(p.fetchall())
        # Сохраняем действия
        conn.commit()

        return k

    # Этот метод отвечает за добавление продуктов в корзину пользователя
    def get_cart(self, user_id, product_name, product_count):
        conn = sqlite3.connect('dostavka.db')
        sql = conn.cursor()

        # Отправляем SQL запрос добавления
        p = sql.execute(f'INSERT INTO cart VALUES ("{user_id}", "{product_name}", "{product_count}");')

        # Сохраняем действия
        conn.commit()

    # Этот метод показывает все корзину пользователя
    def full_cart(self, user_id):
        conn = sqlite3.connect('dostavka.db')
        sql = conn.cursor()

        # Отправляем SQL запрос ддля получения корзины конкретного пользователя
        p = sql.execute(f'SELECT product, quantity FROM cart WHERE user_id=  "{user_id}";')

        o = list(p.fetchall())
        # Сохраняем действия
        conn.commit()

        return o