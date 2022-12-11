class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} поехала {direction}!')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость! Ваша скорость: {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость! Ваша скорость: {self.speed} км/ч')


class PoliceCar(Car):
    pass


town_car = TownCar(55, 'белый', 'Lexus')
sport_car = SportCar(110, 'красный', 'Ferrari')
work_car = WorkCar(50, 'серый', 'UAZ')
police_car = PoliceCar(60, 'белый', 'Vesta', True)
print(police_car.is_police)
print(town_car.speed, town_car.name, town_car.color, town_car.is_police)
work_car.go()
sport_car.stop()
town_car.turn('прямо')
police_car.show_speed()
work_car.show_speed()
