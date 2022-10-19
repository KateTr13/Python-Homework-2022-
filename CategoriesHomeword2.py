from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, INTEGER, VARCHAR, ForeignKey, Boolean
from sqlalchemy.sql.functions import now
from sqlalchemy import create_engine


Base = declarative_base()


class Order(Base):
    __tablename__: str = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status_id = (Integer, ForeignKey('statuses.id', ondelete='CASCADE')nullable=False)


class Status(Base):
    __tablename__: str = 'statuses'

    id = Column(Integer, primary_key=True)
    name = (VARCHAR(24), nullable=False, unique=True)


class User(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    name = (VARCHAR(24), nullable=False)
    email = (VARCHAR(24), nullable=False, unique=True)


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(Integer, primary_key=True)
    name = (VARCHAR(24), nullable=False, unique=True)


class Product(Base):
    __tablename__: str = 'products'

    id = Column(Integer, primary_key=True)
    title = (VARCHAR(36), nullable=False)
    descr = (VARCHAR(140))
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class Order_item(Base):
    __tablename__: str = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = (Integer, ForeignKey('products.id', ondelete='CASCADE')nullable=False)

