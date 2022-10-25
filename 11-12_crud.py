from crud import CRUDCategory
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from CategoriesHomeword2 import Category
from settings import DATABASE_URL

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.functions import now
from sqlalchemy import create_engine, select

class CRUD(object):

def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session) #здесь передаем сессию
        return wrapper



class CRUDCategory(object):
    @staticmethod
    @create_session
    def add(category: Category, session=None) -> Optional[Category]:
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(category)
            return category