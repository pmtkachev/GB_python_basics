from time import sleep
import colorama


class TrafficLight:
    __color = colorama.Fore.RED

    def running(self):
        print(self.__color + 'Загорелся красный')
        sleep(7)
        self.__color = colorama.Fore.YELLOW
        print(self.__color + 'Загорелся желтый')
        sleep(2)
        self.__color = colorama.Fore.GREEN
        print(self.__color + 'Загорелся зеленый')
        sleep(5)


colorama.init()
traffic_light_1 = TrafficLight()
traffic_light_1.running()
