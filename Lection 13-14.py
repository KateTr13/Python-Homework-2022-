
#Тестирование

#Создаем папку tests (такова договоренность) (new - python package). Там создаем файл для тестов

def multiply(a, b):
    return a * b

#И в файле для тестов будет:
#import untittest
#from main import multiply

#class TestSimple(unittest.TestCase):

#    def test_multiply(self):
#        self.assertEqual(multiply(2, 4), 8)

#Для запуска тестов в консоли python -m unittest tests/Testcases.py


#Pytest
#pip install pytest потом в init файл папки с тестами добавляем
#from .Testcases import TestSimple

#__all__ = [
#    'TestSimple',
#]


#pip install flake8