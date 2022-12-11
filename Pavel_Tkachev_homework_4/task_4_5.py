from utils import currency_rates
import sys

# 4 задача решена
# print(currency_rates('usd'))
# print(currency_rates('EuR'))
# print(currency_rates('Zar'))

# 5 задача
if __name__ == '__main__':
    for i in sys.argv[1:]:
        print(currency_rates(i))
