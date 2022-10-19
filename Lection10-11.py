SQL SHELL

Server localhost
database enter
port enter
Username

Для переключения языка чтобы ру не был иероглифами
psql \! chcp 1251
set client_encoding='win1251';
Повторить команду два раза, сработает

create user dev with password 'mypassword';

create database bh34kate owner dev;

\dt - схема, имя, тип, владелец, хранение
\dt+ подробнее
\l - список созданных бд

\connect bh34kate

CREATE TABLE IF NOT EXISTS categories(
ID SERIAL PRIMARY KEY,
name VARCHAR(24) NOT NULL UNIQUE;
)

CREATE TABLE IF NOT EXISTS products(
ID SERIAL PRIMARY KEY,
name VARCHAR(24) NOT NULL UNIQUE,
descr VARCHAR(512) NOT NULL,
price DECIMAL(6,2) DEFAULT (100.00), #6 общее количество цифр, 2 количество цифр после запятой
is_published BOOLEAN DEFAULT(false),
category_id INTEGER NOT NULL,
FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE;
)


INSERT INTO categories(name) VALUES('Food');
INSERT INTO categories(name) VALUES('Drinks');
INSERT INTO products(name, descr, price, category_id) VALUES('Beaf', 'Very cold', 50.00, 2);
INSERT INTO products(name, descr, price, category_id) VALUES('Bear', 'Very big', 90.00, 2);

SELECT * FROM categories;

SELECT * FROM products WHERE category_id=1 ORDER BY id DESC;
SELECT * FROM products GROUP BY id;



SELECT * FROM categories JOIN products ON products.category_id = categories_id;


CREATE TABLE IF NOT EXISTS orders(
id SERIAL PRIMARY KEY,
product_id INTEGER NOT NULL,
FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE);
)
INSERT INTO orders(product_id) values(4);



РАБОТА В ПАЙЧАРМ В sqlite3

import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(24) NOT NULL UNIQUE
);    
''')
conn.commit()


SQLiteStudio

Database - add database -(pycharm projects - python ver - файл бд)

#cur.executemany('''
#INSERT INTO categories(name) VALUES(?);
#''', (('Food, '), ('Drinks', )))
#conn.commit

cur.execute('''
SELECT * FROM categories WHERE id=?;
''')
print(cur.fectchall())
fetchmany - нужно указать количество, например два. Выдаст первых два, потом следующие два

ALCHEMY
pip install sqlalchemy alembic psycopg2-binary
python.exe -m pip install --upgrade pip

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, INTEGER, VARCHAR, ForeignKey, Boolean
from sqlalchemy.sql.functions import now
from sqlalchemy import create_engine  #движок для создания таблиц

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(Integer, primary_key=True)
    name = (VARCHAR(24), nullable=False, unique=True)


class Product(Base):
    __tablename__: str = 'products'

    id = Column(Integer, primary_key=True)
    name = (VARCHAR(24), nullable=False, unique=True)
    descr = (VARCHAR(512), nullable=False)
    is_published = Column(Boolean, default=False)
    date_published = Column(TIMESTAMP, default=now())
#если импортировано from sqlalchemy.sql.functions import now то значение нау будет выставлено
# не на уровне бд а на уровне кода
    category_id = Column(INTEGER, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

СОЗДАНИЕ ТАБЛИЦ
engine = create_engine('postgressql://kate:teacup@local:5432/db34kate') #и добавить ссылку для подключения к бд. Через +
#можно добавить движок но create_engine включен по умолчанию

ИНИЦИАЛИЗИРУЕМ alembic
alembic init alembic #создаем файл, второй аолембик этот папка где будет файл
Создаем внутри проекта файл settings.py
Пихаем туда DATABASE_URL: str = 'postgressql://kate:teacup@local:5432/db34kate'
Настраиваем. В alembic.ini строка 58.
sqlalchemy.url = driver://user:pass@localhost/dbname
Комментируем строку:
В папке alembic открываем env.py и на 8 строке импортируем
from settings import DATABASE_URL
from models import Base
Далее строка 23-24, комментируем target_metadata = None
и раскомментируем target_metadata = mymodel.Base.metadata
но меняем на target_metadata = Base.metadata

Потом нужны run_migrations_offline и run_migrations_online
Строка 44, url. Это теперь url = DATABASE_URL

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = DATABASE_URL #добавляем урл который закомментирован в ини файле и даем значение
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )


МИГРАЦИИ ЧЕРЕЗ alembic

alembic revision --autogenerate -m "" # -m чтобы в кавычках указать комментарий
alembic upgrade/downgrade номерверсии revision из файла миграции(alembic/versions)
Если мигрироваться в самую новую версию то alembic upgrade head

