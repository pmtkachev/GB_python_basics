class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphaltum(self):
        result = (self._length * self._width * 25 * 5) // 1000
        print(f'{result} т')


road_1 = Road(20, 5000)
road_1.mass_of_asphaltum()
