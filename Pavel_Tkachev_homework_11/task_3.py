class ExceptIntList(Exception):
    pass


print('--Заполните список только числами--')
dig_list = []
while True:
    try:
        a = input('Введите число или stop для выхода: ')
        if a == 'stop':
            print(dig_list)
            break
        elif a.isdigit():
            dig_list.append(int(a))
        else:
            raise ExceptIntList('Вы ввели не число! Попробуйте еще раз.')
    except ExceptIntList as err:
        print(err)
