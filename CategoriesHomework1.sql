CREATE TABLE IF NOT EXISTS orders(
ID SERIAL PRIMARY KEY,
user_id INTEGER,
status_id INTEGER
)
# В statuses, В users, ОТ order_items

CREATE TABLE IF NOT EXISTS statuses(
ID SERIAL PRIMARY KEY,
name VARCHAR(10) NOT NULL UNIQUE
)
#ОТ order_items

CREATE TABLE IF NOT EXISTS users(
ID SERIAL PRIMARY KEY,
name VARCHAR(24),
email VARCHAR(24) UNIQUE
)
#ОТ users

CREATE TABLE IF NOT EXISTS categories(
ID SERIAL PRIMARY KEY
name VARCHAR(24) UNIQUE
)
# ОТ products

CREATE TABLE IF NOT EXISTS products(
ID SERIAL PRIMARY KEY,
title VARCHAR(36),
descr VARCHAR(140),
category_id INTEGER NOT NULL,
FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
)
#ОТ order_items, В categories

CREATE TABLE IF NOT EXISTS order_items(
ID SERIAL PRIMARY KEY,
order_id INTEGER NOT NULL,
FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
product_id INTEGER NOT NULL,
FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
)
#В orders, В products


