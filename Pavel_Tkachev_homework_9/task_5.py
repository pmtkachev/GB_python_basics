class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        print('Я пишу ручкой!')


class Pencil(Stationery):
    def draw(self):
        print('Я рисую карандашом!')


class Handle(Stationery):
    def draw(self):
        print('Я раскрашиваю маркером!')


pen_ = Pen('Ручка')
pencil_ = Pencil('Карандаш')
handle_ = Handle('Маркер')
pen_.draw()
pencil_.draw()
handle_.draw()
