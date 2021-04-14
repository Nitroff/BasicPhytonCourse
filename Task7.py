#  7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.

import re
class Complex:
    x:int
    y:int
    def __init__(self, x:int, y):
        self.x = x
        if y == "i" :
            self.y = 1
        elif y == "-i":
            self.y = -1

        else:
            list = (re.search(r'-?\d+', y))
            self.y = int(list[0])
    def __add__(self, other):
        real = str(self.x + other.x)
        im =  self.y + other.y
        sign = "+" if im >= 0 else ""
        if im == -1 :
            im = "-"
        elif im == 1:
            im = ""
        return real + sign + str(im) + "i"

    def __mul__(self, other):
        real =str(self.x * other.x - self.y * other.y)
        im = self.x * other.y + other.x * self.y
        sign = "+" if im >= 0 else ""
        if im == -1 :
            im = "-"
        elif im == 1:
            im = ""
        return real + sign + str(im) + "i"

number1 = Complex(-1, "-12i")
number2 = Complex(2, "13i")
print((number1 + number2))
print((number1 * number2))