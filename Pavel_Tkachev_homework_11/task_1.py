class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_str_to_int(cls, date_str):
        day, month, year = date_str.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        return type(day), type(month), type(year)

    @staticmethod
    def validator(date_str):
        day, month, year = date_str.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        if (1 <= day <= 31) and (1 <= month <= 12) and 1 <= year:
            return 'Дата верная!'
        else:
            raise ValueError('Ошибка в формате даты!')


print(Date.date_str_to_int('16-04-2022'))
print(Date.validator('16-04-2022'))
print(Date.validator('16-00-2022'))
