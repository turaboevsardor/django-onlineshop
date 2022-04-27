# import sqlite3
# conn = sqlite3.connect('dostavka.db')
# sql = conn.cursor()
#
# #sql.execute('CREATE TABLE users_list(user_id integer ,username TEXT);')
# #sql.execute('INSERT INTO users_list(user_id,username)VALUES (1234567,"alex");')
# #sql.execute('SELECT*FROM users_list;')
# conn.commit()
# conn.close()

import sqlite3
conn = sqlite3.connect('dostavka.db')
sql = conn.cursor()
sql.execute('CREATE TABLE user1 (user_id INTEGER);')
#sql.execute('CREATE TABLE cart (users_id INTEGER ,product TEXT,quantity INTEGER )')
conn.commit()
conn.close()
class User:
    def add_user(self,user_ids):
        conn = sqlite3.connect('dostavka.db')
        sql = conn.cursor()
        u = sql.execute('SELECT * FROM users;')
        if user_ids not in u:
            sql.execute(f'INSERT INTO users_id(user_id)VALUES ({user_ids})')
            conn.commit()

        else:
            pass







