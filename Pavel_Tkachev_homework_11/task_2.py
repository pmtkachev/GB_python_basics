class ZeroException(Exception):
    pass


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

try:
    if b == 0:
        raise ZeroException('Делить на ноль нельзя!')
    else:
        print(a // b)
except ZeroException as err:
    print(err)
