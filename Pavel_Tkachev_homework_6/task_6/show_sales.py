import sys

with open('bakery.csv', 'r', encoding='UTF-8') as file:
    if len(sys.argv) == 3:
        for sale in file.readlines()[int(sys.argv[1]) - 1:int(sys.argv[2])]:
            print(sale, end='')
    elif len(sys.argv) == 2:
        for sale in file.readlines()[int(sys.argv[1]) - 1:]:
            print(sale, end='')
    else:
        for sale in file.readlines():
            print(sale, end='')
