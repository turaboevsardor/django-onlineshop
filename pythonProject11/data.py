import sqlite3
conn = sqlite3.connect('cars.db')

c = conn.cursor()
c.execute('create table my_cars(model text,name text,year integer);')
c.execute('INSERT INTO mycars(model,name,year)VALUES ("tesla","x",2022);')
conn.commit()
conn.close()
