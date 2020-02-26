#Zadanie1
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''
    def __str__(self):
        return '\n'.join(map(str, self.my_list))
    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)
m = Matrix([[5, 1, 2], [4, 2, 1], [6, 2, 7], [1, 3, -8]])
new_m = Matrix([[-4, 0, 2], [-5, 1, 7], [1, 23, -6], [3, 1, -5]])
print(m.__add__(new_m))
#zadanie2
from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'
    @abstractmethod
    def abstract(self):
        return
class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'
    def abstract(self):
        return
class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'
    def abstract(self):
        pass
coat = Coat(100)
costume = Costume(20)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())
class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass
coat = Coat(200)
costume = Costume(155)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())
#zadanie3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __add__(self, other):
        return f'Две клетки - хорошо, а одна большая - лучше! Размер клетки равен: {self.quantity + other.quantity}'
    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клеточка стала меньше, теперь она равна: {sub} клетокам' if sub > 0 else 'Клетка исчезла :('
    def __truediv__(self, other):
        return self.quantity // other.quantity
    def __mul__(self, other):
        return self.quantity * other.quantity
    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result
cell = Cell(24)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))
