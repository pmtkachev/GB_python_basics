prices_list = [57.8, 46.51, 97, 78.54, 100.47, 99.99, 547.5, 48.6, 78.12, 67.56]


# 5.1 Преобразование в строку вида <rr> руб <cc> коп
def prices_to_string(prices):
    result_string = ''
    for price in prices:
        penny = str(round(price - int(price), 2))
        penny = penny.replace('.', '')
        result_string += f'{int(price)} руб {int(penny):02} коп, '
    return result_string[:-2]


print(prices_to_string(prices_list))
# 5.2 Вывод цен по возрастанию
print(id(prices_list))
prices_list.sort()  # Первый вывод ячейки памяти
print(prices_to_string(prices_list))
print(id(prices_list))  # Так как вывод ячейки памяти соответствует первому выводу, объект тот же

# 5.3 Вывод цен по убыванию
prices_list_rev = prices_list[:]
prices_list_rev.reverse()
print(prices_to_string(prices_list_rev))

# 5.4 Вывод 5 самых дорогих товаров с минимумом кода
prices_list.sort()  # Это можно убрать, так как сортировка была выше (если пишем код с нуля, оставить)
print(f'5 самых дорогих товаров {prices_to_string(prices_list[-1:-6:-1])}')
