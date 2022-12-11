class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'Суммарный доход: {self.wage + self.bonus} rub')


pos_1 = Position('Иван', 'Иванов', 'Программист', 150000, 20000)
pos_2 = Position('Петр', 'Петров', 'Директор', 250000, 50000)
print(pos_1.name, pos_1.surname, pos_1.position, pos_1.bonus, pos_1.wage)
pos_2.get_full_name()
pos_2.get_total_income()
