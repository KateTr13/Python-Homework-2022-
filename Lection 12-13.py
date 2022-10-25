#Конкуретность, паралеллизм, синхронность, асинхронность

from time import sleep
import threading
import multiprocessing
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


#Threading
#import threading

def foo(i):
    for _ in range(10):
        sleep(1)
        print(i)


#Импорт threading. Для запуска потоков нужна точка входа, без нее не запустится
if __name__ = '__main__':
    threads = [threading.Thread(target=foo, args=(j, )) for j in range(10)] #С помощью генератора списков делает 10 экземпляров класса Thread
    #Target - ссылка на ф-ю которую хотим запустить,аргументы - список кортежей
    for thread in threads:
        thread.start()


#Мультипроцессинг
# самый ресурсозатратный. Библиотека multiprocessing
#import multiprocessing

if __name__ = '__main__':
    threads = [multiprocessing.Process(target=foo, args=(j, )) for j in range(10)] #С помощью генератора списков делает 10 экземпляров класса Thread
    #Target - ссылка на ф-ю которую хотим запустить,аргументы - список кортежей
    for thread in threads:
        thread.start()


#Asyncio
#Если у программы 1 есть простой, то в это время вкл программа 2, потом возвращается к программе1
#чтобы не терять время
#Корутину(асинхронн.процесс) можно вызвать только внутри корутины. 1ю корутину можно вызывать
#import asyncio

def foo(i):
    for _ in range(10):
        sleep(1)
        print(i)


def main():
    tasks = [asyncio.create_task(foo(j)) for j in range(10)]
    await asyncio.wait(tasks)


if __name__ = '__main__':
    #если на винде при запуске цикла событий вылазит ошибка то добавить это:
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    #и потом продолжить нормальный код
    asyncio.run(main())


#Sqlalchemy
#from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# В venv/settings добавляем еще одну ссылку.
DATABASE_ASYNC_URL: str = 'postgresql+asyncpg://kate:teacup@local:5432/db34kate'

engine = create_async_engine()