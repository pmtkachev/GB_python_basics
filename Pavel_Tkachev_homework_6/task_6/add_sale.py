import sys

try:
    with open('bakery.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{sys.argv[1]}\n')
except IndexError:
    print('Введите сумму продаж!')
