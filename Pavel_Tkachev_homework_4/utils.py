from datetime import date
from decimal import Decimal
import requests


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.text.split('<Valute ID="')[1:]
    currency = currency.upper()
    date_course = response.text.split()[3]
    date_course = date_course.split('Date="')[1][0:-1].split('.')
    date_course = date(year=int(date_course[2]), month=int(date_course[1]), day=int(date_course[0]))
    date_course = date_course.strftime('%d/%m/%Y')
    for i in content:
        if currency in i:
            nominal = i.split('</Nominal>')[0].split('<Nominal>')[1]
            value = Decimal((i.split('</Value>')[0].split('<Value>')[1]).replace(',', '.'))
            return f"Курс на {date_course}: {nominal} {currency} = {round(value, 2)} RUB"
    return None


if __name__ == '__main__':
    print('Hello')
    print(currency_rates('usd'))
