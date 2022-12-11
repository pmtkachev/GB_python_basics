class Warehouse:
    """Класс описывающий склад"""
    pass


class OfficeEquipment:
    """Базовый класс для оргтехники"""

    def __init__(self, name, model, manufacturer):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer


class Printer(OfficeEquipment):
    def __init__(self, name, model, manufacturer, speed_print, printing_technology, color):
        super().__init__(name, model, manufacturer)
        self.speed_print = speed_print
        self.printing_technology = printing_technology
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self, name, model, manufacturer, dpi, copy_of_loop):
        super().__init__(name, model, manufacturer)
        self.dpi = dpi
        self.copy_of_loop = copy_of_loop


class Scanner(OfficeEquipment):
    def __init__(self, name, model, manufacturer, color_depth, resolution):
        super().__init__(name, model, manufacturer)
        self.color_depth = color_depth
        self.resolution = resolution

