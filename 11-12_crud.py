from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from CategoriesHomeword2 import Category, User, Base
from settings import DATABASE_URL
#from crud import CRUDCategory
from contextlib import contextmanager

# add get delete update для каждой таблицы


engine = create_engine('sqlite://')



@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations.
    Использовать если нужно закоммитить изменения в бд. Если read без коммита то лучше session, sessio_scope бессмысленнен """
    session = Session(engine)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



def first_data_for_new_database():
    with session_scope() as session:

         subzero = User(
            name="subzero",
            email="iceall@sqlalchemy.org"
         )
         shaokahn = User(
            name="shaokahn",
            email="smashall@sqlalchemy.org"
         )
         melina = User(
            name="melina",
            email="melinaemail@gmail.com"
         )

         session.add_all([subzero, shaokahn, melina]) #+1 пробел чтобы было внутри with и сработал коммит
    print(read_data())

def add_data(users):
    with session_scope() as session:
        session.add_all([users]) #принимает все типы, юзерс может быть любым типом


def read_data():
    with Session(engine) as session:
        acquired = session.query(User.name).all()
    return acquired

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    first_data_for_new_database()
