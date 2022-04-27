import sqlite3

conn = sqlite3.connect('kino.db')
sql = conn.cursor()
# sql.execute('CREATE TABLE products (name TEXT , photo_id TEXT, price REAL);')
# sql.execute('CREATE TABLE users (user_id INTEGER);')
# sql.execute('CREATE TABLE cart (user_id INTEGER, product TEXT, quantity INTEGER);')
conn.commit()
conn.close()


class User:
    def add_user(self, user_ids):

        conn = sqlite3.connect('kino.db')
        sql = conn.cursor()
        u = sql.execute('SELECT * FROM users;')


        if user_ids not in u:
            sql.execute(f'INSERT INTO users (user_id) VALUES ("{user_ids}");')

            conn.commit()
        else:
            pass


    def add_product(self, text, photo_ids, prices):

        conn = sqlite3.connect('kino.db')
        sql = conn.cursor()


        sql.execute(f'INSERT INTO products VALUES ("{text}", "{photo_ids}", "{prices}");')


        conn.commit()


    def get_products(self):

        conn = sqlite3.connect('kino.db')
        sql = conn.cursor()

        p = sql.execute('SELECT name FROM products;')

        k = list(p.fetchall())


        conn.commit()

        return k


    def get_info(self, name):

        conn = sqlite3.connect('kino.db')
        sql = conn.cursor()


        p = sql.execute(f'SELECT * FROM products WHERE name = "{name}";')

        k = list(p.fetchall())

        conn.commit()

        return k

    # Этот метод отвечает за добавление продуктов в корзину пользователя
    def get_cart(self, user_id, product_name, product_count):
        conn = sqlite3.connect('kino.db')
        sql = conn.cursor()

        # Отправляем SQL запрос добавления
        p = sql.execute(f'INSERT INTO cart VALUES ("{user_id}", "{product_name}", "{product_count}");')


        conn.commit()


    def full_cart(self, user_id):
        conn = sqlite3.connect('kino.db')
        sql = conn.cursor()

        # Отправляем SQL запрос ддля получения корзины конкретного пользователя
        p = sql.execute(f'SELECT product, quantity FROM cart WHERE user_id=  "{user_id}";')

        o = list(p.fetchall())

        conn.commit()

        return o