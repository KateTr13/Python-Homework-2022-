from sqlalchemy.exc import IntegrityError

from CategoriesHomeword2 import Category, Product
from settings import DATABASE_URL

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, INTEGER, VARCHAR, ForeignKey, Boolean, update, delete
from sqlalchemy.sql.functions import now
from sqlalchemy import create_engine, select, and_, or_,

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
#Открываем подключение к бд и потом его нужно будет закрыть
with Session() as session:
    #записываем данные
    category = Category(
        name='Food',
        descr='Description'
    )
    session.add(category)
    try:
        session.commit()
    except IntegrityError

#ИЛИ
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
# Открываем подключение к бд и потом его нужно будет закрыть
def add_category(category: Category) -> Category | None:
    with Session() as session:
    # записываем данные
        category = Category(
            name='Food',
            descr='Description'
        )
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(category)
#Рефреш берет нашу переменную и после успешной записи(после успешного коммита) добавляет новые данные
category = Category(
        name='Food',
        descr='Description'
    )
print(add_category(category))

#Select запрос
def get_category(category_id: int) -> Optional[Category]:
    with Session() as sesion:
        category = session.execute(
            select(Category.name, Category.descr).where(Category_id==category_id)
            #если просто Category то покажет все а не выбранные части
        )
#ИЛИ
    with Session() as sesion:
        category = session.execute(
            select(Category)
            .where(and_(Category_id==category_id, Category_name=='Food'))
            #если просто Category то покажет все а не выбранные части
        )
category = get_category(1)
if category:
    print(category.name, category.descr)
    #print(category.__dict__)

#Сортировка
def all_categories() -> List[Category]:
    with Session() as session:
        categories = session.execute(
            select(Category)
            .order_by(Category.id)
        )
        return [category[0] for category in categories] #выведет в виде словаря
        #return categories.all() #список кортежей с моделями

print(all_categories())



text = 'MENU:\n'
for category in all_categories():
    text += f'{category.id}: {category.name} | {category.descr}\n'
print(text)



def add_product(product: Product) -> Optional[Product]:
    with Session() as session:
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(product)
            return product

product = Product( #записываем товары
    name='Meat',
    descr='Very Cool',
    category_id=1
)
add_product(Product)

#Join запрос чтобы посмотреть товары
def categories_join_products() -> List[Tuple[Category, Product]]
    with Session() as session:
        response = session.execute(
            select(Category, Product)
            .join(Product, Category.id == Product.category_id)
        )
        return response.all()

print(categories_join_products())
#или
#for result in categories_join_products():
#print(result[0].name, result[1].name)

#Запись / update
def update_category(category_id: int, name: str = None, descr: str = None, descr=None) -> bool:
# =None это если не изменилось то оставить по умолчанию. Если новых данных нет то останется как было
    with Session() as session:
        session.execute(
            update(Category)
            .where(Category.id == category_id)
            .values(
                name=name if name else Category.name,
                descr=descr if descr else Category.desr
            )
        )
        try:
            session.commit() #если коммит не удался то будет ошибка
        except IntegrityError:
            return False
        else:
            return True

#ИЛИ

def update_category(category: Category, category_id=None) -> bool:
# =None это если не изменилось то оставить по умолчанию. Если новых данных нет то останется как было
    category = category.__dict__
    del category['sa_instance_state'] #эта штука вылазила в предыдущей версии кода
    with Session() as session:
        session.execute(
            update(Category)
            .where(Category.id == category_id)
            .values(
                **category
            )
        )
        try:
            session.commit() #если коммит не удался то будет ошибка
        except IntegrityError:
            return False
        else:
            return True

print(get_category(1).__dict__)
category.name = 'Еда'
update_category(category)
category = get_category(1)
print(category.name)


def delete_category(category_id: int) -> bool:
    with Session() as session:
        session.execute(
            delete(Category)
            .where(Category.id == category_id)

        )
        session.commit()

delete_category(1)



def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session) #здесь передаем сессию
    return wrapper


@create_session
def add_category(category: Category, session= None) -> Optional[Category]:
#здесь принимаем сессию, но оно должно быть необязательно
    session.add(category)
    try:
        session.commit()
    except IntegrityError:
        return None
    else:
        session.refresh(category)
        return category
#Теперь каждый раз при вызове ф-ии все аргументы внутри этой ф-ии нужно передавать явно
#То есть по имени, а не позиционно.


#Стандартный класс для изменения всего. Если использовать круды - ф-ии будут в одной переменной (круде).
class CRUD(object):

    @staticmethod
    @create_session
    def add(model, session=None):
        session.add(model)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(model)
            return model
#Теперь это подходит вообще для любой таблицы








from crud import CRUDCategory


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


    @staticmethod
    @create_session
    def get(category_id: int, session=None) -> Optional[Category]:
        category = session.execute(
            select(Category)
            where(Category_id == category_id)
        )
        category = category.first()
        if category:
            return category[0]


    @staticmethod
    @create_session
    def all(session=None) -> list[Category]:
        categories = session.execute(
            select(Category)
            .order_by(Category.id)
        )
        return [category[0] for category in categories]


    @staticmethod
    @create_session
    def update(category: Category, session=None) -> bool:
        category = category.__dict__
        del category['sa_instance_state']
        session.execute(
            update(Category)
            .where(Category.id == category.get('id'))
            .values(
                **category
            )
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True


    @staticmethod
    @create_session
    def delete(category_id: int, session=None) -> None:
        session.execute(
            delete(Category)
            .where(Category_id == category.id)
        )
        session.commit()

    print(CRUDCategory.get(category_id=3))





from csv import DictReader
from typing import List, Optional


def parse_categories() -> List[dict]: #считывает файл, по разделителю точка с запятой
    with open('categories.csv', 'r', encoding='utf-8') as file:
        reader = DictReader(file, delimeter=';')
        data = []
        for cat in reader:
            data.append(cat)
            return data

def create_models(data: List[dict]) -> List[Category]: #превращает список словарей в список моделей
    return list(map(lambda x: Category(**x), data))

def upload_categories(models: List[Category]) -> List[Category]: #загружает модели в бд
    result = []
    for model in models:
        category = CRUDCategory.add(category=model)
        if category:
            result.append(category)

    return result

print(upload_categories(create_models(parse_categories())))



#HTTP
from requests import Session

def get_response():
    with Session() as session:
        response = session.get(
            url=''
        )
        print(response.status_code)