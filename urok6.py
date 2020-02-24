#Zadanie1
from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1
t = TrafficLight()
t.running()

#zadanie2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5
    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')
road = Road(5000, 20)
road.asphalt_mass()
#zadanie3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]
p = Position('Вася', 'Обломов', 'Питон разработчик', '200000', '50000')
print(p.get_full_name(), p.get_total_income())


#zadanie4
class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'\n{self.name} встала'
    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nскорость {self.speed}'
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nпревышение скорости {self.speed}'
        else:
            return f'\nскорость {self.name} в порядке'
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nпревышение скорости {self.speed}'
        else:
            return f'скорость{self.name} в порядке'
class PoliceCar(Car):
    pass
town = TownCar('Мерседес', 70, 'черный', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('влево'), town.turn('вправо'), town.stop())
sport = SportCar('Ламборгини', 150, 'желтый', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('влево'), sport.stop())
work = WorkCar('Жигули', 40, 'синий', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())
police = PoliceCar('Лада', 90, 'желтый', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())

#zadanie5
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки'
class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'
pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашом')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())
