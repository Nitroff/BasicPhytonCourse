# 1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.
import datetime
class Data:
    # data: str
    def __init__(self,data:str):
        Data.data = data
    @classmethod
    def method(cls):
        cls.data = cls.data.split("-")
        year, month, day = map(int, cls.data)
        print (f"{day}.{month}.{year} г.")
    @staticmethod
    def dateValidate(str):
        try:
            data = datetime.date(*str)
            print("Дата прошла проверку на валидность", end=" >>  ")
        except ValueError:
            print("Такой даты не существует, проверьте корректность введенных данных.")
            exit(-1)

arg = "2015-02-28"
date = Data(arg)
Data.dateValidate([int(x) for x in arg.split("-")])
Data.method()
