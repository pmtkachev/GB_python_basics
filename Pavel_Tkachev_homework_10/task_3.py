class Cell:
    def __init__(self, slot):
        self.slot = slot

    def __add__(self, other):
        return Cell(self.slot + other.slot)

    def __sub__(self, other):
        if self.slot - other.slot > 0:
            return Cell(self.slot - other.slot)
        else:
            print('Разность ячеек меньше нуля!')

    def __mul__(self, other):
        return Cell(self.slot * other.slot)

    def __floordiv__(self, other):
        return Cell(self.slot // other.slot)

    def __truediv__(self, other):
        return Cell(self.slot // other.slot)

    def make_order(self, slot_row):
        result = ''
        for i in range(self.slot // slot_row):
            result += '*' * slot_row + '\n'
        if self.slot - slot_row * (self.slot // slot_row):
            result += '*' * (self.slot - slot_row * (self.slot // slot_row))
        return result


cell_1 = Cell(20)
cell_2 = Cell(2)
# Объединение
cell_3 = cell_2 + cell_1
print(cell_3.slot)
# Вычитание
cell_3 = cell_1 - cell_2
print(cell_3.slot)
cell_3 = cell_2 - cell_1
# Умножение
cell_3 = cell_2 * cell_1
print(cell_3.slot)
# Деление
cell_3 = cell_1 / cell_2
print(cell_3.slot)
print(cell_1.make_order(6))
