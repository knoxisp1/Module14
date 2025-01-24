import sqlite3

connection = sqlite3.connect("initiate_db.db")
cursor = connection.cursor()
#Создаем таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)

''')
# Добавляем Продукты.
for i in range(1, 5):
    cursor.execute("INSERT INTO Products(title,description,price) VALUES(?,?,?)",
                   (f"Продукт {i}", f"Описание {i}", f"Цена {i * 100}"))
    connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()
