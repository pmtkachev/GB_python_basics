import requests
from decimal import Decimal
from datetime import date


def currency_rates(currency, content, date_course):
    currency = currency.upper()
    date_course = date_course.split('Date="')[1][0:-1].split('.')
    date_course = date(year=int(date_course[2]), month=int(date_course[1]), day=int(date_course[0]))
    date_course = date_course.strftime('%d/%m/%Y')
    for i in content:
        if currency in i:
            nominal = i.split('</Nominal>')[0].split('<Nominal>')[1]
            value = Decimal((i.split('</Value>')[0].split('<Value>')[1]).replace(',', '.'))
            return f"Курс на {date_course}: {nominal} {currency} = {round(value, 2)} RUB"
    return None


# Заметил, что если запрос оставить в функции, то это замедляет ее работу
# Сейчас делаем запрос один раз и уже данные используем, когда захотим
response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
cbr_info = response.text.split('<Valute ID="')[1:]
date_response = response.text.split()[3]

print(currency_rates('eur', cbr_info, date_response))
print(currency_rates('USD', cbr_info, date_response))
print(currency_rates('zar', cbr_info, date_response))
print(currency_rates('huf', cbr_info, date_response))
print(currency_rates('aaa', cbr_info, date_response))
